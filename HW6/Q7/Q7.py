# Create the data structure (custom data type and the organizer)
class Node:
    def __init__(self, data):
        self.too_big = None
        self.big = None
        self.small = None
        self.data = data # Node data
   
# Create the insert() function for this data structure
    def insert(self, data):
        if data - self.data >= 10:
            if self.too_big:
                self.too_big.insert(data)
            else:
                self.too_big = Node(data)
        elif data - self.data < 10 and data - self.data >= 0:
            if self.big:
                self.big.insert(data)
            else:
                self.big = Node(data)
        else:
            if self.small:
                self.small.insert(data)
            else:
                self.small = Node(data)

# Create the delete() function for this data structure                    
    def delete(self, data):
        all_values = []
        self.traversal_return(all_values)
        # Reset everything
        self.too_big = None
        self.big = None
        self.small = None
        self.data = None
        for val in all_values:
            if val == data:
                continue
            if not self.data:
                self.data = val
            else:
                self.insert(val)
    
    def traversal_return(self, return_values=None):
        if self.small:
            self.small.traversal_return(return_values)
        if return_values is not None:
            return_values.append(self.data)
        if self.big:
            self.big.traversal_return(return_values)
        if self.too_big:
            self.too_big.traversal_return(return_values)

 # Create traversal() function for this data structure   
    def traversal(self):
        if self.small:
            self.small.traversal()
        print(self.data)
        if self.big:
            self.big.traversal()
        if self.too_big:
            self.too_big.traversal()

# test the output:
root = Node(20) # Instantiate the tree
root.insert(40)
root.insert(29)
root.insert(45)
root.insert(32)
root.insert(10)
print("Tree contents after insertion using the traversal():")
root.traversal()
root.delete(45)
print("Tree contents after deleting 45 using the traversal():")
root.traversal()