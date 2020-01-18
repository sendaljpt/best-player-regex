import re

data = input("please input number of fans and the maximum number of fans can meet: ")

split_data = data.split(" ")

if len(split_data) != 2:
    print("ooppss.. wrong format brooo. ex: 3 2")
    exit(0)

n = int(split_data[0])
t = int(split_data[1])

if not (1 <= t <= n <= 1000):
    print("number of fans must be greater than fans can meet. ex: 6 2")


list_fan = {}
for i in range(n):
    name_quo = input("please input Name and Fan Quotient. : ")

    split_name = name_quo.split(" ")

    if len(split_name) != 2:
        print("ooppss.. wrong format brooo. ex: fajrin 2")
        exit(0)
    
    check_name = re.match("[a-z]", split_name[0])

    if not check_name:
        print("ooppss.. name must in lower case")
        exit(0)

    name = split_name[0]
    quo = int(split_name[1])

    if not (1 <= len(name) <= 20) or not (1 <= quo <= 109):
        print("ooppss.. length of name must be in range 1-20 and fan quotient in range 1-109")
        exit(0)


    list_fan[name] = quo


sort_fan = sorted(list_fan, key=list_fan.get, reverse=True)
length_fan = sort_fan[:t]

print("yyaaaayyyy... fan can meet :) :")
for i in length_fan:
    print(i)