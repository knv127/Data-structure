#6장 연습문제 
class Node:				                    
    def __init__ (self, elem, link=None):	
        self.data = elem 			        
        self.link = link
#6.2
class LinkedStack :
    def __init__( self ):	
        self.top = None
        self.s = 0	    

    def isEmpty( self ): return self.s == 0
    def clear( self ): self.top = None		    
    def push( self, item ):	                	
        n = Node(item, self.top)	        	
        self.top = n
        self.s += 1			

    def pop( self ):			
        if not self.isEmpty():	
            n = self.top		
            self.top = n.link
            self.s -= 1	
            return n.data		

    def peek( self ):			
        if not self.isEmpty():	
            return self.top.data

    def size( self ):			
        return self.s			

    def display( self, msg='LinkedStack:'): 
        print(msg, end='')		
        node = self.top			
        while not node == None :	 	
            print(node.data, end=' ')	
            node = node.link		    
        print()
   



#6.12
class CircularLinkedQueue:
    def __init__( self ):		
        self.tail = None			

    def isEmpty( self ): return self.tail == None 
    def clear( self ): self.tail = None		
    def peek( self ):				        
        if not self.isEmpty():			    
            return self.tail.link.data		

    def enqueue( self, item ):	
        node = Node(item, None)	
        if self.isEmpty() :		
           node.link = node		
           self.tail = node		
        else :				           
            node.link = self.tail.link	
            self.tail.link = node	   
            self.tail = node		   

    def dequeue( self ):
        if not self.isEmpty():
            data = self.tail.link.data		   
            if self.tail.link == self.tail :
                self.tail = None		               
            else:			                	
                self.tail.link = self.tail.link.link
            return data			

    def size( self ):
        if self.isEmpty() : return 0	
        else :				            
            count = 1			        
            node = self.tail.link   	
            while not node == self.tail:
                node = node.link        
                count += 1		        
            return count		        

    def display( self, msg='CircularLinkedQueue:' ):
        print(msg, end='')
        if not self.isEmpty() :
            node = self.tail.link		    
            while not node == self.tail :	
                print(node.data, end=' ')	
                node = node.link		    
            print(node.data, end=' ')		
        print()

def queue():
    q = CircularLinkedQueue()
    m = int(input("양의 정수를 입력하세요(종료: -1): "))
    while m != -1:
        q.enqueue(m)
        m = int(input("양의 정수를 입력하세요(종료: -1): "))
    for i in range(q.size()):
        print(q.dequeue(),"-> ", end='')
        if q.isEmpty():
            print("None")


#6.13
class LinkedList:			
    def __init__( self ):			
        self.head = None			

    def isEmpty( self ): return self.head == None	
    def clear( self ) : self.head = None		    

    def size( self ):			
        node = self.head		
        count = 0
        while not node == None :
            node = node.link	
            count += 1			
        return count			

    def display( self, msg='LinkedList:'): 
        print(msg, end='')		        
        node = self.head			    
        while not node == None :		
            print(node.data, end=' ')	
            node = node.link		    
        print()

    def getNode(self, pos) :		     
        if pos < 0 : return None
        node = self.head;			     
        while pos > 0 and node != None :
            node = node.link		     
            pos -= 1			         
        return node	

    def getEntry(self, pos) :		    
        node = self.getNode(pos)		
        if node == None : return None	
        else : return node.data		    

    def replace(self, pos, elem) :	    
        node = self.getNode(pos)		
        if node != None: node.data = elem	

    def find(self, data) :		    
        node = self.head;
        while node is not None:		
            if node.data == data : return node	
            node = node.link
        return node			

    def insert(self, pos, elem) :
        before = self.getNode(pos-1)		    
        if before == None :         		    
            self.head = Node(elem, self.head)	
        else :					                
            node = Node(elem, before.link)		
            before.link = node		


    def delete(self, pos) :
        before = self.getNode(pos-1)		
        if before == None :         		
            if self.head is not None :		
                self.head = self.head.link	
        elif before.link != None :		    
            before.link = before.link.link
#P6.2
    def merge(self, list):
        if not list.isEmpty():
            n = self.getNode(self.size()-1)
            n.link = list.head
            list.clear()


l = LinkedList()
def l_list():
    a = int(input("노드의 개수: "))
    for i in range(a):
        data = int(input("노드 #%s 데이터: " % str(i+1)))
        l.insert(i, data)
    print("생성된 연결리스트: ",end='')
    for i in range(l.size()):
        print(l.getEntry(i),"-> ",end='')
    print()

#6.14
def data_add():
    add = input("끝에 추가할 데이터: ")
    l.insert(l.size(), add)

