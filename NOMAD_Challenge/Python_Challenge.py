# 1일차 퀴즈 관련

myNameIs = "nico"
print(myNameIs)

my_name_is = "nico"
print(my_name_is)

dic = {"tup":("T","U","P","L","E")}
print(dic)
print(dic["tup"])


# 2일차 퀴즈 관련

# This Blueprint code is broken. There are some functions missing, you need to create them. When you run the code, the output must look like this!
#오늘의 과제를 열어보시면 제대로 작동하지 않습니다. 그 이유는 프로그램이 돌아가기 위한 몇몇 코드들이 없기 때문입니다. 그러므로 프로그램이 제대로 돌아가기 위해 여러분들이 직접 코드를 작성 하셔야 됩니다.

"""
As you can see, the code is broken.
Create the missing functions, use default arguments.
Sometimes you have to use 'return' and sometimes you dont.
Start by creating the functions
"""

# 입력된 문자열이 리스트에 있는지 확인
def is_on_list(list, string):
  if string in list:
    return "True"
  return "False"

# 리스트의 n 번째 요소 출력
def get_x(list, integer):
  return list[integer]

# 리스트에 요소 추가
def add_x(list, string):
  list.append(string)
  return list

# 리스트에서 요소 삭제
def remove_x(list, string):
  list.remove(string)
  return list

# \/\/\/\/\/\/\  DO NOT TOUCH AREA  \/\/\/\/\/\/\ #

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

print("Is Wed on 'days' list?", is_on_list(days, "Wed"))

print("The fourth item in 'days' is:", get_x(days, 3))

add_x(days, "Sat")
print(days)

remove_x(days, "Mon")
print(days)

# /\/\/\/\/\/\/\ END DO NOT TOUCH AREA /\/\/\/\/\/\/\ #


