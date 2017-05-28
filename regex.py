import re

pattern = re.compile(r'hello')
m = pattern.match("helloworld")
if m:
    print m.group(0)

m = re.match('(h*.*l+.+)(d)', "helloworldabc")
print m.group(0) #it means this big group
print m.group(1)
print m.group(2)