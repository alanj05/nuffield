import linkedlist  ##Use the name of your linkedlist file in the same folder


def What(myLL, n):
     if n == 0:
         return myLL
     else:
         node = myLL.RemoveAtPosition(0)
         myLL.InsertNode(node)
         return What(myLL, n-1)

myLinkedList = linkedlist(5,1,3,4,2,9)
print(What(myLinkedList, 2))
