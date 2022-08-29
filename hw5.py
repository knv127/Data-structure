MAX_QSIZE = 20
class CircularDeque :	          
    def __init__( self ) :		                  
        self.front = 0			
        self.rear = 0			
        self.items = [None] * MAX_QSIZE

    def isEmpty( self ) : return self.front == self.rear
    def isFull( self ) : return self.front == (self.rear+1)%MAX_QSIZE
    def clear( self ) : self.front = self.rear

    def size( self ) :
       return (self.rear - self.front + MAX_QSIZE) % MAX_QSIZE			                  

    def addRear( self, item ):
        if not self.isFull():
            self.rear = (self.rear+1)% MAX_QSIZE
            self.items[self.rear] = item

    def deleteFront( self ):
        if not self.isEmpty():
            self.front = (self.front+1) % MAX_QSIZE
            return self.items[self.front]

    def getFront( self ):
        if not self.isEmpty():
            return self.items[(self.front + 1) % MAX_QSIZE]
   
    def addFront(self, item):			          
        if not self.isFull():
            self.items[self.front] = item        
            self.front = self.front - 1		      
            if self.front < 0 : self.front = MAX_QSIZE - 1

    def deleteRear( self ):			      
        if not self.isEmpty():
            item = self.items[self.rear]
            self.rear = self.rear - 1		
            if self.rear < 0 : self.rear = MAX_QSIZE - 1
            return item			     

    def getRear( self ):			 
        return self.items[self.rear]



def palindrome(statement):
    dq = CircularDeque()
    s = statement.lower()
    for i in s:
        if i.isalnum():
            dq.addRear(i)

    for i in range(dq.size() // 2):
        if dq.deleteFront() != dq.deleteRear():
            return False
        else:
            return True

n = palindrome("leddel")
print(n)


