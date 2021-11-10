class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

# Class to create a Linked List
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    # Print the linked list
    def print_list(self):
        if self.head == None:
            raise ValueError("List is empty")
        current = self.head
        while current:
            print(current.data, end="  ")
            current = current.next
        print("\n")

    # Insert a node in a linked list
    def insert(self, data):
        node = Node(data)
        current = self.head
        if not current:
            self.head = node
        else:
            while (current.next):
                current = current.next
            current.next = node

    # Remove duplicates from singly linked list
    def remove_dups(self):
        # Case: No duplicates if length is 0 or 1
        if self.head is None or self.head.next is None:
            return
        values = set()
        current = self.head
        values.add(current.data)
        ptr = current.next
        while ptr:
            data = ptr.data
            if data not in values:
                values.add(data)
                current = ptr
            else:
                current.next = ptr.next
            ptr = ptr.next   

# test the output:
first_node = Node(11)            
linked_list = LinkedList(first_node)
linked_list.insert(3)
linked_list.insert(6)
linked_list.insert(3)
linked_list.insert(11)
linked_list.insert(6)
linked_list.insert(5)
linked_list.insert(7)
linked_list.insert(5)

print("The Linked List is:")
linked_list.print_list()

linked_list.remove_dups()
print("After removing duplicates, the Linked List is:")
linked_list.print_list()         