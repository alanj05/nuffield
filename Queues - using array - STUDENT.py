class Queue:

    def __init__(self, maxArraySize = 10):
        self.nxtFreeIndex = 0
        self.start = 0 #Start / Front of queue
        self.queue = [0] * maxArraySize
        self.maxArraySize = maxArraySize
        self.maxQueueSize = maxArraySize - 1


    def __str__(self):
        if self.IsEmpty():
            txt = "\nThe queue is empty!"
        else:
            #Insert code to traverse the queue (wrapping if required)
            #And add the active queue contents to the txt variable.
            txt = ""

        txt += "\nMax queue size:\t\t" + str(self.maxQueueSize)
        txt += "\nUnderlying array:\t" + str(self.queue)
        return txt


    def Queue(self):
        #Returns active queue, not full underlying array.

        activeQueue = []
        queueIndex = self.start
        
        while queueIndex != self.nxtFreeIndex:
            activeQueue.append(self.queue[queueIndex])
            queueIndex = (self.queueIndex + 1) % maxArraySize
            
        return activeQueue


    def Size(self):
        #Returns size of active queue, not underlying array.
        
        return (self.nxtFreeIndex - self.start) % self.maxArraySize

    def IsEmpty(self):
        #Returns true or false, depending on whether queue is empty.

        return self.start == self.nxtFreeIndex - 1
        


    def IsFull(self):
        #Returns true or false, depending on whether queue is full.

        return self.start == self.nxtFreeIndex + 1

    def Peek(self):
        #Return None if stack is queue (use IsEmpty() to check)
        #Otherwise, return but do not remove start item.

        if self.IsEmpty:
            return None
        return self.start


    def Enqueue(self, *dataFields):
        #Use IsFull() to check if the queue is currently full.
        #If so, display an error message.

        #If the stack is not full, create a loop to iterate through
        #the varying number of dataFields supplied to the method.
        #Add each dataField to the end of the queue.
        #What other variable will you need to update ...?

        for dataField in dataFields:
            if self.IsFull():
                return None

            self.queue[self.nxtFreeIndex] = dataField
            self.nxtFreeIndex = (self.nxtFreeIndex + 1) % self.maxArraySize
            


    def Dequeue(self):
        #Use IsEmpty() to check if the queue is currently empty.
        #If so, display an error message.

        #If the queue is not empty, retrieve start data value in queue.
        #What other variable will you need to update ...?
        #NOTE: there is no need to actually delete the data value from the array.
        #Remember to return the retrieved item.

        if self.IsEmpty():
            return None

        value = self.queue[self.start]
        self.start = (self.start + 1) % self.maxArraySize
        return value


myQueue = Queue()
myQueue.Enqueue(5, 8, 4)
print(myQueue)
myQueue.Enqueue(3, -1)
print(myQueue)
print(myQueue.Peek())
myQueue.Enqueue(7)
print(myQueue)
myQueue.Enqueue(66)
print(myQueue)
myQueue.Dequeue()
print(myQueue)
myQueue.Dequeue()
print(myQueue)
myQueue.Enqueue(12)
print(myQueue)
myQueue.Enqueue(99)
print(myQueue)
myQueue.Enqueue(16)
print(myQueue)
myQueue.Enqueue(23)
print(myQueue)
myQueue.Enqueue(12)
print(myQueue)
myQueue.Dequeue()
print(myQueue)
myQueue.Dequeue()
print(myQueue)
myQueue.Dequeue()
print(myQueue)
myQueue.Dequeue()
print(myQueue)
myQueue.Dequeue()
print(myQueue)
myQueue.Dequeue()
print(myQueue)
print(myQueue.Peek())
myQueue.Dequeue()
print(myQueue)
myQueue.Enqueue(4,7,3,6,8,4,2,88)
print(myQueue)
myQueue.Dequeue()
print(myQueue)
myQueue.Enqueue(881)
print(myQueue)
myQueue.Dequeue()
print(myQueue)
