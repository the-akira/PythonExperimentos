class Node:
    def __init__(self, data=None):
        self.data = data 
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = Node()

    def append(self, data):
        new_node = Node(data)
        cur = self.head 
        while cur.next != None:
            cur = cur.next 
        cur.next = new_node 

    def length(self):
        cur = self.head 
        total = 0
        while cur.next != None:
            total += 1 
            cur = cur.next
        return total 

    def display(self):
        elems = []
        cur_node = self.head 
        while cur_node.next != None:
            cur_node = cur_node.next 
            elems.append(cur_node.data)
        print(elems)

    def get(self, index):
        if index >= self.length():
            print('Error: Index out of range')
            return None
        cur_idx = 0
        cur_node = self.head 
        while True:
            cur_node = cur_node.next 
            if cur_idx == index:
                return cur_node.data
            cur_idx += 1

    def erase(self, index):
        if index >= self.length():
            print('ERROR: Index out of range')
            return 
        cur_idx = 0 
        cur_node = self.head 
        while True:
            last_node = cur_node 
            cur_node = cur_node.next 
            if cur_idx == index:
                last_node.next = cur_node.next 
                return 
            cur_idx += 1

linked_list = LinkedList()
linked_list.display()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)
linked_list.display()
linked_list.erase(1)
linked_list.display()

print(f'Tamanho da Linked List: {linked_list.length()}')
print(f'Elemento no 1º índice: {linked_list.get(1)}')
print(f'Elemento no 2º índice: {linked_list.get(2)}')