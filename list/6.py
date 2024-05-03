# Exercise 6: Remove empty strings from the list of strings

# Solution Pseudocode
# - Iterate over each item
# - Initialize a new list variable
# - If the length of an item is less than 1:
        # skip it
#   else:
        # append to a new variable

        
from typing import List 
def remove_empty_string(list1: List) -> List:
    """
    Arguments:
        List (list1): Takes a list of strings
    Return:
        List: A list of strings with no null or empty characters.
    """

    new_list = []
    for list_item in list1:
        if list_item is None or len(str(list_item)) == 0: # Lazy evaluation
            pass
        else:
            new_list.append(list_item)
    return new_list


list1 = ["Mike", "", "Emma", "Kelly", "", None, 1]
result = remove_empty_string(list1)

print(result)