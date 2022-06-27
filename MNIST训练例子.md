torchvision.datasets.MNIST() 中，有transforms参数，用来对数据进行处理


```
import torchvision
from torchvision import transforms

data = torchvision.datasets.MNIST(train=True, download=False, root="./data")




```


#### 1、transforms.ToTensor()(img1)  

后面的括号放需要转换的图

#### 2、transforms.Normalize(mean,std)(img1) 

标准化

#### 3、transforms.Compose([])

eg： a=transforms.Compose([transforms.ToTensor()(img1),transforms.Normalize(mean,std)(img1)])

     data = torchvision.datasets.MNIST(train=True, download=False, root="./data",transforms=a)
