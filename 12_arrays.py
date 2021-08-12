# Python không có mảng, nhưng có thể dùng list để thay thế choa array, tuy nhiên phải dùng thư viện
# hỗ trợ, ví dụ như numpy

cars = ["Ford", "Volvo", "BMW"]

# append() để thêm 1 phần tử vào mảng

cars.append("VinFast")
print(cars)

# pop() để xóa 1 phần tử của mảng, hoặc sự dụng remove

cars.pop(1) # index của vị trí cần xóa
print(cars) 
# cars.remove("Ford")