


### 介绍 
**异构图对比学习推荐系统(即HGCL)** 通过异构图对比学习极大地提升了推荐系统的性能。该模型通过将元网络与自适应增强的对比学习方法相结合，实现了用户与物品之间的只是转移。模型还利用定制化的跨视图增强来进一步提升对比学习的性能

### 代码运行环境 
pyTorch:
	Python=3.7.10
	Torch=1.8.1
	Numpy=1.20.3
	Scipy=1.6.2
### 数据集
原作者团队使用了三类数据集 *Yelp*, *Epinions*, and *CiaoDVD*。 按照通常的数据集构建方法，假设用户u评价了物品j，就将元素（u,j）设置为1，否则设置为0。除此之外，原作者在原有数据集上过滤了评价或者被评价次数较少的用户或者物品，并将处理后的数据集的所有数据按照1：n-1的比例划分为训练集与测试集


### 如何运行代码
原团队所提供的Yelp数据集在实际运行中出现了一些bug，暂时不推荐使用，而CiaoDVD与Epinions数据集可以正常训练并用于模型评估。在正式开始训练模型之前，需要先进行一系列预处理操作。首先，CiaoDVD与Epinions数据集中的rawdata文件夹均包含rating.mat与trust.mat两个mat文件，需要先将这两个文件从rawdata文件夹中取出，直接存放在与loadMat.py,GenerateDistanceMat.py,GenerateICI.py三个py文件相同的目录下。这之后，首先运行loadMat.py代码，该程序会基于上述两个mat文件生成data.pkl文件。随后，依次运行GenerateDistanceMat.py与GenerateICI.py代码，这两个代码将均以data.pkl文件为基础，分别生成ItemDistance_mat.pkl，UserDistance_mat.pk，distanceMat_addIUUI.pkll和ICI.pkl文件。
模型的训练要求读入distanceMat_addIUUI.pkl，data.pkl以及ICI.pkl这三个数据文件，因此请务必确保在运行模型前，已经按照上述方法生成了所需的的pkl文件。

除了处理数据集外，还需要在main.py所在目录（即HGCL-main）目录下创建History与Model空文件夹，并且创建好对应的模型名字的子文件夹。比方说，当前希望运行测试CiaoDVD文件夹，就必须在History与Model下均建立一个名字为CiaoDVD的空文件夹，否则运行训练程序将会报错。根据主程序代码设定，模型每次训练一epoch后，将会将当前测试得到的loss，HR（命中率），NDCG（归一化折损累计增益）存入到History文件夹下的模型所读取的数据集的同名文件夹下。Model文件夹仅在取消掉主程序代码main.py的run函数中的saveModel语句的注释后才会发挥效果，功能为存储历史HR得分最高的一轮epoch中的模型参数，可根据需要选择是否运行或注释这个语句。

在完成所有预处理操作后，在HGCL-main目录下运行主文件并提供必要参数，即可开始训练并且评估HGCL模型。以下指令为原作者给出的参考指令。
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


### 重要声明
* `--ssl_temp` 为InfoNCE损失的温度系数，参考值为 {0.1, 0.3, 0.45, 0.5, 0.55,0.6, 0.65}.
* `--ssl_ureg, ssl_ireg` 分别为用户视图与物品视图的损失的权重系数，参考值为
{(3e-2,4e-2),( 4e-2,5e-2),( 5e-2,6e-2), (6e-2,7e-2),( 7e-2,8e-2)}.
* `--lr`学习率，参考值为
{1e-2, 3e-2, 4e-2, 4.5e-2, 5e-2, 5.5e-2, 6e-2}.
* `--reg` 模型参数正则化系数，参考值为 {1e-2, 3e-2, 4.3e-2, 5e-2, 6e-2, 6.5e-2, 6.8e-2}.
* `--ssl_beta` 对比学习总损失的平衡系数，参考值为{0.2, 0.27, 0.3, 0.32, 0.4, 0.45, 0.48, 0.5}.
* `--rank` 低秩矩阵分解的维度, 参考值为{1, 2, 3, 4, 5}.
### 其余部分可调整参数
*`--seed`随机数种子，默认为29.
*`--batch`每批读入数据量，默认为8192.
*`--topk`输出概率最大的样本的个数，默认为10.
*`--epoches`训练批次最大数目，默认为400.
*`--patience`早停阈值，默认为5，以HR指标作为判断模型能力的标准，当模型连续运行patience个epoches后HR相比历史最优HR不能得到提升，即停止模型训练.


