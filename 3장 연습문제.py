#3장 연습문제
#3.5
def find_max(list):
    a = list[0]
    for i in range(len(list)):
        if a < list[i]:
            a = list[i]
    return a

list = [1,3,7]
l2 = [2,4,5,8]
print(find_max(list))

#3.6
def find_minmax(list):
    min = list[0]
    max = list[0]
    for i in range(len(list)):
        if max < list[i]:
            max = list[i]
        if min > list[i]:
            min = list[i]
    return min, max

print(find_minmax(list))

#3.7
def same_item(list1, list2):
    for i in list1:
        if i in list2: return True
    return False

print(same_item(list, l2))

#3.8
def sum_list(l1, l2):
    c = []
    k = 0
    j = 0
    while k != len(l1) and j != len(l2):
        if l1[k] < l2[j]:
            c.append(l1[k])
            k += 1
        elif l1[k] > l2[j]:
            c.append(l2[j])
            j += 1
    while j != len(l2):
        c.append(l2[j])
        j += 1
    while k != len(l1):
        c.append(l1[k])
        k += 1
    return c


#3.9
class Set:				        
    def __init__( self ):		
        self.items = []			

    def size( self ): 			
        return len(self.items)	
    def display(self, msg =''):		
        print(msg, self.items)	

#    def contains(self, item) :
#       return item in self.items

    def contains(self, item) :
        for i in range(len(self.items)):
            if self.items[i] == item :	
                return True
        return False		

    def insert(self, elem) :
        if elem not in self.items :
           self.items.append(elem)

    def delete(self, elem) :
        if elem in self.items :
           self.items.remove(elem)

    def union( self, setB ):		    
        setC = Set()			        
        setC.items = list(self.items)	
        for elem in setB.items :	    
            if elem not in self.items :	
                setC.items.append(elem)	
        return setC			            

    def intersect( self, setB ):	
        setC = Set()
        for elem in setB.items :	
            if elem in self.items :	
                setC.items.append(elem)	
        return setC

    def difference( self, setB ):	    
        setC = Set()
        for elem in self.items:		    
            if elem not in setB.items:	
                setC.items.append(elem)	
        return setC

    def isproperSubset(self, setB):
        if setB.size() > self.size():
            c = self.intersect(setB)
            if self.items == c.items and self.items != setB.items:
                return True
        return False


#P3.1
items = []
def insert(pos, elem):
    n = len(items)
    if n == 0:
        items.append(elem)
    else:
        items.append(items[-1])
        for i in range(n-pos-1, 0, -1):
            items[pos+i] = items[pos+i-1]
        items[pos] = elem

def delete(pos):
    new = items[pos+1:len(items)]
    for i in range(len(items)-pos):
        items.pop(-1)
    items.extend(new)

def find(item):
    for i in range(len(items)):
        if items[i] == item:
            return i

def merge(list):
    for i in list:
        insert(len(items), i)

insert(0, 10);		insert(0, 20);     insert(1, 30)
insert(3, 40);		insert(2, 50)
print(items)
delete(1)
print(items)
#P3.2
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
        self.items.sort()
    def merge(self, lst) :
        self.items.extend(lst)
    def display(self, msg='ArrayList:' ):
        print(msg, self.size(), self.items)

def myLineEditor() :	
    list = ArrayList()	
    while True :
        command = input("[메뉴선택] i-입력, d-삭제, r-변경, p-출력, l-파일읽기, s-저장, q-종료, f-찾기=> ")
        if command == 'i' :		
            pos = int( input("  입력행 번호: "))
            str = input("  입력행 내용: ")	    
            list.insert(pos, str)		
        elif command == 'd' :			
            pos = int( input("  삭제행 번호: "))
            list.delete(pos)			
        elif command == 'r' :			
            pos = int( input("  변경행 번호: "))
            str = input("  변경행 내용: ")	    
            list.replace(pos, str)		        
        elif command == 'q' : return	        
        elif command == 'p' :		            
            print('Line Editor')
            for line in range (list.size()) :   
                print('[%2d] '%line, end='')    
                print(list.getEntry(line))      
            print()			                    
        elif command == 'l' :			        
            filename = input("파일이름을 입력하세요: ")
            infile = open(filename , "r")       
            lines = infile.readlines()	        
            for line in lines:		            
                list.insert(list.size(), line.rstrip('\n'))
            infile.close()			
        elif command == 's' :		
            filename = input("파일이름을 입력하세요: ")
            outfile = open(filename , "w")
            for i in range(list.size()) :
                outfile.write(list.getEntry(i)+'\n')
            outfile.close()
        elif command == 'f':
            str = input("문자열을 입력하세요: ")
            for i in range(list.size()):
                if str in list.getEntry(i):
                    print(list.getEntry(i))

