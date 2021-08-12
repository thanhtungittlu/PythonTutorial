x = 4
y = str(4) # y = "4"
z = "alo"
print(x, type(x))
print(y, type(y))
print(z, type(z))
a="5"
b="10"
c=a+b
print(c, type(c))

x = "awesome"


def myfunc():
  x = "fantastic" #Muốn khai báo 1 biến toàn cục trong 1 hàm thì dùng từ khóa global
  print("Python is " + x)
myfunc()

print("Python is " + x)