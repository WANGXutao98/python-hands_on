# # 列表后面添加元素
# cars = ['ducatti', 'audi']
# cars.append('benz')
# print(cars)
# #列表插入元素
# cars.insert(2,'bmw')
# print(cars)
#
# #列表删除元素
# del cars[0]
# print(cars)
#
# #使用pop()方法删除元素 并且继续使用值. 弹出栈顶元素
# popped_cars = cars.pop()
# print(popped_cars)
# print(cars)
#
# #弹出列表中任何位置的元素
# all_cars = ['ducatti', 'audi','porsche','ferrali']
# first_owned = all_cars.pop(0)
# print(first_owned)
#
#
# # 根据值删除元素 remove
# all_cars.remove('audi')
# print(all_cars)

#3-4 3-5 3-6
# 嘉宾名单
# people = ['wang','tian','ge','zhaung']
# print('I want to invite',people,'to come to the party')
# # 无法赴约嘉宾
# not_come = people.pop(3)
# print(not_come)
# # 邀请新嘉宾
# people.append("fang")
# print(people)
#
# print('Large table')
# people.insert(0,'wan')
#
# people.insert(2,'qing')
#
# people.append('zhuan')
#
# print(people)
#
# #3-7 缩减名单
# print('Only invite two people')
# people_num = len(people)
# print(people_num)
#
# print(people.pop())
#
# # 删除
# del people[0]
# del people[0]
#
# for (int p=0; p<people_num;p++):
#     if people_num > 2:
#         people.pop()
#         p = p-1
#
#     else:
#         print('finish')

# while True:
#     if people_num > 2:
#         people.pop()
#         people_num-1
#
#     else:
#         print('pop end')
#         break

# 列表排序
# cars = ['ducatti', 'audi','porsche','ferrali']
# cars.sort()
# print(cars)
#
# cars.sort(reverse=True)
# print(cars)
#
# # 列
# print(sorted(cars))
# print(cars)

# # 遍历整个列表
# magicians = ['wang','tian','ge','zhaung']
# for m in magicians:
#     print(m)
#
# # 使用range函数
# for value in range(1,7):
#     print(value)
#
# numbers = list(range(1,7))
# print(numbers)
#
# # 把前十个整数的平方加入到一个列表中
# squares = []
# for number in range(1,11):
#     number = number**2
#     squares.append(number)
#
# print(squares)
#
# #列表生成式
# squares = [value**2 for value in range(1,11)]
# print(squares)

# 4-6 打印奇数
# odds = [value for value in range(1,11,2)]
# print(odds)
#
# #4-7 3的倍数
# three_multiple = [value for value in range(1,11,2) if value%3 ==0]
# print(three_multiple)

# 列表切片
#cars = ['ducatti', 'audi','porsche','ferrali']
# print(cars[0:3])
# print(cars[-2:])

#遍历切片
# cars = ['ducatti', 'audi','porsche','ferrali']
# for c in cars[:2]:
#     print(c.title())

# 复制列表
# food = ['chicken', 'beef','fish','duck','pig']
# food_1 =food[:]
#
# # print(food_1)
#
# #4-10
# print(food[0:3])
# print(food[1:4])
# print(food[-3:])

#元组:不可修改的列表
# dimensions = (200,50)
# for dimension in dimensions:
#     print(dimension)
