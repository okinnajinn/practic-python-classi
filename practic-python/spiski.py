
#Предложение со списком и добавлением из списка слов
#names = ['robert','daun','govo','pedik']
#massage = f"him names {names [0]}, he {names [1]}, likes {names [2]}, because he is {names [3]}"
#print (massage)

#предложение с одним списком из слов
#names = ['robert','daun','govo','pedik']
#message = f"i like {names [2]}, because im a pedik and sosy chlena hahahahahahahaha"
#print (message)

#изменение списка
#names = ['privet','poke','net','armagedon','pochka']
#names[0] = 'sosi'
#print (names[0])

#добавление в список

#names = ['privet','poke','net','armagedon','pochka']
#names.append ('pizda')
#print(names)

#здесь уже мы в пустой список добавляем элементы
#names = []

#names.append ('lada')
#names.append ('xyeglot')
#names.append ('pizda')
#print (names)

#вставка элементов в список

#names = ['privet','poke','net','armagedon','pochka']

#names.insert  (2,"xui")
#print (names)


#удаление из списка при помощи команды del()

#names = ['privet','poke','net','armagedon','pochka']
#del names[1]
#print (names)


#удаление при помоши команды pop()

#names = ['privet','poke','net','armagedon','pochka']

#popped_names = names.pop()

#print (names)
#print (popped_names)

#просто вывести простое сообщение
#names = ['privet','poke','net','armagedon','pochka']
#popped_names = names.pop()
#message = f"hello, please sell your {popped_names}"
#print (message)

#вывод сообщение с извлечением из произволной позиции списка 

#names = ['privet','poke','net','armagedon','pochka']
#popa_names = names.pop(3)
#message = f"hello, go to play {popa_names.upper()} together?"
#print(message)

#удаление элементов по значению

#names = ['privet','poke','net','armagedon','pochka']
#names.remove("privet")
#print(names)

#names = ['privet','poke','net','armagedon','pochka']
#no_privet = "privet"
#names.remove(no_privet)
#print (names)
#message = (f"im not {no_privet}, im zdarova")
#print(message)

#постоянная сортировка списка методом sort()

#names = ['oleg','daun','sosi','sahur','demon','akira']
#names.sort()
#print(names)

#names = ['oleg','daun','sosi','sahur','demon','akira']
#names.sort (reverse=True)
#print(names)

#временная сортировка списка функцией sorted()

#names = ['oleg','daun','sosi','sahur','demon','akira']
#print ('\nтут оригинал')
#print(names)

#print("\nтут отсортировка")
#print (sorted(names))

#print("\nа тут опять орига")
#print( names)

#вывод списка в обратном порядке
#names = ['oleg','daun','sosi','sahur','demon','akira']
#names.reverse()
#print(names)

#возвращение элементов
#names = ['oleg','daun','sosi','sahur','demon','akira']
#print("вот тут орига")
#print(names)

#print("тут реверс")
#names.reverse()
#print(names)

#print("вот тут оргиа")
#names.reverse()
#print(names)


#Определение длинны списка 

#names = ['oleg','daun','sosi','sahur','demon','akira']

#len(names)


#ошибка ондексации

#names = []
#print(names[-1])

#Задания

#names = ['илясик','темочка','рома']

#print (f'\nпривет {names[0]},приглашаю тебя на блядки')
#print (f'\nпривет даун {names[1]},приглашаю тебя на блядки тоже')
#print (f'\nпривет даун {names[2]},приглашаю тебя на блядки но не со мной')



#names = ['илясик','темочка','рома']


#print (f'\nпривет {names[0]},приглашаю тебя на блядки')

#print (f'\nпривет даун {names[1]},приглашаю тебя на блядки тоже')

#print (f'\nпривет даун {names[2]},приглашаю тебя на блядки но не со мной')


#print (f'\nпривет даун {names[2]},ты не смог придти хуеглот,но я тебя все равно люблю')

#roma_names = names.pop(2)

#names.append('саша')

#print(f"\nвот пусть {names[2]} пойдет вместо {roma_names} на блядки, потому что он не смог прийти")



#names = ['илясик','темочка','рома']


