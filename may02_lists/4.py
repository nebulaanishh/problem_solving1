from typing import List

list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir", "hehe"]

## Solution in pseudocode
# iterate list1
    # iterate list2 
    # concatenate list2 items with list1
    # append to result_list

# Edge cases
# - Unequal length of lists
# - different datatype 

def list_cross_product(list1: List, list2: List) -> List:
    """
    Eg: 
    Given: list1 = ["Hello ", "take "]
           list2 = ["Dear", "Sir"]
           Output: ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']

    ARGUMENT:
        List (list1): First list
        List (list2): Second list
    RETURN:
        List: A list containing cross product of the each string in both lists
    """
    result_list = []
    for index in range(len(list1)):
        for inner_index in range(len(list2)):
            concatenated_string = str(list1[index]) + str(list2[inner_index])
            result_list.append(concatenated_string)
    return result_list

result = list_cross_product([], list2)
print(result)


# Tests

assert list_cross_product(['hi'], ['hello']) == ['hihello'], "Base condition 1"
assert list_cross_product(['hi', 'hello'], ['hi','hello']) == ['hihi', 'hihello','hellohi', 'hellohello'], "Base condition 2"
assert list_cross_product([], ['hi']) == [], "one empty list"
assert list_cross_product(['hi'], ['hi','hello']) == ['hihi', 'hihello'], "list1 < list2"
assert list_cross_product(['hi', 'hello'], ['hi']) == ['hihi','hellohi'], "list1 > list2"