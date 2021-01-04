people = ['wang','tian','ge','zhaung']


# if-elif-else结构
# age = 12
#
# if age<4:
#     print("cost is 0")
# elif age<18:
#     print("cost is 5")
# else:
#     print("cost is 10")

# if语句处理列表
# 检查特殊元素
# people = ['wang','tian','ge','zhaung']
# for p in people:
#     if p == "tian":
#         print("person not found")
#     else:
#         print("person found")
#
# print("finish")

# available = ['mushroom','ham','hawaii','cheese','pepper']
#
# request = ['fries','pepper']
#
# for r in request:
#     if r in available:
#         print("Adding:"+ r)
#     else:
#         print("sorry, we dont have"+r)
#
# print("finish")

#5-8 5-9

# people = ['wang','tian','ge','zhaung','admin']
# #people = []
# if people:
#     for p in people:
#         if p =='admin':
#             print("hello admin")
#         else:
#             print("hi")
#
# else:
#     print("NO user")
#
# #5-10
# current_users = ['eric', 'willie', 'admin', 'erin', 'Ever']
# new_users = ['sarah', 'Willie', 'PHIL', 'ever', 'Iona']
#
# current_users_lower = [user.lower() for user in current_users]
# print(current_users_lower)
#
# for n in new_users:
#     if n.lower() in current_users_lower:
#         print("used,need to create a unique one")
#     else:
#         print("username okay")

#5-11
numbers_list = [n for n in range(1,9)]
print(numbers_list)

for n in numbers_list:
    if n == 1:
        print("1st\n")
    elif n ==2:
        print("2nd\n" )

    else:
        print(str(n)+'th\n')

print("finish")