#print (f"Расширение гостей сучки")

#names.insert(0 , "сеня")

#names.insert(2 , "максимка")

#names.append("гарфилд")


#print (f'\nпривет {names[1]},приглашаю тебя на блядки')

#print (f'\nпривет даун {names[3]},приглашаю тебя на блядки тоже')

#print (f'\nпривет даун {names[4]},приглашаю тебя на блядки но не со мной')

#print (f'\nпривет {names[0]},приглашаю тебя на блядки')

#print (f'\nпривет даун {names[2]},приглашаю тебя на блядки тоже')

#print (f'\nпривет даун {names[-1]},приглашаю тебя на блядки но не со мной')




#Задание 3.7

#names = ['илясик','темочка','рома']


#print (f"Расширение гостей сучки")

#names.insert(0 , "сеня")

#names.insert(2 , "максимка")

#names.append("гарфилд")


#print (f'\nпривет {names[1]},приглашаю тебя на блядки')

#print (f'\nпривет даун {names[3]},приглашаю тебя на блядки тоже')

#print (f'\nпривет даун {names[4]},приглашаю тебя на блядки но не со мной')

#print (f'\nпривет {names[0]},приглашаю тебя на блядки')

#print (f'\nпривет даун {names[2]},приглашаю тебя на блядки тоже')

#print (f'\nпривет даун {names[-1]},приглашаю тебя на блядки но не со мной')

#print (f"\nИзвините сучки, но на блядки придет только двое, потому что у меня нет места в машине")

#popa_names1 = names.pop(0)

#print(f"\nСорян ублюдки, но {popa_names1} не сможет прийти на блядки")

#popa_names2 = names.pop(1)

#print(f"\nСорян ублюдки, но {popa_names2} не сможет прийти на блядки")

#popa_names3 = names.pop(2)

#print(f"\nСорян ублюдки, но {popa_names3} не сможет прийти на блядки")

#popa_names4 = names.pop(2)

#print(f"\nСорян ублюдки, но {popa_names4} не сможет прийти на блядки")

#print(f"\nвы {names[0]} и {names[1]} все еще приглашены на блядки, потому что вы лучшие друзья, и я вас люблю")

#del names[0]
#del names[0]

#print(f"\nОчищен список гостей по блядскому заданию {names}")


#strani = ['Россия','Америка','Китай','Япония','Германия']

#print(sorted(strani))

#print(f"\n{strani}")


#print(sorted(strani,reverse=True))

#print(f"\n{strani}")

#strani.reverse()

#print(strani)

#strani.reverse()

#print(strani)

#strani.sort()

#print(strani)

#strani.sort(reverse=True)

#print(strani)


#3.9 задание


#names = ['илясик','темочка','рома']


#print (f"Расширение гостей сучки")

#names.insert(0 , "сеня")

#names.insert(2 , "максимка")

#names.append("гарфилд")


#print (f'\nпривет {names[1]},приглашаю тебя на блядки')

#print (f'\nпривет даун {names[3]},приглашаю тебя на блядки тоже')

#print (f'\nпривет даун {names[4]},приглашаю тебя на блядки но не со мной')

#print (f'\nпривет {names[0]},приглашаю тебя на блядки')

#print (f'\nпривет даун {names[2]},приглашаю тебя на блядки тоже')

#print (f'\nпривет даун {names[-1]},приглашаю тебя на блядки но не со мной')

#print (f"\nИзвините сучки, но на блядки придет только двое, потому что у меня нет места в машине")

#popa_names1 = names.pop(0)

#print(f"\nСорян ублюдки, но {popa_names1} не сможет прийти на блядки")

#popa_names2 = names.pop(1)

#print(f"\nСорян ублюдки, но {popa_names2} не сможет прийти на блядки")

#popa_names3 = names.pop(2)

#print(f"\nСорян ублюдки, но {popa_names3} не сможет прийти на блядки")

#popa_names4 = names.pop(2)

#print(f"\nСорян ублюдки, но {popa_names4} не сможет прийти на блядки")

#print(f"\nвы {names[0]} и {names[1]} все еще приглашены на блядки, потому что вы лучшие друзья, и я вас люблю")

