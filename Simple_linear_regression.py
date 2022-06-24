# pytorch 练习一：简单线性回归
# 使用：优化器类，损失函数类，线性层nn.Moudle类

import torch
import matplotlib.pyplot as plt
from torch import nn


class mylinear(nn.Module):
    def __init__(self):
        super(mylinear, self).__init__()
        self.l1 = nn.Linear(1, 1)

    def forward(self, x):
        out = self.l1(x)
        return out


x = torch.rand([500, 1])
y_true = 3 * x + 0.8
model = mylinear()
optimizer = torch.optim.SGD(model.parameters(), lr=0.001)
lossfunc = nn.MSELoss()

# 循环，梯度下降，参数更新

for i in range(30000):
    predict = model(x)
    loss = lossfunc(predict, y_true)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

model.eval()  # 转化为评估模式
predict = model(x)
predict = predict.data.numpy()
plt.scatter(x.data.numpy(), y_true.data.numpy(), c='r')
plt.plot(x.data.numpy(), predict)
plt.show()
