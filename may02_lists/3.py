from typing import List
numbers = [1,2,3,4,5]

def square_list(num: List) -> any:
    """
    Arguments:
        List(num): A list of numbers
    Return:
        List: A list of numbers with the squares of each term
    """
    # return [int(x)**2 for x in num]

    for index, value in enumerate(num):
        try:
            if not None:
                num[index] = int(value)**2
                
        except Exception as e:
            print(f"{e}")
            return None
    return num

result = square_list(numbers)
print(result)

# Tests
assert square_list([1,2,3]) == [1, 4, 9], "Base condition"
assert square_list([1,2, "hi"]) == None, "String contains"
assert square_list([]) == [], "Empty list"
