class Node:

    def __init__(self, dataField, nxtNode = None, prvNode = None):
        self.dataField = dataField
        self.nxtNode = nxtNode
        self.prvNode = prvNode


    def __str__(self):
        #Python will use this method if you try to print your object.
        txt = "\nData field: \t" + str(self.dataField)
        if self.prvNode != None:
            txt += "\n" + "Previous node:\t" + str(self.prvNode.dataField)
        if self.nxtNode != None:
            txt += "\n" + "Next node:\t" + str(self.nxtNode.dataField)
        return txt

    def GetNxtNode(self):
        return self.nxtNode

    def GetPrvNode(self):
        return self.prvNode

    def GetDataField(self):
        return self.dataField

    def SetNxtNode(self, nxtNode):
        self.nxtNode = nxtNode

    def SetPrvNode(self, prvNode):
        self.prvNode = prvNode

    def SetDataField(self, dataField):
        self.dataField = dataField

    
class LinkedList:

    def __init__(self, *dataValues):
        self.head = None #None = empty list
        self.tail = None
        #Add any data supplied to this constructor.
        for dataValue in dataValues:
            self.InsertNode(Node(dataValue))

    def __str__(self):
        if self.IsEmpty():
            txt = "\nThe list is empty!"
        else:
            txt = "\nLinked-list:\n" + str(self.GetLinkedList())
        return txt


    def IsEmpty(self):
        return self.GetHead() == None

    def GetHead(self):
        return self.head

    def GetTail(self):
        return self.tail

    def SetHead(self, newHead):
        self.head = newHead

    def SetTail(self, newTail):
        self.tail = newTail

    def GetLinkedList(self):
        orderedList = []
        if not self.IsEmpty():
            currentNode = self.GetHead()
            while currentNode != None:
                orderedList.append(currentNode.dataField)
                currentNode = currentNode.GetNxtNode()
        return orderedList
    
    def Length(self):
        return len(self.GetLinkedList())

    def AddNode(self,node, prvNode, nxtNode):
        node.SetNxtNode(nxtNode)
        node.SetPrvNode(prvNode)
        if prvNode == None:
            self.SetHead(node)
        else:
            prvNode.SetNxtNode(node)
        if nxtNode == None:
            self.SetTail(node)
        else:
            nxtNode.SetPrvNode(node)


    def GetNodeAt(self, posInLinkedList):
        if self.IsEmpty():
            return None
        currentNode = self.GetHead()
        indexPos = 0
        while currentNode != None:
            if indexPos == posInLinkedList:
                return currentNode
            currentNode = currentNode.GetNxtNode()
            indexPos += 1
        return None #Not enough positions in list


    def InsertNode(self, newNode, posNxtNode = None):
        if posNxtNode == None or posNxtNode > self.Length():
            #Append to end of list
            posNxtNode = self.Length()

        prvNode = self.GetNodeAt(posNxtNode - 1)
        nxtNode = self.GetNodeAt(posNxtNode)
        self.AddNode(newNode, prvNode, nxtNode)


    def RemoveAtPosition(self, posInLinkedList):
        deadNode = self.GetNodeAt(posInLinkedList)
        if deadNode == None:
            print("No node to remove at that position!")
            return None
        
        prvNode = deadNode.GetPrvNode()
        nxtNode = deadNode.GetNxtNode()

        if nxtNode == None:
            self.SetTail(prvNode)
        else:
            nxtNode.SetPrvNode(prvNode)
        if prvNode == None:
            self.SetHead(nxtNode)
        else:
            prvNode.SetNxtNode(nxtNode)

        return deadNode


