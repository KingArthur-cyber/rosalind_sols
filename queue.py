#Simple Queue
class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self,value):
        self.queue.append(value)
    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)
    def print_queue(self):
        print(self.queue)
    def size(self):
        return len(self.queue)
queue =  Queue()
for i in range(0,10):
    queue.enqueue(i)
queue.print_queue()
queue.dequeue()
queue.print_queue()

#Priority Queue
