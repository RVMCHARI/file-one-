# inheritence parent & child method

class customer:
    cust_name=input("enter name:")
    cust_no= int(input("enter no:"))
    b = input("enter item name=")
    a = input("enter item price")
    cust_dp = float(input("enter emp deposit ="))
    cust_wd = float(input("enter withdraw amount ="))
    cust_totalbill = float(input("enter customer bill paid amount:"))

    def items(a,b):
        print(a*b)

class item(customer):
    c= 100
    d=200
    e=300
    def msg():
        print("your item list")

print(item.cust_wd)
print(item.cust_dp)
print(item.c)
print(item.e)
print(item.b)

item.items(10,100)
item.msg()