def bubble_sort(list_ele):
    # Iterate through the list as many times as the number of elements present
    for i in range(len(list_ele)):
        # Variable for keeping track of swapping
        sorted_already = True

        # Pair of elements that would be made will be (n-1) in first iteration, (n-2) in
        # second iteration and so on as the end elements would be in their correct
        # position after each iteration
        for j in range(len(list_ele) - i - 1):
            # Comparing two adjacent elements
            if list_ele[j] > list_ele[j + 1]:
                # swapping places of elements if first element is greater than
                # second element in order to bring them in proper position
                (list_ele[j], list_ele[j + 1]) = (list_ele[j + 1], list_ele[j])
                sorted_already = False

        if sorted_already:
            break


# Take list elements from user
num_ele = int(input("Number of elements in the array:- "))
list1 = list(map(int, input("Array Elements:- ").strip().split()))[:num_ele]

print("List before sorting:", list1)
bubble_sort(list1)  # Function Call
print("List after sorting:", list1)
