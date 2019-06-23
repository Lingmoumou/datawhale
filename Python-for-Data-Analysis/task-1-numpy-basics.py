#%% [markdown]
# #这100道练习，带你玩转Numpy
# Numpy是Python做数据分析所必须要掌握的基础库之一。本文内容由科赛网翻译整理自!(Github开源项目)[https://github.com/rougier/numpy-100](部分题目保留了原文作参考).

#%%
# 1.导入numpy库并简写为 np
import numpy as np

#%%
# 2.打印numpy的版本和配置说明
print(np.__version__)
np.show_config()

#%%
# 3.创建一个长度为10的空向量(提示: np.zeros)
print(np.zeros(10))

#%%
# 4.如何找到任何一个数组的内存大小(提示: size, itemsize)
Z = np.zeros((10,10))
print("%d bytes" % (Z.size * Z.itemsize))

#%%
# 5.如何从命令行得到numpy中add函数的说明文档(提示: np.info)
numpy.info(numpy.add)

#%%
# 6.创建一个长度为10并且除了第五个值为1的空向量(提示: array[4])
Z = np.zeros(10)
Z[4] = 1
print(Z)

#%%
# 7.创建一个值域范围从10到49的向量(提示: np.arange)
print(np.arange(10,50))

#%%
# 8.反转一个向量(第一个元素变为最后一个) (提示: array[::-1])
Z = np.arange(50)
Z = Z[::-1]
print(Z)

#%%
# 9.创建一个 3x3 并且值从0到8的矩阵(提示: reshape)
print(np.arange(9).reshape(3,3))

#%%
# 10.找到数组[1,2,0,0,4,0]中非0元素的位置索引(提示: np.nonzero)
print(np.nonzero([1,2,0,0,4,0]))

#%%
# 11.创建一个 3x3 的单位矩阵(提示: np.eye)
print(np.eye(3))

#%%
# 12.创建一个 3x3x3的随机数组(提示: np.random.random)
print(np.random.random((3,3,3)))

#%%
# 13.创建一个 10x10 的随机数组并找到它的最大值和最小值(提示: min, max)
Z = np.random.random((10,10))
Zmin, Zmax = Z.min(), Z.max()
print(Zmin, Zmax)

#%%
# 14.创建一个长度为30的随机向量并找到它的平均值(提示: mean)
Z = np.random.random(30)
print(Z.mean())

#%%
# 15.创建一个二维数组，其中边界值为1，其余值为0(提示: array[1:-1, 1:-1])
Z = np.ones((10,10))
Z[1:-1,1:-1] = 0
print(Z)

#%%
# 16.对于一个存在在数组，如何添加一个用0填充的边界(提示: np.pad)
Z = np.ones((5,5))
print(np.pad(Z, pad_width=1, mode='constant', constant_values=0))

#%%
# 17. 以下表达式运行的结果分别是什么?
# 0 * np.nan
# np.nan == np.nan
# np.inf > np.nan
# np.nan - np.nan
# 0.3 == 3 * 0.1
# (提示: NaN = not a number, inf = infinity)
print(0 * np.nan)
print(np.nan == np.nan)
print(np.inf > np.nan)
print(np.nan - np.nan)
print(0.3 == 3 * 0.1)

#%%
# 18.创建一个 5x5的矩阵，并设置值1,2,3,4落在其对角线下方位置(提示: np.diag)
print(np.diag(1+np.arange(4),k=-1))

#%%
# 19.创建一个8x8 的矩阵，并且设置成棋盘样式(提示: array[::2])
Z = np.zeros((8,8),dtype=int)
Z[1::2,::2] = 1
Z[::2,1::2] = 1
print(Z)

#%%
# 20.考虑一个 (6,7,8) 形状的数组，其第100个元素的索引(x,y,z)是什么(提示: np.unravel_index)
print(np.unravel_index(100,(6,7,8)))

#%%
# 21.用tile函数去创建一个 8x8的棋盘样式矩阵(提示: np.tile)
print(np.tile( np.array([[0,1],[1,0]]), (4,4)))

#%%
# 22.对一个5x5的随机矩阵做归一化(提示: (x - min) / (max - min))
Z = np.random.random((5,5))
Zmax, Zmin = Z.max(), Z.min()
Z = (Z - Zmin)/(Zmax - Zmin)
print(Z)

#%%
# 23.创建一个将颜色描述为(RGBA)四个无符号字节的自定义dtype(提示: np.dtype)
color = np.dtype([("r", np.ubyte, 1),("g", np.ubyte, 1),("b", np.ubyte, 1),("a", np.ubyte, 1)])

