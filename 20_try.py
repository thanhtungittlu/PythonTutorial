try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")

try:
  print("Hello")
except:
  print("Something went wrong")                      #Sai thi xảy ra
else:
  print("Nothing went wrong")                   # Đúng thì xảy ra
finally:                                       #Khi nào cũng xảy ra
  print("The 'try except' is finished")