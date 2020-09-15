import csv
import telebot

bot = telebot.TeleBot('1373724185:AAEgivKEaG2ZKIMCvx7wlq1WXxwKwKkyQ90')

f = open('dict2.csv', 'r')
reader = csv.reader(f)

Python_txt = open('python_methods.txt', 'r')

str_methods = {}
list_methods = {}
dict_methods = {}
set_methods = {}
tuple_methods = {}
python_methods = []


string_ = ['capitalize', 'casefold', 'center', 'count',
           'encode', 'endswith', 'expandtabs', 'find',
           'format', 'format_map', 'index', 'isalnum',
           'isalpha', 'isascii', 'isdecimal', 'isdigit',
           'isidentifier', 'islower', 'isnumeric','isprintable',
           'isspace', 'istitle', 'isupper', 'join',
           'ljust', 'lower', 'lstrip', 'maketrans',
           'partition', 'replace', 'rfind', 'rindex',
           'rjust', 'rpartition', 'rsplit', 'rstrip',
           'split', 'splitlines', 'startswith', 'strip',
           'swapcase', 'title', 'translate', 'upper',
           'zfill', ]
list_ = ['append', 'clear', 'copy', 'count', 'extend',
         'index', 'insert', 'pop', 'remove', 'reverse',
         'sort', ]
dict_ = ['clear', 'copy', 'fromkeys', 'get', 'items',
         'keys', 'pop', 'popitem', 'setdefault', 'update',
         'values']
set_ = ['add', 'clear', 'copy', 'difference', 'difference_update',
         'discard', 'intersection', 'intersection_update',
         'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove',
         'symmetric_difference', 'symmetric_difference_update',
         'union', 'update', ]
tuple_ = ['count', 'index', ]

list_= ['append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'] 

python_all_methods = ['bool()', 'bytearray()', 'bytes()', 'complex()',
                   'dict()', 'float()', 'frozenset()', 'int()', 'list()',
                   'memoryview()', 'object()', 'range()', 'set()', 'slice()',
                   'str()', 'tuple()', 'abs()', 'all()', 'any()', 'ascii()', 'bin()',
                   'callable()', 'chr()', 'classmethod()', 'compile()', 'delattr()',
                   'dir()', 'divmod()', 'enumerate()', 'eval()', 'exec()', 'filter()',
                   'format().', 'getattr()', 'globals()', 'hasattr()', 'hash()', 'help()',
                   'hex()', 'id()', 'input()', 'isinstance()', 'issubclass()', 'iter()',
                  'len()', 'locals()', 'map()', 'max()', 'min()', 'next()', 'oct()', 'open()',
                  'ord()', 'pow()', 'reversed()', 'repr()', 'print()', 'property()', 'round()',
                  'setattr()', 'sorted()', 'staticmethod()', 'sum()', 'super()', 'type()', 'type()',
                  'vars()', 'zip()', ]

for row in reader:
    if row == "":
        continue
    else:
        str_methods.update({row[0]:row[1]})
        list_methods.update({row[2]:row[3]})
        dict_methods.update({row[4]:row[5]})
        set_methods.update({row[6]:row[7]})
        tuple_methods.update({row[8]:row[9]})
for i in Python_txt:
    if i == '\n':
        continue
    else:
        python_methods.append(i)
python_methods = list(map(lambda s: s.strip(), python_methods))















def poisk_in_str(x):
    for i in str_methods.keys():
        if x in i:
            return f" Метод {i} - {str_methods[i]}"

def poisk_in_list(x):
    for i in list_methods.keys():
        if x in i:
            return f" Метод {i} - {list_methods[i]}"


def poisk_in_dict(x):
    for i in dict_methods.keys():
        if x in i:
            if x == "keys":
                if "fromkeys" in i:
                    continue
                else:
                    return f" Метод {i} - {dict_methods[i]}"
            return f" Метод {i} - {dict_methods[i]}"

def poisk_in_set(x):
    for i in set_methods.keys():
        if x in i:
            if x == "difference":
                if "difference_upd" in i:
                    continue
                else:
                    return f" Метод {i} - {set_methods[i]}"
            return f" Метод {i} - {set_methods[i]}"