#len(names)

#print(names)

#del names[0]
#del names[0]



#print(f"\nОчищен список гостей по блядскому заданию {names}")


#3.10 задание

#names = ['илясик','темочка','рома','даун','соси','педик']

#names[1] = 'сосиска'

#print(names)

#names.append('пидор')

#print(names)

#del names[3]

#print(names)


#pop_names = names.pop(0)

#print(pop_names)

#print(names)

#pop_name = names.pop(0)

#print(pop_name)

#print(f"\nбля {pop_name.upper()} ты кайф поцан ты сюда не входишь")

#pop_name = names.pop(0)

#print(pop_name)

#print(f"\nбля {pop_name} ты кайф поцан ты сюда не входишь")

#re_names = 'педик'

#names.remove(re_names)

#print(names)

#message = (f"\nбля {re_names} ты кайф поцан ты сюда не входишь")

#print(message)

#names.append('гандончик')

#names.append('червячок')

#names.append('прохвост')

#names.append('писун')

#names.append('яблочко')

#names.sort(reverse=True)

#print(names)

#print(sorted(names))

#names.sort()

#print(names)

#names.reverse()

#print(names)

#print(len(names))


#работа с for

#names = ['хуеглотик','педик','жопкич']

#for name in names:
    #print(name)



#names = ['хуеглотик','педик','жопкич']

#for name in names:
    #print(f"привет пистолет {name.title()} рад тя видеть")


#names = ['хуеглотик','педик','жопкич']

#for name in names:
    #print(f"привет пистолет {name.title()} рад тя видеть")
    #print(f"но хотя гандон {name.title()} тоже такой педик ебанный\n")


#names = ['хуеглотик','педик','жопкич']

#for name in names:
    #print(f"привет пистолет {name.title()} рад тя видеть")
    #print(f"но хотя гандон {name.title()} тоже такой педик ебанный\n")

#print("всем ДРАТУТИ")


#names = ['хуеглотик','педик','жопкич']

#for name in names:
    #print(f"привет пистолет {name.title()} рад тя видеть")

#print(f"но хотя гандон {name.title()} тоже такой педик ебанный\n")


#names = ['хуеглотик','педик','жопкич']

#for name in names:
    #print(f"привет пистолет {name.title()} рад тя видеть")
    #print(f"но хотя гандон {name.title()} тоже такой педик ебанный\n")

    #print("всем ДРАТУТИ")

#pizza = ['peperoni','4 сыра','залупня']

#for name in pizza:
    #print(f"я люблю {name.title()} пицку\n")

#print('я реал люблю пицки')

#zoo = ["зебра","лев","шлюха"]

#for anim in zoo:
    #print(f"приколдесики {anim.title()}")
    #print(f"вот мне нравится {anim.title()} потому что он кайфовый рыля\n")

#print("не ну а так все хорошие мрази")

#функция range()

#for value in range(1,5):
    #print(value)

#numbers = list(range(1,6))
#print(numbers)

#numbers = list(range(2,18,2))
#print(numbers)

#numbers = []

#for value in range(1,11):
    #belka = value**2
    #numbers.append(belka)

#print(numbers)

#numbers = [1,2,3,4,5,6,7,8,9,0]

#print(min(numbers))

#print(max(numbers))

#print(sum(numbers))

#numbers = [value**2 for value in range(1,6)]

#print(numbers)



#for value in range(1,21):
    #print(value)


#numbers = []

#for value in range (1,1000000):
    #numbers.append(value)

#print(numbers)


#numbers  = []

#for value in range(1,1000000):
   # numbers.append(value)

#print(min(numbers))

#print(max(numbers))

#print(sum(numbers))


#numbers = []

#for value in range (1,21,3):
    #numbers.append(value)

#print(numbers)

#numbers = []

#for value in range(3,31,3):
    #numbers.append(value)

#print(numbers)

#numbers = [value**3 for value in range(1,11)]

#print(numbers)

#numbers = []

#for value in range(1,11):
    #value = value**3
    #numbers.append(value)
   
#for number in numbers:
   # print(number)


