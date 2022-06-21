### 张量基础操作

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
    
    

```
