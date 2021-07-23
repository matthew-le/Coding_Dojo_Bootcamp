# Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
# Example: biggie_size([-1, 3, 5, -5]) returns that same list, but whose values are now [-1, "big", "big", -5]

num_list = []
def biggie_size(num_list):
    for val in range(len(num_list)):
        if num_list[val] > -1:
            num_list[val] = "big"
    return num_list
print(biggie_size([-1, 3, 5, -5]))

# Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values. (Note that zero is not considered to be a positive number).
# Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it
# Example: count_positives([1,6,-4,-2,-7,-2]) changes the list to [1,6,-4,-2,-7,2] and returns it

num_list = []
def count_positives(num_list):
    count = 0
    for val in range(len(num_list)):
        if num_list[val] > 0:
            count += 1
    num_list[len(num_list) - 1] = count
    return num_list

print(count_positives([-1, 1, 1, 1]))
print(count_positives([1, 6, -4, -2, -7, -2]))

# Sum Total - Create a function that takes a list and returns the sum of all the values in the array.
# Example: sum_total([1,2,3,4]) should return 10
# Example: sum_total([6,3,-2]) should return 7

def sum_total(num_list):
    sum_values = 0
    for val in range(len(num_list)):
        sum_values = num_list[val] + sum_values
    return sum_values
print(sum_total([6,3,-2]))

#Average - Create a function that takes a list and returns the average of all the values.
#Example: average([1,2,3,4]) should return 2.5
# def average(lst):
#     total = 0
#     for val in lst:
#         total += val
#     # if we want a non-integer we must convert at least one number to a float
#     # I chose to convert both for safe measure
#     # typically, we want to be hyper cautious and allow python to do as little
#     # inference as possible
#     return float(total) / float(len(lst))

# print(average([1 ,2 ,3 , 4]))
def average(num_list):
    sum_values = 0
    avg_values = 0
    for val in range(len(num_list)):
        sum_values = num_list[val] + sum_values
        avg_values = sum_values / len(num_list)
    return avg_values
print(average([1,2,3,4]))

# Length - Create a function that takes a list and returns the length of the list.
# Example: length([37,2,1,-9]) should return 4
# Example: length([]) should return 0

def length(val_list):
    return len(val_list)
print(length([]))
print(length([37,2,1,-9]))

# Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have the function return False.
# Example: minimum([37,2,1,-9]) should return -9
# Example: minimum([]) should return False

def minimum(num_list):
    if len(num_list) == 0:
        return False
    result = num_list[0]
    for val in range(len(num_list)):
        if num_list[val] < result:
            result = num_list[val]
    return result
print(minimum([-37,2,1,-9]))

# Maximum - Create a function that takes a list and returns the maximum value in the array. If the list is empty, have the function return False.
# Example: maximum([37,2,1,-9]) should return 37
# Example: maximum([]) should return False

def maximum(num_list):
    if len(num_list) == 0:
        return False
    result = num_list[0]
    for val in range(len(num_list)):
        if num_list[val] > result:
            result = num_list[val]
    return result
print(maximum([-37,2,1,-9]))

# # Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list.
# # Example: ultimate_analysis([37,2,1,-9]) should return {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4 }

# def ultimate_analysis(lst):
#     # handle
#     result = {
#         'sum_total': None,
#         'maximum': None,
#         'minimum': None,
#         'average': None,
#         'length': 0
#     }
#     if len(lst) == 0:
#         return result
#     else:
#         result['sum_total'] = 0
#         result['maximum'] = lst[0]
#         result['minimum'] = lst[0]
    
#     for val in lst:
#         if val > result['maximum']:
#             result['maximum'] = val
#         elif val < result['minimum']:
#             result['minimum'] = val

#         result['sum_total'] += val
#         result['length'] += 1
#     result['average'] = result['sum_total'] / len(lst)

#     return result

# print(ultimate_analysis([37, 2, 1, -9]))
# print(ultimate_analysis([]))

# # Reverse List - Create a function that takes a list and return that list with values reversed. Do this without creating a second list. (This challenge is known to appear during basic technical interviews.)
# # Example: reverse_list([37, 2, 1, -9]) should return [-9, 1, 2, 37]
# def reverse_list(lst):
#     half_len = int(len(lst) / 2)
#     for i in range(half_len):
#         # this is a neat way to do a python swap, a temp is equally valid
#         lst[i] , lst[len(lst) - 1 - i] = lst[len(lst) - 1 - i], lst[i]
#     return lst

# # some robust test cases
# print(reverse_list([37, 2, 1, -9]))
# print(reverse_list([37, 2, 1, -9, 5]))
# print(reverse_list([]))
# print(reverse_list([1]))
# print(reverse_list([1, 2]))