# Được sắp xếp theo thứ tự và không thể thay đổi, được viết bằng dấu ngoặc tròn
mytuple = ("apple", "banana", "cherry")
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

onetuple = ("apple",) # khi khai báo tuple duy nhất 1 phần tư thì cần thêm dấu phẩy cuối cùng
print(type(onetuple))

# tuple không thể thay đổi, nên khi muốn thay đổi thì thể convert sang list rồi thay đổi, sau đó convert lại tuple

x = ("apple", "banana", "cherry")
y = list(x) # convert to list
y[1] = "kiwi"
x = tuple(y)

print(x)

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

#cách 2: thêm tuple và 1 tuple khác

thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)

fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits #unpack Số lượng biến phải bằng với số lượng phần tử của tuple
print(green)
print(yellow)
print(red)
#nếu ít hơn có thể dùng dấu * ở biến cuối cùng để hiện thị dưới dạng danh sách: #(green, yellow*) = fruits
# Nếu * ở giữa
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)

thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

x = thistuple.count(5)# Đếm số lần xuất hiện
y = thistuple.index(8) #trả về index đầu tiền xuất hiện 8
print(x)
print(y)
