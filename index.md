### 张量基础操作 https://zhuanlan.zhihu.com/p/334788042

```
t=torch.Tensor([])

张量方法和属性：

t.size()
t.numpy() # 转化为数组类型
t.view((3,4))  # 转换形状，浅拷贝，类似array中的reshape

t.dim()
t.min()
t.max()
t.std()
t.t()  # 表示转置
t.dtype

t1=torch.Tenser(np.arange(24).reshape(2,3,4))
t1.transpose(0,1)  # 交换0维和1维顺序
t1.permute(1,2,0)  # 把原来的 0,1,2 变成 1,2,0

```

### 计算图

```
t = torch.ones(2, 2, requires_grad=True)

with torch.no_grad()  # 评估模型时，不需要更新，此时可以把参数梯度更新设置在这条语句下
    c=t*t  # 此时c.grad_fn=None
    
x=t.mean()
x.backward()  # 用于标量对张量求梯度，梯度是累加的


```

tensor.data  # 获取张量里的数据

当不希望累加梯时：每次反向传播前，梯度置零

``` 

暂时没看懂

optimizer.zero_grad() # 网络梯度清零
loss.backward()  # 误差的反向传播
optimizer.step() # 根据反向传播的误差更新参数
```
