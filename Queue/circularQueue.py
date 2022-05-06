# Circular Queue implementation in Python
class CircularQueue:
    def __init__(self, queue_size):
        self.queue_size = queue_size  # Initializing size of queue
        self.queue = [None] * queue_size  # Initializing Queue
        self.front = self.rear = -1  # Initializing the "front" and "rear" variable
        # to -1

    # Inserting an element into circular queue
    def enqueue_item(self, data):
        if (self.rear + 1) % self.queue_size == self.front:
            print("Circular Queue Overflow!\n")

        # Condition for empty queue
        elif self.front == -1:
            self.front = 0
            self.rear = 0
            self.queue[self.rear] = data
        else:
            # Assign data to next position of rear
            self.rear = (self.rear + 1) % self.queue_size
            self.queue[self.rear] = data

    # Deleting an element from circular queue
    def dequeue_item(self):
        if self.front == -1:
            print("Circular Queue Underflow!\n")

        # Condition for checking if there is only one element
        elif self.front == self.rear:
            temp = self.queue[self.front]
            self.front = -1
            self.rear = -1
            return temp
        else:
            temp = self.queue[self.front]
            self.front = (self.front + 1) % self.queue_size
            return temp

    # Printing elements present inside priority queue
    def print_queue_items(self):
        # Condition for empty queue
        if self.front == -1:
            print("Circular Queue Empty!")

        elif self.rear >= self.front:
            for i in range(self.front, self.rear + 1):
                print(self.queue[i], end=" ")
            print()
        else:
            for i in range(self.front, self.queue_size):
                print(self.queue[i], end=" ")
            for i in range(0, self.rear + 1):
                print(self.queue[i], end=" ")
            print()


if __name__ == "__main__":
    obj = CircularQueue(5)  # Object creation of "CircularQueue" class and
    # initializing size of circular queue

    obj.enqueue_item(6)
    obj.enqueue_item(12)
    obj.enqueue_item(18)
    obj.enqueue_item(24)
    obj.enqueue_item(36)

    print("Initial Queue")
    obj.print_queue_items()
    print("")

    obj.dequeue_item()
    print("After removing element from queue")
    obj.print_queue_items()
    print("")

    obj.enqueue_item(30)
    print("After adding new element in queue")
    obj.print_queue_items()
