DicName = {
   "01" : "boy",
   "02" : "girl"
}
Dic = {
   01 : "boy",
   02 : "girl"
}
print DicName.get("01")
print Dic.get(2)
print DicName["02"]
print DicName.has_key("01")
print DicName.keys()
print DicName.items()

for i in DicName.keys():
   print i, "price:", DicName.get(i)

DicName.popitem()

for i in DicName.keys():
   print i, "secprice:", DicName.get(i)

DicName["03"] = "transfer gender"
for i in DicName.keys():
   print i, "thirdprice:", DicName.get(i)

DicName.pop("01")
for i in DicName.keys():
   print i, "fourthprice:", DicName.get(i)

DicName["04"] = "middle gender" #add new item
for i, j in DicName.items():
   print i, " and ", j
input = raw_input("please input a string:").strip()
print input
print "\"", input, "\""

