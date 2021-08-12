# Kế thừa
# Cho phép định nghĩa 1 lớp kế thừa tất cả phương thức, thuộc tính từ lớp khác

#Tạo 1 Parent Class ( Lớp cha)

class Person:
    def __init__(self, fname, lname):
        self.firstName = fname
        self.lastName = lname
    def printName(self):
        print(self.firstName + " " + self.lastName)

p1 = Person("Thanh", "Tùng")
p1.printName()

#Tạo 1 Child Class (Lớp con), Dùng pass khi không muốn thêm các phương thức hay thuộc tính vào lớp con
class Student(Person):
  pass
p2 = Student("Mike", "Olsen")
p2.printName()

class Teacher(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname) # Hoặc có thể dùng super().__init__(fname, lname)
    self.age = 30 #Thêm thuộc tính mới vào lớp con
  def printFirstName(self): # Thêm phương thức mới vào lớp con
    print(self.firstName )  
  def printAge(self): # Thêm phương thức mới vào lớp con
    print(self.age ) 

p3 = Teacher("Minh", "Thu")
p3.printFirstName()
p3.printName()
p3.printAge()