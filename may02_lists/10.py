# Exercise 10: Remove all occurrences of a specific item from a list.
# Given a Python list, write a program to remove all occurrences of item 20.

from typing import List
def remove_item_all(list1: List, target: int) -> List:
    """
    Arguments:
        List (list1): List of numbers
        int (target): a target value
    """
    target = int(target)
    for item in list1:
        if int(item) == int(target):
            list1.remove(target)
    return list1

list1 = [5, 20, 15, 20, 25, 50, 20]
result = remove_item_all(list1, 20)
print(result)