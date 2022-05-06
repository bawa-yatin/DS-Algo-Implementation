# class for Node with data and item_priority
class Node:
    def __init__(self, data_item, item_priority):
        self.data_item = data_item
        self.item_priority = item_priority


# Priority Queue Class
class PriorityQueue:
    def __init__(self):
        self.queue_list = list()

    def enqueue_ele(self, node):
        # Condition for checking if queue is empty
        if self.queue_size() == 0:
            # Adding new node
            self.queue_list.append(node)
        else:
            # Traversing the queue to find the right place for new node
            for x in range(0, self.queue_size()):
                # Checking if the item_priority of new node is greater
                if node.item_priority >= self.queue_list[x].item_priority:
                    # if we have traversed the complete queue
                    if x == (self.queue_size() - 1):
                        # add new node at the end
                        self.queue_list.insert(x + 1, node)
                    else:
                        continue
                else:
                    self.queue_list.insert(x, node)
                    return True

    def dequeue_ele(self):
        max_priority = 0  # Variable holding index first element assuming it has
        # max priority

        for i in range(1, self.queue_size()):
            # Condition checking if priority of present element is less than the
            # current max priority element
            if self.queue_list[i].item_priority < self.queue_list[max_priority].item_priority:
                max_priority = i

        item = self.queue_list.pop(max_priority)
        return item

    # Function for printing all the elements present in queue and displaying their
    # data and priority
    def print_items(self):
        for item in self.queue_list:
            print(str(item.data_item) + " : " + str(item.item_priority))

    # Function for calculating the number of elements in queue list
    def queue_size(self):
        return len(self.queue_list)


pqObj = PriorityQueue()

# Initializing nodes with their data and priority
first_node = Node("C", 125)
sec_node = Node("B", 171)
third_node = Node("A", 101)
fourth_node = Node("Z", 96)
fifth_node = Node("Y", 145)

# Pushing elements into priority queue
pqObj.enqueue_ele(first_node)
pqObj.enqueue_ele(sec_node)
pqObj.enqueue_ele(third_node)
pqObj.enqueue_ele(fourth_node)
pqObj.enqueue_ele(fifth_node)

pqObj.print_items()  # Function call for printing all queue items
print("")

pqObj.dequeue_ele()  # Function call for removing element with max priority
pqObj.print_items()
print("")

pqObj.dequeue_ele()
pqObj.print_items()
print("")

sixth_node = Node("L", 152)
pqObj.enqueue_ele(sixth_node)
pqObj.print_items()
