"""
@author : Hyunwoong
@when : 2019-12-18
@homepage : https://github.com/gusdnd852
"""
import torch
from torch import nn

from models.model.decoder import Decoder
from models.model.encoder import Encoder


class Transformer(nn.Module):

    def __init__(self, src_pad_idx, trg_pad_idx, trg_sos_idx, enc_voc_size, dec_voc_size, d_model, n_head, max_len,
                 ffn_hidden, n_layers, drop_prob, device):
        super().__init__()
        self.src_pad_idx = src_pad_idx # source 패딩 idx -> <pad> 토큰이 무엇을 의미?
        self.trg_pad_idx = trg_pad_idx # target 패딩 idx -> <pad> 토큰이 무엇을 의미?
        self.trg_sos_idx = trg_sos_idx # target start of sequence idx
        self.device = device

        # 나머지는 같고, enc_voc_size / dec_voc_size가 들어감
        self.encoder = Encoder(d_model=d_model,
                               n_head=n_head,
                               max_len=max_len,
                               ffn_hidden=ffn_hidden,
                               enc_voc_size=enc_voc_size,
                               drop_prob=drop_prob,
                               n_layers=n_layers,
                               device=device)

        self.decoder = Decoder(d_model=d_model,
                               n_head=n_head,
                               max_len=max_len,
                               ffn_hidden=ffn_hidden,
                               dec_voc_size=dec_voc_size,
                               drop_prob=drop_prob,
                               n_layers=n_layers,
                               device=device)

    def forward(self, src, trg):
        src_mask = self.make_src_mask(src) # source에서 마스크 할 거 마스킹
        trg_mask = self.make_trg_mask(trg) # target에서 마스킹할 거 마스킹
        enc_src = self.encoder(src, src_mask) # 마스크된 거랑 src랑 다시 인코더?? 뭐하는거지?
        output = self.decoder(trg, enc_src, trg_mask, src_mask) # 타겟이랑, 소스에서 나온 컨텍스트 벡터와, 타겟의 마스킹과, 소스의 마스킹?
        return output

    def make_src_mask(self, src): # unsqueeze(1)과 unsqueeze(2)의 의미?
        src_mask = (src != self.src_pad_idx).unsqueeze(1).unsqueeze(2)
        return src_mask

    def make_trg_mask(self, trg): # torch.ByteTensor의 의미
        trg_pad_mask = (trg != self.trg_pad_idx).unsqueeze(1).unsqueeze(3)
        trg_len = trg.shape[1]
        trg_sub_mask = torch.tril(torch.ones(trg_len, trg_len)).type(torch.bool).to(self.device) # torch.ByteTensor 에서 torch.bool로 수정
        trg_mask = trg_pad_mask & trg_sub_mask
        return trg_mask
        # trg_pad_mask 인 동시에 trg_sub_mask이어야 한다.
        # 1) 일단 패딩이 아니다 2) 그 와중에 submask가 아니다 약간 이런 식.
        # 패딩을 일단 가려주고.