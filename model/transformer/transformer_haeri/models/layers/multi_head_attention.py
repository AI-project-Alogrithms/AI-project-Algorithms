"""
@author : Hyunwoong
@when : 2019-10-25
@homepage : https://github.com/gusdnd852
"""
from torch import nn

from models.layers.scale_dot_product_attention import ScaleDotProductAttention


class MultiHeadAttention(nn.Module):

    def __init__(self, d_model, n_head):
        super(MultiHeadAttention, self).__init__()
        self.n_head = n_head
        self.attention = ScaleDotProductAttention()
        self.w_q = nn.Linear(d_model, d_model)
        self.w_k = nn.Linear(d_model, d_model)
        self.w_v = nn.Linear(d_model, d_model)
        self.w_concat = nn.Linear(d_model, d_model)

    def forward(self, q, k, v, mask=None):
        # 1. dot product with weight matrices
        q, k, v = self.w_q(q), self.w_k(k), self.w_v(v)

        # 2. split tensor by number of heads
        q, k, v = self.split(q), self.split(k), self.split(v) # self.split은 도대체 어디서 정의된 함수지? nn.Module에 있나? 의미가 뭐야? -> 밑에 있어

        # 3. do scale dot product to compute similarity
        out, attention = self.attention(q, k, v, mask=mask)

        # 4. concat and pass to linear layer
        out = self.concat(out) # concat 함수도 어디서 남? -> 밑에 있어
        out = self.w_concat(out)

        # 5. visualize attention map
        # TODO : we should implement visualization # TODO는 또 뭐야. 왜 혼자 파란색?

        return out

    def split(self, tensor): # view 함수와 reshape 함수의 차이
        """
        split tensor by number of head -> 텐서를 헤드의 수에 따라 나눈다

        :param tensor: [batch_size, length, d_model]
        :return: [batch_size, head, length, d_tensor]
        """
        batch_size, length, d_model = tensor.size()

        d_tensor = d_model // self.n_head # 전체 모델에 대해 헤드의 숫자로 나눴을 때 한 헤드에 차지하는 길이 같은거임.
        tensor = tensor.view(batch_size, length, self.n_head, d_tensor).transpose(1, 2)
        # length의 의미는?
        # it is similar with group convolution (split by number of heads)

        return tensor

    def concat(self, tensor):
        """
        inverse function of self.split(tensor : torch.Tensor) -> 컨캣의 inverse function이라 함

        :param tensor: [batch_size, head, length, d_tensor]
        :return: [batch_size, length, d_model]
        """
        batch_size, head, length, d_tensor = tensor.size() # 배치 사이즈, 헤드 숫자, 무슨 길이, 텐서 차원 수
        d_model = head * d_tensor # 헤드 * 텐서 차원

        tensor = tensor.transpose(1, 2).contiguous().view(batch_size, length, d_model)
        return tensor
