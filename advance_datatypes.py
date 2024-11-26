# list is changable(mutable)
thisList = ['Hardik','paritosh','rohan','affan']
print(thisList)

# list can have same values
first_list = ['apple','bannana','apple'];
print(first_list)

# list length
print(len(first_list))

# list can contain multiple datatype
second_list = ['VU',12,'VIT',True]
print(second_list)

# type of list
print(type(second_list))

# using constructor to create list
third_list = list(("apple", "banana", "cherry"))
print(third_list)

# accessing items
print(thisList[0])

# negative indexing
print(thisList[-2])

# accessing in range
print(thisList[1:4])

# this prints from the beginning to the index mentioned (not included)
print(third_list[:2])

# startes from the index mentioned to the end
print(thisList[1:])

if "Hardik" in thisList:
  print("Hardik is present")

# change list items
thisList[1] = 'vedant'
print(thisList)

# change the values using range
thisList[1:3] = ['Apple','banana'] 
print(thisList)

# using insert (this does not change the list like it does not overwrite)
thisList.insert(2,'nani') 
print(thisList)

# appending to the list
new_list = ["apple", "banana", "cherry"]
new_list.append('mango')
print(new_list)

# merging two list
tropical = ["pineapple", "papaya","mango"]
new_list.extend(tropical)
print(new_list)

# removing element (removes the first elemet it finds)
new_list.remove('mango');
print(new_list)

# popping element pop(1) if index not specified it pops the last element
new_list.pop(1)
print(new_list)

new_list.pop()
print(new_list)

# deleting using del
del new_list[0]
print(new_list)

del new_list # deletes the list entirely
# print(new_list)

# looping list
loop_list = ["apple", "banana", "cherry"]
for i in loop_list:
  print(i)

# using range
for i in range(len(loop_list)):
  print(i,": ",loop_list[i])

# using while loop
i = 0
while i < len(loop_list):
  print(loop_list[i])
  i+=1

# list comprihension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if 'a' in x:
    newlist.append(x)
print(newlist)

# with list comprihension this can be done in single line
newlist = [x for x in fruits if 'a' in x]
print(newlist)

newlist = [x for x in fruits if x != 'apple']
print(newlist)

newlist = [x for x in fruits]
print(newlist)

newlist = [x for x in range(10) if x<5]
print(newlist)

newlist = [x.upper() for x in fruits]
print(newlist)

newlist = ['hello' for x in fruits]
print(newlist)

newlist = [x if x != 'banana' else 'orange' for x in fruits]
print(newlist)

# sorting of list in ascending
fruits_2 = ["orange", "mango", "kiwi", "pineapple", "banana"]
fruits_2.sort()
print(fruits_2)

# sorting of list in descending
fruits_2.sort(reverse=True)
print(fruits_2)

# customizing the sort function
# the below code sorts the element by checking the closest to 50
numbers = [100, 50, 65, 82, 23]
def sortFn(n):
  return abs(n - 50)

numbers.sort(key=sortFn)
print(numbers)

# python's sort function is case sensitive so that means it sorts the capital letter first and small later which results in un expected result
fruits_3 = ["banana", "Orange", "Kiwi", "cherry"]
fruits_3.sort(key = str.lower)
print(fruits_3)

# just reverse the order not sorting

fruits_3.reverse()
print(fruits_3)