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


# 3 일차

dictionary = {}
dictionary["a"] = "A"
print(dictionary)

"""
Again, the code is broken, you need to create 4 functions.
  - add_to_dict: Add a word to a dict.
  - get_from_dict: Get a word from inside a dict.
  - update_word: Update a word inside of the dict.
  - delete_from_dict: Delete a word from the dict.

All this functions should check for errors, follow the comments to see all cases you need to cover.

There should be NO ERRORS from Python in the console.
"""

def add_to_dict(dic,*args):
  if type(dic) != dict:
    print(f"You need to send a dictionary. You sent: {type(dic)}")
  elif len(args) != 2:
    print("You need to send a word and a definition.")
  elif args[0] in dic:
    print(f"{args[0]} is already on dictionary. Won't add.")
  else:
    print(f"{args[0]} has benn added.")
    dic[args[0]] = args[1]
  pass

def get_from_dict(dic,*args):
  if type(dic) != dict:
    print(f"You need to send a dictionary. You sent: {type(dic)}")
  elif len(args) != 1:
    print("You need to send a word to search for.")
  elif args[0] in dic:
    print(f"{args[0]}: {dic[args[0]]}")
  else:
    print(f"{args[0]} was not found in this dict.")
  pass

def update_word(dic,*args):
  if type(dic) != dict:
    print(f"You need to send a dictionary. You sent: {type(dic)}")
  elif len(args) != 2:
    print("You need to send a word and a definition to update.")
  elif args[0] in dic:
    print(f"{args[0]} has been updated to: {dic[args[0]]}")
  else:
    print(f"{args[0]} is no on the dict. Can't update non-existing word.")
  pass

def delete_from_dict(dic,*args):
  if type(dic) != dict:
    print(f"You need to send a dictionary. You sent: {type(dic)}")
  elif len(args) != 1:
    print("You need to specify a word to delete.")
  elif args[0] in dic:
    print(f"{args[0]} has been deleted.")
    dic.pop(args[0])
  else:
    print(f"{args[0]} is not in tihs dict. Won't delete.")
  pass

# \/\/\/\/\/\/\ DO NOT TOUCH  \/\/\/\/\/\/\

import os

os.system('clear')


my_english_dict = {}

print("\n###### add_to_dict ######\n")

# Should not work. First argument should be a dict.
print('add_to_dict("hello", "kimchi"):')
add_to_dict("hello", "kimchi")

# Should not work. Definition is required.
print('\nadd_to_dict(my_english_dict, "kimchi"):')
add_to_dict(my_english_dict, "kimchi")

# Should work.
print('\nadd_to_dict(my_english_dict, "kimchi", "The source of life."):')
add_to_dict(my_english_dict, "kimchi", "The source of life.")

# Should not work. kimchi is already on the dict
print('\nadd_to_dict(my_english_dict, "kimchi", "My fav. food"):')
add_to_dict(my_english_dict, "kimchi", "My fav. food")


print("\n\n###### get_from_dict ######\n")

# Should not work. First argument should be a dict.
print('\nget_from_dict("hello", "kimchi"):')
get_from_dict("hello", "kimchi")

# Should not work. Word to search from is required.
print('\nget_from_dict(my_english_dict):')
get_from_dict(my_english_dict)

# Should not work. Word is not found.
print('\nget_from_dict(my_english_dict, "galbi"):')
get_from_dict(my_english_dict, "galbi")

# Should work and print the definiton of 'kimchi'
print('\nget_from_dict(my_english_dict, "kimchi"):')
get_from_dict(my_english_dict, "kimchi")

print("\n\n###### update_word ######\n")

# Should not work. First argument should be a dict.
print('\nupdate_word("hello", "kimchi"):')
update_word("hello", "kimchi")

# Should not work. Word and definiton are required.
print('\nupdate_word(my_english_dict, "kimchi"):')
update_word(my_english_dict, "kimchi")

# Should not work. Word not found.
print('\nupdate_word(my_english_dict, "galbi", "Love it."):')
update_word(my_english_dict, "galbi", "Love it.")

# Should work.
print('\nupdate_word(my_english_dict, "kimchi", "Food from the gods."):')
update_word(my_english_dict, "kimchi", "Food from the gods.")

# Check the new value.
print('\nget_from_dict(my_english_dict, "kimchi"):')
get_from_dict(my_english_dict, "kimchi")


print("\n\n###### delete_from_dict ######\n")

# Should not work. First argument should be a dict.
print('\ndelete_from_dict("hello", "kimchi"):')
delete_from_dict("hello", "kimchi")

# Should not work. Word to delete is required.
print('\ndelete_from_dict(my_english_dict):')
delete_from_dict(my_english_dict)

# Should not work. Word not found.
print('\ndelete_from_dict(my_english_dict, "galbi"):')
delete_from_dict(my_english_dict, "galbi")

# Should work.
print('\ndelete_from_dict(my_english_dict, "kimchi"):')
delete_from_dict(my_english_dict, "kimchi")

# Check that it does not exist
print('\nget_from_dict(my_english_dict, "kimchi"):')
get_from_dict(my_english_dict, "kimchi")

# \/\/\/\/\/\/\ END DO NOT TOUCH  \/\/\/\/\/\/\