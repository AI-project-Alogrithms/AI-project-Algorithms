import torch
import torch.nn as nn
import torch.optim as optim
import math

print(1 / (1 + math.exp(0.5)))
print(math.log(0.3775))
# 단일 입력 데이터와 실제 레이블
x = torch.tensor([2.0, 3.0])  # 입력 데이터 (1x2)
y = torch.tensor([1.0])  # 실제 레이블 (1)

# 모델 정의
model = nn.Linear(2, 1)  # 입력 크기 2, 출력 크기 1

# 모델의 가중치와 편향을 설정
with torch.no_grad():
    model.weight = torch.nn.Parameter(torch.tensor([[0.5, -0.5]]))  # A = [0.5, -0.5]
    model.bias = torch.nn.Parameter(torch.tensor([0.0]))  # B = 0

# 시그모이드 함수 적용하여 로지스틱 회귀 예측값 계산
sigmoid = nn.Sigmoid()
output = sigmoid(model(x))

# 손실 계산 (Binary Cross-Entropy Loss)
criterion = nn.BCELoss()
loss = criterion(output, y)

# SGD 옵티마이저 정의
optimizer = optim.SGD(model.parameters(), lr=0.1)

# 역전파 계산
loss.backward()

# 가중치와 편향 업데이트
optimizer.step()

# 업데이트 후 모델 출력
updated_output = sigmoid(model(x))

# 결과 출력
print(output.item(), updated_output.item())

import math

hat_y = 1 / (1 + math.exp(0.5))

print(
    torch.tensor([0.5, -0.5])
    - 0.1 * (-(1 / hat_y)) * ((hat_y) * (1 - hat_y)) * (torch.tensor([2.0, 3.0]))
)  # w 업데이트
print(
    torch.tensor([0.0]) - 0.1 * (-(1 / hat_y)) * ((hat_y) * (1 - hat_y))
)  # b 업데이트
