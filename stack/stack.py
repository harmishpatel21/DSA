class Stack:
    def __init__(self, max_size=10):
        self.max_size = max_size
        self.stack = []

    def is_full(self):
        return len(self.stack) == self.max_size

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, data):
        if not self.is_full():
            self.stack.append(data)
        else:
            print("Stack is full!!")

    def pop(self):
        if not self.is_empty():
            self.stack.pop()
        else:
            print("Stack is empty!!")

    def print_stack(self):
        if self.is_empty():
            print("Stack is empty!")
        else:
            print("Stack:", end=" ")
            for item in self.stack:
                print(item, end=" ")
            print()  # New line after printing the stack


# Main function to demonstrate stack functionality
if __name__ == "__main__":
    stack = Stack()

    stack.push(44)
    stack.push(10)
    stack.push(50)
    stack.push(1)

    stack.print_stack()  # Print current stack

    data = stack.pop()
    if data is not None:
        print(f"Popped: {data}")

    stack.print_stack()  # Print current stack after pop

