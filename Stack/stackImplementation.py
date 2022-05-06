class StackImplementation:
    # Constructor
    def __init__(self):
        self.stack_list = list()  # List variable for holding stack items
        self.stack_stack_size = 7  # Total elements stack can have
        self.top = 0  # Initial value of "top" variable

    # Pushing element to the Stack
    def push_ele(self, data_item):
        # Condition checking if value of "top" is equal or greater than the actual
        # size of stack
        if self.top >= self.stack_stack_size:
            return "Stack Full!"

        self.stack_list.append(data_item)
        self.top += 1

    # Popping element from the Stack
    def pop_ele(self):
        # Condition checking if value of "top" is equal or less than 0
        if self.top <= 0:
            return "Stack Empty!"

        item = self.stack_list.pop()
        self.top -= 1
        return item

    # Size of Stack
    def stack_size(self):
        return self.top

    # Retrieving topmost element of stack
    def peek_ele(self):
        # Condition checking if value of "top" is equal or less than 0
        if len(self.stack_list) <= 0:
            raise Exception('Stack underflow')
        else:
            return self.stack_list[-1]

    # Traversing the stack list
    def print_stack(self):
        return self.stack_list


stackObj = StackImplementation()

# Pushing elements onto stack
stackObj.push_ele(9)
stackObj.push_ele(19)
stackObj.push_ele(29)
stackObj.push_ele(39)
stackObj.push_ele(49)
result = stackObj.print_stack()

print("Original List:", result)
print("Size of stack:", stackObj.stack_size())

stackObj.push_ele(52)
print("After inserting new element:", result)
print("Size of stack:", stackObj.stack_size())

# Function call for removing present topmost element
stackObj.pop_ele()
print("After popping element from list:", result)
print("Size of stack:", stackObj.stack_size())

stackObj.pop_ele()
print("After popping element from list:", result)
print("Size of stack:", stackObj.stack_size())

print("Topmost element in stack:", stackObj.peek_ele())
