class Noda:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def printlist(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def push(self,new_data):
        new_data = Noda(new_data)
        new_data.next = self.head
        self.head = new_data

    def insertAfter(self,prev_node,new_data):
        if prev_node is None:
            print("tugun mavjud emas!")
            return
        new_node = Noda(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node
    def append(self,new_data):
        new_node = Noda(new_data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def deleteNode(self,key):
        temp = self.head
        if (temp and temp.data == key ):
            self.head = temp.next
            temp = None
            return
        while temp:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        if temp==None:
            return
        prev.next = temp.next
        temp = None