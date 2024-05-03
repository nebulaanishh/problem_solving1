# Exercise 5: Iterate both lists simultaneously

## Solution pseudocode
# - Reverse the second list
# - Iterate over all the list items


from typing import List

def both_list_iterate(list1: List, list2: List) -> None:
    """
    Arguments: 
        List (list1): First list of numbers
        List (list2): Second list of numbers
    Return:
        None
    """
    list2 = list2[::-1]
    if len(list2) > len(list1):
        list1, list2 = list2, list1
    for index in range(len(list1)):
        if index < len(list2):
            print(list1[index], list2[index])
        else:
            print(list1[index])



list1 = [10, 20, 30,5,6,7]
list2 = [100, 200, 300, 400]

both_list_iterate(list1, list2)