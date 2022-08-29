#1장 연습문제
#1.1 (1), (2), (4), (5)
#1.2
def contains(bag, e) :
    return e in bag		

def insert(bag, e) :	
    bag.append(e)		

def remove(bag, e) :	
    bag.remove(e)		

def count(bag):		  
    return len(bag)		

def numOf(bag, item):
    count = 0
    for i in bag:
        if i == item:
            count += 1
    return count

#1.3
#1.4

def asterisk(i):
    if i>1:
        asterisk(i/2)
        asterisk(i/2)
    print("*",end='')

asterisk(5)

print(5/2)