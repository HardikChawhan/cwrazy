# sets are unchangeble* (but we can still add or delete) unordered and unindexed

set1 = {'Hardik','Vedant','Chawhan'}
print(set1) # since it is unordered we dont know the order in which they will appear
print(type(set1))

# duplicates are not allowed
duplicate = {'Hardik','Hardik'} # it will consider the duplicates as one
print(duplicate)

# in set (true and 1) && (false and 0) are considered as same value so they are duplicate
duplicate2 = {'hardik',5,True,1,False,0}
print(duplicate2)

print(len(set1))

# sets can have multiple values
multiple_value_set = {'hardik',20,True}
print(multiple_value_set)

#accessing elements in sets, we cannot index through set so we need to use for loop of condition to access
for i in set1:
  print(i)

print('Hardik' in set1) # prints true if it finds

print('Hardik' not in set1)

# inserting in set

set1.add('Rohan')
print(set1)

x = {1,2}
y = {3,4,5}

x.update(y)
print(x)

set1.remove('Rohan')
print(set1)

set1.discard('Chawhan')
print(set1)

# remove a random item using pop

x = duplicate.pop()
print(x)

# to erase the entire set we can use clear method or del
duplicate2.clear()
print(duplicate)

del duplicate

