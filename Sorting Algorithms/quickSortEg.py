from random import randint


def sort_elements_quicksort(list_items):
    # Condition implemented when there are less than 2 items in the list
    # Simply return the list items
    if len(list_items) < 2:
        return list_items

    low_elements, high_elements, same_elements = [], [], []

    # Selecting pivot element randomly
    pivot_element = list_items[randint(0, len(list_items) - 1)]

    # Condition to check where element smaller than the `pivot` go to the `low_elements`
    # list, elements that are larger than `pivot` go to the `high_elements` list and elements
    # that are equal to `pivot` go to the `same_element` list.
    for item in list_items:
        if item < pivot_element:
            low_elements.append(item)
        elif item > pivot_element:
            high_elements.append(item)
        elif item == pivot_element:
            same_elements.append(item)

    # Recursively calling the function until there are less than 2 elements left
    # and then combining them to form a sorted list
    return sort_elements_quicksort(low_elements) + same_elements + sort_elements_quicksort(high_elements)


# Take list elements from user
num_ele = int(input("Number of elements in the array:- "))
list_nums = list(map(int, input("Array Elements:- ").strip().split()))[:num_ele]

print("List before sorting:", list_nums)
result = sort_elements_quicksort(list_nums)  # Function Call
print("List after sorting:", result)
