# Singly linked list implementation
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
    
    def delete(self, value):
        if self.head is None:
            return
        
        if self.head.value == value:
            self.head = self.head.next
            return
        
        current = self.head
        while current.next is not None:
            if current.next.value == value:
                current.next = current.next.next
                return
            current = current.next
    
    def traverse(self):
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")
