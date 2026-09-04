# class dog():
#     def __init__(self , name , age ):
#         self.name = name
#         self.age = age

#     def sit(self):
#         print(f"сейчас {self.name} села и покакала")

#     def roll_over(self):
#         print(f"{self.name} делает перекатыч")


# my_dog = dog("вилли" , 6)
# print(f"мою собачку зовут {my_dog.name}")
# print(f"и ему {my_dog.age} лет")
# my_dog.sit()
# my_dog.roll_over()

# your_dog = dog("кристи" , 4)
# print(f"\nтвою собачку зовут {your_dog.name}")
# print(f"и ей {your_dog.age} лет")
# your_dog.sit()
# your_dog.roll_over()



# class Restuarant():
#     def __init__(self , rest_name , cuisine_type):
#         self.rest_name = rest_name
#         self.cuisine_type = cuisine_type

#     def open_rest(self):
#         print(f"сейчас ресторан - {self.rest_name} открыт")

#     def close_restik(self):
#         print(f"сейчас ресторан - {self.rest_name} закрыт")

#     def one_rest(self):
#         print(f"\nвот кароч ресторанчик так называется - {self.rest_name}")

   


# rest_vibe = Restuarant("ля попа" , 45 )

# rest_vibe.one_rest()

# print(f"сколько столов свободных в ресторане - {rest_vibe.cuisine_type}")

# rest_vibe.open_rest()



# close_rest = Restuarant("ля писька" , 24)

# close_rest.one_rest()

# print(f"сколько столов свободных в ресторане - {close_rest.cuisine_type}")

# close_rest.close_restik()


# rest_last = Restuarant("ля какаха" , 67)

# rest_last.one_rest()

# print(f"сколько столов свободных в ресторане - {rest_last.cuisine_type}")

# rest_last.open_rest()



# class User():
#     def __init__(self , f_name , l_name , age , info):
#         self.first_name = f_name
#         self.last_name = l_name
#         self.age = age
#         self.information = info


#     def name_user(self):
#         print(f"\nимя - {self.first_name}")

#     def last_n_user(self):
#         print(f"фамилия - {self.last_name}")

#     def age_user(self):
#         print(f"возраст - {self.age}")

#     def info_user(self):
#         print(f"информация о человеке - {self.information}")

#     def hi(self):
#         print(f"приветствую нового пользователя - привет {self.first_name} {self.last_name}")

# print(f"вот вся информация о пользователе:")

# full_info = User("иля" , "моладав" , "19" , "люблю дашу и играть в гамесы" )

# full_info_2 = User("тема" , "льянов" , "19" , "любит своих шпицыков")

# full_info.name_user()
# full_info.last_n_user()
# full_info.age_user()
# full_info.info_user()
# full_info.hi()

# full_info_2.name_user()
# full_info_2.last_n_user()
# full_info_2.age_user()
# full_info_2.info_user()
# full_info_2.hi()


# class Car():

#     def __init__(self, make , model , year):
#         self.make = make
#         self.model = model
#         self.year= year
#         self.odometer_reading = 0

#     def get_full_name(self):
#         long_name = f"{self.make} {self.model} {self.year}"
#         return long_name.title()

#     def odom_reading(self):
#         print(f"пробег машины - {self.odometer_reading}")

# my_new_car = Car("BMW" , "amg192" , "2023")

# print(my_new_car.get_full_name())
# my_new_car.odom_reading()
    

# class Car():

#     def __init__(self, make , model , year):
#         self.make = make
#         self.model = model
#         self.year= year
#         self.odometer_reading = 0

#     def get_full_name(self):
#         long_name = f"{self.make} {self.model} {self.year}"
#         return long_name.title()

#     def odom_reading(self):
#         print(f"пробег машины - {self.odometer_reading}")

#     def update_probeg(self , probeg):
#         if probeg > self.odometer_reading:
#             self.odometer_reading = probeg
#         else:
#             print(f"что у тя с пробегом даун?")

