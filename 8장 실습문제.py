#P8.1
MAX_QSIZE = 10				    
class CircularQueue :
    def __init__( self ) :		
        self.front = 0			
        self.rear = 0			
        self.items = [None] * MAX_QSIZE	

    def isEmpty( self ) : return self.front == self.rear
    def isFull( self ) : return self.front == (self.rear+1)%MAX_QSIZE
    def clear( self ) : self.front = self.rear

    def enqueue( self, item ):
        if not self.isFull():			            
            self.rear = (self.rear+1)% MAX_QSIZE	
            self.items[self.rear] = item		    

    def dequeue( self ):
        if not self.isEmpty():			            
            self.front = (self.front+1)% MAX_QSIZE	
            return self.items[self.front]	        

    def peek( self ):
        if not self.isEmpty():
            return self.items[(self.front + 1) % MAX_QSIZE]

    def size( self ) :
       return (self.rear - self.front + MAX_QSIZE) % MAX_QSIZE

    def display( self ):
        out = []
        if self.front < self.rear :
            out = self.items[self.front+1:self.rear+1]
        else:
            out = self.items[self.front+1:MAX_QSIZE] \
                + self.items[0:self.rear+1]		
        print("[f=%s,r=%d] ==> "%(self.front, self.rear), out)

class TNode:								
    def __init__ (self, data, left, right):	
        self.data = data 					
        self.left = left					
        self.right = right	

root = TNode( "A", None, None )
root.left = TNode("B", None, None)
root.right = TNode("C", None, None)
root.left.left = TNode("D", None, None)
root.right.left = TNode("E", None, None)
root.right.right = TNode("F", None, None)
root.right.left.left = TNode("G", None, None)
root.right.left.right = TNode("H", None, None)

def preorder(n) :				
    if n is not None :
        print(n.data, end=' ')	
        preorder(n.left)		
        preorder(n.right)		

def inorder(n) :				
    if n is not None :
        inorder(n.left)			
        print(n.data, end=' ')	
        inorder(n.right)		

def postorder(n) :
    if n is not None :
        postorder(n.left)
        postorder(n.right)
        print(n.data, end=' ')


def levelorder(root) :
    queue = CircularQueue()			
    queue.enqueue(root)				
    while not queue.isEmpty() :		
        n = queue.dequeue()			
        if n is not None :
            print(n.data, end=' ')	
            queue.enqueue(n.left)	
            queue.enqueue(n.right)

def count_node(n) :
    if n is None : 
        return 0
    else : 			
        return 1 + count_node(n.left) + count_node(n.right)

def count_leaf(n) :
    if n is None :	
        return 0
    elif n.left is None and n.right is None :
        return 1
    else : 		
        return count_leaf(n.left) + count_leaf(n.right)


def calc_height(n) :
    if n is None : 					
        return 0
    hLeft = calc_height(n.left)		
    hRight = calc_height(n.right)	
    if (hLeft > hRight) : 			
        return hLeft + 1
    else: 
        return hRight + 1

preorder(root)
print()
inorder(root)
print()
postorder(root)
print()
levelorder(root)
print()

print(" 노드의 개수 = %d개" % count_node(root))
print(" 단말의 개수 = %d개" % count_leaf(root))
print(" 트리의 높이 = %d" % calc_height(root))

a = TNode("A", None, None)
b = TNode("B", None, None)
f = TNode("/", a, b)
c = TNode("C", None, None)
s = TNode("*", f, c)
d = TNode("D", None, None)
s2 = TNode("*", s, d)
e = TNode("E", None, None)
root2 = TNode("+", s2, e)

preorder(root2)
print()
inorder(root2)
print()
postorder(root2)
print()
levelorder(root2)
print()

print(" 노드의 개수 = %d개" % count_node(root2))
print(" 단말의 개수 = %d개" % count_leaf(root2))
print(" 트리의 높이 = %d" % calc_height(root2))

#P8.2
def is_complete_binary_tree(root):
    if root is not None:
        if root.left == None and root.right != None:
            return False
        r = is_complete_binary_tree(root.left)
        if r == True:
            return is_complete_binary_tree(root.right)	
    return True

d1 = TNode("D", None, None)
f1 = TNode("F", None, None)
c1 = TNode("C", d1, None)
b1 = TNode("B", c1, None)
a1 = TNode("A", b1, None)

preorder(a1)
print()
print(is_complete_binary_tree(a1))

#P8.3
def level(root, node):
    if root is not None:
        if root == node:
            return 1
        elif root.left == node:
            return 2
        elif root.right == node:
            return 2
        else:
            l = level(root.left, node)
            if l == 0:
                return level(root.right, node)+1 
            else:
                return l+1
    return 0

print(level(a1, a1))
print(level(a1, b1))
print(level(a1, c1))
print(level(a1, d1))
print(level(a1, f1))

#P8.4
def calc_height(n) :
    if n is None : 					
        return 0
    hLeft = calc_height(n.left)		
    hRight = calc_height(n.right)	
    if (hLeft > hRight) : 			
        return hLeft + 1
    else: 
        return hRight + 1

def is_balanced(root):
    hLeft = calc_height(root.left)		
    hRight = calc_height(root.right)
    if hLeft - hRight < 2:
        print("균형잡힌 트리입니다.")

is_balanced(a1)

#P8.5
def path_length(root):
    if root == None:
        return 2
    else:
        return path_length(root.left) + path_length(root.right) - 1

print(path_length(a1))

#P8.6
def reverse(root):
    if root is not None:
        if root.left != None:
            n = root.left
            root.left = root.right
            root.right = n
        else:
            root.left = root.right
            root.right = None
        reverse(root.left)
        reverse(root.right)

reverse(a1)
levelorder(a1)

#P8.7
def isMaxHeapRecur(A, id):
    if id <= len(A):
        if A[id] >= A[id*2] and A[id] >= A[id*2+1]:
            return True
        isMaxHeapRecur(A, id*2)
        isMaxHeapRecur(A, id*2+1)
    return False

def isMinHeapRecur(A, id):
    if id <= len(A):
        if A[id] <= A[id*2] and A[id] <= A[id*2+1]:
            return True
        isMinHeapRecur(A, id*2)
        isMinHeapRecur(A, id*2+1)
    return False

print()
A = [0,9,7,6,5,4,3,2]
print(isMaxHeapRecur(A, 1))

