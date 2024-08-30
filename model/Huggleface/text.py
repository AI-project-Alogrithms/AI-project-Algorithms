import torch
import torch.nn as nn
import torch.optim as optim

# 두 개의 입력 데이터와 실제 값
x = torch.tensor([[1.0, 2.0], [2.0, 3.0]])  # 입력 데이터 (2x2)
y = torch.tensor([[3.0], [5.0]])  # 실제 값 (2)
print(x.shape, y.shape)
# 모델 정의
model = nn.Linear(2, 1)  # 입력 크기 2, 출력 크기 1

# 모델의 가중치와 편향을 설정
with torch.no_grad():
    model.weight = torch.nn.Parameter(torch.tensor([[2.0, 1.0]]))  # A = [2, 1]
    model.bias = torch.nn.Parameter(torch.tensor([5.0]))  # B = [5]

# 모델 예측
output = model(x)  # ax + b 계산
print(output.shape)
# 손실 계산
print(y - output)
loss = torch.sum((y - output) ** 2)

print(loss)
# SGD 옵티마이저 정의
optimizer = optim.SGD(model.parameters(), lr=0.1)

# 역전파 계산
loss.backward()

# 가중치와 편향 업데이트
optimizer.step()

# 업데이트 후 모델 출력
updated_output = model(x)

# 결과 출력
# print(output.item(), updated_output.item())
# 결과 출력
print("Initial Output:", output.detach().numpy())
print("Updated Output:", updated_output.detach().numpy())

print("Updated Weight:", model.weight.detach().numpy())
print("Updated Bias:", model.bias.detach().numpy())