#     def plus_probeg(self , plus_probeg):
#         self.odometer_reading += plus_probeg



# my_new_car = Car("BMW" , "amg192" , "2023")
# print(my_new_car.get_full_name())


# my_new_car.update_probeg(67_500)
# my_new_car.odom_reading()
# my_new_car.plus_probeg(400)
# my_new_car.odom_reading()





# class Restuarant():
#     def __init__(self , rest_name , cuisine_type):
#         self.rest_name = rest_name
#         self.cuisine_type = cuisine_type
#         self.number_people = 23

#     def open_rest(self):
#         print(f"сейчас ресторан - {self.rest_name} открыт")

#     def close_restik(self):
#         print(f"сейчас ресторан - {self.rest_name} закрыт")

#     def one_rest(self):
#         print(f"\nвот кароч ресторанчик так называется - {self.rest_name}")

#     def numbers_people(self):
#         print(f"обслуженные посетители - {self.number_people}")


#     def set_number_served(self , save_number):
#         save_number > self.number_people 
#         self.number_people = save_number
#         print(f"новые посетители, обслуженные посетители - {save_number}")

#     def plus_number_people(self , plus_people):
#         self.number_people += plus_people
#         print(f"за день обслужено гостя/гостей - {plus_people} ")
        


        
# rest_vibe = Restuarant("ля попа" , 45 )
# rest_vibe.one_rest()
# print(f"сколько столов свободных в ресторане - {rest_vibe.cuisine_type}")
# rest_vibe.open_rest()
# rest_vibe.numbers_people()
# rest_vibe.set_number_served(26)
# rest_vibe.plus_number_people(123)


# close_rest = Restuarant("ля писька" , 24)
# close_rest.one_rest()
# print(f"сколько столов свободных в ресторане - {close_rest.cuisine_type}")
# close_rest.close_restik()
# close_rest.numbers_people()
# close_rest.set_number_served(34)
# close_rest.plus_number_people(152)

# rest_last = Restuarant("ля какаха" , 67)
# rest_last.one_rest()
# print(f"сколько столов свободных в ресторане - {rest_last.cuisine_type}")
# rest_last.open_rest()
# rest_last.numbers_people()
# rest_last.set_number_served(69)
# rest_last.plus_number_people(300)






# class User():
#     def __init__(self , f_name , l_name , age , info):
#         self.first_name = f_name
#         self.last_name = l_name
#         self.age = age
#         self.information = info
#         self.open_site = 0

#     def name_user(self):
#         print(f"\nимя - {self.first_name}")

#     def last_n_user(self):
#         print(f"фамилия - {self.last_name}")

#     def age_user(self):
#         print(f"возраст - {self.age}")

#     def info_user(self):
#         print(f"информация о человеке - {self.information}")

#     def hi(self):
#         print(f"приветствую нового пользователя - привет {self.first_name} {self.last_name}")


#     def plus_login_attempents(self ):

#         self.open_site = self.open_site + 1
#         print(f"количество попыток входа в систему -  {self.open_site} ")
        
#     def reset_login_attempents(self):
#         self.open_site = 0
#         print(f"попыток входа в систему обнулился - {self.open_site} ")

# print(f"вот вся информация о пользователе:")

# full_info = User("иля" , "моладав" , "19" , "люблю дашу и играть в гамесы" )

# full_info_2 = User("тема" , "льянов" , "19" , "любит своих шпицыков")

# full_info.name_user()
# full_info.last_n_user()
# full_info.age_user()
# full_info.info_user()
# full_info.hi()
# full_info.plus_login_attempents()
# full_info.reset_login_attempents()

# full_info_2.name_user()
# full_info_2.last_n_user()
# full_info_2.age_user()
# full_info_2.info_user()
# full_info_2.hi()
# full_info_2.plus_login_attempents()
# full_info_2.reset_login_attempents()







