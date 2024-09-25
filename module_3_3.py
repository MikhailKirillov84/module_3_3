#1.Функция с параметрами по умолчанию:

def print_params(a = 1, b = 'строка', c = True):   #Создайте функцию print_params(a = 1, b = 'строка', c = True),
    # которая принимает три параметра со значениями по умолчанию (например сейчас это: 1, 'строка', True).
    print(a, b, c)   #Функция должна выводить эти параметры.

print_params('*1.Функция', 'с параметрами', 'по умолчанию:')

print_params()           #Вызовите функцию print_params с разным количеством аргументов, включая вызов без аргументов.
print_params(1, 'строка')
print_params(b = 25)       #Проверьте, работают ли вызовы print_params(b = 25) print_params(c = [1,2,3])
print_params(c = [1,2,3])  #Проверьте, работают ли вызовы print_params(b = 25) print_params(c = [1,2,3])

print_params('__', '__', '__')
print_params('*2.', 'Распаковка', 'параметров:')
#2.Распаковка параметров:

values_list = [1, "строка", True]                      #Создайте список values_list с тремя элементами разных типов
values_dict = {'a': 4, 'b': 'помогите', 'c': False}    #Создайте словарь values_dict с тремя ключами, соответствующими
                                                       # параметрам функции print_params, и значениями разных типов.
print_params(values_dict)

values_list = [1, "строка"]
values_dict = {'c': False}
print_params(*values_list, **values_dict)    #Передайте values_list и values_dict в функцию print_params, используя
                                             # распаковку параметров (* для списка и ** для словаря).

print_params('__', '__', '__')
print_params('*3.Распаковка', '+ отдельные', 'параметры:')
#3.Распаковка + отдельные параметры

values_list_2 = [54.32, 'Строка' ]        #Создайте список values_list_2 с двумя элементами разных типов
print_params(*values_list_2, 42)       #Проверьте, работает ли print_params(*values_list_2, 42)

