class Queue:
	def __init__(self, list_size):
		self.queue_list = [0] * list_size
		print(self.queue_list)

		self.total_size = list_size
		self.current_size = 0

		self.head = 0
		self.tail = 0
        
        
	def enqueue(self, item):
		if self.current_size == self.total_size:
			print('Queue is full!')
			return
		
		print("Inserting", item)
		self.queue_list[self.tail] = item
		self.tail = (self.tail +1) % self.total_size
		self.current_size += 1
		

	def dequeue(self):
		if self.total_size == 0:
			print('Queue is empty!')
			return
		
		item = self.queue_list[self.head]
		print("Remove", item)
		self.head = (self.head +1) % self.total_size 
		self.current_size -= 1

		return item
	

q = Queue(3)
q.enqueue("Rifat")
print(q.queue_list)

q.enqueue("Jamil")
print(q.queue_list)

q.enqueue("Ibrahim")
print(q.queue_list)

q.enqueue("Khalid")
print(q.queue_list)

q.dequeue()
print(q.queue_list)

q.dequeue()
print(q.queue_list) 

q.enqueue("Ibrahim")
print(q.queue_list)

q.enqueue("Khalid")
print(q.queue_list)