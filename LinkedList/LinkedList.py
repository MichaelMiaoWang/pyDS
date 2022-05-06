class Node:
    def __init__(self,initData):
        self.data = initData
        self.next = None
    
    def getData(self):
        return self.data

    def getNext(self):
        return self.next
    
    def setData(self,newData):
        self.data = newData
    
    def setNext(self,nextNode):
        self.next = nextNode


class LinkedList:
    def __init__(self,headInitData):
        self.head = Node(headInitData)
        self.head.next = None
        self.currentNode = self.head


    def add(self,data):
        tempNode = Node(data)
        self.currentNode.setNext(tempNode)
        self.currentNode = tempNode
    
    # Return the index when data2search was first found, otherwise return -1
    def search(self,dataToSearch):
        currentNode = self.head
        idxFound = -1
        idxCount = 0
        while currentNode != None and idxFound == -1:
            if currentNode.getData() == dataToSearch:
                idxFound = idxCount
                break
            else:
                currentNode = currentNode.getNext()
                idxCount += 1
                continue
        return idxFound
    
    def printLinkedList(self):
        currentNode = self.head
        print("head",end = "->")
        while currentNode != None:
            print(currentNode.getData(), end = '->')
            currentNode = currentNode.getNext()
        print("None")    

# an easy test case
if __name__ == '__main__':
    list = LinkedList(233)
    for x in range(20):
        list.add(x)
    list.printLinkedList()
    print("0 first found at:", list.search(0))