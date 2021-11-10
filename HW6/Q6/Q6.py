# Create the Data Structure (storage data type and the organizer)
class Node(object):
    def __init__(self, data):
        self.data = data
        self.previous = None

# Class to create a Reverse Linked List
class ReverseLinkedList(object):
    def __init__(self, tail=None):
        self.tail = tail

    # Print the reverse linked list
    def print_list(self):
        if self.tail == None:
            raise ValueError("List is empty")
        current = self.tail
        while current:
            print(current.data, end="  ")
            current = current.previous
        print("\n")

# Create the insert() function
    # Insert a node in a reverse linked list
    def insert(self, data):
        node = Node(data)
        node.previous = self.tail
        self.tail = node

# Create the delete() function
    # Delete a node in a reverse linked list
    def delete(self, data):
        if not self.tail:
            return
        temp = self.tail
        # Check if tail node is to be deleted
        if self.tail.data == data:
            print("Deleted node is " + str(self.tail.data))
            self.tail = temp.previous
            return
        while temp.previous:
            if temp.previous.data == data:
                print("Node deleted is " + str(temp.previous.data))
                temp.previous = temp.previous.previous
                return
            temp = temp.previous
        print("Node not found")

# Create search() function
    # Search a given data in the nodes  
    def search(self, data):
        if not self.tail:
            return False
        current = self.tail
        while current:
            if current.data == data:
                return True
            else: 
                current = current.previous
        return False

# test the output:
first_node = Node(11)            
reverse_linked_list = ReverseLinkedList(first_node)
reverse_linked_list.insert(3)
reverse_linked_list.insert(6)
reverse_linked_list.insert(5)

print("The Reverse Linked List is (after insertion):")
reverse_linked_list.print_list()

reverse_linked_list.delete(6)
print("The Reverse Linked List is (after deleting 6):")
reverse_linked_list.print_list()

print("Does 5 exist in the Reserve Liked List?")
print(reverse_linked_list.search(5))

print("Does 17 exist in the Reserve Liked List?")
print(reverse_linked_list.search(17))