# touples are ordered and immutable (unchangable) once created we cannot add or delete items from touple.
# touple allows duplicate

thistouple = ('Hardik','Vedant','Paritosh','Hardik')
print(thistouple)

# length of tuple
print(len(thistouple))
print(type(thistouple))

# single item touple (just add a comma after the one item, it will be a single item touple)
single = ('Apple',)
print(type(single))

test = ('apple')
print('this is not a tupple: ',type(test))

# tuple can contain different datatypes

tuple1 = ('Hardik',100,True)
print(tuple1)

# creating a tuple using constructor
new_tuple = tuple(('Hardik','vedant'))
print(new_tuple)

# accessing a tuple is same as list
#...


# since touple are immutable we can still change its value by converting them into list and then back to tuple

x = (10,20,30);
y = list(x);

# y[1] = 100
x = tuple(y)
print(x)

# unpacking the tuple

fruits = ('Apple','Mango','Banana')

(first,second,third) = fruits
print(first)
print(second)
print(third)

# If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list

fruits_2 = ("apple", "banana", "cherry", "strawberry", "raspberry","mango")

(first,second, *third) = fruits_2
print(first)
print(second)
print(third) # this is now a list

# If the asterisk is added to another variable name than the last, Python will assign values to the variable until the number of values left matches the number of variables left.

(first,*second,third) = fruits_2
print(first)
print(second)
print(third)

# looping is same as the list
# ...

# multiply the tuple
name = ('hardik','vedant','chawhan')
my_tuple = name*2 # adds the tuple 2 times
print(my_tuple)