#%%
# 24.一个5x3的矩阵与一个3x2的矩阵相乘，实矩阵乘积是什么(提示: np.dot | @)
print(np.dot(np.ones((5,3)), np.ones((3,2))))

#%%
# 25.给定一个一维数组，对其在3到8之间的所有元素取反(提示: >, <=)
Z = np.arange(11)
Z[(3 < Z) & (Z <= 8)] *= -1
print(Z)

#%%
# 26.下面脚本运行后的结果是什么?
# print(sum(range(5),-1))
# from numpy import *
# print(sum(range(5),-1))
# (提示: np.sum)

print(sum(range(5),-1))
from numpy import *
print(sum(range(5),-1))

#%%
# 27.考虑一个整数向量Z,下列表达合法的是哪个?
# Z**Z
# 2 << Z >> 2
# Z <- Z
# 1j*Z
# Z/1/1
# Z<Z>Z

Z = np.arange(5)
Z ** Z  # legal

Z = np.arange(5)
2 << Z >> 2  # false

Z = np.arange(5)
Z <- Z   # legal

Z = np.arange(5)
1j*Z   # legal

Z = np.arange(5)
Z/1/1   # legal

Z = np.arange(5)
Z<Z>Z    # false

#%%
# 28.下列表达式的结果分别是什么?
# np.array(0) / np.array(0)
# np.array(0) // np.array(0)
# np.array([np.nan]).astype(int).astype(float)

