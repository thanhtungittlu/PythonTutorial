# Lớp và đối tượng
# Python là lập trình hướng đối tượng, hầu hết mọi thứ trong python đều là đối tượng
# Lớp giống như phương thức khởi tạo đối tượng, hoặc một bản thiết kế để tạo các đối tượng

# Khởi tạo class
class MyClass:
  x = 5
  y = 7
# Bây giờ có thể tạo 1 lớp tên MyClass để tạo các đối tượng

p1 = MyClass()
print(p1.x, p1.y)

# __init__() tất cả các lớp đều có hàm này, hàm này dùng để gán giá trị cho thuộc tính đối tượng
# hoặc các thao tác cần thực hiện khi đối tượng đang được khởi tạo

# Ví dị khởi tạo 1 lớp tên person, sử dụng __init__() để gán giá trị tên và tuổi
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def myfunc(self):  # Tạo 1 phương thức trong đối tương
    print("Hello my name is " + self.name)

p1 = Person("John", 36)

print(p1.name)
print(p1.age)
p1.myfunc()

# Có thể sửa đổi các thuộc tính
p1.age = 40
print(p1.age)

# Có thể xóa đối tưởng p1
del p1
# print(p1.age)

# Khi để trống 1 lớp thì cần dùng pass
class Person:
  pass