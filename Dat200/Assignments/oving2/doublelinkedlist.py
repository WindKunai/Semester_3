#for å sette opp circular linked list:

class Node:
  def __init__(self, data):
    self.data = data
    self.next = None
    self.prev = None
    self.first = None

class circularsingleLinkedList:
  def __init__(self):
    self.head = None

  def printlist(self):
    temp = self.head
    if (temp != None):
      print('list contains: ')
      while(temp.next != self.head ):
        if temp.next == node1:
           print(temp.data, end = '')
        else:
            print(temp.data, end = ' -> ')
        temp = temp.next

      print(temp.data)
      print("\n")
    else:
      print('List is empty')

  def pushfront(self, data):
        temp = self.head
        self.head = data
        temp = None

  def remove_dupes(self):
    if not self.head:
        return

    current = self.head
    templist = set()

    while True:
        if current.data in templist:
            print(f"Duplicate of number {current.data} found, now removed")
            current.prev.next = current.next
            current.next.prev = current.prev
        else:
            templist.add(current.data)

        current = current.next

        if current == self.head:
            break


  def swap_first_last_k(self, k):
        length = self.len_of_list()
        if k > length // 2:
            print("Cannot swap. K is too large.")
            return

        first_k = self.head
        last_k = self.head

        # Move the last_k pointer to the Kth node from the end
        for _ in range(length - k):
            last_k = last_k.next

        for _ in range(k):
            first_k.data, last_k.data = last_k.data, first_k.data
            first_k = first_k.next
            last_k = last_k.next  # Move last_k forward, not backward

  def countNodes(self):
    count = 0
    node = self.head
    while node.next is not node1:
        count += 1
        node = node.next
    return count

  def swapKth(self, k):
  
        # Count nodes in linked list
        n = self.countNodes()
  
        # check if k is valid
        if n < k:
            return

        if (2 * k - 1) == n:
            return
  
        x = self.head
        x_prev = Node(None)
        for i in range(k - 1):
            x_prev = x
            x = x.next
  
        y = self.head
        y_prev = Node(None)
        for i in range(n - k):
            y_prev = y
            y = y.next
  
        if x_prev is not None:
            x_prev.next = y
  
        # Same thing applies to y_prev
        if y_prev is not None:
            y_prev.next = x
  
        temp = x.next
        x.next = y.next
        y.next = temp
  
        # Change head pointers when k is 1 or n
        if k == 1:
            self.head = y
  
        if k == n:
            self.head = x


  def len_of_list(self):
        temp = self.head
        length = 1
        while (temp.next != node1):
            temp = temp.next
            length += 1
        return length


mylist = circularsingleLinkedList()

node1 = Node(1)
mylist.head = node1

node2 = Node(2)
node1.next = node2


node3 = Node(3)
node2.next = node3
node2.prev = node1

node4 = Node(4)
node3.next = node4
node3.prev = node2

node5 = Node(5)
node4.next = node5
node4.prev = node3
node5.prev = node4

node6 = Node(1)
node5.next = node6
node6.prev = node5
node1.prev = node6

node7 = Node(6)
node6.next = node7
node7.prev = node6
node7.next = node1
node1.prev = node7



print("\n")
mylist.printlist()
mylist.remove_dupes()
mylist.printlist()

#mylist.swapKth(1)
# mylist.printlist()