b = "Hello, World!"
print(b[2:5])
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"
age = 36
address= 8
# txt = "My name is John, I am " + age // Không thể dùng như thế này.
txt = "My name is John, and I am {0} {0} {1}"
print(txt.format(age,address))
string1 = "We are the so-called \"Vikings\" from the north."
print(string1)
txt = "Hello     \bWorld!"
print(txt) 
