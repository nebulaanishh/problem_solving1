# Exercise 7: Add new item to list after a specified item
# Input:     list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
# Output:    [10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40]


# Solution Pseudocode
# Iterate over each item in the list
    # If the type of item is a list:
        # iterate over it again with target (recursively)
        # base condition of recursion will return a list with the to_insert item inserted


from typing import List
def add_after(list1: List, target, to_insert) -> List:
    """
    Arguments:
        List (list1): Takes a List as input 
        target: Target is the item after which the to_insert is to be inserted
        to_insert: It is the value to be inserted
    Return:
        List: Returns a List containing the item inserted after the target number
    """
    if target in list1:
        index = list1.index(target)
        list1.insert(index, to_insert)
        # swap the items
        list1[index], list1[index+1] = list1[index+1], list1[index]
        return list1

    for item_index in range(len(list1)):
        # print(type(list1[item_index]))
        if type(list1[item_index]) == type([]):
            result = add_after(list1[item_index], target, to_insert)
            # list1.append(result) 
            list1[item_index] = result
        
                
    return list1


list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
target = 6000


result = add_after(list1, target, 7000)
print(result)