


### 介绍 
**异构图对比学习推荐系统(即HGCL)** 通过异构图对比学习极大地提升了推荐系统的性能。该模型通过将元网络与自适应增强的对比学习方法相结合，实现了用户与物品之间的只是转移。模型还利用定制化的跨视图增强来进一步提升对比学习的性能

### 代码运行环境 
pyTorch:
	Python=3.7.10
	Torch=1.8.1
	Numpy=1.20.3
	Scipy=1.6.2
### 数据集
原作者团队使用了三类数据集 *Yelp*, *Epinions*, and *CiaoDVD*。 按照通常的数据集构建方法，假设用户u评价了物品j，就将元素（u,j）设置为1，否则设置为0。除此之外，原作者在原有数据集上过滤了评价或者被评价次数较少的用户或者物品，并将所有数据按照1：n-1的比例划分为训练集与测试集


### How to Run the Code
Please unzip the datasets first. Also you need to create the History/ and the Models/ directories. The command to train HGCL on the Yelp/Epinions/CiaoDVD dataset is as follows. The commands specify the hyperparameter settings that generate the reported results in the paper.
* Yelp
```
python main.py --dataset Yelp --ssl_temp 0.5 --ssl_ureg 0.06 --ssl_ireg 0.07 --lr 0.058 --reg 0.05 --ssl_beta 0.45 --rank 3
```
* Epinions
```
python main.py --dataset Epinions --ssl_temp 0.5 --ssl_ureg 0.04 --ssl_ireg 0.05 --lr 0.055 --reg 0.043 --ssl_beta 0.32 --rank 3
```
* CiaoDVD
```
python3 main.py --dataset CiaoDVD --ssl_temp 0.6 --ssl_ureg 0.04 --ssl_ireg 0.05 --lr 0.055 --reg 0.065 --ssl_beta 0.3 --rank 3
```


### Important arguments
* `--ssl_temp` It is the temperature factor in the InfoNCE loss in our contrastive learning. The value is selected from {0.1, 0.3, 0.45, 0.5, 0.55,0.6, 0.65}.
* `--ssl_ureg, ssl_ireg` They are the weights for the contrastive learning loss of user’s and item’s aspect respectively. The value of this pair are tuned from 
{(3e-2,4e-2),( 4e-2,5e-2),( 5e-2,6e-2), (6e-2,7e-2),( 7e-2,8e-2)}.
* `--lr` The learning rate of the mode. We tuned it from
{1e-2, 3e-2, 4e-2, 4.5e-2, 5e-2, 5.5e-2, 6e-2}.
* `--Reg` It is the weight for weight-decay regularization. We tune this hyperparameter from the set {1e-2, 3e-2, 4.3e-2, 5e-2, 6e-2, 6.5e-2, 6.8e-2}.
* `--ssl_beta` This is the balance cofficient of the total contrastive loss , which is tuned from{0.2, 0.27, 0.3, 0.32, 0.4, 0.45, 0.48, 0.5}.
* `--rank` A hyperparameter of the dimension of low rank matrix decomposition, This parameter is recommended to tune from{1, 2, 3, 4, 5}.

