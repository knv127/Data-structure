class BSTNode:				            
    def __init__ (self, key, value):	
        self.key = key		        	
        self.value = value	          	
        self.left = None		    	
        self.right = None

#P9.1
def search_max_bst(n) :	
    if n != None and n.right != None:
        n = search_max_bst(n.right)
    return n

def search_min_bst(n) :	
    if n != None and n.left != None:
        n = search_min_bst(n.left)
    return n

#P9.2
def search_bst_iter(n, key) :
    while n != None :			        
        if key == n.key:		        
            return n
        elif key < n.key:		        
            n = n.left			        
        else:				            
            n = n.right			        
    return None	

def insert_bst(r, n) :
    while r != None:
        if n.key < r.key:			
            if r.left is None :		
                r.left = n			
                return True
            else :			    	
                r = r.left	
        elif n.key > r.key :	        	
            if r.right is None :	    	
                r.right = n		        	
                return True
            else :			            	
                r = r.right
        else : 				        
            return False

#P9.3
def sort(data):
    def insert(self, key, value=None):	
        n = BSTNode(key, value)		    
        if self.isEmpty() :		        
           self.root = n			    
        else :				            
           insert_bst(self.root, n)
    for i in data:
        insert(i)
    def inorder(n) :				
        if n is not None :
            inorder(n.left)			
            print(n.key, end=' ')	
            inorder(n.right)

    inorder(n)
    print()	

