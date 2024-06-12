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
        src_mask = self.make_src_mask(src) # source sequence masking
        trg_mask = self.make_trg_mask(trg) # target sequence masking
        enc_src = self.encoder(src, src_mask) # enc_src: [batch_size, seq_len, d_model] = [128, 31, 512]
        output = self.decoder(trg, enc_src, trg_mask, src_mask) # 타겟, 인코더에서 나온 컨텍스트 벡터, 타겟&소스 마스킹
        return output

    def make_src_mask(self, src): # pad_idx랑 인덱스가 "다르면" True / "같으면" False. 
        # unsqueeze를 통해 새로운 차원을 생성해서 [batch_size, src_len] -> 최종 마스크 텐서의 shape이 [batch_size, 1, 1, src_len]이 되게끔
        src_mask = (src != self.src_pad_idx).unsqueeze(1).unsqueeze(2)
        return src_mask

    def make_trg_mask(self, trg): # torch.ByteTensor의 의미
        trg_pad_mask = (trg != self.trg_pad_idx).unsqueeze(1).unsqueeze(3) # 최종 마스크 텐서: [batch_size, 1, trg_len, 1]
        trg_len = trg.shape[1]
        trg_sub_mask = torch.tril(torch.ones(trg_len, trg_len)).type(torch.bool).to(self.device) # [trg_len, trg_len] 의 하삼각행렬
        trg_mask = trg_pad_mask & trg_sub_mask
        return trg_mask # [batch_size, 1, trg_len, trg_len] shape로 broadcasting
