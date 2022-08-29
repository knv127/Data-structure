#P7.1
class ArrayList:		  
    def __init__( self ):
        self.items = []		

    def insert(self, pos, elem) :
        self.items.insert(pos, elem)
    def delete(self, pos) :
        self.items.pop(pos)
    def isEmpty( self ):
        return self.size() == 0
    def getEntry(self, pos) :
        return self.items[pos]
    def size( self ):
        return len(self.items)
    def clear( self ) :
        self.items = []	
    def find(self, item) :
        return self.items.index(item)
    def replace(self, pos, elem) :
        self.items[pos] = elem
    def sort(self) :
        n = self.size()
        for i in range(1, n) :				
            key = self.items[i]
            j = i-1
            while j>=0 and self.items[j] > key :		
                self.items[j + 1] = self.items[j]				
                j -= 1
            self.items[j + 1] = key
    def merge(self, lst) :
        self.items.extend(lst)
    def display(self, msg='ArrayList:' ):
        print(msg, self.size(), self.items)

s = ArrayList()
s.display('파이썬 리스트로 구현한 리스트 테스트')
s.insert(0, 10);		s.insert(0, 20);     s.insert(1, 30)
s.insert(s.size(), 40);		s.insert(2, 50)
s.display("파이썬 리스트로 구현한 List(삽입x5): ")
s.sort()
s.display("파이썬 리스트로 구현한 List(정렬후): ")

#P7.2
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

    def sort(self):
        n = self.size()
        for i in range(n-1, 0, -1) :		
            bChanged = False
            for j in range (i) :
                s = self.getNode(j)
                n = s.link
                d = self.getNode(j-1)
                if d == None:			
                    if s.data > n.data :
                        s.link = s.link.link
                        n.link = s
                        self.head = n                     
                        bChanged = True
                else:
                    if s.data > n.data :
                        d.link = n
                        s.link = n.link
                        n.link = s                     
                        bChanged = True		
            if not bChanged: break;

l = LinkedList()
l.display('파이썬 리스트로 구현한 리스트 테스트')
l.insert(0, 1);		l.insert(0, 2);     l.insert(1, 3)
l.insert(l.size(), 4);		l.insert(2, 5)
l.display("파이썬 리스트로 구현한 List(삽입x5): ")
l.sort()
l.display("파이썬 리스트로 구현한 List(정렬후): ")

#P7.3, 7.4
class Set:				        
    def __init__( self ):		
        self.items = []			

    def size( self ): 			
        return len(self.items)	
    def display(self, msg):		
        print(msg, self.items)	

#    def contains(self, item) :
#       return item in self.items

    def contains(self, item) :
        for i in range(len(self.items)):
            if self.items[i] == item :	
                return True
        return False		

    def delete(self, elem) :
        if elem in self.items :
           self.items.remove(elem)
		            

    def insert(self, elem) :                
            if elem in self.items : return      
            for idx in range(len(self.items)) : 
                if elem < self.items[idx] :     
                    self.items.insert(idx, elem)
                    return
            self.items.append(elem)             


    def __eq__( self, setB ):       	
            if self.size() != setB.size() :	
                return False
            for idx in range(len(self.items)): 			
                if self.items[idx] != setB.items[idx] :	
                    return False
            return True

    def union( self, setB ):        	
        newSet = Set()					
        a = 0							
        b = 0							
        while a < len( self.items ) and b < len( setB.items ) :
            valueA = self.items[a]		
            valueB = setB.items[b]		
            if valueA < valueB :		
                newSet.items.append( valueA )	
                a += 1					
            elif valueA > valueB :		
                newSet.items.append( valueB )	
                b += 1			
            else : 				
                newSet.items.append( valueA )	
                a += 1					
                b += 1
        while a < len( self.items ):	
            newSet.items.append( self.items[a] )
            a += 1
        while b < len( setB.items) :	
            newSet.items.append( setB.items[b] )
            b += 1
        return newSet

    def intersect( self, setB ):	
        setC = Set()
        a = 0							
        b = 0	
        while a < len( self.items ) and b < len( setB.items ) :
            valueA = self.items[a]		
            valueB = setB.items[b]
            if valueA < valueB :		
                a += 1					
            elif valueA > valueB :		
                b += 1			
            else : 				
                setC.items.append( valueA )	
                a += 1					
                b += 1		
        return setC

    def difference( self, setB ):	    
        newSet = Set()					
        a = 0							
        b = 0							
        while a < len( self.items ) and b < len( setB.items ) :
            valueA = self.items[a]		
            valueB = setB.items[b]		
            if valueA < valueB :		
                newSet.items.append( valueA )	
                a += 1					
            elif valueA > valueB :		
                b += 1			
            else : 				
                a += 1					
                b += 1
        while a < len( self.items ):	
            newSet.items.append( self.items[a] )
            a += 1
        return newSet

#P7.5
def binary_search(A, key, low, high) :
	if (low <= high) :				        
		middle = (low + high) // 2	        
		if key == A[middle].key :		    
			return middle
		elif (key<A[middle].key) :	        
			return binary_search(A, key, low, middle - 1)
		else :						
			return binary_search(A, key, middle + 1, high)
	return None

class Entry:
    def __init__( self, key, value ):
        self.key = key
        self.value = value

    def __str__( self ):
        return str("%s:%s"%(self.key, self.value) )

class Binary_searchMap:							
    def __init__( self ):
        self.table = []					    	

    def size( self ): return len(self.table)	
    def display(self, msg):				    	
        print(msg)
        for entry in self.table :				
            print("  ", entry)					

    def insert(self, key, value) :				
        self.table.append(Entry(key, value))	

    def search(self, key) :             		
        pos = binary_search(self.table, key, 0, self.size()-1)
        if pos is not None : return self.table[pos]
        else : return None

    def delete(self, key) :					
        for i in range(self.size()):
            if self.table[i].key == key :	
                self.table.pop(i)			
                return

#P7.6
class LinearprobingMap:						
    def __init__( self, M ):
        self.table = [None]*M			
        self.M = M

    def hashFn(self, key) :							
        return key % self.M

    def insert(self, value) :		
        idx = self.hashFn(value)
        if self.table[idx] == None: 
            self.table[idx] = value
        else:
            if idx == self.M+1:
                idx == 0
                while self.table[idx] != None:
                    idx += 1
                self.table[idx] = value
            

    def search(self, key) :
        idx = self.hashFn(key)
        if self.table[idx] == key:
            return self.table[idx]

        while self.table[idx] == None:
            idx += 1
            if self.table[idx] == key:
                return self.table[idx]
            if idx == self.M+1:
                idx == 0
        return None

    def delete(self, key) :
        idx = self.hashFn(key)
        use = []
        if self.table[idx] == key :
            self.table.pop(idx)
            use.append(idx)
            return

        while self.table[idx] != None and idx not in use:         		
            idx += 1
            if self.table[idx] == key:
                self.table.pop(idx)
                use.append(idx) 
            if idx == self.M+1:
                idx == 0
        return None
                					

    def display(self, msg):
        print(msg)
        for idx in range(len(self.table)) :
            print("[%2d] -> "%idx, end='')
            print(self.table[idx], end=' ')
            print()

'''map = LinearprobingMap(13)						
map.insert(45)					
map.insert(27)
map.insert(88)
map.insert(9)
map.insert(71)
map.insert(60)
map.insert(46)
map.insert(38)
map.insert(24)	
map.display("나의 단어장: ")			

print(map.search(46))	
print(map.search(39))

map.delete(60)
map.delete(46)								
map.display("나의 단어장: ")'''