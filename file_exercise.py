# filename = 'programming.txt'
# with open (filename,'w') as file_object:
#     file_object.write('I love programming')

# 10-3
# name = input('whats your name')
#
# file_name = 'guest.txt'
# # with open(file_name,'w') as f:
# #     f.write(name)
#
# #10-4
# while True:
#     name = input('whats your name')
#     if name == 'quit':
#         break
#     else:
#         with open(file_name, 'a') as f:
#             f.write(name + "\n")
#         print("Hi " + name + ", you've been added to the guest book.")

# 10-5

filename = 'programming_poll.txt'

responses = []
while True:
    response = input("\nWhy do you like programming? ")
    responses.append(response)

    continue_poll = input("Would you like to let someone else respond? (y/n) ")
    if continue_poll != 'y':
        break

with open(filename, 'a') as f:
    for response in responses:
        f.write(response + "\n")
# filename = 'programming_poll.txt'
# reason = []
#
# while True:
#     answer = input('why do you like programming?')
#     reason.append(answer)
#     if answer == 'quit':
#         break
#
# with open(filename,'w')as f:
#     for r in reason:
#         f.write(r+'\n')

#10-6
try:
    x = input("Give me a number: ")
    x = int(x)

    y = input("Give me another number: ")
    y = int(y)

except ValueError:
    print("Sorry, I really needed a number.")

else:
    sum = x + y
    print("The sum of " + str(x) + " and " + str(y) + " is " + str(sum) + ".")


