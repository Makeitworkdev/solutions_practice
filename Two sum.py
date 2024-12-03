#two sum
#return the indices of two numbers that add up to a target value
#assume that each input has exactly one solution, and the same cannot be used twice

class Solution:
    def twoSum(self, nums, target):            #initialize the contents of the class
        self.nums=nums
        self.target=target

        seen={}  #crete empty dictionary to store values we've seen

        for i, num in enumerate(nums):
            complement= target- num #calculate the complement i.e. the number needed to add up to the target

            if complement in seen:
                return [seen[complement], i]   #return the index of the complement and the number if complement is already in seen

            seen[num] =i
            #otherwise, add the current number and its index to the dict

    
x= Solution()
nums=[2, 7, 9, 11, 15]
target= 9

print(x.twoSum(nums, target))



    

            

    
        
        