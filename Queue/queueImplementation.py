class QueueImplement:
    # Queue class constructor
    def __init__(self, size):
        self.queue_items = list()  # Initializing the Queue
        self.size = size  # Initializing size of queue

    # Adding data element to queue
    def enqueue_ele(self, data_item):
        # Condition for checking whether queue is full or not
        if self.queue_size() >= self.size:
            print("Queue is full!")
        else:
            self.queue_items.insert(0, data_item)

    # Removing first data element from the front
    def dequeue_ele(self):
        # Condition for checking whether queue is empty or not
        if len(self.queue_items) > 0:
            return self.queue_items.pop()
        else:
            print("Queue is empty!")

    # Returning number of elements in queue
    def queue_size(self):
        return len(self.queue_items)

    # Accessing the front element
    def queue_peek(self):
        return self.queue_items[-1]

    # Traversing the queue
    def print_queue_items(self):
        print(self.queue_items)


if __name__ == "__main__":
    obj1 = QueueImplement(5)
    obj1.enqueue_ele(9)
    obj1.enqueue_ele(18)
    obj1.enqueue_ele(27)
    obj1.enqueue_ele(35)
    obj1.enqueue_ele(41)

    obj1.print_queue_items()  # Prints the Complete Queue
    print("Size of queue:", obj1.queue_size())  # Return's size of queue
    print(obj1.queue_peek(), "is the current peek element!")
    print("")

    print(obj1.dequeue_ele(), "was removed!")  # Return's the element removed
    obj1.print_queue_items()
    print(obj1.queue_peek(), "is the current peek element!")
    print("")

    print(obj1.dequeue_ele(), "was removed!")  # Return's the element removed
    obj1.print_queue_items()
    print(obj1.queue_peek(), "is the current peek element!")
