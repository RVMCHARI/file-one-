
# List = [1,2,"hello",3.14]
# [ expr for val in collection]
# [ expr for val in collection if <test>]
# [ expr for val in collection if <test1> and <test2>]
# [ expr for val in collection1 and val2 in collection2]




# in this code list will display like as 0 1 4 9 16 25 36


square = []

for i in range (0, 101):
    square = (i**2)
    i +=1
    #print(square)

# list is disply in one after one like [0,1,4,9,16,25,36,49]
squares = []
for i in range (0,101):
    squares.append(i**2)
#print(squares)



# single line code

squares2 = [i**2   for i in range(0,101) ]
#print(squares2)

# another

remainders5 = [x**2 % 5 for x in range (1,101)]
#print(remainders5)

remainders11 = [x**2 % 11 for x in range(1,101)]
#print(remainders11)


# prime_remainders
#p_remainders = [x%2 == 0 for x in range(0,101)]
p=int(input("enter number values"))
      
p_remainders = [x**2%p for x in range(0,p)]

print("printing squares",p_remainders)


#
# lst = [1, 2, 3, 'Alice', 'Alice']
# indices = [i for i in range(len(lst)) if lst[i]=='Alice']
# print(indices)
