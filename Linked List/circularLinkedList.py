# Class for initializing new nodes with data item passed as parameter and also
# initializing the value of the "next" part
class NodeData:
    def __init__(self, data_item):
        self.data_item = data_item
        self.next_node = None


class CircularLinkedList:
    def __init__(self):
        self.head = None  # Points to the first node of list

    # Inserting Node At Beginning
    def node_at_start(self, new_node):
        new_node.next_node = self.head
        node_start = self.head

        while node_start.next_node is not self.head:
            node_start = node_start.next_node

        node_start.next_node = new_node
        self.head = new_node

    # Inserting Node At End
    def node_at_end(self, last_node):
        node_data = self.head

        while node_data.next_node is not self.head:
            node_data = node_data.next_node

        node_data.next_node = last_node
        last_node.next_node = self.head

    # Inserting node after another node
    def add_after_node(self, target_node, new_node):
        if self.head is None:
            print("List is empty!")

        node = self.head

        while node.next_node is not self.head:
            if node.data_item == target_node:
                new_node.next_node = node.next_node
                node.next_node = new_node
                break
            node = node.next_node

        else:
            print(f"Node with data item {target_node} not found!")

    # Inserting node before another node
    def add_before_node(self, target_node, new_node):
        if self.head is None:
            print("List is empty!")

        if self.head.data_item == target_node:
            return self.node_at_start(NodeData(target_node))

        temp = self.head
        prev_node = None

        while temp.next_node is not self.head:
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
        if self.head is None:
            print("Empty List!")

        if self.head.next_node is self.head:
            self.head = None

        node = self.head
        while node.next_node is not self.head:
            node = node.next_node

        node.next_node = self.head.next_node
        self.head = self.head.next_node

    # Removing last node
    def remove_end_node(self):
        if self.head is None:
            print("Empty List!")

        if self.head.next_node is self.head:
            self.head = None

        node_data = self.head
        while node_data.next_node.next_node is not self.head:
            node_data = node_data.next_node

        node_data.next_node = self.head

    # Removing a node by value
    def remove_node(self, node_item):
        if self.head is None:
            print("List is empty!")

        # Condition executed to check if the target node is the first node only
        if self.head.data_item == node_item:
            curr = self.head
            while curr.next_node is not self.head:
                curr = curr.next_node
            curr.next_node = self.head.next_node
            self.head = self.head.next_node

        temp = self.head
        prev_node = None

        while temp.next_node is not self.head:
            if temp.data_item == node_item:
                prev_node.next_node = temp.next_node
                break
            prev_node = temp
            temp = temp.next_node
        else:
            print(f"Node with data item {node_item} not found!")

    # Searching a node
    def search_node(self, element):
        if self.head is None:
            print("List is empty!")

        start_node = self.head
        while start_node.next_node is not self.head:
            if start_node.data_item == element:
                return True
            start_node = start_node.next_node
        else:
            return False

    # Traversing the List
    def print_list_nodes(self):
        temp = self.head
        all_nodes = []
        while temp is not None:
            all_nodes.append(temp.data_item)
            temp = temp.next_node
            if temp == self.head:
                break
        return all_nodes


if __name__ == "__main__":
    clList = CircularLinkedList()

    # Assigning item values
    clList.head = NodeData(6)
    second_node = NodeData(12)
    third_node = NodeData(18)

    # Updating "head" part of nodes created
    clList.head.next_node = second_node
    second_node.next_node = third_node
    third_node.next_node = clList.head

    # Function call to print nodes
    result = clList.print_list_nodes()
    print("Original List:", result)

    # Function call to insert node at start
    clList.node_at_start(NodeData(8))
    start_node_res = clList.print_list_nodes()
    print("After adding node 8 at start:", start_node_res)

    # Function call to insert node at end
    end_node = NodeData(30)
    clList.node_at_end(end_node)
    end_node_res = clList.print_list_nodes()
    print("After adding node 30 at end:", end_node_res)

    # Function call to insert new node after a node
    clList.add_after_node(18, NodeData(24))
    add_after_node_res = clList.print_list_nodes()
    print("After adding node 24 after node 18:", add_after_node_res)

    # Function call to insert new node before a node
    clList.add_before_node(24, NodeData(22))
    add_before_node_res = clList.print_list_nodes()
    print("After adding node 22 before node 24:", add_before_node_res)

    # Function call to remove a node from start
    clList.remove_start_node()
    remove_start_node_res = clList.print_list_nodes()
    print("After removing first node:", remove_start_node_res)

    # Function call to remove a node from end
    clList.remove_end_node()
    remove_end_node_res = clList.print_list_nodes()
    print("After removing last node:", remove_end_node_res)

    # Function call to remove a node by value
    clList.remove_node(18)
    remove_node_res = clList.print_list_nodes()
    print("After removing node 18:", remove_node_res)

    # Function Call to search a node
    search_ele = int(input("Element to be searched: "))
    if clList.search_node(search_ele):
        print(f"{search_ele} was found!")
    else:
        print(f"{search_ele} wasn't found!")


