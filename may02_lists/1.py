# Possible Cases
# Case 1: Length of both lists are same
# Case 2: Length of list1 is greater
# Case 3: Length of list2 is greater

# Find minimum length
# Initialize the new list
# Iterate till the minimum length
    # concatenate the items of list1 and list2 in a new string
    # append it to the new list
# Append list items from minimum length to end in the list with higher length

# Test Cases
l1 = ["Hi", "Hello"] 
l2 = ["Here", "There"]

l1 = ["M", "na", 2, "Ke", None]
l2 = ["y", "me", 2]

# Code
from typing import List
def concatenate_lists(list1: List, list2: List) -> List:
    """
    Concatenates items in two lists index-wise
    Arguments:
        list1: first list 
        list2: second list
    Return:
        List: Returns a list with items concatenated index-wise
    """
    final_list = []
    if len(list1) == 0:
        return list2
    if len(list2) == 0:
        return list1

    min_length = min(len(list1), len(list2))
    for index in range(min_length):
        concatenated_string = str(list1[index]) + str(list2[index])
        final_list.append(concatenated_string)

    if len(list1) > len(list2):
        final_list += list1[min_length:]
    else:
        final_list += list2[min_length:]

    return final_list

result = concatenate_lists(l1, l2)    
print(result)