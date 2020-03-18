# print a and b method
# -*- coding: UTF-8 -*-
import sys
import os
import exceptions


def printStr(a,b):
    s = a+b
    print s

# print index of the arr list
def printTuple():
    a=(1,2,3,4,5)
    print a[1]

# list remove method
def listArr():
    a=["1","2","3","4"]
    c=countOutPut(a)
    c.remove("4")
    del c[0],c[1]
    print c

# appedn method test
def countOutPut(a):
    a.append("4")
    a.append("4")
    return a

# list method
def comparaTwoList():
    a,b=[1,2,3,4,5],[1,2,3,4,5]
    print str(cmp(a,b))+" a total Size "+str(len(a))+" b size is "+str(len(b))

# list test
def maxList():
    a=[1,2,3,4,5,6,76]
    print min(a)

# dictionart test
def dictionary():
    dic ={1:"a",2:"b",3:"c"}
    dic[1]="d"
    str = 1
    print type(str)

# simple else
def judge(a):
    if a>1:
        print "more than one"
    else:
        print "less than one"

# if and elif and else
def judgeMore(a):
    if a==1:
        print "a=1"
    elif a==2:
        print "a=2"
    elif a>3:
        if a==4:
            print "a==4"
        else:
            print "a>4"
    else:
        print "else value"

# while and continue
def whileTest():
    count = 10
    while count>0:
        print count
        count-=1
        if count%2!=0:
            continue
    else:
        print "while end"

# while and else
def whileBreak():
    a=10
    while a>0:
        a-=1
        if a%2>0:
            continue
        print a
    else:
        print "end"

# for test arr
def forTestArr():
    a=[1,2,3,4,5,6,7,8]
    for i in a:
        print i

#  for test str
def forTestStr():
    a="Stronger"
    for i in a:
        print i

# for list through element index
def throughIndex():
    a=[1,2,3,4,4,5,5]
    for i in range(len(a)):
        print a[i]

# interator test
def interatorTest():
    a=[1,2,3,4,4,5,5]
    it=iter(a)
    while True:
        try:
            print (next(it))
        except StopIteration:
            sys.exit()

#liebiaotuidaoshi
def listDetected():
    vec=[2,4,6]
    vec2=[8,9,10]
    fruit = {1:'apple',2:'banna'}
    print [2*i for i in vec]
    print [[a*2,a*3] for a in vec]
    print [[a*2,a*3,a+1] for a in vec]
    print [10*i for i in vec if i>3]
    print [a*b for a in vec for b in vec2]

#set test
def setTest():
    lis ={"a","a","b","c"}
    for i in lis:
        print i

# dictionary bianli
def dictBianLi():
    fruit = {1:'apple',2:'banna'}
    for a,b in fruit.items():
        print(a,b)
    for i,v in enumerate(['1','2','3']):
        print (i,v)

# zip method test
def zipTest():
    questions = ['name', 'quest', 'favorite color']
    answers = ['lancelot', 'the holy grail', 'blue']
    for a,b in zip(questions,answers):
        print (a,b)
        print (sys.path)

# input test
def inputTest():
    str = input("plz input ur words")
    print (str)

#file test
def fileTest():
    fp = open("股票测试B卷.docx","wb")
    print ("filename",fp.name)
    print ("cloes status",fp.closed)
    print ("visit mode",fp.mode)
    print ("space attached",fp.softspace)

# file write
def fileReadAndWrite():
    fp = open("股票测试B卷.docx","wb")
    fp.write("new string input")
    fp.closed

# file read
def fileRead():
    fp = open("test.txt","r+")
    result = fp.read(2)
    print result

# file rename
def fileRename():
    os.rename("test.txt","kris-test.txt")

# class
class member:
    age=11
    def __init__(self,name,height):
        self.name=name
        self.height=height
    def tes(self):
        print (self)
        print (self.__class__)
    def __privaeMethod(self):
        print ("private method")
    def testStr(self):
        print ("test string")

# class implement
class memberImpl(member):
    def __init__(self,name,height,grade):
        member.__init__(self,name,height)
        self.grade=grade



# test class method
def testClass():
    m = member("Kris",11)
    # print m.tes()
    print (m.age)
    print (m.height)
    print (m.name)
    m.testStr()


testClass()