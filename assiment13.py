import numpy as np
a=np.array([[6,-8,73,-110],[np.nan,-8,0,94]])
a=np.nan_to_num(a)
print(a.T)
a=np.arange(24).reshape(2,3,4)
print(np.moveaxis(a,0,2))
a=np.array([[1,np.nan,3],[4,5,np.nan]])
m=np.nanmean(a,axis=0)
a[np.where(np.isnan(a))]=m[np.where(np.isnan(a))[1]]
print(a)
a=np.array([10,-5,7,-2])
a[a<0]=0
print(a)
from scipy.stats import mode

a=np.array([[3,4],[5,6]])
b=np.array([[1,0],[7,8]])

avg=(a+b)/2
print("Average=\n",avg)
print("Mean=",np.mean(avg))
print("Median=",np.median(avg))
print("Mode=",mode(avg,axis=None).mode)

A=np.array([[1,-2,3],[-1,3,-1],[2,-5,5]])
B=np.array([9,-6,17])

x=np.linalg.solve(A,B)
print(x)

import matplotlib.pyplot as plt

sub=['M','P','D','O','C']
sem1=[70,75,80,78,72]
sem2=[82,85,88,84,80]

plt.plot(sub,sem1,'bo-',label='Sem1')
plt.plot(sub,sem2,'ro-',label='Sem2')
plt.title("Semester Comparison")
plt.legend()
plt.grid()
plt.show()
