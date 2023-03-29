class Queue:
    def __init__(self, size):
        self.items = [0] * size
        self.max_size = size
        self.head, self.tail, self.size = 0, 0, 0

    def is_empty(self):
        if self.size == 0:
            return True
        return False

    def is_full(self):
        if self.size == self.max_size:
            return True
        return False       

    def enqueue(self, item):
        if self.is_full():
            print("Queue Completed")
            return
        
        print("Inserting", item)
        self.items[self.tail] = item
        self.tail = (self.tail +1) % self.max_size
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            print("Queue Empty")
            return


        item = self.items[self.head]
        print('Remove', item)
        self.head = (self.head +1) % self.max_size
        self.size -= 1
        return item
    


if __name__== '__main__':
    q = Queue(3)
    print(q.items)


    q.enqueue('Rifat')

    print(q.items)

    print(q.tail)


    print(q.items)




    print(q.head)




