torchvision.datasets.MNIST() 中，有transforms参数，用来对数据进行处理


```
import torchvision
from torchvision import transforms
from torchvision.transforms import ToTensor, Normalize, Compose
from torch.utils.data import DataLoader


# 数据准备，train=True表示是训练数据
data1 = torchvision.datasets.MNIST(train=True, download=False, root="./data",
                                   transform=Compose([ToTensor(),
                                                      Normalize(0.1307, 0.3081)]))
# 数据加载（打乱，分批）
data_loader = DataLoader(data1, shuffle=False, batch_size=2)


```





#### 1、transforms.ToTensor()(img1)  

     后面的括号放需要转换的图

#### 2、transforms.Normalize(mean,std)(img1) 

     标准化

#### 3、transforms.Compose([])

     eg： a=transforms.Compose([transforms.ToTensor()(img1),transforms.Normalize(mean,std)(img1)])

     data = torchvision.datasets.MNIST(train=True, download=False, root="./data",transforms=a)
