#multiply two non-negative integers represented as strings, return the product represented as a string
#without using any built-in biginteger library or convert the inputs to integer directly
from math import *

def string_to_int(s):
    result=0
    is_negative= False  #check if number is negative
    
    if s[0]== '-':
        is_negative = True
        s=s[1:] #Remove the negative sign for easier processing

    #loop through each character in the string
    for char in s:
        #convert character to its numeric value by using ascii codes
        digit = ord(char)- ord('0') 
        result = result*10 +digit

    if is_negative:
        result =-result

    return result
num1='10'
num2='45'
num1= string_to_int(num1)
num2= string_to_int(num2)

Product = num1*num2
y = str(Product)
print(y)


