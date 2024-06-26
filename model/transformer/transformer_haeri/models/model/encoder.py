"""
@author : Hyunwoong
@when : 2019-12-18
@homepage : https://github.com/gusdnd852
"""
from torch import nn

from models.blocks.encoder_layer import EncoderLayer
from models.embedding.transformer_embedding import TransformerEmbedding # 호출되는 위치는 처음 train.py 기준인 듯!


class Encoder(nn.Module):
    '''
    enc_voc_size: 인코더의 vocabulary size
    max_len: 시퀀스의 최대 길이 (이것보다 크면 잘라)
    d_model: 임베딩 차원
    ffn_hidden
    n_head
    n_layers
    drop_prob
    device: 'cpu'
    '''

    def __init__(self, enc_voc_size, max_len, d_model, ffn_hidden, n_head, n_layers, drop_prob, device):
        super().__init__()
        # emb_size, 
        self.emb = TransformerEmbedding(d_model=d_model,
                                        max_len=max_len,
                                        vocab_size=enc_voc_size,
                                        drop_prob=drop_prob,
                                        device=device)

        self.layers = nn.ModuleList([EncoderLayer(d_model=d_model,
                                                  ffn_hidden=ffn_hidden,
                                                  n_head=n_head,
                                                  drop_prob=drop_prob)
                                     for _ in range(n_layers)])

    def forward(self, x, src_mask): # x = src, src_mask = src_mask
        x = self.emb(x) # [batch_size, src_seq] -> [batch_size, src_seq, emb_size]

        for layer in self.layers: # 여러 번의 인코더 레이어를 순차적으로 통과
            x = layer(x, src_mask) 

        return x