#players = ["хуеглот","жопочлен","дебил","педик"]

#print(players[0:2])


#players = ["хуеглот","жопочлен","дебил","педик"]

#print(players[-2:])


#players = ["хуеглот","жопочлен","дебил","педик"]

#print ('Здарова чудики ебанные')

#for player in players[0:4]:
    #print(player.title())



#my_eda = ["жопа","котлети","пепероня"]

#ne_eda = my_eda[:]

#print("мне нравится такая еда")
#print(my_eda)

#print("а мне нравится такая елда")
#print(ne_eda)



#my_eda = ["жопа","котлети","пепероня"]
#ne_eda = my_eda[:]

#my_eda.append("морожка")
#print("мне нравится такая еда")
#print(my_eda)


#ne_eda.append("член")
#print("а мне нравится такая елда")
#print(ne_eda)

#my_eda = ["жопа","котлети","пепероня"]
#ne_eda = my_eda

#my_eda.append("морожка")
#ne_eda.append("член")
#print("мне нравится такая еда")
#print(my_eda)



#print("а мне нравится такая елда")
#print(ne_eda)

#names = ["даун","негр","блич","пидрила","гандончик"]

#print(names[1:4])

#pizza = ["пеперони","4 сыра","залупня"]

#friends_pizza = pizza[:]

#pizza.append('хуеглот с пенисами')
#pizza.append("пеперони с ананасами")
#friends_pizza.append("4 сыра с ананасами")

#print("мне нравится такая пицца")

#for pizz in pizza:
    #print(pizz.title())


#print("\nа моим друзьям нравится такая пицца")
#for pizz in friends_pizza:
    #print(pizz.title())


#my_eda = ["жопа","котлети","пепероня","морожка","член"]

#ne_eda = my_eda[:]

#print("мне нравится такая еда")
#for eblan in my_eda:
    #print(eblan)

#print("а моему другу нравится такая еда")
#for eblan in ne_eda:
    #print(eblan.title())


#hui = (200,50)

#print(hui[0])

#print(hui[1])

#dimensions = (200,50)

#dimensions[0] = 250


#dimensions = (200,50)

#for dimension in dimensions:
    #print(dimension)


#xui = (200,50)

#print("original xui")
#for xueglot in xui:
   #print(xueglot)


#xui = (400,100)
#print("модифицированный xui")
#for xueglot in xui:
    #print(xueglot)


#stol = ("пудик","стейк","пельмени","сосиска","котлеты")

#print("вывод меню")
#for food in stol:
    #print(food)

#stol = ("шлюха","корм для собак","пельмени","сосиска","котлеты")

#print("\nизменение меню")
#for food in stol:
    #print(food)

#car = ["bmx","audi","mercedes","toyota","lexus"]

#for cars in car:
    #if cars == "audi":
        #print(cars.upper())
    #else:
        #print(cars.title())


#reqiested_toping = "грибы"

#if reqiested_toping != "анчоусы":
    #print("принеси мне анчоусы сука")


#answer = "17"

#if answer != "42":
    #print("не корректно вводишь пидорас нельзя те")

#age0 = "21"
#age1 = "18"
#age12 = "13"
#age13 = "14"
#age2 = "67"
#age3 = "3214124"
#if age1 < age0 and age12:
    #print("не проходишь в стрипуху сорянькич")

#if age0 >= age1:
    #print("прохордишь блядуй")


#if age2 >= age0 and age3:
    #print("старик иди нахрен")

#if age12 and age13 < age0:
    #print("идите в детсад дауны")

# request_topings = ["писечко","попочка","дерьмо"]

# print("пепероня" in request_topings)

# print("писечко" in request_topings)

#ban = ["дебил","антон","темик"]

#user = "иля"

#if user not in ban:
#     print(f"привет {user.title()},ты не в бане сударь")

# name = "иля"

# print("это имя == 'темик', я думаю это False")
# print(name == "темик")

# print("это имя == 'пепероня' и думаю это False")
# print(name == "пепероня")

# print("это имя == 'иля' и думаю это False")
# print("иля" in name)

# print("это имя 'хуеглот' и думаю это False")
# print(name == "хуеглот")

