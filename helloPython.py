# this is a comment
name = 'Todd'
age = 33
is_fit = False
speed_factor = 0.56
j = 34
current_speed = speed_factor * j
str_to_int = '35'
complex_no = 32+5j
my_cars = ['AMC', 'Audi', 'BMW']
tupling = ('Ed', 'Charles', 'Mike')
my_set = {'Renault', 'McLaren', 'Ferrari'}
footy_dict = {'goals': 22, 'team':'MCY'}
my_team = input('What is your fave team?')

print(name + ' is my name.')
print(name + ' is ' + str(age) + ' years old.')
print(int(str_to_int))
print(age)
print(complex_no)
print(my_cars)
print(my_set)
print(footy_dict)
print(current_speed)
print(my_team)
print(type(age))
print(type(name))
print(type(is_fit))
print(type(complex_no))
print(type(my_cars))
my_cars.append('Cadillac')
print(my_cars)
my_cars[1] = 'Dodge'
print(my_cars)
print(type(tupling))
print(type(my_set))
print(type(footy_dict))
print(type(current_speed))
if(age >= j):
    print("Age is bigger than j")
else:
    print("Your variables are all messed up")
if('Cadillac' in my_cars):
    print('you got a Cadillac!!!')
for car in my_cars:
    print(car)

def hold_on_print():
    print("This is being sent to the console via a function")

hold_on_print()

def return_values_func():
    return "This is being returned via a function value"

print(return_values_func())

def return_num():
    return 10, 3

print(return_num())

def whats_the_num(num):
    return num

print(whats_the_num(16))

def add_nums(a, b):
    return a + b

print(add_nums(14, 62))