# class Car():

#     def __init__(self, make , model , year):
#         self.make = make
#         self.model = model
#         self.year= year
#         self.odometer_reading = 0
#         self.battery_size = 75
#     def get_full_name(self):
#         long_name = f"{self.make} {self.model} {self.year}"
#         return long_name.title()

#     def odom_reading(self):
#         print(f"пробег машины - {self.odometer_reading}")

#     def update_probeg(self , probeg):
#         if probeg > self.odometer_reading:
#             self.odometer_reading = probeg
#         else:
#             print(f"что у тя с пробегом даун?")

#     def plus_probeg(self , plus_probeg):
#         self.odometer_reading += plus_probeg

# class Battery():

#     def __init__(self , battery_size = 75):
#         self.battery_size = battery_size
        
#     def discribe_battery(self):
#         print(f"емкость аккумулятора этого эллектро автомобиля - {self.battery_size} киловатт")

#     def get_zapas(self ):
#         if self.battery_size == 75:
#             range = 260
#         elif self.battery_size == 100:
#             range = 310
#         print(f"запас хода у машинки - {range} км при полной зарядке")

# class ElectricCar(Car):

#     def __init__(self , make , model , year ):
#         super().__init__(make , model , year)
#         self.battery = Battery()

#     def fill_gas_zapravka(self):
#         print(f"у электромобиля нет бензобака даун")

  



# my_new_car = Car("BMW" , "amg192" , "2023")
# print(my_new_car.get_full_name())


# my_new_car.update_probeg(67_500)
# my_new_car.odom_reading()
# my_new_car.plus_probeg(400)
# my_new_car.odom_reading()


# my_electro_car = ElectricCar("tesla" , "model x" , 2024)
# print(my_electro_car.get_full_name())
# my_electro_car.fill_gas_zapravka()
# my_electro_car.battery.discribe_battery()
# my_electro_car.battery.get_zapas()




# class Restuarant():
#     def __init__(self , rest_name , cuisine_type):
#         self.rest_name = rest_name
#         self.cuisine_type = cuisine_type
#         self.number_people = 23
#     def open_rest(self):
#         print(f"сейчас ресторан - {self.rest_name} открыт")

#     def close_restik(self):
#         print(f"сейчас ресторан - {self.rest_name} закрыт")

#     def one_rest(self):
#         print(f"\nвот кароч ресторанчик так называется - {self.rest_name}")

#     def numbers_people(self):
#         print(f"обслуженные посетители - {self.number_people}")


#     def set_number_served(self , save_number):
#         save_number > self.number_people 
#         self.number_people = save_number
#         print(f"новые посетители, обслуженные посетители - {save_number}")

#     def plus_number_people(self , plus_people):
#         self.number_people += plus_people
#         print(f"за день обслужено гостя/гостей - {plus_people} ")
        
# class IceCreamStand(Restuarant):
#     def __init__(self , rest_name , cuisine_type ):
#         super().__init__(rest_name , cuisine_type)
#         self.flavor =  flavors
#     def ice_cream_name(self ):
#         print(f"вот как называется мороженщица - {self.rest_name}")
#     def ice_cream_people(self ):
#         print(f"вот обслуженные посетители - {self.number_people}")
#     def ice_cream_flavor(self):
#         print(f"какое мороженное в наличии - {self.flavor}")


    
        
# rest_vibe = Restuarant("ля попа" , 45 )
# rest_vibe.one_rest()
# print(f"сколько столов свободных в ресторане - {rest_vibe.cuisine_type}")
# rest_vibe.open_rest()
# rest_vibe.numbers_people()
# rest_vibe.set_number_served(26)
# rest_vibe.plus_number_people(123)
# flavors = ["ванильное" , "шоколадное" , "клубничное" , "мята"]
# flavors = ["какашка" , "мята" , "дыня"]
# ice_cream = IceCreamStand("у виталика" , 24 )

