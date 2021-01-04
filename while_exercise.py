# number = input("please enter a number to tell odd or even: ")
# number = int(number)
#
# if number%2 == 0:
#     print("\n The input is even")
#
# else:
#     print("\nThe input is odd")

# while 循环
# current = 1
# while current <= 5:
#     print(current)
#     current += 1


prompt = '\n Tell me something'
prompt +='\n Enter quit to end '

# active = True
# while active:
#     message = input(prompt)
#
#     if message == 'quit':
#         active = False
#
#     else:
#         print(message)


# while True:
#     city  = input(prompt)
#
#     if city == 'quit':
#         break
#     else:
#         print("ok")
#
# current = 0
# while current < 10:
#     current +=1
#     if current %2 ==0:
#         continue
#
#     print(current)


#7-5

# age = "please input age: "
#
#
# while True:
#     audience = input(age)
#
#
#     if audience == 'quit':
#         break
#
#     aud = int(audience)
#     if 3 <= aud <= 12:
#         print("fee is 10")
#     if aud <= 3:
#         print("free")
#
#     elif aud > 12:
#         print("fee is 15")
#
#     else:
#         print('continue')

# 使用while循环处理列表和字典
unconfirmed = ['alice','brian','candice','alice','alice']
confirmed = []

# while unconfirmed:
#     current = unconfirmed.pop()
#     print("verifying user"+current.title())
#     confirmed.append(current)
#
# print('\n All the confirmed users are: ')
# for c in confirmed:
#     print(c.title())

# while 'alice' in unconfirmed:
#     unconfirmed.remove('alice')
#
# print(unconfirmed)

# responses = {}
# active = True
#
# while active:
#     name = input('\n what is  your name')
#     response = input("indicate a day")
#
#     responses[name] = response
#
#     repeat = input('\n would you like to let another person?')
#     if repeat == 'no':
#         active = False
#
#     for name, response in responses.items():
#         print(name+'would like to come '+response)


#7-8
# sandwich_orders = [
#     'pastrami', 'veggie', 'grilled cheese', 'pastrami',
#     'turkey', 'roast beef', 'pastrami']
# finished_sandwiches = []
#
# for sw in sandwich_orders:
#     print("I made your sandwich: "+sw)
#     finished_sandwiches.append(sw)
#
# print(finished_sandwiches)

responses = {}
active = True

while active:
    name = input('\n what is  your name')
    response = input("give me a place")

    responses[name] = response

    repeat = input('\n would you like to let another person?')
    if repeat == 'no':
        active = False

    for name, response in responses.items():
        print(name+'would like to come '+response)