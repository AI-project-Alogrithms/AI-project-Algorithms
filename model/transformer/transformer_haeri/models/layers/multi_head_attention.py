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
        q, k, v = self.w_q(q), self.w_k(k), self.w_v(v) # q, k, v shape: [batch_size, seq_len, d_model] = [128, 31, 512]

        # 2. split tensor by number of heads: 텐서를 head의 수에 따라 나눔 
        q, k, v = self.split(q), self.split(k), self.split(v) # q, k, v shape: [batch_size, n_head, seq_len, d_tensor] = [128, 8, 31, 64]

        # 3. do scale dot product to compute similarity
        out, attention = self.attention(q, k, v, mask=mask) # out: score@v, attention: attention score

        # 4. concat and pass to linear layer
        out = self.concat(out) # concat 함수도 어디서 남? -> 밑에 있어
        out = self.w_concat(out)

        # 5. visualize attention map
        # TODO : we should implement visualization # TODO는 또 뭐야. 왜 혼자 파란색?

        return out


    def split(self, tensor):
        """
        split tensor by number of head: 텐서를 여러 개의 헤드에 따라 나누는 함수 (multi-head attention)

        :param tensor: [batch_size, length, d_model]
        :return: [batch_size, head, length, d_tensor]
        """
        batch_size, length, d_model = tensor.size()

        d_tensor = d_model // self.n_head # 전체 임베딩(d_model) 크기를 헤드의 숫자로 나눴을 때 한 헤드의 임베딩이 차지하는 길이
        tensor = tensor.view(batch_size, length, self.n_head, d_tensor).transpose(1, 2)
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

''' 
decoder의 enc_dec_attention의 경우 shape이 다르다
query: x ([batch_size, trg_seq_len, d_model])
key, value: enc ([batch_size, src_seq_len, d_model])
'''
