#remove duplicates from a sorted array nums and return the number of unique elements
import numpy as np

def removeDuplicates(nums):
    nums=np.unique(nums)
    print("k= ", len(nums))
    print("Unique nums is: ",nums)

nums= np.array([2, 2, 4, 5, 6, 6, 7, 8, 8, 10, 10])
removeDuplicates(nums)
