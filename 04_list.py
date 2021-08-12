thislist = ["apple", "banana", "cherry",1,4]
print(len(thislist))

for i in range(len(thislist)):
  print(thislist[i])

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x] # Tạo mới 1 danh sách có chữ a
print(newlist)