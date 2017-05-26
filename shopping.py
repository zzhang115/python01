print '''/---------menu----------/
'''
f = file("item.txt")
for line in f.readlines():
    new_line = line.split("$") #split by '$'
    print new_line[0], " price:", new_line[1]
itemList=[]
salary = int(raw_input("input your salary:"))
while salary > 0:
    ifbuy = raw_input("what do you want to buy?")
    if ifbuy == "coffee":
        if salary > 11:
            salary -= 11
            itemList.append("coffee")
            print "done, your balance%d" %salary
            print "you have bought :", itemList
        else:
            print "sorry, your balance is not enough to support these beverage"
    elif ifbuy == "tea":
        if salary > 10:
            salary -= 10
            itemList.append("tea")
            print "done, your balance%d" %salary
            print "you have bought :", itemList
        else:
            print "sorry, your balance is not enough to support these beverage"
    elif ifbuy == "orange juice":
        if salary > 5:
            salary -= 5
            itemList.append("orange juice")
            print "done, your balance%d" %salary
            print "you have bought :", itemList
        else:
            print "sorry, your balance is not enough to support these beverage"
    else:
        print "byebye"
        break




