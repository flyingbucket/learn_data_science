'''第一部分'''
import numpy as np
arr2=np.array([list(range(i,i+3)) for i in [2,4,6]])
list2=[list(range(i,i+3)) for i in [2,4,6]]
list3=[list(range(i,i+3)) for i in [2,4,6]]
arr3=np.array(list3)
print(arr2)
print(list3)
print(arr3)

a=list(range(2,5))
print(a)


'''第二部分'''
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

print(arr3)
print(arr4)
print(arr5)
print(arr6)

'''第三部分'''
import numpy as np
arr7 = np.array([[1, 2], [3, 4]])
arr8 = np.array([[5, 6], [7, 8]])

# 矩阵乘法
arr9 = arr7 @ arr8
print(arr9)

'''第四部分'''