#6.15
def delete():
    l.delete(0)
    print("첫 번째 노드 삭제 후 연결 리스트: ",end='')
    for i in range(l.size()):
        print(l.getEntry(i),"-> ",end='')


#6.16
def print_sum():
    sum = 0
    for i in range(l.size()):
        sum = sum + l.getEntry(i)
    print("연결 리스트의 데이터 합: ", sum)


#6.17
def count():
    c =0
    a = int(input("탐색할 값을 입력하시오: "))
    for i in range(l.size()):
        if l.getEntry(i) == a:
            c += 1
    print("%d는 연결 리스트에서 %d번 나타납니다." %(a, c))


#P6.1
def palindrome(statement):
    s = LinkedStack()
    statement = statement.lower()
    str = ''
    for i in statement:
        if i.isalnum():
            s.push(i)
            str += i
    for i in range(s.size()):
        if str[i] != s.pop():
            return False
    return True

#P6.3
class linkedQueue:
    def __init__(self):
        self.front = None
        self.rear = None
    
    def isEmpty(self): return self.front ==  None
    def clear(self): self.front == self.rear == None
    def peek(self):
        if not self.isEmpty():
            return self.front.data
    
    def enqueue(self, item):
        n = Node(item, None)
        if not self.isEmpty():
            self.rear.link = n
            self.rear = n
        else:
            self.front = n
            self.rear = n

    def dequeue(self):
        if not self.isEmpty():
            data = self.front.data
            if self.front.link == None:
                self.front = None
                self.rear = None
            else:
                self.front = self.front.link
            return data
    
    def size(self):
        if self.isEmpty(): return 0
        else:
            count = 1
            node = self.front
            while node != None:
                node = node.link
                count += 1
        return count
    
    def display(self):
        if not self.isEmpty():
            node = self.front
            while node != None:
                print(node.data, end=' ')
                node = node.link
        print()


#P6.4
class DNode:				
    def __init__ (self, elem, prev = None, next = None):
        self.data = elem 
        self.prev = prev
        self.next = next

class LinkedList:			
    def __init__( self ):			
        self.head = None
        self.tail = None			

    def isEmpty( self ): return self.head == None	
    def clear( self ) : self.head = self.tail = None		    

    def size( self ):			
        node = self.head		
        count = 0
        while not node == None :
            node = node.next	
            count += 1			
        return count			

    def display( self, msg='LinkedList:'): 
        print(msg, end='')		        
        node = self.head			    
        while not node == None :		
            print(node.data, end=' ')	
            node = node.next		    
        print()

    def getNode(self, pos) :		     
        if pos < 0 : return None
        if pos+1 < self.size()-pos:
            node = self.head;			     
            for _ in range(pos) :
                node = node.next		     
        else:
            node = self.tail
            for _ in range(self.size()-pos-1):
                node = node.prev		     
        return node	

    def getEntry(self, pos) :		    
        node = self.getNode(pos)		
        if node == None : return None	
        else : return node.data		    

    def replace(self, pos, elem) :	    
        node = self.getNode(pos)		
        if node != None: node.data = elem	

    def find(self, data) :		    
        node = self.head;
        while node is not None:		
            if node.data == data : return node	
            node = node.next
        return node			

    def insert(self, pos, elem) :
        before = self.getNode(pos-1)
        node = DNode(elem, None, None)		    
        if self.isEmpty() :         		    
            self.head = self.tail = node
        elif before == None :					                
            node.next = self.head
            self.head.prev = node		
            self.head = node
        elif before.next == None:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        else:
            node.prev = before
            node.next = before.next
            before.next.prev = node
            before.next = node
            

    def delete(self, pos) :
        if not self.isEmpty():
            p = self.getNode(pos)
            if p.prev == None :         				
                self.head = self.head.next
                self.head.prev = None
            elif p.next == None :		    
                p.prev.next = p.next
                self.tail = p.prev
            else:
                p.prev.next = p.next
                p.next.prev = p.prev



s = LinkedList()
s.display('단순연결리스트로 구현한 리스트(초기상태):')
s.insert(0, 10);	s.insert(0, 20);     s.insert(1, 30)
s.insert(s.size(), 40);	s.insert(2, 50)
s.display("단순연결리스트로 구현한 리스트(삽입x5): ")
s.replace(2, 90)
s.display("단순연결리스트로 구현한 리스트(교체x1): ")
s.delete(2);	s.delete(s.size() - 1);	s.delete(0)
s.display("단순연결리스트로 구현한 리스트(삭제x3): ")
s.clear()
s.display("단순연결리스트로 구현한 리스트(정리후): ")