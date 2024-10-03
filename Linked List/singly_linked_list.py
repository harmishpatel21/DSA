class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None 
    
    def print_list(self):
        current = self.head
        while current:
            print(f"{current.data} -> ", end="")
            current = current.next
        print("None")

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    
    def insert_at_begin(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete_at_begin(self):
        if self.head is None:
            return
        self.head = self.head.next

    def delete_at_end(self):
        if self.head is None:
            return
        
        if self.head.next is None:
            self.head = None
            return
        
        current = self.head
        while current.next.next is not None:
            current = current.next
        current.next = None
    
    def reverse(self):
        prev = None
        current = self.head

        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node 
        self.head = prev
    
    def search(self, value):
        current = self.head
        while current is not None:
            if current.data == value:
                return 1
            current = current.next
        return 0

if __name__ == "__main__":
    sll = SinglyLinkedList()

    sll.print_list()
    sll.insert_at_end(1)
    sll.insert_at_end(2)
    sll.insert_at_end(3)
    sll.print_list()
    sll.insert_at_begin(10)
    sll.insert_at_begin(12)
    sll.print_list()
    sll.insert_at_begin(19)
    sll.print_list()
    sll.delete_at_begin()
    sll.print_list()
    sll.insert_at_end(100)
    sll.print_list()
    sll.delete_at_end()
    sll.print_list()
    sll.reverse()
    sll.print_list()

    value = 15
    if sll.search(value):
        print(f"Found {value}")
    else:
        print(f"Not Found")
