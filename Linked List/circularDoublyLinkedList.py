# NodeData structure
class NodeData:
    # constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class CircularDoublyList:
    # constructor to create an empty CircularDoublyList
    def __init__(self):
        self.head = None

    # Inserting Node At Beginning
    def node_at_start(self, new_node):
        if self.head is None:
            self.head = new_node

        curr_node = self.head
        while curr_node.next is not self.head:
            curr_node = curr_node.next

        curr_node.next = new_node
        new_node.prev = curr_node
        new_node.next = self.head
        self.head = new_node

    # Inserting Node At End
    def node_at_end(self, value):
        end_node = NodeData(value)
        if self.head is None:
            self.head = end_node

        node_var = self.head
        while node_var.next is not self.head:
            node_var = node_var.next

        node_var.next = end_node
        end_node.prev = node_var
        end_node.next = self.head
        self.head.prev = end_node

    # Inserting node after another node
    def add_after_node(self, target_node, new_node):
        if self.head is None:
            print("List is empty!")

        node = self.head
        while node.next is not self.head:
            if node.data == target_node:
                new_node.next = node.next
                new_node.prev = node
                node.next.prev = new_node
                node.next = new_node
                break
            node = node.next

        else:
            print(f"Node with data item {target_node} not found!")

    # Removing first node
    def remove_start_node(self):
        if self.head is None:
            print("Empty List!")

        if self.head.next is self.head:
            self.head = None

        node = self.head
        while node.next is not self.head:
            node = node.next

        node.next = self.head.next
        self.head.next.prev = node
        self.head = self.head.next

    # Removing last node
    def remove_end_node(self):
        if self.head is None:
            print("Empty List!")

        if self.head.next is None:
            self.head = None

        node_data = self.head
        while node_data.next is not self.head:
            node_data = node_data.next

        node_data.prev.next = self.head
        self.head.prev = node_data.prev

    # Remove node by value
    def remove_node_value(self, node_item):
        if self.head is None:
            print("List is empty!")

        if self.head.data == node_item:
            self.head.next.prev = self.head.prev
            self.head.prev.next = self.head.next
            self.head = self.head.next

        temp = self.head
        prev_node = None

        while temp.next is not self.head:
            if temp.data == node_item:
                prev_node.next = temp.next
                temp.next.prev = prev_node
                break
            prev_node = temp
            temp = temp.next
        else:
            print(f"Node with data item {node_item} not found!")

    # Searching a node
    def search_node(self, element):
        if self.head is None:
            print("List is empty!")

        start_node = self.head
        while start_node.next is not self.head:
            if start_node.data == element:
                return True
            start_node = start_node.next
        else:
            return False

    # Traversing the list
    def print_list_nodes(self):
        temp = self.head
        if temp is not None:
            all_nodes = []
            while True:
                all_nodes.append(temp.data)
                temp = temp.next
                if temp == self.head:
                    break
            return all_nodes
        else:
            print("List is empty!")


if __name__ == "__main__":
    # create an empty CircularDoublyList
    cdlList = CircularDoublyList()
    first = NodeData(4)
    cdlList.head = first
    second = NodeData(8)
    third = NodeData(12)

    first.next = second
    first.prev = third

    second.next = third
    second.prev = first

    third.next = first
    third.prev = second

    # Function call to traverse the nodes
    result = cdlList.print_list_nodes()
    print("Original List:", result)

    # Function call to insert node at start
    cdlList.node_at_start(NodeData(2))
    start_node_res = cdlList.print_list_nodes()
    print("After adding node 2 at start:", start_node_res)

    # Function call to insert node at end
    cdlList.node_at_end(20)
    end_node_res = cdlList.print_list_nodes()
    print("After adding node 20 at end:", end_node_res)

    # Function call to insert new node after a node
    cdlList.add_after_node(12, NodeData(14))
    add_after_node_res = cdlList.print_list_nodes()
    print("After adding node 14 after node 12:", add_after_node_res)

    # Function call to remove a node from start
    cdlList.remove_start_node()
    remove_start_node_res = cdlList.print_list_nodes()
    print("After removing first node:", remove_start_node_res)

    # Function call to remove a node from end
    cdlList.remove_end_node()
    remove_end_node_res = cdlList.print_list_nodes()
    print("After removing last node:", remove_end_node_res)

    # Function call to remove a node by value
    cdlList.remove_node_value(4)
    remove_node_res = cdlList.print_list_nodes()
    print("After removing node 4:", remove_node_res)

    # Function Call to search a node
    search_ele = int(input("Element to be searched: "))
    if cdlList.search_node(search_ele):
        print(f"{search_ele} was found!")
    else:
        print(f"{search_ele} wasn't found!")
