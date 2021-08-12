# trình lặp
# Lists, tuples, dictionaries, and sets đều có thể lặp bằng phương thức iter()

mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))


for x in mytuple:
  print(x)

# Vòng lặp for là tạo ra 1 trình lặp, và sử dụng phương thức next() cho mỗi lần lặp

# Chuỗi cũng có thể dùng trình lặp
mystr = "banana"
myit = iter(mystr)
print(next(myit))
print(next(myit))

print("---------------")

# Khởi tạo trình lặp
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 10:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration # Điều kiện kết thúc

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))


for x in myiter:
  print(x)