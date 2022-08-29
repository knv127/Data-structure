class Node:				                    
    def __init__ (self, elem, link=None):	
        self.data = elem 			        
        self.link = link

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
        node = self.head
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

class Term:
    def __init__(self, expo, coef):
        self.expo = expo
        self.coef = coef

class SprasePoly(LinkedList):

    def __init__(self):
        super().__init__()

    def read(self):
        a = input("계수 차수 입력(종료:-1): ")
        a = a.split()
        while not (a[1] == '-1' and a[0] == '-1'):
            a[0] = float(a[0])
            a[1] = int(a[1])
            self.insert(self.size(), Term(a[1], a[0]))
            a = input("계수 차수 입력(종료:-1): ")
            a = a.split()

    def display(self, msg='입력 다항식: '):
        print(msg, end='')		        
        node = self.head			    
        while not node == None :		
            print("%5.1fx^%d + " % (node.data.coef, node.data.expo), end=' ')	
            node = node.link		    
        print()

    def add(self, polyB):
        s = SprasePoly()
        node1 = self.head
        node2 = polyB.head
        while node1 != None and node2 != None :
            if node1.data.expo == node2.data.expo:
                s.insert(s.size(), Term(node1.data.expo, node1.data.coef + node2.data.coef))
                node1 = node1.link
                node2 = node2.link
            elif node1.data.expo < node2.data.expo:
                s.insert(s.size(), Term(node2.data.expo, node2.data.coef))
                node2 = node2.link
            elif node1.data.expo > node2.data.expo:
                s.insert(s.size(), Term(node1.data.expo, node1.data.coef))
                node1 = node1.link
        while node1 != None:
            s.insert(s.size(), Term(node1.data.expo, node1.data.coef))
            node1 = node1.link
        while node2 != None:
            s.insert(s.size(), Term(node2.data.expo, node2.data.coef))
            node2 = node2.link
        return s

a = SprasePoly()
a.read()
a.display()
b = SprasePoly()
b.read()
b.display()
c = a.add(b)
c.display("A+B= ")
                





