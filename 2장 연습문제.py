#2장 연습문제 
#2.1

for i in range(1, 10):
    print("%d x %d = %d" % (6, i ,6*i))

#2.2
i = 1
while i<10:
    print("%d x %d = %d" % (6, i ,6*i))
    i += 1

#2.3
for i in range(9, 0, -1):
    print("%d x %d = %d" % (6, i ,6*i))

#2.4
def change(c):
    f = 32+1.8*c
    return f

#2.5
def change2(f):
    c = (f-32)/1.8
    return c

#2.6
a = [1,2,3,4,5]
for i in range(1, len(a)+1):
    print(a[-i])

#2.7
def add_all(list):
    a = 0
    for i in list:
        a += i
    return a
print(add_all(a))

#2.8
msg = "Data Structures in Python"
print(msg)
print(msg.upper())
print(msg.lower())

#2.9
price ={'콩나물해장국':4500, '갈비탕':9000, '돈가스':8000}
price['팟타이'] = 7000
print(price)

#2.10
for i in price:
    price[i] = price[i] - 500
print(price)

#2.11
def sum(n):
    if n == 1: return 1
    else: return n + sum(n-1)

#2.12
def sum1(n):
    if n == 1: return 1
    else: return 1/n + sum1(n-1)

#2.13
def bc(n, k):
    if k == 0 or k == n: return 1
    else:
        return bc(n-1, k-1)+ bc(n-1, k)

print(bc(5, 2))

#2.14
def bc_d(n, k):
    if k == 0 or k == n: return 1
    else:
        r = 1
        for i in range(k):
            r *= (n-i)/(k-i)
        return r

print(bc_d(5,4))

#2.15
def reverse(msg):
    return msg[::-1]

print(reverse("ABCDE"))

#2.16
def printNum(n):
    if n == 1: return 1
    else: 
        print(printNum(n-1) , end=' ')
        return n

print(printNum(10))

def printRevNum(n):
    if n == 1: return 1
    else: 
        print(n , end=' ')
        return printRevNum(n-1)

print(printRevNum(10))

#2.17
def fib(n):
    if n==0: return 0
    elif n == 1: return 1
    else:
        return fib(n-1)+fib(n-2)


#실습문제
#P2.1
a = int(input("소득을 입력하세요: "))
if a <= 1200:
    print("전체 세금은: ", a*0.06)
    print("세후소득: ", a - a*0.06)
elif 1200 < a <= 4600:
    print("전체 세금은: ", 1200*0.06+(a-1200)*0.15)
    print("세후소득: ", a - (1200*0.06+(a-1200)*0.15))
elif 4600 < a <= 8800:
    print("전체 세금은: ", 4600*0.15 + (a-4600)*0.24)
    print("세후소득: ", a - (4600*0.15 + (a-4600)*0.24))
elif 8800 < a <= 15000:
    print("전체 세금은: ", 8800*0.24 + (a-8800)*0.35)
    print("세후소득: ", a - (8800*0.24 + (a-8800)*0.35))    
else:
    print("전체 세금은: ", a*0.38)
    print("세후소득: ", a - a*0.38)    

#P2.2
answer = 36 
min = 0
max = 99
cnt = 0
for i in range(10):
    guess = int(input('숫자를 입력하세요(범위:%d~%d): ' %(min, max)))
    if guess > answer:
        print("아닙니다. 더 작은 숫자 입니다!")
        max = guess
    elif guess < answer:
        print("아닙니다. 더 큰 숫자 입니다!")
        min = guess
    else:
        cnt += 1
        print("정답입니다. %d번 만에 맞추셨습니다." % cnt)
        break
    cnt += 1
print("게임이 끝났습니다.")    

#P2.3
c = int(input("피라미드의 높이를 입력하세요: "))
for i in range(1, c+1):
    k = 1
    for j in range(c+1-i):
        print("   ", end='')
    for j in range(i):
        print("%3d"%k, end='')
        k += 2
    k -= 2
    for j in range(i-1):
        k -= 2
        print("%3d"% k, end='')
    print()

#P2.4
def draw_tree(row, left, right):
    if row == 0:
        print('-'*int((left+right)/2)+'X'+'-'*int((left+right)/2))
    else:
        draw_tree(row-1, left, right)
        print(('-'*int((left+right)/2/2)+'X'+'-'*int((left+right)/2/2))*(row*2))

draw_tree(6, 0, 12)

#P2.5
class Bag():
    def __init__(self):
        self.bag = []
    def insert(self, e):
        self.bag.append(e)
    def remove(self, e):
        self.bag.remove(e)
    def contains(self, e):
        return e in self.bag
    def count(self):
        return len(self.bag)

