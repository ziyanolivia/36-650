class Queue:
    inner_list = []
    counter = 0
    def enqueue(self, value):
        self.inner_list.insert(self.counter,value)
        self.counter = self.counter + 1
    def dequeue(self):
        value = self.inner_list.pop(0)
        self.counter = self.counter - 1
        return value
    def delete(self, value):
        for i in range(self.counter):
            first_value = self.dequeue()
            if first_value != value:
                self.enqueue(first_value)
        
# test the output:
obj = Queue()
obj.enqueue(5)
obj.enqueue(7)
obj.enqueue(13)
obj.enqueue(4)
obj.enqueue(7)
print("The Queue is:")
print(obj.inner_list)
obj.delete(7) 
print("After deleting 7, the Queue is:")
print(obj.inner_list)
print(obj.dequeue()) # Should return 5