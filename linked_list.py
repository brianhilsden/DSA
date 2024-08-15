""" class Node:
    def __init__(self,data,next_node = None):
        self.data = data
        self.next_node = next_node

class Singly_Linked_List:
    def __init__(self,head = None,tail = None):
        self.head = head
        self.tail = tail

    def append(self, node):
        if self.head == None:
            self.head = node
            self.tail = node
            return

        self.tail.next_node = node
        self.tail = node

lst = Linked_List()
lst.append(Node("50"))
lst.append(Node(10))
 """


# Doubly linked list

class Node:
    def __init__(self, data, next_node = None, prev_node = None):
        self.data = data
        self.next_node = next_node
        self.prev_node = prev_node

class Doubly_Linked_List:
    def __init__(self,head = None, tail = None):
        self.head = head
        self.tail =tail

    def __repr__(self):
        nodes = []
        current = self.head

        while current:
            if current == self.head:
                nodes.append(f"Head: {self.head.data}")
            elif current == self.tail:
                nodes.append(f"Tail: {self.tail.data}")
            else:
                nodes.append(str(current.data))
            current = current.next_node

        if nodes:
            return "->".join(nodes)
        else:
            return "No nodes"


    def search(self,key):
        current = self.head

        while current:
            if current.data == key:
                return current
            current = current.next_node
        return False

    
    def append(self,node):
        if self.head == None:
            self.head = node
            self.tail = node
            return
        
        node.prev_node = self.tail
        self.tail.next_node = node
        self.tail = node

    def addToBegginning(self,data):
        current = self.head
        new_node = Node(data)
        current.prev_node = new_node
        new_node.next_node = current
        self.head = new_node
        
    def insert(self,data,index):
        position = 0
        current = self.head
        new_node = Node(data)
        if index == 0:
            new_node.next_node = current
            current.prev_node = new_node
            self.head = new_node
            return
            
        while current and position+1 != index:
            current = current.next_node
            position = position +1

        if current!= None:
            next_node = current.next_node
            new_node.next_node = next_node
            new_node.prev_node = current
            current.next_node  = new_node 
            if next_node is not None:
                next_node.prev_node = new_node
            else:
                 self.tail = new_node

        else:
            print( "Index not found")

    def deleteItem(self,key):
        node = self.search(key)
        if node:
            if node == self.head:
                if self.head.next_node:
                    next = node.next_node
                    next.prev_node = None
                    self.head = next
                else:
                    self.head = None
                    self.tail = None
            elif node == self.tail:
                prev= node.prev_node
                prev.next_node = None
                self.tail = prev
            else:
                next = node.next_node
                prev = node.prev_node
                next.prev_node = prev
                prev.next_node = next
        

    def deleteLast(self):
        if self.head == self.tail:
            self.head = None
            self.tail = None
            return
        else: 
            prev = self.tail.prev_node
            prev.next_node = None
            self.tail = prev 


lst = Doubly_Linked_List()
lst.append(Node(50))
lst.append(Node(10))
lst.append(Node(30))
lst.deleteItem(10)
print(lst)

            
#search, insert, insert_beginning 


