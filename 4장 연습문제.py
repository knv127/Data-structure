#4장 연습문제
#4.9, 4.11
class Stack :
    def __init__( self ):   
        self.top = []       

    def isEmpty( self ): return len(self.top) == 0
    def size( self ): return len(self.top)
    def clear( self ): self.top = []	

    def push( self, item ):
        self.top.append(item)

    def pop( self ):
        if not self.isEmpty():
            return self.top.pop(-1)
        else:
            print("잘못된 접근입니다.")
            return 0

    def peek( self ):
        if not self.isEmpty():
            return self.top[-1]
        else:
            print("잘못된 접근입니다.")
            return 0

    def __str__(self ):
        return str(self.top[::-1])
    
    def display(self):
        for i in range(self.size()):
            print("%2d" % self.top[-1-i], end=' ')

#4.19
def isValidPos(x, y) :		
    if x < 0 or y < 0 or x >= MAZE_SIZE or y >= MAZE_SIZE :
        return False		
    else :			        
        return map[y][x] == '0' or map[y][x] == 'x'


def DFS() :			   
    stack = Stack()		
    stack.push( (0,1) )
    print('DFS: ')

    while not stack.isEmpty(): 	
        here = stack.pop()	    
        print(here, end='->')
        (x, y) = here		     
        if (map[y][x] == 'x') :	
            return True
        else :
            map[y][x] = '.'	
            
            if isValidPos(x - 1, y): stack.push((x - 1, y)) 
            if isValidPos(x + 1, y): stack.push((x + 1, y))
            if isValidPos(x, y - 1): stack.push((x, y - 1)) 
            if isValidPos(x, y + 1): stack.push((x, y + 1)) 
 
        print(' 현재 스택: ', stack)	
    return False			            


map = [ [ '1', '1', '1', '1', '1', '1' ],
	  [ 'e', '0', '0', '0', '0', '1' ],
	  [ '1', '0', '1', '0', '1', '1' ],
	  [ '1', '1', '1', '0', '0', 'x' ],
	  [ '1', '1', '1', '0', '1', '1' ],
	  [ '1', '1', '1', '1', '1', '1' ]]
MAZE_SIZE = 6
result = DFS()
if result : print(' --> 미로탐색 성공')
else : print(' --> 미로탐색 실패')

#P4.1
def readStr(statement):
    s = Stack()
    str = ''
    for i in statement:
        s.push(i)
    for i in range(s.size()):
        str += s.pop()
    return str

print(readStr('pentagon'))

#P4.3
def checkBrackets(statement):
    stack = Stack()
    infile = open(statement, "r")
    lines = infile.readlines()
    for line in lines:
        l = 0
        for j in line:		    
            if j in ('{', '[', '('):	
                stack.push(j)
            elif j in ('}', ']', ')'):	
                if stack.isEmpty() :
                    print("조건2 위반")
                    return 2, lines.index(), l 		
                else :
                    left = stack.pop()
                    if (j == "}" and left != "{") or \
                    (j == "]" and left != "[") or \
                    (j == ")" and left != "(") :
                        print("조건3 위반")	
                        return 3, lines.index(), l
            l += 1
    if stack.isEmpty(): return 0
    else: 
        print("조건1 위반")
        return 1, lines.index(), l		    

#P4.5
def precedence (op):			        
    if   op=='(' or op==')' : return 0	
    elif op=='+' or op=='-' : return 1	
    elif op=='*' or op=='/' : return 2	
    else : return -1


def Infix2Postfix():		
    s = Stack()
    output = []
    expr = input("중위표기식을 입력하세요: ")			        
    for term in expr :
        if term in '(' :		
            s.push('(')			
        elif term in ')' :		
            while not s.isEmpty() :
                op = s.pop()
                if op=='(' : break;	
                else :			    
                    output.append(op)
        elif term in "+-*/" :		
            while not s.isEmpty() :	
                op = s.peek()		
                if( precedence(term) <= precedence(op)):
                    output.append(op)
                    s.pop()
                else: break
            s.push(term)		
        else :				    
            output.append(term)	

    while not s.isEmpty() :		
        output.append(s.pop())	

    return output

print(Infix2Postfix())