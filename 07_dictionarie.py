# lưu giữ các cặp giá trị gồm key và value
# Có thể thay đổi, nhưng không cho phép trùng lặp
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(thisdict)

# Có thể tham chiếu bằng cách sử dụng tên khóa
print(thisdict["brand"])

# Trả về danh sách các keys
x = thisdict.keys()
print(x)
# Trả về danh sách các values
y = thisdict.values()
print(y)

# Trả về mỗi mục dưới dạng các bộ
a = thisdict.items()
print(a)

# Kiểm tra xem key có trong dictionary không
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")

# Update
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})

# Xóa với key
thisdict.pop("model")
## popitem() xóa phần tử cuối
print(thisdict)

# clear() làm trống từ điển
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)

# Vòng lặp trả về các keys
for x in thisdict:
  print(x)

# Muốn trả về các values 
for x in thisdict.values():
  print(x)
  
# Muốn lặp qua cả 2
for x, y in thisdict.items():
  print(x, y)

# Cách copy, nếu dùng dictcopy = thisdict thì cả 2 sẽ cùng tham chiếu đến 1 vùng giá trị
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)

# Từ điển lồng nhau
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print(myfamily["child1"]["name"])