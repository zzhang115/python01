import function
account = ["abccd"]
print account[0]
account.append("ef")
print account[1]

print function.sayHello()
binary=0b110
hex=0xFF
print binary
print hex.bit_length()

# f = file("Fire.png", "rb")#reading in binary mode
# for line in f.readlines():
#     print line

import pickle
account_info = {
                '100' : ['alex324', 150000, 140000],
                '101' : ['rachel', 9000, 9000]
}
temp = account_info['100']
print temp[1]
f = open("pickleTest.pkl", "w+")
pickle.dump(account_info, f)
f.close()
f = open("pickleTest.pkl", "r")
