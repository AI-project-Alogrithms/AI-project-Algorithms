"""
@author : Hyunwoong
@when : 2019-10-22
@homepage : https://github.com/gusdnd852
"""
import torch

# GPU device setting
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

# model parameter setting
batch_size = 128
max_len = 256
d_model = 512
n_layers = 6
n_heads = 8
ffn_hidden = 2048
drop_prob = 0.1

# optimizer parameter setting
init_lr = 1e-5
factor = 0.9 
adam_eps = 5e-9
patience = 10 
warmup = 100
epoch = 3
clip = 1.0
weight_decay = 5e-4 # regularization
inf = float('inf')


'''
init_lr: 초기 learning rate
factor: learning rate scheduler 하이퍼파라미터 1 (학습률 감쇠 비율)
patience: learning rate scheduler 하이퍼 파라미터 2 (메트릭이 개선되지 않는 epoch 수 (early stopping과 유사))
epoch: 전체 epoch 수
'''