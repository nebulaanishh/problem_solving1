# Exercise 9: Replace list’s item with new value if found
# You have given a Python list. Write a program to find value 20 in the list, 
# and if it is present, replace it with 200. Only update the first occurrence of an item.



# list1 = [5, 10, 15, 20, 25, 50, 20]
# Expected Output: [5, 10, 15, 200, 25, 50, 20]



from typing import List
def replace_item(list1: List, target, replacement) -> List:
    """
    Arguments:
        List (list1) : The list of numbers
        target: The target to replace
        replacement: The number to be replaced by
    """

    for index, value in enumerate(list1):
        if value == target:
            list1[index] = replacement
            return list1
        
    return list1


list1 = [5, 10, 15, 20, 25, 50, 20]

result = replace_item(list1, 20, 200)
print(result)