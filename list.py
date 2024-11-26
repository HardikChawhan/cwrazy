for i in range(50):
  if i%5 == 0:
    print(i)

listId = []
listName = []

for i in range(10):
  id = int(input("Enter id: "))
  name = input("enter name: ")
  listId.append(id)
  listName.append(name)

for i in range(len(listId)):
  print("#",listId[i],"-",listName[i])

list1 = [1,2,3,4,5,6,7,8,9,10,11,12,13]

even = []
odd = []

for i in range(len(list1)):
  if list1[i]%2==0:
    even.append(list1[i])
  else:
    odd.append(list1[i])

print('Even list')
for i in range(len(even)):
  print(even[i])

print('odd list')
for i in range(len(odd)):
  print(odd[i])