def poisk_in_tuple(x):
    for i in tuple_methods.keys():
        if x in i:
            return f" Метод {i} - {tuple_methods[i]}"

def poisk_in_Python(x):
    for i in python_methods:
        if x in i:
            return i
        else:
            continue


def return_all_methods(x):
    if x == "str":
        a = "Методы str: "
        b = (', '.join(map(str, string_)))
        c = a + b
        return c
    elif x == 'list':
        a = "Методы list: "
        b = (', '.join(map(str, list_)))
        c = a + b
        return c
    elif x == 'set':
        a = "Методы set: "
        b = (', '.join(map(str, set_)))
        c = a + b
        return c
    elif x == 'dict':
        a = "Методы dict: "
        b = (', '.join(map(str, dict_)))
        c = a + b
        return c
    elif x == 'tuple':
        a = "Методы tuple: "
        b = (', '.join(map(str, tuple_)))
        c = a + b
        return c
    elif x == 'python':
        b = "Встроенные функции Python: "
        a = "Методы Python: "
        b = (', '.join(map(str, python_all_methods)))
        c = a + b
        return c













@bot.message_handler(commands=['start', ])
def start_message(message):
    bot.send_message(message.chat.id, 'Начнем!!! \nВведите поиск согласно инстукции бота!\n\nВызвать инструкцию - /instructions')


@bot.message_handler(commands=['instructions', ])
def instructions_message(message):
    bot.send_message(message.chat.id, 'Для того чтобы осуществить поиск, вам нужно написать:  "метод" in "тип данных". \nНапример: append in list \n \nЕще можно искать встроенные функции Питона. Для этого вместо типа данных введите " Python".\nНапример: print in Python\n \nЕще можно вызвать все встроенные функции, либо все методы определенного типа данных.\nНапример: List\nЕще пример: Python')

@bot.message_handler(content_types=['text'])
def send_text(message):
    zapros = message.text
    zapros = list(zapros.split(' '))
    if len(zapros) > 1:
        try:
            pois = zapros[0]
            zapros_2 = zapros[2]
            zapros_2 = zapros_2.lower()
            pois = pois.lower()
            if zapros_2 == "list":
                bot.send_message(message.chat.id, poisk_in_list(pois))
            elif zapros_2 == "str":
                bot.send_message(message.chat.id, poisk_in_str(pois))
            elif zapros_2 == "set":
                bot.send_message(message.chat.id, poisk_in_set(pois))
            elif zapros_2 == "dict":
                bot.send_message(message.chat.id, poisk_in_dict(pois))
            elif zapros_2 == "tuple":
                bot.send_message(message.chat.id, poisk_in_tuple(pois))
            elif zapros_2 == "python" or zapros_2 == "Python":
                bot.send_message(message.chat.id, poisk_in_Python(pois))
            else:
                bot.send_message(message.chat.id, "Извините, мы не нашли такого метода, либо вы допустили ошибку при поиске. Введите поисковые данные согласно инструкции!\n\nВызвать инструкцию - /instructions")
                bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEBVaRfYGkmkgfI-5jQBbkWVPW2--kiBwACoQMAAnwFBxvz_axKdt0ixhsE")
        except:
            return bot.send_message(message.chat.id, "Извините, мы не нашли такого метода, либо вы допустили ошибку при поиске. Введите поисковые данные согласно инструкции!\n\nВызвать инструкцию - /instructions") , bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEBVaRfYGkmkgfI-5jQBbkWVPW2--kiBwACoQMAAnwFBxvz_axKdt0ixhsE")
    elif len(zapros) == 1:
        try:
            lower_zapros = zapros[0]
            lower_zapros = lower_zapros.lower()
            bot.send_message(message.chat.id, return_all_methods(lower_zapros))
        except:
            return bot.send_message(message.chat.id, "Извините, мы не нашли такого метода, либо вы допустили ошибку при поиске. Введите поисковые данные согласно инструкции!\n\nВызвать инструкцию - /instructions") , bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEBVaRfYGkmkgfI-5jQBbkWVPW2--kiBwACoQMAAnwFBxvz_axKdt0ixhsE")

bot.polling()