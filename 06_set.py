#Không có thứ tự, và không có chỉ mục, không thể thay đổi, không cho phép trùng lặp
# Có thể lặp qua bằng vòng for , và từ khóa in
thisset = {"apple", "banana", "cherry"}
print(thisset, type(thisset))

#Không thể thay đổi nhưng có thể thêm (add)
thisset.add("orange")
print(thisset)

#thêm vào từ 1 set khác từ update(), loại bỏ phần tử trùng lặp
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

#Xóa 1 phần tử
thisset.remove("banana") #Nếu mục xóa k tồn tại thì remove gây ra lỗi
print(thisset)
thisset.discard("mango") #Nếu mục xóa k tồn tại thì discard không gây ra lỗi
print(thisset)

#Có thể dùng thisset.pop() để xóa mục cuối cùng, nhưng set không có thứ tự, nên sẽ không biết được mục nào bị xóa
# pop() trả về mục vị xóa

#clear() làm trống danh sách

#union cũng có thể ghép dánh sách, loại bỏ phần tử trùng lặp
set1 = {"a", "b" , "c",3}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)

#intersection_update() giữ lại các mục chung của 2 tập hợp
x = {"apple", "banana", "cherry","56"}
y = {"google", "microsoft", "apple","56"}
k = x.intersection_update(y)
z = x.intersection(y)   # trả về 1 new set

print(x,type(k))
print(z,type(z))

#symmetric_difference_update() Phương thức giữ lại những phần tử không có trong cả 2 tập hợp
a = {"apple", "banana", "cherry"}
b = {"google", "microsoft", "apple"}
a.symmetric_difference_update(b)
print(a)



x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)  # trả về 1 new set
print(z)

