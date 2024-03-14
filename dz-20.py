# def find_unique_value(l):
#     return [num for num in l if l.count(num) == 1][0]

def find_unique_value(l):
    count_dict = {num: l.count(num) for num in l}
    for key, value in count_dict.items():
        if value == 1:
            return key

# Example usage:
my_list = [1, 2, 2, 3, 3, 4, 4, 5, 5]
assert find_unique_value([1, 2, 1, 1]) == 2, 'Test1'
assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2, 'Test2'
assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5, 'Test3'
print("ОК")