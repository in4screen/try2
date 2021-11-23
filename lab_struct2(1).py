class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

    def __str__(self):
        return self.data


class OneWayList:
    def __init__(self):
        self.length = 0
        self.top = None

    def push(self, e):
        node = Node(e)
        if self.length == 0:
            self.top = node
        else:
            node.next = self.top
            self.top = node
        self.length += 1

    def pop(self):
        if self.length > 0:
            tmp = self.top.next
            del self.top
            self.top = tmp
            self.length -= 1

    def __str__(self):
        acc = ''
        cur = self.top
        while (cur):
            acc += cur.__str__()
            cur = cur.next
        return acc


# class Node:
# def __init__(self, data=None, next=None, prev=None):
# self.data = data

class TwoWayList:
    def __init__(self):
        self.length = 0
        self.begin = None
        self.end = None

    def add_q(self, e):
        node = Node(e)
        if self.length == 0:
            self.begin = node
            self.end = node
        else:
            node.next = self.end
            self.end.prev = node

            self.end = node
        self.length += 1

    def del_q(self):
        if self.length > 0:
            tmp = self.begin.prev
            del self.begin
            self.begin = None
            if self.begin != None:
                self.begin.next = None
            self.length -= 1

    def __str__(self):
        acc = ''
        # cur = self.begin

        # while (cur):
        #     print(cur)
        #     acc += cur.__str__()
        #     cur = cur.next
        cur = self.end
        while (cur):
            print(cur)
            acc += cur.__str__()
            cur = cur.next
        return acc
    def search_node(self, i):
        cur = self.end
        for r in range(i):
            cur = cur.next
        return cur
    
        
        


one = OneWayList()
two = TwoWayList()

one.push('1')
one.push('2')
one.push('3')

print(one.__str__())

two.add_q('1')
two.add_q('2')
two.add_q('3')
two.add_q('4')

print(two.length)
print(two.__str__())
print(two.search_node(0))
print('hllo wrld')

class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

    def __str__(self):
        return self.data


class OneWayList:
    def __init__(self):
        self.length = 0
        self.top = None

    def push(self, e):
        node = Node(e)
        if self.length == 0:
            self.top = node
        else:
            node.next = self.top
            self.top = node
        self.length += 1

    def pop(self):
        if self.length > 0:
            tmp = self.top.next
            del self.top
            self.top = tmp
            self.length -= 1

    def __str__(self):
        acc = ''
        cur = self.top
        while (cur):
            acc += cur.__str__()
            cur = cur.next
        return acc


# class Node:
# def __init__(self, data=None, next=None, prev=None):
# self.data = data
# self.next = next
# self.prev = prev
class TwoWayList:
    def __init__(self):
        self.length = 0
        self.begin = None
        self.end = None

    def add_q(self, e):
        node = Node(e)
        if self.length == 0:
            self.begin = node
            self.end = node
        else:
            node.next = self.end
            self.end.prev = node

            self.end = node
        self.length += 1

    def del_q(self):
        if self.length > 0:
            tmp = self.begin.prev
            del self.begin
            self.begin = None
            if self.begin != None:
                self.begin.next = None
            self.length -= 1

    def __str__(self):
        acc = ''
        # cur = self.begin

        # while (cur):
        #     print(cur)
        #     acc += cur.__str__()
        #     cur = cur.next
        cur = self.end
        while (cur):
            print(cur)
            acc += cur.__str__()
            cur = cur.next
        return acc
    



one = OneWayList()
two = TwoWayList()

one.push('1')
one.push('2')
one.push('3')

print(one.__str__())

two.add_q('1')
two.add_q('2')
two.add_q('3')
two.add_q('4')

print(two.length)
print(two.__str__())

def Ackerman (n, m):
    if n==0:
        return m+1
    else:
        if n!=0 and m==0:
            return Ackerman(n-1,1)
        else:
            if n > 0 and m > 0:
                return Ackerman(n-1,Ackerman(n,m-1))
print(Ackerman(3, 2))

import math
def C(m,n):
    if (m==0 and n>0) or (m==n and n>=0):
         return 1
    if m>n and n>=0:
        return 0
    else:
        return C(((math.factorial(n-1))/(math.factorial(m-1) * math.factorial((n-1)-(m-1))) + C(((math.factorial(n-1))/(math.factorial(m) * math.factorial((n-1)-m)))
print(1)

f = open('abc.txt', 'r')

# rmax=len(a)
# cmax=len(a[0]) # реальні розміри лабіринта
def BFS(r,c,arr): # r, c: координати початку обходу
    que=[]
    if arr[r][c]=0 # перетворюємо клітинку на стіну
    que.append([r,c])
    while len(que)>0:
        tmp=que.pop(0)
        r=tmp[0]
        c=tmp[1]
    if ((c+1)<cmax) and (a[r][c+1]==1):
        que.append([r,c+1])
        a[r][c+1]=0 #якщо можна йти вправо, то йдемо
    if ((r+1)<rmax) and (a[r+1][c]==1):
        que.append([r+1,c])
        a[r+1][c]=0 # якщо можна йти вниз, то йдемо
        if ((c-1)>=0) and (a[r][c-1]==1):
            que.append([r,c-1])
            a[r][c-1]=0 # якщо можна йти вліво, то йдемо
        if ((r-1)>=0) and (a[r-1][c]==1):
            que.append([r-1,c])
            a[r-1][c]=0 # якщо можна йти вгору, то йдемо
arr = []
BFS(0,1)
print(a)

class Rectangle:
    def __init__(self,length=0,width=0):
        self.length=length
        self.width=width
    def square(self):
        return self.length * self.width
    def perimeter(self):
        return (self.length + self.width) * 2
a=int(input('введіть довжину прямокутника:'))
b=int(input('введіть ширину прямокутника:'))
s=Rectangle(a,b)
print(s.length, s.width)
print(s.square())
print(s.perimeter())
