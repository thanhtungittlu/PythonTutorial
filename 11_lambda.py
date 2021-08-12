# là 1 hàm ẩn danh nhỏ
# Có thể nhận bất kỳ số lượng đối số nào nhưng chỉ có thể có một biểu thức

# Cú pháp
#lambda (tham số truyền vào) : (Biểu thức gái trị)

# Ví dụ

x = lambda a : a + 10
print(x(5))

x = lambda a, b : a * b
print(x(5, 6))

# Cách sử dụng: Thường sử dụng như một hàm ẩn danh bên trong một hàm khác

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
print(mydoubler(10))
