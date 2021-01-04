# def describe(pet_name, animal_type = 'dog'):
#     print(pet_name+' and '+animal_type)
#
#
# describe('harry')
# describe('ham', animal_type = 'cat')


# def get_formatted_name(first_name, last_name):
#     full_name = first_name +' '+last_name
#     return full_name.title()
#
# while True:
#     print('\nPlease tell me your name: ')
#     print('\n Enter q to quit: ')
#
#     f_name = input('FIRST NAME')
#     if f_name == 'q':
#         break
#     l_name = input('last name')
#     if l_name == 'q':
#         break
#
#     formatted_name = get_formatted_name(f_name,l_name)
#     print(formatted_name)


# musician = get_formatted_name('john','lee','hooker')
# print(musician)


# 8-6
# def city_country(city, country):
#     description = city+' '+country
#     return description.title()
#
# while True:
#     print('\nPlease give city and country: ')
#     print('Enter q to quit: ')
#     input_city = input("CITY")
#     if input_city == 'q':
#         break
#
#     input_country = input("country")
#     if input_country == 'q':
#         break
#
#     describe = city_country(input_city, input_country)
#     print(describe)

# 8-7
# def make_album(name, album, songs = ''):
#     if songs:
#         description = name.title()+' '+album.title()+' '+songs
#
#     else:
#         description = name.title() + ' ' + album.title()
#
#     return description
#
# while True:
#
#
#     print('Enter q to quit: ')
#     input_name = input("name")
#     if input_name == 'q':
#         break
#
#     input_album = input("album")
#     input_age = input("age")
#
#     describe = make_album(input_name,input_album,input_age)
#     print(describe)

# def greet_users(names):
#     for name in names:
#         msg = 'hello '+ name.title()
#         print(msg)
#
# usernames = ['hannah','try','margot']
# greet_users(usernames)

# 8-9, 8-10

# def show_magicians(names):
#     for name in names:
#         print(name)
#
#
# def make_great(names):
#     great_magicians = []
#     while names:
#         magician = names.pop()
#         great_magician = magician + ' the Great'
#         great_magicians.append(great_magician)
#
#     for great_magician in great_magicians:
#         names.append(great_magician)
#
#     return names
#
#
# magicians = ['znn', 'david', 'amy']
# show_magicians(magicians)
#
# print("\nGreat magicians:")
# great_magicians = make_great(magicians[:])
# show_magicians(great_magicians)
#
# print("\nOriginal magicians:")
# show_magicians(magicians)
#

# 使用任意数量的关键字实参
# def build_profile(first, last, **userinfo):
#     profile = {}
#     profile['fname'] = first
#     profile['lname'] = last
#
#     for key, value in userinfo.items():
#         profile[key] = value
#
#     return profile
#
#
# user_profile = build_profile('albert', 'einstein', location='princeton', major='physics')
# print(user_profile)

# 8-12
# 这里的topping是一个空的元组，将收到的所有的值
# 封装到这个元组中
# def sandwich(*toppings):
#     print('The sandwich has；' )
#     for t in toppings:
#         print(t)
#
#
# sandwich('ham', 'pepper', 'cheese')

# 8-13
def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value

    return profile


user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics')

print(user_profile)


def car_info(maker, model, **options):
    car_dict = {}
    car_dict['maker'] = maker
    car_dict['model'] = model
    for key, value in options.items():
        car_dict[key] = value

    return car_dict


car_information = car_info('audi', 'a8', color=True)
print(car_information)
