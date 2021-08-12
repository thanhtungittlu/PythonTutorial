def my_function():
  print("Hello from a function")
my_function()

def my_function1(fname): #tham số dc truyền vào hàm
  print(fname + " Refsnes")

my_function1("Emil") # Đối số
my_function1("Tobias")

#Tham số là biến được liên kết bên trong dấu ngoặc đơn trong định nghĩa của hàm.
#Đối số là giá trị được gửi đến hàm khi nó được gọi.

# Thêm dấu * vào trước tham số truyền vào để không giới hạn cố tham số được truyền 
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")




# Gửi đối số dưới dạng key: value, danh sách các tham số truyền vào không quan trọng thứ tự
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)
my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

# Thêm 2 dấu sao trước tham số truyền vào khi không biết số lượng
def my_function(**kid):
  print("His last name is " + kid["lname"])
my_function(fname = "Tobias", lname = "Refsnes")



# Nếu gọi hàm mà không truyền đối số vào thì sẽ được chạy với tham số mặc định
def my_function(country = "Norway"):
  print("I am from " + country)
my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

# Kết quả trả về
def my_function(x):
  return 5 * x
print(my_function(3))

# Định nghĩa hàm không được để trống nhưng nếu có lý do cần thiết thì cần dùng pass để để trống
def myfunction():
  pass


# Hàm đệ quy: Gọi lại chính nó trong hàm
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)