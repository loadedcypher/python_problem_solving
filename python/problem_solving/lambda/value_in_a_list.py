# Given a list, the task is to write a Python program to check if the value exists in the list or not using the lambda function.

# Input  :  L = [1, 2, 3, 4, 5]
#           element = 4
# Output :  Element is Present in the list

# Input  :  L = [1, 2, 3, 4, 5]
#           element = 8
# Output :  Element is NOT Present in the list

L = [1, 2, 3, 4, 5]
element = 4
value = lambda x : element in L
print(value)