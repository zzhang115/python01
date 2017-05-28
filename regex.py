import re

pattern = re.compile(r'hello')
m = pattern.match("helloworld")
if m:
    print m.group(0)

m = re.match('(h*.*l+.+)(d)', "helloworldabc")
print m.group(0) #it means this big group
print m.group(1)
print m.group(2)

p = re.compile("\\d+")
r= p.split("one1two2three3four")
print r #result:['one', 'two', 'three', 'four']
print p.findall("one1two2three3four")

r= p.split("0one1two2three3four4")
print r #result:['', 'one', 'two', 'three', 'four', '']

p = re.compile("\\D+")
r= p.split("one1two2three3four") #cut in this way (\\D)
print r #result:['', '1', '2', '3', '']

print re.sub("[abc]", "o", "Mark") #replace a to o, select replace item from abc
print re.sub("\\d+", "cd", "123Mark")

