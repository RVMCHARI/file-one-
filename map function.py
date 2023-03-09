'''map function is define mapping of two functions or one function and iterable  for functioning
map() function returns a map object(which is an iterator) of the results after applying the given function to each item of a given iterable (list, tuple etc.)

Syntax :

map(fun, iter)
Parameters :

fun : It is a function to which map passes each element of given iterable.
iter : It is a iterable which is to be mapped.

NOTE : You can pass one or more iterable to the map() function.
Returns :

Returns a list of the results after applying the given function
to each item of a given iterable (list, tuple etc.)

NOTE : The returned value from map() (map object) then can be passed to functions like list() (to create a list), set() (to create a set) .
'''

def square(num):
    return num**2
my_num = [1,2,3,4,5]

print(list(map(square,my_num)))
# square functions




# mapping
def square(num):
    return num ** 2


my_num = [1,2,3,4,5,6]

print("square of given number 1-6 ",list(map(square,my_num)))

# splicer function using map
def splicer(str):
    if len(str)%2==0:
        return"even"
    else:
        return str[0]

list1 = ["john" , "hari", 'krish', 'kanya','kumar','ravi']


print("given list check even or not with mapping if not print list[0]",list(map(splicer,list1)))


# return double of one number
def addition(n):
    return n + n
number = (1,2,3,4)
print("given number 1 2 3 4 is doubled",list(map(addition,number)))

# double the all numbers using lambda and map functions

numbers = (1,2,3,4)
print(type(numbers))

print("double the number with lambda and map ",list(map(lambda x: x + x,numbers)),type(list))


num = (1,2,3,4,5,6)

print(list(map(lambda x:x ** 2, num )))

#  adding two lists using map and lambda
n1 = [1,2,3,4]
n2 = [5,6,7,8]

print(list(map(lambda x, y: x + y , n1 ,n2)))


#  list of string is print listify of individually
str = ["hello", "hi","good","morning"]

print((list(map(list,str))))


