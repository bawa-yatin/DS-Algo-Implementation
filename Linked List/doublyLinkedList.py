# Class for initializing new nodes with data item passed as parameter and also
# initializing the value of the "next_ref" and "rev_ref" part
class NodeData:
    def __init__(self, data_item):
        self.data_item = data_item
        self.next_ref = None
        self.prev_ref = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None  # "head" variable containing the address of first node

    # Inserting Node At Beginning
    def node_at_start(self, new_node):
        new_node.next_ref = self.head
        self.head.prev_ref = new_node
        self.head = new_node

    # Inserting Node At End
    def node_at_end(self, last_node):
        # Condition checking if list is empty. If yes, then make the passed node as
        # the first node of linked list and update "head" variable
        if self.head is None:
            end_node = NodeData(last_node)
            self.head = end_node

        # Loop for traversing to end of linked list and then updating the "next"
        # and "prev" part of the current last node to point to newly created last node
        node_var = self.head
        while node_var.next_ref is not None:
            node_var = node_var.next_ref

        end_node = NodeData(last_node)
        node_var.next_ref = end_node
        end_node.prev_ref = node_var

    # Inserting node after another node
    def add_after_node(self, target_node, new_node):
        # Condition checking if list is empty.
        if self.head is None:
            print("List is empty!")

        else:
            node = self.head
            while node is not None:
                # Condition for checking if the "data" part of the current node is equal
                # to the value of "target_node", then add the new node after it and update
                # "next" part of prev node and also the "next" and "prev" part of
                # new node
                if node.data_item == target_node:
                    new_node.prev_ref = node
                    new_node.next_ref = node.next_ref
                    node.next_ref = new_node
                    break
                node = node.next_ref

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
            # "next" part of prev node and also the "next" and "prev" part of new node
            if temp.data_item == target_node:
                new_node.next_ref = temp
                new_node.prev_ref = prev_node
                prev_node.next_ref = new_node
                temp.prev_ref = new_node
                break
            prev_node = temp
            temp = temp.next_ref
        else:
            print(f"Node with data item {target_node} not found!")

    # Removing first node
    def remove_start_node(self):
        # Condition checking if list is empty.
        if self.head is None:
            print("Empty List!")

        # Condition checking if list has only one node.
        if self.head.next_ref is None:
            self.head = None

        self.head = self.head.next_ref
        self.head.next_ref.prev_ref = None

    # Removing last node
    def remove_end_node(self):
        # Condition checking if list is empty.
        if self.head is None:
            print("Empty List!")

        # Condition checking if list has only one node.
        if self.head.next_ref is None:
            self.head = None

        node_data = self.head
        # Loop for traversing to the end of linked list and then updating the "next"
        # part of last node
        while node_data.next_ref is not None:
            node_data = node_data.next_ref

        node_data.prev_ref.next_ref = None

    # Removing a node by value
    def remove_node_value(self, node_item):
        # Condition checking if list is empty.
        if self.head is None:
            print("List is empty!")

        # Deleting first node
        if self.head.next_ref is None:
            if self.head.data_item == node_item:
                self.head = None
            else:
                print("Item not found")

        if self.head.data_item == node_item:
            self.head = self.head.next_node
            self.head.prev_ref = None

        temp = self.head
        prev_node = None

        while temp is not None:
            if temp.data_item == node_item:
                prev_node.next_ref = temp.next_ref
                temp.next_ref.prev_ref = temp.prev_ref
                break
            prev_node = temp
            temp = temp.next_ref
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
            start_node = start_node.next_ref
        else:
            return False

    # Traversing the List
    def print_list_nodes(self):
        # Condition checking if list is empty.
        if self.head is None:
            print("List is empty!")
        else:
            # Loop traversing through each node and assigning its data part to
            # "all_nodes" list and simultaneously using "next" part of current node
            # to move to next node
            all_nodes = []
            temp = self.head
            while temp is not None:
                all_nodes.append(temp.data_item)
                temp = temp.next_ref
            return all_nodes


if __name__ == "__main__":
    dlList = DoublyLinkedList()

    # Assigning item values
    dlList.head = NodeData(7)
    second_node = NodeData(14)
    third_node = NodeData(21)

    # Updating "prev_ref" and "next_ref" of nodes created
    dlList.head.next_ref = second_node

    second_node.prev_ref = dlList.head
    second_node.next_ref = third_node

    third_node.prev_ref = second_node

    # Function call to traverse the nodes
    result = dlList.print_list_nodes()
    print("Original List:", result)

    # Function call to insert node at start
    dlList.node_at_start(NodeData(30))
    start_node_res = dlList.print_list_nodes()
    print("After adding node 30 at start:", start_node_res)

    # Function call to insert node at end
    dlList.node_at_end(35)
    end_node_res = dlList.print_list_nodes()
    print("After adding node 35 at end:", end_node_res)

    # Function call to insert new node after a node
    dlList.add_after_node(14, NodeData(19))
    add_after_node_res = dlList.print_list_nodes()
    print("After adding node 19 after node 14:", add_after_node_res)

    # Function call to insert new node before a node
    dlList.add_before_node(35, NodeData(28))
    add_before_node_res = dlList.print_list_nodes()
    print("After adding node 28 before node 35:", add_before_node_res)

    # Function call to remove a node from start
    dlList.remove_start_node()
    remove_start_node_res = dlList.print_list_nodes()
    print("After removing first node:", remove_start_node_res)

    # Function call to remove a node from end
    dlList.remove_end_node()
    remove_end_node_res = dlList.print_list_nodes()
    print("After removing last node:", remove_end_node_res)

    # Function call to remove a node by value
    dlList.remove_node_value(21)
    remove_node_res = dlList.print_list_nodes()
    print("After removing node 21 by value:", remove_node_res)

    # Function Call to search a node
    search_ele = int(input("Element to be searched: "))
    if dlList.search_node(search_ele):
        print(f"{search_ele} was found!")
    else:
        print(f"{search_ele} wasn't found!")
