# alien_0 = {'color': 'green', 'point': 5}
# # print(alien_0['color'])
# # print(alien_0['point'])
#
# alien_0['x_position'] = 0
# alien_0['y_position'] = 25
# print(alien_0)
#
# alien_1 = {}
# alien_1['x_position'] = 0
# alien_1['y_position'] = 25
# alien_1['speed'] = 'medium'
#
# print('Original x-position is； '+str(alien_1['x_position']))
#
# # move alien right
#
# if alien_1['speed'] == 'low':
#     x_increment  = 1
# elif alien_1['speed'] =='medium':
#     x_increment = 2
# else:
#     x_increment = 3
#
# alien_1['x_position'] = alien_1['x_position']+x_increment
# print('New position:'+str(alien_1['x_position']))
#
# #删除键值对
#
# person = {
#     'first_name': 'zoctopus',
#     'last_name': 'zhang',
#     'age': 21,
#     'city': 'chengdu',
#     }
#
# print(person['first_name'])
# print(person['last_name'])
# print(person['age'])
# print(person['city'])

# 6-3
glossary = {
    'string': 'A series of characters.',
    'comment': 'A note in a program that the Python interpreter ignores.',
    'list': 'A collection of items in a particular order.',
    'loop': 'Work through a collection of items, one at a time.',
    'dictionary': "A collection of key-value pairs.",
    'eee': "A collection of key-value pairs.",
    }

# word = 'string'
# print("\n"+word.title()+":"+glossary[word])
#
# #遍历字典
# for key,value in glossary.items():
#     print('\nKey: '+ key)
#     print('Value；'+ value)

# for key in glossary.keys():
#     print(key.title())

# for key in sorted(glossary.keys()):
#     print(key.title())
#
# for value in sorted(glossary.values()):
#     print(value.title())

#加入set 去重处理
# for des in set(glossary.values()):
#     print(des)

dictionary = {'nile':'egypt','huanghe':'china','amazon':'brazil'}

# for key,value in dictionary.items():
#     print('River '+key +'floats in '+ value )
#
# for key in dictionary.keys():
#     print(key)
#
# for value in dictionary.values():
#     print(value)

#
# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python',
#     }
#
# for name, language in favorite_languages.items():
#     print(name.title() + "'s favorite language is " +
#         language.title() + ".")
#
# print("\n")
#
# coders = ['phil', 'josh', 'david', 'becca', 'sarah', 'matt', 'danielle']
# for c in coders:
#     if c in favorite_languages.keys():
#         print("Thanks for coding, "+c)
#     else:
#         print(c+' we want you to code')


# 嵌套
aliens = []
for alien_number in range(0,30):
    new_alien = {'color':'green', 'points':5,'speed':'low'}
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] ='yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

# for alien in aliens[0:5]:
#     print(alien)

# print('total number of aliens: '+str(len(aliens)))

pizza = {
    'crust':'thick',
    'toppings': ['mushroom','extra_cheese'],
}

# print('you order a '+ pizza['crust']+ '-crust pizza'+
#       'with the following toppings:')
#
# for topping in pizza['toppings']:
#     print('\t'+topping)
#
# 字典中存储字典

users = {
    'aeinstein':{
        'first':'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
}

for username, user_info in users.items():
    print('\n Username: '+username)

    full_name = user_info['first']+''+user_info['last']
    location = user_info['location']

    print('\t Full name；'+full_name.title())
    print('\tLocation: '+location.title())




