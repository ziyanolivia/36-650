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
   
    # Swap the data between two nodes in a linked list
    def swap(self, nodeA, nodeB):
        tmp = nodeA.data
        nodeA.data = nodeB.data
        nodeB.data = tmp

    # Sort linked list in ascending order of the data values in the nodes
    def sort(self):
        # Selection Sort
        # Traverse through all elements
        current_head = self.head
        while current_head:
            # Find the minimum element in remaining list
            current = current_head
            min_node = current
            while current:
                if (current.data < min_node.data):
                    min_node = current
                current = current.next
            self.swap(current_head, min_node)
            current_head = current_head.next
         
# test the output:
first_node = Node(11)
linked_list = LinkedList(first_node)
linked_list.insert(3)
linked_list.insert(6)
print("The Linked List is:")
linked_list.print_list()

linked_list.sort()
print("After sorting, the Linked List is:")
linked_list.print_list()