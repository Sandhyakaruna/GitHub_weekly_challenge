class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_head(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def insert_at_tail(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def delete_node(self, value):
        temp = self.head
        if temp and temp.value == value:
            self.head = temp.next
            return
        prev = None
        while temp and temp.value != value:
            prev = temp
            temp = temp.next
        if temp:
            prev.next = temp.next

    def display(self):
        temp = self.head
        while temp:
            print(temp.value, end=" -> ")
            temp = temp.next
        print("None")

# Example Usage
ll = SinglyLinkedList()
ll.insert_at_head(3)
ll.insert_at_head(2)
ll.insert_at_tail(4)
ll.insert_at_tail(5)
ll.display()
ll.delete_node(3)
ll.display()
