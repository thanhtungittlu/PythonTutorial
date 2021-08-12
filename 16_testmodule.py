import mymodule 

mymodule.greeting("Jonathan")
a = mymodule.person1["age"]
print(a)

import mymodule  as mx
mx.greeting("Jonathan")


import platform #modele mặc định của python

x = dir(platform) # Liệt kê tất cả các hàm tron module
print(x)

from mymodule import person1 # Chỉ nhập person1
print (person1["age"])