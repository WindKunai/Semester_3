class Node:
    def __init__(self, data):
        self.head = data
        self.next = None 

class LinkedList:
    def __init__(self):
        self.head = None
    
    def printlist(self):
        temp = self.head
        if (temp != None):
            while(temp != None):
                print(temp.head, end  =" ")
                temp = temp.next
            print("")
        else:
            print("List is empty")
    
    #def pushfront(self, data):
    #    node = Node(data)
    #    self.head = node
    #    self.next = 

    def append(self, data):
        newnode = Node(data)

        temp = self.head
        while(temp.next != None):
            temp = temp.next

        temp.next = newnode

    def remove_front(self):
        temp = self.head
        self.head = temp.next 
        temp = None

    def pushfront(self, data):
        temp = self.head
        self.head = data
        temp = None



    def pop(self):
        temp = self.head
        while(temp.next.next != None):
            temp = temp.next

        temp.next = None

    def len_of_list(self):
        temp = self.head
        length = 1
        while (temp.next != None):
            temp = temp.next
            length += 1
        return length

    def push_at(self, data, position):
        newnode = Node(data)
        leng = self.len_of_list()


        if position == 1:
            self.pushfront(data)
        
        elif position > leng:
            print("out of range")
        
        else:
            temp = self.head
            position -= 1
            for i in range(position):
                temp = temp.next

            
            newnode.next = temp.next.next
            temp.next = newnode

    def push_atM(self, data, position):
        newnode = Node(data)
        leng = self.len_of_list()


        if position == 1:
            self.pushfront(data)
        
        elif position > leng:
            print("out of range")
        
        else:
            temp = self.head
            i = 1
            while(i > position):
                temp = temp.next
                i += 1
            newnode.next = temp.next.next
            temp.next = newnode 



mylist = LinkedList()

node1 = Node(10)
mylist.head = node1

node2 = Node(20)
node1.next = node2

node3 = Node(30)
node2.next = node3

node4 = Node(40)
node3.next = node4

mylist.printlist()

newnode = Node(5)
mylist.head = newnode
newnode.next = node1
mylist.printlist()

mylist.append(60)
mylist.printlist()

mylist.pop()
mylist.printlist()

mylist.push_at(3, 3)
mylist.printlist()

mylist.push_atM(19, 3)
mylist.printlist()

print(mylist.len_of_list())
