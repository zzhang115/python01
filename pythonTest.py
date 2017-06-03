import linecache

print("Hello World!")
a = [1,2,3]
a.append(4)
a.append(4)
print(a)
b = (1,2,2,3)

print(b)
a=1
a=2
print(a)
print(id(a))

print 1 ==1
a = bool(1==1)
print(a)
print(bool(1=="1"))

str = "abcdefg"
print(len(str))
str = "abc\"e"
print(str)
str = 'abdef\,'
print(str)
str = 'abcde\nsaf\nsadf'
print(str)
str = '\\n'
print(str)
print r"\nabcv"
a = "abdesadfdfs"
print a[0]
print a[3]
print a[len(a)-1]
print a[0:]
print a[0:11]
print len(a)
print a[7:10]
print a[2:3]
print a[:-1]
str ="abcde"

print str.replace('a','cc')
print str
str = str.replace('a','cc')
print str

print "abcd%def" %1
print "abcd%sefg" %'hhhh'

a="abcedf"
b="1234324"
c="ewiqoru"
print ",".join([a,b,c])
a = open('/home/zzc/NewSpace/Python/abc.txt', 'r')
# print a.readline()
# print a.readline()
print a.readline(60)
print a.read()
print linecache.getline("abc.txt", 1)
print linecache.getline("abc.txt", 2)
print linecache.getline("abc.txt", 1)
a = open('abc.txt','w')
a.write('wqjewirjfsjdfl;jasdkl;fjas\nsdfsdf')
a.close()
a = "test"
print a[0]
a = a.replace('t','abc')
print a

a = [1,1,34,5,32]
print a[0]
a[0] = 3
print a[0]

# a = (1,1,34,5,32) #immutable tuple
# print a[0]
# a[0] = 3
print a[0]

print "sadfjl;asdkf"\
      "sdfks" \
      "d"

a = "helloworld"
print a.find('z')
a = 'hello %s I am %s I am %d' %('priyam', 'ZZC', 23)
print a
a ="this is {} {}".format("my", "apple")
print a
a ="this is {1} {0}".format("my", "apple")
print a
a ="this is {whose} {fruit}".format(whose="my", fruit="apple")
print a
a = [[1,2,3],[4,5,6]]
print a
print a[0][2]
a = [1,2,3,4,5,6,7,8]
print a[-1:-4:-1]
b = [3,4,5,6,6543]
print a+b

a.extend(b)
print a

a.append(b)
print a
del a[8]
print a
del a[0]
print a

a.append(20)
print a
a.remove(5)
print a
a.remove(20)
print a
a.pop()
print a
a.pop()
print a

print (3 not in a)
# x = range(1,30)
# print x
print [x for x in range(1,30)]

y = [x for x in range(1,30,1) if x%2 == 1]
print y
y = [x for x in range(1,30,10)]
print y
a = [3,4123,5,2,1,324,21,53,34]
b = a.sort()
print b
print a
a = [3,4123,5,2,1,324,21,53,34]
a.reverse()
print a
a="abcdefg"
list(a)
print list(a)
a = xrange(1,10)
print a

for m in range(100):
    if m%10 == 0:
        print 'hello'

for m in xrange(100):
    if m%10 == 0:
        print "hi"
a = [x*x for x in range(100)]
print a

a = dict([(x,y) for x in range(2) for y in range(2)])
print a

a = ['i','b','cde']
b = a
a[2] = 'asldjfklasd'
print b
print id(a)
print id(b)
del a[2]
print a
print b
del a
# print a delete reference, this sentence will lead an error, name a is not defined
print b
name = 'name'
if name == 'name':
    print 'hello', name
a = (1+1+1+1+1) > 6
print a
name = "I am Taylor"
print name
name = "I'm Taylor"
print name
name = '''hello
    world three
    quotes'''
print name
age = 23
new_year_age = age + 1
print new_year_age
import sys, os
print sys.path
help(sys)
print sys.version_info
os.system('ls -l')
if os.system('ls -l') == 0:
    print "command carry out correct!"
else:
    print "command has some problems!"
# name = raw_input("input your name:")
# sex = raw_input("input your sex:")
# age = int(raw_input("input your age:"))
# print "Information of student"
# print "name:\t", name, "\nsex:\t", sex, "\nage:\t", age
# print '''name:\t %s
# sex:\t %s
# \nage:\t %d''' %(name, sex, age)
for i in range(1, 10):
    if i % 2 == 0:
        print 'Hello %dth num' %i
i = 0
while os.system('ls') == 0:
    i = i + 1
    if i > 10:
        break
    if i % 2 == 0:
        continue
    print "haha", i

data = "abc"
if data:
    print "is data"
elif not data:
    print "not data"



