class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def find_middle(self):
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.value if slow else None

# Example Usage
ll = LinkedList()
for i in range(1, 6):  # List: 1 -> 2 -> 3 -> 4 -> 5
    ll.insert(i)
print(ll.find_middle())  # Output: 3

ll.insert(6)  # List: 1 -> 2 -> 3 -> 4 -> 5 -> 6
print(ll.find_middle())  # Output: 4 (second middle)
