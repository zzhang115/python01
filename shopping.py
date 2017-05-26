print '''/---------menu----------/
coffe: $11
tea: $10
coca cola: $1
orange juice: $5
'''
salary = int(raw_input("input your salary:"))
while salary > 0:
    ifbuy = raw_input("Do you want to buy?")
    if ifbuy == "yes":
        if salary > 27:
            salary -=27
            print "done, your balance%d" %salary
        else:
            print "sorry, your balance is not enough to support these beverage"
    else:
        print "byebye"
        break




