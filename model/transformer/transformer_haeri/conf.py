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
max_len = 256 # positional encoding에 쓰이는 하이퍼 파라미터
d_model = 512 # head 수*임베딩 차원수
n_layers = 6 # 인코더 / 디코더 블록의 수
n_heads = 8 # 멀티 헤드 어텐션에서 헤드의 수
ffn_hidden = 2048 # FFN
drop_prob = 0.1 #dropout probability

# optimizer parameter setting
init_lr = 1e-5 # initial learning rate
factor = 0.9  # learning rate scheduler hyperparameter (줄이려는 learning rate 비율)
adam_eps = 5e-9
patience = 10  # learning rate scheduler hyperparameter (loss가 줄어들지 않았을 때 인내하는 에폭 수)
warmup = 100 # 해당 에폭 이후부터 learning rate scheduler 업데이트
epoch = 3
clip = 1.0 # gradient clipping: 그래디언트의 노름이 clip 이상으로 안커지게
weight_decay = 5e-4 # regularization
inf = float('inf')


'''
init_lr: 초기 learning rate
factor: learning rate scheduler 하이퍼파라미터 1 (학습률 감쇠 비율)
patience: learning rate scheduler 하이퍼 파라미터 2 (메트릭이 개선되지 않는 epoch 수 (early stopping과 유사))
epoch: 전체 epoch 수
'''