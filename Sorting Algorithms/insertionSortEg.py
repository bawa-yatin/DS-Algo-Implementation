def insertion_sort(list_items):
    # Starting from the second element of array as it is assumed that first element
    # is sorted and belongs to the sorted array
    for i in range(1, len(list_items)):
        # Element we want to position in its correct place
        curr_ele = list_items[i]

        # Variable used for finding correct position of element referenced by
        # "curr_ele"
        current_position = i - 1

        # Loop for finding the correct position of "curr_ele". Changes are made
        # if value of "curr_ele" variable is smaller than it's adjacent values
        while current_position >= 0 and list_items[current_position] > curr_ele:
            list_items[current_position + 1] = list_items[current_position]
            # list_items[current_position] = curr_ele
            current_position -= 1

        # After shifting of elements is done, we can insert "curr_ele" at it's
        # correct position, or we can simultaneously update its value when we change
        # the place of it's left adjacent element
        list_items[current_position + 1] = curr_ele


# Take list elements from user
num_ele = int(input("Number of elements in the array:- "))
list1 = list(map(int, input("Array Elements:- ").strip().split()))[:num_ele]

print("List before sorting:", list1)
insertion_sort(list1)  # Function Call
print("List after sorting:", list1)
