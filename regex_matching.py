import re

your_string = input("input your string : ")
pattern = input("input your patter : ")

special_char = "[a-z.*]"

check_string = re.match(special_char, your_string)
check_pattern = re.match(special_char, pattern)

if (not check_pattern) or (not check_string):
    print("your pattern/string wrong")
    exit()

result = re.match(pattern, your_string)

if result:
    print("result :", True)
else:
    print("result :", False)
