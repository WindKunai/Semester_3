class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList:

    def __init__(self, *args, **kwargs):
        self.head = Node(None)

    def push(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def printList(self):
        node = self.head
        while node.next is not None:
            print(node.data, end=" ")
            node = node.next

    def countNodes(self):
        count = 0
        node = self.head
        while node.next is not None:
            count += 1
            node = node.next
        return count

    def swapKth(self, k):
        n = self.countNodes()

        if n < 2 * k:
            print("K value too big")

        elif n < k:
            return print("K value too big")

        elif (2 * k - 1) == n:
            return print("K value out of range")
        else:
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

            if y_prev is not None:
                y_prev.next = x

            temp = x.next
            x.next = y.next
            y.next = temp

            if k == 1:
                self.head = y

            if k == n:
                self.head = x

if __name__ == "__main__":
    llist = LinkedList()
    for i in range(8, 0, -1):
        llist.push(i)
    llist.printList()
    print("\n")
    k = int(input("Give K value: "))
    for i in range(1, k+1):
        llist.swapKth(i)
    print("Modified List for k =", k)
    llist.printList()
    print("\n")
