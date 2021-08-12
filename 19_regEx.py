# regex là 1 chuỗi các ký tự tạo thành mẫu tìm kiếm
# có thể dùng để tìm kiếm
import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt) # Bắt đầu bằng The và kết thúc bằng spain

if x:
  print("YES! We have a match!")
else:
  print("No match")