class Node():
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

    def __repr__(self):
        return repr(self.name)
    

n = Node('rifat', 12)
print(n)
        