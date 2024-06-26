"""
@author : Hyunwoong
@when : 2019-10-22
@homepage : https://github.com/gusdnd852
"""
import torch
from torch import nn


class PositionalEncoding(nn.Module):
    """
    compute sinusoid encoding.
    """

    def __init__(self, d_model, max_len, device):
        """
        constructor of sinusoid encoding class

        :param d_model: dimension of model
        :param max_len: max sequence length
        :param device: hardware device setting
        """
        super(PositionalEncoding, self).__init__()

        # same size with input matrix (for adding with input matrix)
        self.encoding = torch.zeros(max_len, d_model, device=device) # self.encoding:  256 * 512
        self.encoding.requires_grad = False  # we don't need to compute gradient -> 포지셔널 인코딩은 학습 대상이 아님.

        pos = torch.arange(0, max_len, device=device) # pos: [0,1,2,3,..,255]의 1차원 벡터
        pos = pos.float().unsqueeze(dim=1) # pos: 256*1
        # 1D => 2D unsqueeze to represent word's position

        _2i = torch.arange(0, d_model, step=2, device=device).float()
        # 'i' means index of d_model (e.g. embedding size = 50, 'i' = [0,50])
        # "step=2" means 'i' multiplied with two (same with 2 * i)

        self.encoding[:, 0::2] = torch.sin(pos / (10000 ** (_2i / d_model))) # 0부터 끝까지 2칸 간격씩 띄워가며 (즉, 0, 2, 4, 6, .. 인덱스에 대해)
        self.encoding[:, 1::2] = torch.cos(pos / (10000 ** (_2i / d_model))) # 1부터 끝까지 2칸 간격씩 띄워가며 (즉 1, 3, 5, 7, .. 인덱스에 대해)
        # compute positional encoding to consider positional information of words

    def forward(self, x):
        # self.encoding
        # [max_len = 512, d_model = 512]

        batch_size, seq_len = x.size()
        # [batch_size = 128, seq_len = 30] -> seq_len 어디서 남?

        return self.encoding[:seq_len, :]
        # [seq_len = 30, d_model = 512]
        # it will add with tok_emb : [128, 30, 512]
