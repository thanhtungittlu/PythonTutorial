# gồm while và for

#break thoát khỏi vòng lặp
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

# continue : bỏ qua lượt lặp đấy
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)


# Kết hợp với else
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")


# Vòng for không yêu cầu phải đặt trước biến chỉ mục
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
for x in range(len(fruits)):
  print(x)

for x in range(2, 6): # in ra 2 3 4 5 
  print(x)

for x in range(2, 30, 3): # chỉ số cuối cùng là bước nhảy
  print(x)

for x in range(6):
  print(x)
else:
  print("Finally finished!")

# Muốn để trống thì dùng pass
for x in [0, 1, 2]:
  pass