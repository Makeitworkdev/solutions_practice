#given a large integer rep as an integer aray digits, where each digits[i] is the ith digit of the integer and they are ordered from most significant to the least significant in left-to-right order. Increment the large integer and return the resulting aray of digits.

import numpy as np

class Solution:
    def add_digit(self, digits):
        n =len(digits)
        self.digits=digits
        digits[-1]+=1 #increment the last element by 1

        for i in range(n-1, -1, -1):
            if digits[i]>9:
                digits[i]=0   #reset the digit to 0

                if i>0:
                    digits[i-1]+=1  #carry-over to previous digit
            
            else:
                break 
        #if the first element is 0 after carry-over insert 1 at the beginning 
        if digits[0]==0: 
            digits= np.insert(digits, 0, 1)   #insert 1 at index 0
        return digits
x=Solution()
digits=np.array([4, 3, 2, 1])

print(x.add_digit(digits))

digits=np.array([9])

print(x.add_digit(digits))