# ice_cream.ice_cream_name()
# ice_cream.ice_cream_people()
# ice_cream.ice_cream_flavor()

# ice_cream_2 = IceCreamStand("у темы" , 24)
# ice_cream_2.ice_cream_name()
# ice_cream_2.ice_cream_people()
# ice_cream_2.ice_cream_flavor()



# close_rest = Restuarant("ля писька" , 24)
# close_rest.one_rest()
# print(f"сколько столов свободных в ресторане - {close_rest.cuisine_type}")
# close_rest.close_restik()
# close_rest.numbers_people()
# close_rest.set_number_served(34)
# close_rest.plus_number_people(152)

# rest_last = Restuarant("ля какаха" , 67)
# rest_last.one_rest()
# print(f"сколько столов свободных в ресторане - {rest_last.cuisine_type}")
# rest_last.open_rest()
# rest_last.numbers_people()
# rest_last.set_number_served(69)
# rest_last.plus_number_people(300)




# class User():
#     def __init__(self , f_name , l_name , age , info):
#         self.first_name = f_name
#         self.last_name = l_name
#         self.age = age
#         self.information = info
#         self.open_site = 0

#     def name_user(self):
#         print(f"\nимя - {self.first_name}")

#     def last_n_user(self):
#         print(f"фамилия - {self.last_name}")

#     def age_user(self):
#         print(f"возраст - {self.age}")

#     def info_user(self):
#         print(f"информация о человеке - {self.information}")

#     def hi(self):
#         print(f"приветствую нового пользователя - привет {self.first_name} {self.last_name}")


#     def plus_login_attempents(self ):

#         self.open_site = self.open_site + 1
#         print(f"количество попыток входа в систему -  {self.open_site} ")
        
#     def reset_login_attempents(self):
#         self.open_site = 0
#         print(f"попыток входа в систему обнулился - {self.open_site} ")


# class Admin(User):
#     def __init__(self, f_name , l_name , age , info  ):
#         super().__init__(f_name , l_name , age , info )
#         self.privileges = Previliges()
        
# class Previliges():
#     def __init__(self):
#         self.privileges = admin_info
        
#     def show_privileges(self ):
#         print(f"вот ваши привелегии как администратора - {self.privileges}")
        
        

# admin_info = ["возможность добавлять сообщения" , "разрешено удалять сообщения" , "удалять пользователей"]
# admin_full = Admin("темик" , "льянов" , "18" , "люблю член ильи"  )

# admin_full.name_user()
# admin_full.last_n_user()
# admin_full.privileges.show_privileges()



# admin_full = Admin("темик" , "льянов" , "18" , "люблю член ильи")
# admin_full.name_user()
# admin_full.last_n_user()
# admin_info.show_privileges()


# print(f"вот вся информация о пользователе:")

# full_info = User("иля" , "моладав" , "19" , "люблю дашу и играть в гамесы" )

# full_info_2 = User("тема" , "льянов" , "19" , "любит своих шпицыков")

# full_info.name_user()
# full_info.last_n_user()
# full_info.age_user()
# full_info.info_user()
# full_info.hi()
# full_info.plus_login_attempents()
# full_info.reset_login_attempents()

# full_info_2.name_user()
# full_info_2.last_n_user()
# full_info_2.age_user()
# full_info_2.info_user()
# full_info_2.hi()
# full_info_2.plus_login_attempents()
# full_info_2.reset_login_attempents()






# class Car():

#     def __init__(self, make , model , year):
#         self.make = make
#         self.model = model
#         self.year= year
#         self.odometer_reading = 0
#         self.battery_size = 75
#     def get_full_name(self):
#         long_name = f"{self.make} {self.model} {self.year}"
#         return long_name.title()

#     def odom_reading(self):
#         print(f"пробег машины - {self.odometer_reading}")