myLineEditor()

#P3.3
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

    def insert(self, elem) :
        if not self.contains(elem) :
           self.items.append(elem)

    def delete(self, elem) :
        if self.contains(elem):
            for i in range(len(self.items)):
                if self.items[i] == elem :	
                    self.items.pop(i)

    def union( self, setB ):		    
        setC = Set()			        
        setC.items = list(self.items)	
        for elem in setB.items :	    
            if not self.contains(elem) :	
                setC.items.append(elem)	
        return setC			            

    def intersect( self, setB ):	
        setC = Set()
        for elem in setB.items :	
            if self.contains(elem) :	
                setC.items.append(elem)	
        return setC

    def __sub__(self, rhs):
        return self - rhs

    def difference( self, setB ):	    
        setC = Set()
        for elem in self.items:		    
            if not self.contains(setB.items):	
                setC.items.append(elem)	
        return setC

    def isSubsetOf(self, otherSet):
        if otherSet.intersect(self) == self.items:
            return True
        return False

setA = Set()
setA.insert('휴대폰')
setA.insert('지갑')
setA.insert('손수건')
setA.display('Set A:')

setB = Set()
setB .insert('빗')
setB .insert('파이썬 자료구조')
setB .insert('야구공')
setB .insert('지갑')
setB.display('Set B:')

setB.insert('빗')
setA.delete('손수건')
setA.delete('발수건')
setA.display('Set A:')
setB.display('Set B:')

setA.union(setB).display('A U B:')
setA.intersect(setB).display('A ^ B:')
setA.difference(setB).display('A – B:')

class Polynomial: 
    def __init__( self ):
        self.items = []
    def degree(self) :
        return len(self.items) - 1
    
    def evaluate(self, scalar):
        a = 0
        for i in range(len(self.items)):
            a += self.items[i] * scalar**(self.degree()-i)
        return a
    
    def add(self, rhs):
        p = Polynomial()
        if len(self.items) < len(rhs.items):
            a = rhs.degree() - self.degree()
            for i in range(a):
                p.items.append(rhs.items[i])
            for i in range(len(self.items)):
                p.items.append(self.items[i] + rhs.items[i+a])
        else:
            a = self.degree() - rhs.degree()
            for i in range(a):
                p.items.append(self.items[i])
            for i in range(len(rhs.items)):
                p.items.append(rhs.items[i] + self.items[i+a])
        return p
    
    def subtract(self, rhs) :
        p = Polynomial()
        if len(self.items) < len(rhs.items): 
            a = rhs.degree() - self.degree()
            for i in range(a):
                p.items.append(-rhs.items[i])
            for i in range(len(self.items)):
                p.items.append(self.items[i] - rhs.items[i+a])
        else:
            a = self.degree() - rhs.degree()
            for i in range(a):
                p.items.append(self.items[i])
            for i in range(len(rhs.items)):
                p.items.append(self.items[i+a] - rhs.items[i])
        return p

    def multiply(self, rhs):
        p = Polynomial()
        d1 = self.degree()
        d2 = rhs.degree()
        degree = d1 + d2
    
        for i in range(degree + 1):
            p.items.append(0)
            if len(self.items) > len(rhs.items):
                for j in range(min(i, d2)+1):
                    if i - j > d1:
                        continue
                    p.items[i] += rhs.items[j] * self.items[i-j]
            else:
                for j in range(min(i, d1)+1):
                    if i - j > d2:
                        continue
                    p.items[i] += self.items[j] * rhs.items[i-j]
        return p

    def display(self, msg="f(x) = "):
        print(msg, end='')
        for i in range(self.degree(), 0, -1): 
            print("%5.1fx^%d + " % (self.items[self.degree()-i], i), end = '')
        print("%4.1f" % self.items[-1])
    
    def read_poly():
        a = int(input("다항식의 최고 차수를 입력하시오: "))
        p = Polynomial()
        for i in range(a+1):
            b = float(input("x^%d의 계수 : " %(a-i)))
            p.items.append(b)
        return p