#merge two sorted arrays and instead of returning a new array, merge them in-place in the first array
import numpy as np
from numpy import sort
 
class Solution:
    def merge(self, num1, num2, m, n):
        self.num1=np.array(num1)
        self.num2=np.array(num2)
        self.m=m
        self.n=n
        m=len(num1)
        n=len(num2)
        m+n=len(num1)
        num1=np.sort(np.insert, num2)

x=Solution()
num1=[1,, 2, 4, 5, 6, 7]
num2=[2, 4, 6, 7, 8, 9]

print(x.merge(num1, num2,))

