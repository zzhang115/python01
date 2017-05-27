# import function
# account = ["abccd"]
# print account[0]
# account.append("ef")
# print account[1]
#
# print function.sayHello()
# binary=0b110
# hex=0xFF
# print binary
# print hex.bit_length()

# f = file("Fire.png", "rb")#reading in binary mode
# for line in f.readlines():
#     print line

import pickle
account_info = {
                '100' : ['alex324', 150000, 140000],
                '101' : ['rachel', 9000, 9000]
}

a = {'hello': 'world'}

with open('filename.pickle', 'wb') as handle:
    pickle.dump(a, handle, protocol=pickle.HIGHEST_PROTOCOL)

with open('filename.pickle', 'rb') as handle:
    b = pickle.load(handle)

print "if equal", a == b

with open("pickTestFile.pkl", "wb") as handle:
    pickle.dump(account_info, handle)

with open("pickTestFile.pkl", "rb") as handle:
    new = pickle.load(handle)
handle.close()
print new