#     def update_probeg(self , probeg):
#         if probeg > self.odometer_reading:
#             self.odometer_reading = probeg
#         else:
#             print(f"что у тя с пробегом даун?")

#     def plus_probeg(self , plus_probeg):
#         self.odometer_reading += plus_probeg

# class Battery():

#     def __init__(self , battery_size = 75):
#         self.battery_size = battery_size
        
#     def discribe_battery(self):
#         print(f"емкость аккумулятора этого эллектро автомобиля - {self.battery_size} киловатт")

#     def get_zapas(self ):
#         if self.battery_size == 75:
#             range = 260
#         elif self.battery_size == 100:
#             range = 310
#         print(f"запас хода у машинки - {range} км при полной зарядке")

#     def upgrade_battery(self):
        
#         if self.battery_size < 100:
#             self.battery_size = 100

#         print(f"полный запас хода - {self.battery_size}")

# class ElectricCar(Car):

#     def __init__(self , make , model , year ):
#         super().__init__(make , model , year)
#         self.battery = Battery()

#     def fill_gas_zapravka(self):
#         print(f"у электромобиля нет бензобака даун")

  



# my_new_car = Car("BMW" , "amg192" , "2023")
# print(my_new_car.get_full_name())


# my_new_car.update_probeg(67_500)
# my_new_car.odom_reading()
# my_new_car.plus_probeg(400)
# my_new_car.odom_reading()


# my_electro_car = ElectricCar("tesla" , "model x" , 2024)
# print(my_electro_car.get_full_name())
# my_electro_car.fill_gas_zapravka()
# my_electro_car.battery.discribe_battery()
# my_electro_car.battery.get_zapas()
# my_electro_car.battery.upgrade_battery()
# my_electro_car.battery.get_zapas()



# import random


# lottery = [1 , 2 ,3 ,4 ,5 ,6 ,7 ,8, 9 ,10 , "a" , "b" , "c" , "d" , "f"]
# my_ticket = [7 , "a" , 3 , 5]
# popitki = 0

# while True:
#     winning_combo = random.choices(lottery , k=4)
#     if winning_combo == my_ticket:
#         print(f"ты выиграл, твоя комбинация - {winning_combo}")
#         popitki += 1
#         break
#     if winning_combo != my_ticket:
#         popitki += 1
#         print(winning_combo)

# print(f"количество попыток {popitki}")


class Product():
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def name_product(self):
        print(f"\nпродукт - {self.name}")

    def price_product(self):
        print(f"цена продукта - {self.price}")

    def quantity_product(self):
        print(f"количество продуктов - {self.quantity}")

    def all_price(self):
        
        for product in products:
            if product.price == max(all_prices):
                print(f"самый дорогой продукт - {product.name} его цена - {product.price} ")

    def find_high_product(self):
        self.high_product = product1
        for product in products:
            if product.price > self.high_product.price:
                self.high_product = product
              
        

product1 = Product("яблоки" , 100 , 50)
product1.name_product()
product1.price_product()
product1.quantity_product()



product2 = Product("бананчики" , 200 ,30)
product2.name_product()
product2.price_product()
product2.quantity_product()



product3 = Product("сыр" , 450 ,58)
product3.name_product()
product3.price_product()
product3.quantity_product()

product4 = Product("колбаса" , 500 , 20)
product4.name_product()
product4.price_product()
product4.quantity_product()


all_name = (product1.name , product2.name, product3.name , product4.name)
all_prices = (product1.price , product2.price , product3.price , product4.price)
products = [product1 , product2 , product3 , product4]


print(f"{product1.find_high_product()}")
product1.high_product.name_product()
product1.high_product.all_price()
print(f"вот все товары - {all_name}")



# if all_prices < max(all_prices):
        #     print(f"самый дорогой продукт - {self.name} , его цена - {self.high_price}")
        # if all_prices > max(all_prices):
        #     print(f"самый дорогой продукт - {self.name} , его цена - {self.price}")