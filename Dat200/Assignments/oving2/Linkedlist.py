class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None

  def printlist(self):
    temp = self.head
    if (temp != None):
      print('list contains: ')
      while(temp != None):
        if temp.next == None:
          print(temp.data, end = '')
        else:
          print(temp.data, end = ' -> ')
        temp = temp.next
      print("\n")
    else:
      print('List is empty')

  def pushfront(self, data):
     node = Node(data)
     temp = self.head
     node.next = temp
     self.head = node

  def pushback(self, data):
    newnode = Node(data)
    temp = self.head
    while(temp.next != None):
        temp = temp.next
    temp.next = newnode

  def remove_front(self):
    temp = self.head
    self.head = temp.next
    temp = None

  def remove_back(self):
     temp = self.head
     while(temp.next.next != None):
        temp = temp.next
     temp.next = None

  def count(self, x):
     temp = self.head
     count = 0

     while(temp != None):
       if temp.data == x:
        count += 1
       temp = temp.next
     return count

  def getminmax(self):
    temp = self.head
    min = self.head.data
    max = self.head.data
    while(temp != None):
      if (temp.data < min):
        min = temp.data
      elif (temp.data > max):
        max = temp.data
      temp = temp.next
    return min, max

  def delete_front(self):
      if(self.head != None):
          temp = self.head
          self.head = temp.next
          temp = None

  def delete_end(self):
      temp = self.head
      while (temp.next.next != None):
          temp = temp.next
          temp.next = None

  def remove_dupes(self):
          if not self.head:
              return

          current = self.head
          templist = set()
          previous = None

          while current:
              if current.data in templist:
                  print(f"Duplicate of number {current.data} found, now removed")
                  previous.next = current.next
              else:
                  templist.add(current.data)
                  previous = current
              current = current.next



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
min, max = mylist.getminmax()
print(f"min is: {min} \nmax is: {max}")
node5 = Node(20)
node4.next = node5

node6 = Node(30)
node5.next = node6

mylist.printlist()

mylist.remove_dupes()
mylist.printlist()
