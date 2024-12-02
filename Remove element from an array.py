#Given an array nums and an integer val, remove all occurrences of val in nums. Return the number of elements in nums which are not equal to val.
import array as arr
nums = arr.array("i", [35, 65, 72, 19, 35, 88, 89, 52, 22, 43])

val = 35

filtered_arr= arr.array("i", [x for x in nums if x!=val])  #remove all instances of val from nums

print(filtered_arr)

k=len(filtered_arr))

print("The length of the filtered array is: ",k)
