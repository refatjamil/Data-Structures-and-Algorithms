class Node:
    def __init__(self, data=None, nextt=None):
        self.data = data
        self.nextt = nextt

class LinkdList:
    def __init__(self):
        self.head = None

    def insert_at_beginner(self, data):
        node = Node(data, self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print("LinkedList is empty")
            return

        itr = self.head
        llstr = ''

        while itr:
            llstr += str(itr.data) + '---->'
            itr = itr.nextt

        print(llstr)

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head
        while itr.nextt:
            itr = itr.nextt

        itr.nextt = Node(data, None)

    def inser_value(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)    

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.nextt

        return count       

if __name__ == '__main__':
    ll = LinkdList()

    # ll.insert_at_end(79)
    # ll.insert_at_end(1)
    
    # ll.insert_at_end(19)
    # ll.print()
    ll.inser_value(["banana", 'mango', 'grapes', 'orenge'])
    ll.print()
    print((ll.get_length()))

