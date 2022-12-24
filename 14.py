'''Given a list of numbers of list, write a Python program to create a list of tuples having first element as the number and second element as the cube of the number. Example:
Input: list = [1, 2, 3]
Output: [(1, 1), (2, 8), (3, 27)]

Input: list = [9, 5, 6]
Output: [(9, 729), (5, 125), (6, 216)]
'''

list1 = [1, 2, 5, 6]
output = [(val, pow(val, 3)) for val in list1]
print(output)