def selection_sort(list_ele):
    n = len(list_ele)
    for i in range(0, len(list_ele) - 1):
        # In each iteration, we start indexing from the first unsorted element which
        # is assigned to a temporary variable which is then compared with
        # the rest of the elements. We skip the comparison part of the last element
        # as by the time it reaches there, the list would be completely sorted.
        curr_min_index = i
        for j in range(i + 1, n):
            # if the current minimum value is greater than the succeeding value, then
            # we assign that particular value as the minimum value to "curr_min_index"
            if list_ele[j] < list_ele[curr_min_index]:
                curr_min_index = j

        # Swapping minimum value with compared value if minimum value is greater
        # than compared value
        (list_ele[i], list_ele[curr_min_index]) = (list_ele[curr_min_index], list_ele[i])


# Take list elements from user
num_ele = int(input("Number of elements in the array:- "))
list_items = list(map(int, input("Array Elements:- ").strip().split()))[:num_ele]

print("List before sorting:", list_items)
selection_sort(list_items)  # Function Call
print("List after sorting:", list_items)
