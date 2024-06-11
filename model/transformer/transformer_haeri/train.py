"""
@author : Hyunwoong
@when : 2019-10-22
@homepage : https://github.com/gusdnd852
"""
import math
import time

from torch import nn, optim
from torch.optim import Adam

from data import *
from models.model.transformer import Transformer
from util.bleu import idx_to_word, get_bleu
from util.epoch_timer import epoch_time


# 학습 가능한 파라미터의 경우, 파라미터의 개수를 모두 합산
def count_parameters(model):
    return sum(p.numel() for p in model.parameters() if p.requires_grad)


def initialize_weights(m):
    if hasattr(m, 'weight') and m.weight.dim() > 1: # weight를 attribute로 가지고 있는 경우
        nn.init.kaiming_uniform(m.weight.data) # initialization 방법 - Kaiming He가 제안한 방식으로, 

model = Transformer(src_pad_idx=src_pad_idx,
                    trg_pad_idx=trg_pad_idx,
                    trg_sos_idx=trg_sos_idx,
                    d_model=d_model,
                    enc_voc_size=enc_voc_size,
                    dec_voc_size=dec_voc_size,
                    max_len=max_len,
                    ffn_hidden=ffn_hidden,
                    n_head=n_heads,
                    n_layers=n_layers,
                    drop_prob=drop_prob,
                    device=device).to(device)

print(f'The model has {count_parameters(model):,} trainable parameters') # 파라미터 개수: 55,205,037 (5천만개)
model.apply(initialize_weights) # applysms nn.Module 클래스에 내장된 메서드로, 각 레이어에 대해 초기화 등 일괄 작업 수행
optimizer = Adam(params=model.parameters(),
                 lr=init_lr,
                 weight_decay=weight_decay,
                 eps=adam_eps)

# 모델 성능(예: 검증 손실)이 개선되지 않을 때 학습률을 감소 시킴. 
# factor는 학습률을 감소 시키는 비율 (예: factor=0.1이고, 현재 학습률 0.01 이라면 학습률을 0.001로 줄임)
# patience
scheduler = optim.lr_scheduler.ReduceLROnPlateau(optimizer=optimizer,
                                                 verbose=True,
                                                 factor=factor,
                                                 patience=patience)

criterion = nn.CrossEntropyLoss(ignore_index=src_pad_idx)


def train(model, iterator, optimizer, criterion, clip):
    model.train()
    return 0

    # epoch_loss = 0
    # for i, batch in enumerate(iterator):
    #     src = batch.src # 128 * 26
    #     trg = batch.trg # 128 * 25

    #     optimizer.zero_grad()
    #     output = model(src, trg[:, :-1]) # 왜 :, :-1 이지? 소스값과 타겟값을 이용하는데 정답 바로 전 시점까지 인 듯.
    #     output_reshape = output.contiguous().view(-1, output.shape[-1])
    #     trg = trg[:, 1:].contiguous().view(-1) # 그래야 맞추려는 거의 정답을 정답으로 세웠을 때 비교하려는 듯.

    #     loss = criterion(output_reshape, trg)
    #     loss.backward()
    #     torch.nn.utils.clip_grad_norm_(model.parameters(), clip) # 뭐하는 코드임?
    #     optimizer.step()

    #     epoch_loss += loss.item()
    #     print('step :', round((i / len(iterator)) * 100, 2), '% , loss :', loss.item())

    # return epoch_loss / len(iterator) # len(iterator)의 의미?


def evaluate(model, iterator, criterion):
    model.eval()
    epoch_loss = 0
    batch_bleu = []

    with torch.no_grad(): # 그래디언트 안흐르게
        for i, batch in enumerate(iterator):
            src = batch.src # 소스 시퀀스: 배치 크기 * 시퀀스 길이 (128 * 13)
            trg = batch.trg # 타겟 시퀀스: 배치 크기 * 시퀀스 길이 (128 * 11)
            output = model(src, trg[:, :-1]) # 모델 예측 (타겟 시퀀스의 마지막 토큰 제외) trg: 128 * 10 # 모델 출력: 배치 크기 * 시퀀스 길이 * 단어 집합 크기 - output: 128 * 10 * 7853 
            output_reshape = output.contiguous().view(-1, output.shape[-1]) 
            # 텐서 메모리를 연속적으로 사용하기 위해 contiguous 사용. 1280 * 7853 으로 변환 -> 각 예측할 토큰들(128*10)에 대해 7853(단어 수) 차원의 확률 벡터로 변환
            trg = trg[:, 1:].contiguous().view(-1) # 맞춰야 할 정답 (타겟 시퀀스의 첫 번째 토큰 제외)

            loss = criterion(output_reshape, trg)
            epoch_loss += loss.item()

            total_bleu = []
            for j in range(batch_size): # 각 배치 별로 하나씩 
                try:
                    trg_words = idx_to_word(batch.trg[j], loader.target.vocab) # 정답 문장
                    output_words = output[j].max(dim=1)[1] # output[j]는 10*7853 이라서, output[j].max(dim=1)은 확률값이 가장 높은 토큰을 선택하고, 그 중 값과 인덱스 중 인덱스를 선택하는 게 [1]
                    output_words = idx_to_word(output_words, loader.target.vocab)
                    bleu = get_bleu(hypotheses=output_words.split(), reference=trg_words.split())
                    total_bleu.append(bleu)
                except:
                    pass

            total_bleu = sum(total_bleu) / len(total_bleu)
            batch_bleu.append(total_bleu)

    batch_bleu = sum(batch_bleu) / len(batch_bleu)
    return epoch_loss / len(iterator), batch_bleu


def run(total_epoch, best_loss):
    train_losses, test_losses, bleus = [], [], [] # 트레인 로스, 테스트 로스, blue score

    for step in range(total_epoch):
        start_time = time.time()
        train_loss = train(model, train_iter, optimizer, criterion, clip)
        valid_loss, bleu = evaluate(model, valid_iter, criterion)
        end_time = time.time()

        if step > warmup:
            scheduler.step(valid_loss)

        train_losses.append(train_loss)
        test_losses.append(valid_loss)
        bleus.append(bleu)
        epoch_mins, epoch_secs = epoch_time(start_time, end_time)

        if valid_loss < best_loss:
            best_loss = valid_loss
            torch.save(model.state_dict(), 'saved/model-{0}.pt'.format(valid_loss))

        f = open('result/train_loss.txt', 'w')
        f.write(str(train_losses))
        f.close()

        f = open('result/bleu.txt', 'w')
        f.write(str(bleus))
        f.close()

        f = open('result/test_loss.txt', 'w')
        f.write(str(test_losses))
        f.close()

        print(f'Epoch: {step + 1} | Time: {epoch_mins}m {epoch_secs}s')
        print(f'\tTrain Loss: {train_loss:.3f} | Train PPL: {math.exp(train_loss):7.3f}')
        print(f'\tVal Loss: {valid_loss:.3f} |  Val PPL: {math.exp(valid_loss):7.3f}')
        print(f'\tBLEU Score: {bleu:.3f}')


if __name__ == '__main__':
    run(total_epoch=epoch, best_loss=inf)
