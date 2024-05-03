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
        if list1[index] is None or list2[index] is None:
            final_list.append(None)
        else:
            concatenated_string = str(list1[index]) + str(list2[index])
            final_list.append(concatenated_string)

    if len(list1) > len(list2):
        final_list += list1[min_length:]
    else:
        final_list += list2[min_length:]

    return final_list

result = concatenate_lists(["hi", "hello"], ["there", "world"]) 
print(result)

# Tests
assert  concatenate_lists(["hi", "hello"], ["there", "world"]) == ['hithere', 'helloworld'], "Equal length of list"
assert  concatenate_lists(["hi"], ["there", "world"]) == ['hithere', 'world'], "list1 > list2"
assert  concatenate_lists(["hi", "hello"], ["there"]) == ['hithere', 'hello'], "list2 > list1"
assert  concatenate_lists(["hi", "hello"], ["there", None]) == ['hithere', None], "Contains None"