# name1 = "шлюха"

# print("думаю это имя 'пися' и это False")
# print (name1 == "пися")

# print("думаю это 'шлюха' и думаю это True")
# print(name1 == "шлюха")

# name2 = "тортик"

# print("думаю это 'тортик' и думаю это True")
# print (name2 == "тортик")


# name3 = "папич"
# print("думаю это 'папич' и это True")
# print ( name3 == "папич")

# name4 = "челик"
# print("думаю это 'челик' и это True")
# print ( name4 == "челик")

# name5 = "какашечка"
# print("думаю это 'какашечка' и это True")
# print ( name5 == "какашечка")



# car = "Audi"

# print (car == "Audi")
# print(car == "audi")

# print(car.lower() == "audi")

# age1 = 18
# age2 = 21
# age3 = 52
# age4 = 67


# print(age1 != '21')
# print(age2 == "18")


# if age1 > age2:
#     print("ты проходтшь")

# if age1 < age2:
#     print("ты не проходтшь ты маленьки")

# if age1 >= age2:
#     print("ты проходтшь")
# else:
#     print("ты маленьки свали")

# if age2 <= age3:
#     print("ты проходишь")

# if age1 < age3 and age2 < age3:
#     print("ебать вы мелкие сучары")

# if age2 >age3 or age2 <age4:
#     print("СИКСЕВЕН")

# name = ("сиксевен","попка","какашечки")

# print("попка" in name)


# print("тимоти шаломе" in name)



# age = "19"

# if age >= "18":
#     print("ты можешь голосовать")
#     print("за че голосовать буш?")


# age = 17

# if age >= 18:
#     print("ты стари ")
# else:
#     print("ты не можешь голосовать иди нах")

# age = 18

# if age < 4:
#     print("вход фри те")
# elif age < 18:
#     print("25 баксов с тя чудик")
# else:
#     print("40 бачей тварь дай ты старый")

# age = 19

# if age < 4:
#     price = 0
# elif age < 18:
#     price = 25
# else:
#     price = 40
# print(f"с тебя {price} баксов чудик")

# age = 23

# if age < 4:
#     price = 0
# elif age < 18:
#     price = 25
# elif age < 65:
#     price = 40
# else:
#     price = 20
# print(f"с тебя {price} баксов чудик")

# age = 65

# if age < 4:
#     price = 0
# elif age < 18:
#     price = 25
# elif age < 65:
#     price = 40
# elif age >= 65:
#     price = 20
# print(f"с тебя {price} баксов чудик")

# toping = ["дохуя сыра","грибы"]

# if "член на палке" in toping:
#     print("добавлен член на палке")
# elif "дохуя сыра" in toping:
#     print("добавлено дохуя сыра ода детка")
# elif "грибы" in toping:
#     print("добавлены грибы ублюдские")

# print("вот твоя пицка")

# toping = ["дохуя сыра","грибы"]

# if "член на палке" in toping:
#     print("добавлен член на палке")
# if "дохуя сыра" in toping:
#     print("добавлено дохуя сыра ода детка")
# if "грибы" in toping:
#     print("добавлены грибы ублюдские")

# print("вот твоя пицка")

# requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
# for requested_topping in requested_toppings:
#     print(f"Adding {requested_topping}.")
# print("\nFinished making your pizza!")

# toping = ["зеленый перчик","пепероня","сир"]

# for topings in toping:
#     if topings == "зеленый перчик":
#         print("перчика нет даун")
#     else:
#         print(f"добавлены {topings}")
# print("ваша пицка готова")

# toping = ['член коня']

# if toping:
#     for topings in toping:
#         print(f"добавлен топинг {topings}")
# else:
#     print("хочешь дефолт пицку?")

# have_toping = ["грибы","лук","броколи","огурцы","бананчики"]

# people_toping = ["грибы","вагина динозавра","бананчики"]

# for people_topings in people_toping:
#     if people_topings in have_toping:
#         print(f"добавлен топинг {people_topings}")
#     else:
#         print(f"такого топинга нет ща {people_topings}")
# print("ваша пицка готова")


