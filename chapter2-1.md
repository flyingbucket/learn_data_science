# Numpy入门

## 2.1数据类型与数组的创建
### python数据类型及其特点
1.python是一种动态类型语言，这意味着变量不需要声明类型，可以随时改变类型，也即每个变量的数据类型是动态推断得出的。
这与c++、java等静态类型语言不同，在静态类型语言中，变量的类型必须在编译时确定，不能随意改变。

2.python的整型、列表都不仅仅是一个整型或列表，实际上是一个指向内存中存储数据的指针。这会带来灵活性，但也会导致数据读写和运算速度变慢。

3.在python3.3以后已经内置了数组模块array，但更加实用的还是numpy模块。

### 数组创建方法
4.用列表创建数组：
1）元素的类型可以不同，但在numpy中，数组的元素必须是相同的类型，如果不同则会向上自动转换。
2）创建数组时可以用dtype参数指定数据类型：

```python
import numpy as np

# 创建一个整数数组
arr1 = np.array([1, 2, 3, 4, 5], dtype=int)
```
3）numpy数组可以被指定为多维的：
```python
#利用循环语句和嵌套列表创建一个二维数组
arr2 = np.array([range(i,i+3) for i in [2,4,6]])
```
输出结果为：
```
[[2 3 4]
    [4 5 6]
    [6 7 8]]
```
4）列表推导式：
列表推导式的基本语法如下：


```python
[expression for item in iterable if condition]
```

其中，expression是表达式，item是迭代器中的元素，iterable是可迭代对象，condition是可选的条件。

例如：

```python
list1 = np.array([i**2 for i in range(10)])
list2=[list(range(i,i+3)) for i in [2,4,6]]
```

输出结果为：

```
[ 0  1  4  9 16 25 36 49 64 81]
[[2, 3, 4], [4, 5, 6], [6, 7, 8]]
```
ps.利用列表推导式创建二维数组式很常见的操作，在numpy中以下两个语句会创建出相同的结果：
```python
arr2_1 = np.array([range(i, i+3) for i in [2, 4, 6]])
arr2_2 = np.array([list(range(i, i+3)) for i in [2, 4, 6]])
```
输出将是相同的：
```
[[2 3 4]
 [4 5 6]
 [6 7 8]]
 ```
 arr2_1和arr2_2的区别在于，arr2_1中的元素是range对象，而arr2_2中的元素是列表;但numpy会自动将range对象转换为列表。两种方式在将range对象转换为列表时，一个使用python内置函数，另一个使用numpy的tolist()方法。两者在效率上没有区别，但使用tolist()方法更加方便，所以推荐使用tolist()方法；显式地将range对象转换为列表，主要好处是增加代码的可读性。
 5）使用numpy的内置函数创建数组：

```python
# 创建一个全0数组
arr3 = np.zeros(5)

# 创建一个全1数组
arr4 = np.ones(5)


# 创建一个等差数组
arr5 = np.arange(1, 10, 2) # 1到9，步长为2

# 创建一个等差数列的平方
arr6 = np.arange(1, 10)**2 # 1到9的平方

# 创建一个等比数组
arr7 = np.linspace(1, 10, 5) # 1到10，分成5份

# 创建一个随机数组
arr8 = np.random.rand(5) # 5个随机数

# 创建一个正态分布随机数组
arr9 = np.random.randn(5) # 5个正态分布随机数
```

6）使用numpy的reshape()函数改变数组形状：

```python
arr10 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
arr10 = arr10.reshape(2, 5)
```

输出结果为：

```
[[ 1  2  3  4  5]
 [ 6  7  8  9 10]]
```

## 2.2数组的运算
### 数组的加减乘除
1.numpy支持数组的加减乘除运算，运算符为+、-、*、/。
此四则运算即在元素级别进行的，即对每个对应位置的元素进行运算。

```python
import numpy as np

arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([5, 4, 3, 2, 1])

# 数组加法
arr3 = arr1 + arr2

# 数组减法
arr4 = arr1 - arr2

# 数组乘法
arr5 = arr1 * arr2

# 数组除法
arr6 = arr1 / arr2
```
输出结果为：

```
[6 6 6 6 6]
[-4 -2  0  2  4]     
[5 8 9 8 5]
[0.2 0.5 1.  2.  5. ]
```

2.numpy还支持矩阵乘法运算，运算符为@。

```python
arr7 = np.array([[1, 2], [3, 4]])
arr8 = np.array([[5, 6], [7, 8]])

# 矩阵乘法
arr9 = arr7 @ arr8
```
输出结果为：


```
[[19 22]
 [43 50]]
```

3.numpy还支持矩阵的转置运算，运算符为.T。



