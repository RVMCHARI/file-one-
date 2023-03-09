''' Python Lambda Functions are anonymous function means that the function is without a name. As we already know that the def keyword is used to define a normal function in Python. Similarly, the lambda keyword is used to define an anonymous function in Python.

Python Lambda Function Syntax:

lambda arguments: expression
This function can have any number of arguments but only one expression, which is evaluated and returned.
One is free to use lambda functions wherever function objects are required.

You need to keep in your knowledge that lambda functions are """syntactically restricted to a single expression""".

It has various uses in particular fields of programming besides other types of expressions in functions.
Let’s look at this example and try to understand the difference between a normal def defined function and lambda function. This is a program that returns the cube of a given value:  '''


def cube(y):
    return y*y*y

lambda_cube = lambda y: y*y*y


print(cube(5))
print(lambda_cube(5))

print("printing 1-10 numbers cube's : ", list(map(lambda x: x**3, list(x for x in range(1,10)))))   #  here 1-10 numbers printing after cubeing

# tables with lambda function


# tables = [lambda x=x: x*10 for x in range(1,11)]
#
# for table in tables:
#     print(table())

# z = int(input("enter which table you want  : "))
# print("printing ",z ,"th table :")
# for x in range(1,11):
#     y = x*z
#     print(x,"x", z ," = ", y)
#
#
# print("printing ",z ,"table :")
#
# for x in range(1,11):
#     print(x,"X",z ,"=",x*z)
'''printing tables'''

# tables = [lambda x=x : x*2 for x in range(1,11)]
# for table in tables:
#     print(table())


# print("2 table",list(map(lambda x:x*y,  list(x for x in range(1,11)))))



'''  list reversing with lambda  function with map  string values'''
# string_list = ["red",'blue' , 'green', 'vilot']
# print("original list")
# print(string_list)
# reverse= list(map(lambda x:'' .join(reversed(x)),string_list))
# print("first method assigning result to another list :")
# print(reverse)