print(np.array(0) / np.array(0))
print(np.array(0) // np.array(0))
print(np.array([np.nan]).astype(int).astype(float))

#%%
# 29.如何从零位对浮点数组做舍入(提示: np.uniform, np.copysign, np.ceil, np.abs)
Z = np.random.uniform(-10,+10,10)
print (np.copysign(np.ceil(np.abs(Z)), Z))

#%%
# 30.如何找到两个数组中的共同元素(提示: np.intersect1d)
Z1 = np.random.randint(0,10,10)
Z2 = np.random.randint(0,10,10)
print(np.intersect1d(Z1,Z2))

#%%
# 31.如何忽略所有的 numpy 警告(尽管不建议这么做)(提示: np.seterr, np.errstate)

# Suicide mode on
defaults = np.seterr(all="ignore")
Z = np.ones(1) / 0

# Back to sanity
_ = np.seterr(**defaults)

An equivalent way, with a context manager:

with np.errstate(divide='ignore'):
    Z = np.ones(1) / 0

#%%
# 32.下面的表达式是正确的吗
# np.sqrt(-1) == np.emath.sqrt(-1)
# (提示: imaginary number)
np.sqrt(-1) == np.emath.sqrt(-1)  # False

#%%
# 33.如何得到昨天，今天，明天的日期(提示: np.datetime64, np.timedelta64)
yesterday = np.datetime64('today', 'D') - np.timedelta64(1, 'D')
today     = np.datetime64('today', 'D')
tomorrow  = np.datetime64('today', 'D') + np.timedelta64(1, 'D')
print ("Yesterday is " + str(yesterday))
print ("Today is " + str(today))
print ("Tomorrow is "+ str(tomorrow))

#%%
# 34.如何得到所有与2016年7月对应的日期(提示: np.arange(dtype=datetime64['D']))
print(np.arange('2016-07', '2016-08', dtype='datetime64[D]'))

#%%
# 35.如何直接在位计算(A+B)\*(-A/2)(不建立副本)(提示: np.add(out=), np.negative(out=), np.multiply(out=), np.divide(out=))
A = np.ones(3)*1
B = np.ones(3)*2
C = np.ones(3)*3
np.add(A,B,out=B)
np.divide(A,2,out=A)
np.negative(A,out=A)
np.multiply(A,B,out=A)

#%%
# 36.用五种不同的方法去提取一个随机数组的整数部分(提示: %, np.floor, np.ceil, astype, np.trunc)
Z = np.random.uniform(0,10,10)
print (Z - Z%1)
print (np.floor(Z))
print (np.ceil(Z)-1)
print (Z.astype(int))
print (np.trunc(Z))

#%%
# 37.创建一个5x5的矩阵，其中每行的数值范围从0到4(提示: np.arange)
Z = np.zeros((5,5))
Z += np.arange(5)
print (Z)

#%%
# 38.通过考虑一个可生成10个整数的函数，来构建一个数组(提示: np.fromiter)
def generate():
    for x in range(10):
        yield x

print (np.fromiter(generate(),dtype=float,count=-1))

#%%
# 39.创建一个长度为10的随机向量，其值域范围从0到1，但是不包括0和1(提示: np.linspace)
print (np.linspace(0,1,11,endpoint=False)[1:])

#%%
# 40.创建一个长度为10的随机向量，并将其排序(提示: sort)
Z = np.random.random(10)
Z.sort()
print (Z)

#%%
# 41.对于一个小数组，如何用比 np.sum更快的方式对其求和(提示: np.add.reduce)
Z = np.arange(10)
np.add.reduce(Z)

#%%
# 42.对于两个随机数组A和B，检查它们是否相等(提示: np.allclose, np.array_equal)
equal = np.array_equal(A,B)
print(equal)

#%%
# 43.创建一个只读数组(read-only)(提示: flags.writeable)
Z = np.zeros(10)
Z.flags.writeable = False
Z[0] = 1

#%%
# 44.将笛卡尔坐标下的一个10x2的矩阵转换为极坐标形式(提示: np.sqrt, np.arctan2)
Z = np.random.random((10,2))
X,Y = Z[:,0], Z[:,1]
R = np.sqrt(X**2+Y**2)
T = np.arctan2(Y,X)
print (R)
print (T)

#%%
# 45.创建一个长度为10的向量，并将向量中最大值替换为1(提示: argmax)
Z = np.random.random(10)
Z[Z.argmax()] = 0
print (Z)

#%%
# 46.创建一个结构化数组，并实现 x 和 y 坐标覆盖 [0,1]x[0,1] 区域 (提示: np.meshgrid)
Z = np.zeros((5,5), [('x',float),('y',float)])
Z['x'], Z['y'] = np.meshgrid(np.linspace(0,1,5),np.linspace(0,1,5))
print(Z)

#%%
# 47.给定两个数组X和Y，构造Cauchy矩阵C (Cij =1/(xi - yj))(提示: np.subtract.outer)
X = np.arange(8)
Y = X + 0.5
C = 1.0 / np.subtract.outer(X, Y)
print(np.linalg.det(C))

#%%
# 48.打印每个numpy标量类型的最小值和最大值(提示: np.iinfo, np.finfo, eps)
for dtype in [np.int8, np.int32, np.int64]:
    print(np.iinfo(dtype).min)
    print(np.iinfo(dtype).max)

for dtype in [np.float32, np.float64]:
    print(np.finfo(dtype).min)
    print(np.finfo(dtype).max)
    print(np.finfo(dtype).eps)

#%%
# 49.如何打印一个数组中的所有数值(提示: np.set_printoptions)
np.set_printoptions(threshold=np.nan)
print (np.zeros((16,16)))

#%%
# 50.给定标量时，如何找到数组中最接近标量的值(提示: argmin)
Z = np.arange(100)
v = np.random.uniform(0,100)
index = (np.abs(Z-v)).argmin()
print (Z[index])

#%%
# 51.创建一个表示位置(x,y)和颜色(r,g,b)的结构化数组(提示: dtype)
Z = np.zeros(10, [ ('position', [ ('x', float, 1),
                                  ('y', float, 1)]),
                   ('color',    [ ('r', float, 1),
                                  ('g', float, 1),
                                  ('b', float, 1)])])
print (Z)

#%%
# 52.对一个表示坐标形状为(100,2)的随机向量，找到点与点的距离(提示: np.atleast_2d, T, np.sqrt)
import scipy
import scipy.spatial

print (scipy.spatial.distance.cdist(Z,Z))

#%%
# 53.如何将32位的浮点数(float)转换为对应的整数(integer)(提示: astype(copy=False))
Z = np.arange(10, dtype=np.int32)
Z = Z.astype(np.float32, copy=False)
print (Z)

#%%
# 54.如何读取以下文件
# 1, 2, 3, 4, 5
# 6,  ,  , 7, 8
#  ,  , 9,10,11
# (提示: np.genfromtxt)


#%%
# 55. 对于numpy数组，enumerate的等价操作是什么？(提示: np.ndenumerate, np.ndindex)
Z = np.arange(9).reshape(3,3)
for index, value in np.ndenumerate(Z):
    print (index, value)
for index in np.ndindex(Z.shape):
    print (index, Z[index])

#%%
# 56.生成一个通用的二维Gaussian-like数组(提示: np.meshgrid, np.exp)
 X, Y = np.meshgrid(np.linspace(-1,1,10), np.linspace(-1,1,10))
D = np.sqrt(X*X+Y*Y)
sigma, mu = 1.0, 0.0
print (G = np.exp(-( (D-mu)**2 / ( 2.0 * sigma**2 ) ) ))

#%%
# 57.对一个二维数组，如何在其内部随机放置p个元素?(提示: np.put, np.random.choice)
n = 10
p = 3
Z = np.zeros((n,n))
np.put(Z, np.random.choice(range(n*n), p, replace=False),1)
print (Z)

#%%
# 58.减去一个矩阵中的每一行的平均值(提示: mean(axis=,keepdims=))
X = np.random.rand(5, 10)
Y = X - X.mean(axis=1, keepdims=True)
print(Y)

#%%
# 59.如何通过第n列对一个数组进行排序? (提示: argsort)
Z = np.random.randint(0,10,(3,3))
print (Z)
print (Z[Z[:,1].argsort()])

#%%
# 60.如何检查一个二维数组是否有空列(提示: any, ~)
Z = np.random.randint(0,3,(3,10))
print ((~Z.any(axis=0)).any())

#%%
# 61.从数组中的给定值中找出最近的值(提示: np.abs, argmin, flat)
Z = np.random.uniform(0,1,10)
z = 0.5
print (Z.flat[np.abs(Z - z).argmin()])

#%%
# 62.如何用迭代器(iterator)计算两个分别具有形状(1,3)和(3,1)的数组?(提示: np.nditer)
A = np.arange(3).reshape(3,1)
B = np.arange(3).reshape(1,3)
it = np.nditer([A,B,None])
for x,y,z in it: 
    z[...] = x + y
print (it.operands[2])

#%%
# 63.创建一个具有name属性的数组类(提示: class方法)
class NamedArray(np.ndarray):
    def __new__(cls, array, name="no name"):
        obj = np.asarray(array).view(cls)
        obj.name = name
        return obj
    def __array_finalize__(self, obj):
        if obj is None: return
        self.info = getattr(obj, 'name', "no name")

Z = NamedArray(np.arange(10), "range_10")
print (Z.name)

#%%
# 64.考虑一个给定的向量，如何对由第二个向量索引的每个元素加1(小心重复的索引)?(提示: np.bincount | np.add.at)
Z = np.ones(10)
I = np.random.randint(0,len(Z),20)
Z += np.bincount(I, minlength=len(Z))
print(Z)

#%%
# 65.根据索引列表(I)，如何将向量(X)的元素累加到数组(F)?(提示: np.bincount)
X = [1,2,3,4,5,6]
I = [1,3,9,3,4,1]
F = np.bincount(I,X)
print (F)


#%%
# 66.考虑一个(dtype=ubyte) 的 (w,h,3)图像，计算其唯一颜色的数量(提示: np.unique)
w,h = 16,16
I = np.random.randint(0,2,(h,w,3)).astype(np.ubyte)
F = I[...,0]*(256*256) + I[...,1]*256 +I[...,2]
n = len(np.unique(F))
print (n)

#%%
# 67.考虑一个四维数组，如何一次性计算出最后两个轴(axis)的和？(提示: sum(axis=(-2,-1)))
print (A.reshape(A.shape[:-2] + (-1,)).sum(axis=-1))

#%%
# 68.考虑一个一维向量D，如何使用相同大小的向量S来计算D子集的均值？(提示: np.bincount)
import pandas as pd
print(pd.Series(D).groupby(S).mean())

#%%
# 69.如何获得点积 dot prodcut的对角线(提示: np.diag)
np.sum(A * B.T, axis=1)

#%%
# 70.考虑一个向量[1,2,3,4,5],如何建立一个新的向量，在这个新向量中每个值之间有3个连续的零？(提示: array[::4])
Z = np.array([1,2,3,4,5])
nz = 3
Z0 = np.zeros(len(Z) + (len(Z)-1)*(nz))
Z0[::nz+1] = Z
print (Z0)

#%%
# 71.

#%%
# 72.

#%%
# 73.

#%%
# 74.

#%%
# 75.

#%%
# 76.

#%%
# 77.

#%%
# 78.

#%%
# 79.

#%%
# 80.

#%%
# 81.

#%%
# 82.

#%%
# 83.

#%%
# 84.

#%%
# 85.

#%%
# 86.

#%%
# 87.

#%%
# 88.

#%%
# 89.

#%%
# 90.

#%%
# 91.

#%%
# 92.

#%%
# 93.

#%%
# 94.

#%%
# 95.

#%%
# 96.

#%%
# 97.

#%%
# 98.

#%%
# 99.

#%%
# 100.