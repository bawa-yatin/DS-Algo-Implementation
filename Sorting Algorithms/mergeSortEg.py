# Function to merge splitted half's to produce sorted array
def merge_input_elements(left_ele, right_ele):
    sorted_list = []  # variable for holding sorted list
    left_index = right_index = 0  # variable for tracking index of "left_ele" and
    # "right_ele" list

    while len(sorted_list) < (len(left_ele) + len(right_ele)):
        # Condition to check which element from "left_ele" or "right_ele" list
        # should be added in resultant array based on condition
        if left_ele[left_index] < right_ele[right_index]:
            sorted_list.append(left_ele[left_index])
            left_index += 1
        else:
            sorted_list.append(right_ele[right_index])
            right_index += 1

        # Condition executed when end of either array has been reached, and only
        # elements of one array needs to added in resultant array "sorted_list"
        if left_index == len(left_ele):
            sorted_list += right_ele[right_index:]
            break

        elif right_index == len(right_ele):
            sorted_list += left_ele[left_index:]
            break

    return sorted_list


# Recursive Function to split the input in half
def split_input_elements(list_items):
    # Condition implemented when there are less than 2 items in the list
    # Simply return the list items
    if len(list_items) < 2:
        return list_items

    # Calculating the midpoint of list
    mid_point = len(list_items) // 2

    # Recursively splitting the list into half until there are less than 2 elements
    # Storing elements to left of midpoint in "left_side_elements"
    left_side_elements = split_input_elements(list_items[:mid_point])
    # Storing elements to right of midpoint in "right_side_elements"
    right_side_elements = split_input_elements(list_items[mid_point:])

    # Function call for merging the half's to produce sorted list
    return merge_input_elements(left_side_elements, right_side_elements)


# Take list elements from user
num_ele = int(input("Number of elements in the array:- "))
list_nums = list(map(int, input("Array Elements:- ").strip().split()))[:num_ele]

print("List before sorting:", list_nums)
result = split_input_elements(list_nums)  # Function Call
print("List after sorting:", result)
