# Class for initializing new nodes with data item passed as parameter and also
# initializing the value of the "next" part
class NodeData:
    def __init__(self, data_item):
        self.data_item = data_item
        self.next_node = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None  # "head" variable containing the address of first node

    # Inserting Node At Beginning
    def node_at_start(self, new_node):
        new_node.next_node = self.head
        self.head = new_node

    # Inserting Node At End
    def node_at_end(self, last_node):
        # Condition checking if list is empty. If yes, then make the passed node as
        # the first node of linked list and update "head" variable
        if self.head is None:
            self.head = last_node

        # Loop for traversing to end of linked list and then updating the "next" part
        # of the current last node to point to newly created last node
        node_var = self.head
        while node_var.next_node is not None:
            node_var = node_var.next_node

        node_var.next_node = last_node

    # Inserting node after another node
    def add_after_node(self, target_node, new_node):
        # Condition checking if list is empty.
        if self.head is None:
            print("List is empty!")

        node = self.head

        while node is not None:
            # Condition for checking if the "data" part of the current node is equal
            # to the value of "target_node", then add the new node after it and update
            # "next" part of prev node and also the "next" part of new node
            if node.data_item == target_node:
                new_node.next_node = node.next_node
                node.next_node = new_node
                break
            node = node.next_node

        else:
            print(f"Node with data item {target_node} not found!")

    # Inserting node before another node
    def add_before_node(self, target_node, new_node):
        # Condition checking if list is empty.
        if self.head is None:
            print("List is empty!")

        # Condition for checking if linked list contains only one node, and we want
        # to add new node before it.
        if self.head.data_item == target_node:
            return self.node_at_start(NodeData(target_node))

        temp = self.head
        prev_node = None  # variable for keeping track of previous node while traversing

        # Loop for traversing until it reaches the last node which contains "None"
        while temp is not None:
            # Condition for checking if the "data" part of the current node is equal
            # to the value of "target_node", then add the new node before it and update
            # "next" part of prev node and also the "next" part of new node
            if temp.data_item == target_node:
                prev_node.next_node = new_node
                new_node.next_node = temp
                break
            prev_node = temp
            temp = temp.next_node

        else:
            print(f"Node with data item {target_node} not found!")

    # Removing first node
    def remove_start_node(self):
        # Condition checking if list is empty.
        if self.head is None:
            print("Empty List!")

        # Condition checking if list has only one node.
        if self.head.next_node is None:
            self.head = None

        self.head = self.head.next_node

    # Removing last node
    def remove_end_node(self):
        # Condition checking if list is empty.
        if self.head is None:
            print("Empty List!")

        # Condition checking if list has only one node.
        if self.head.next_node is None:
            self.head = None

        # Loop for traversing to the end of linked list and then updating the "next"
        # part of last node
        node_data = self.head
        while node_data.next_node is not None:
            node_data = node_data.next_node

        node_data.next_ref = None

    # Removing a node by value
    def remove_node(self, node_item):
        # Condition checking if list is empty.
        if self.head is None:
            print("List is empty!")

        # Deleting first node
        if self.head.data_item == node_item:
            self.head = self.head.next_node

        temp = self.head
        prev_node = None

        while temp is not None:
            if temp.data_item == node_item:
                prev_node.next_node = temp.next_node
                break
            prev_node = temp
            temp = temp.next_node
        else:
            print(f"Node with data item {node_item} not found!")

    # Searching a node
    def search_node(self, element):
        # Condition checking if list is empty.
        if self.head is None:
            print("List is empty!")

        start_node = self.head
        while start_node is not None:
            # Condition checking if the data item of current node is equal to the
            # user input. If yes, return True otherwise False.
            if start_node.data_item == element:
                return True
            start_node = start_node.next_node
        else:
            return False

    # Traversing the List
    def print_list_nodes(self):
        # Condition checking if list is empty.
        if self.head is None:
            print("List is empty!")
        else:
            all_nodes = []
            temp = self.head
            # Loop traversing through each node and assigning its data part to
            # "all_nodes" list and simultaneously using "next" part of current node
            # to move to next node
            while temp is not None:
                all_nodes.append(temp.data_item)
                temp = temp.next_node
            return all_nodes


if __name__ == "__main__":
    listObj1 = SinglyLinkedList()

    # Assigning item values
    listObj1.head = NodeData(5)
    second_node = NodeData(15)
    third_node = NodeData(25)

    # Updating "next" part of every node
    listObj1.head.next_node = second_node
    second_node.next_node = third_node

    # Function call to print nodes
    result = listObj1.print_list_nodes()
    print("Original List:", result)

    # Function call to insert node at start
    listObj1.node_at_start(NodeData(29))
    start_node_res = listObj1.print_list_nodes()
    print("After adding node 29 at start:", start_node_res)

    # Function call to insert node at end
    end_node = NodeData(65)
    listObj1.node_at_end(end_node)
    end_node_res = listObj1.print_list_nodes()
    print("After adding node 65 at end:", end_node_res)

    # Function call to insert new node after a node
    listObj1.add_after_node(15, NodeData(22))
    add_after_node_res = listObj1.print_list_nodes()
    print("After adding node 22 after node 15:", add_after_node_res)

    # Function call to insert new node before a node
    listObj1.add_before_node(25, NodeData(23))
    add_before_node_res = listObj1.print_list_nodes()
    print("After adding node 23 before node 25:", add_before_node_res)

    # Function call to remove a node from start
    listObj1.remove_start_node()
    remove_start_node_res = listObj1.print_list_nodes()
    print("After removing first node:", remove_start_node_res)

    # Function call to remove a node from end
    listObj1.remove_end_node()
    remove_end_node_res = listObj1.print_list_nodes()
    print("After removing last node:", remove_end_node_res)

    # Function call to remove a node by value
    listObj1.remove_node(15)
    remove_node_res = listObj1.print_list_nodes()
    print("After removing node 15:", remove_node_res)

    # Function Call to search a node
    search_ele = int(input("Element to be searched: "))
    if listObj1.search_node(search_ele):
        print(f"{search_ele} was found!")
    else:
        print(f"{search_ele} wasn't found!")
