# Reverse a list

from typing import List
def reverse_list(list1: List) -> List:
    """ """
    return list1[::-1]

def reverse_list_1(list1: List) -> List:
    """"""
    reversed_list = []

    for index in range(len(list1)-1, -1, -1):
        reversed_list.append(list1[index])
    
    return reversed_list


result = reverse_list_1([x for x in range(10)])
print(result)


# Tests
assert reverse_list_1([1,2,3]) == [3,2,1], "Basic Test"
assert reverse_list_1([1,2, "Hi"]) == ["Hi", 2, 1], "Test with string"
assert reverse_list_1([1,2, None]) == [None, 2, 1], "Test with None value"
assert reverse_list_1([])== [], "Test with empty list"