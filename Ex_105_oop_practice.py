# class Goods:
#     title = "Мороженое"
#     weight = 154
#     tp = "Еда"
#     price = 1024
#
#
# setattr(Goods, 'price', 2048)
# setattr(Goods, 'inflation', 100)
# print(Goods.__dict__)
import random

# class MediaPlayer:
#
#     def open(self, file):
#         setattr(self, 'filename', file)
#
#     def play(self):
#         print(f'Воспроизведение {self.filename}')
#
#
# media1 = MediaPlayer()
# media2 = MediaPlayer()
#
# media1.open('filemedia1')
# media2.open('filemedia2')
#
# media1.play()
# media2.play()

# class Graph:
#     LIMIT_Y = [0, 10]
#
#     def set_data(self, data):
#         setattr(self, 'data', data)
#
#     def draw(self):
#         for i in self.data:
#             if self.LIMIT_Y[0] <= i <= self.LIMIT_Y[1]:
#                 print(i, end=' ')
#
#
# graph_1 = Graph()
# graph_1.set_data([10, -5, 100, 20, 0, 80, 45, 2, 5, 7])
# graph_1.draw()

# class Point:
#
#     def set_coords(self, x, y):
#         self.x = x
#         self.y = y
#
#
# pt = Point()
# pt.set_coords(10, 20)
# print(pt.__dict__)  # атрибуты экземпляра отличаются от атрибутов класса
# print(Point.__dict__)

# import sys
#
# # здесь объявляется класс StreamData
# class StreamData:
#
#     def create(self, fields, lst_values):
#         if len(fields) != len(lst_values):
#             return False
#         for i, value in enumerate(fields):
#             setattr(self, value, lst_values[i])
#         return True
# class StreamReader:
#     FIELDS = ('id', 'title', 'pages')
#
#     def readlines(self):
#         lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока
#         sd = StreamData()
#         res = sd.create(self.FIELDS, lst_in)
#         return sd, res
#
#
# sr = StreamReader()
# data, result = sr.readlines()

# import sys

# lst_in = ['1 Сергей 35 120000',
#     '2 Федор 23 12000',
#     '3 Иван 13 1200'
#           ]


# class DataBase:
#     lst_data = []
#     FIELDS = ('id', 'name', 'old', 'salary')
#
#     def insert(self, data):
#         for i in data:
#             d = {}
#             for k, j in enumerate(i.split()):
#                 d[self.FIELDS[k]] = j
#             self.lst_data.append(d)
#
#     def select(self, a, b):
#         l = []
#         if b >= len(self.lst_data):
#             for i in range(a, len(self.lst_data)):
#                 l.append(self.lst_data[i])
#         else:
#             for i in range(a, b + 1):
#                 l.append(self.lst_data[i])
#
#
# db = DataBase()
# db.insert(lst_in)
# print(db.lst_data)

# class Translator:
#     def add(self, eng, rus):
#         if 'tr' not in self.__dict__:
#             self.tr = {}
#
#         self.tr.setdefault(eng, [])
#         if eng in self.tr:
#             if rus not in self.tr[eng]:
#                 self.tr[eng].append(rus)
#
#     def remove(self, eng):
#         self.tr.pop(eng)
#
#
#
#     def translate(self, eng):
#         return self.tr[eng]
#
#
# tr = Translator()
# tr.add("tree", "дерево")
# tr.add("car", "машина")
# tr.add("car", "автомобиль")
# tr.add("leaf", "лист")
# tr.add("river", "река")
# tr.add("go", "идти")
# tr.add("go", "ехать")
# tr.add("go", "ходить")
# tr.add("milk", "молоко")
# tr.remove('car')
# print(*tr.translate('go'))

# class Money:
#     def __init__(self, money):
#         self.money = money
#
#
# my_money = Money(100)
# your_money = Money(1000)


# class Point:
#     def __init__(self, x, y, color='black'):
#         self.x = x
#         self.y = y
#         self.color = color
#
#
# i = 1
# j = 1
# points = []
# for k in range(0, 1000):
#     if k == 1:
#         p = Point(i, j, 'yellow')
#         points.append(p)
#         i += 2
#         j += 2
#     else:
#         p = Point(i, j)
#         points.append(p)
#         i += 2
#         j += 2


# import random
#
#
# class Line:
#     def __init__(self, a, b, c, d):
#         self.sp = (a, b)
#         self.ep = (c, d)
#
#
# class Rect:
#     def __init__(self, a, b, c, d):
#         self.sp = (a, b)
#         self.ep = (c, d)
#
#
# class Ellipse:
#     def __init__(self, a, b, c, d):
#         self.sp = (a, b)
#         self.ep = (c, d)
#
#
# elements = []
# for i in range(0, 217):
#     r = random.randrange(0, 3)
#     if r == 0:
#         cl = Line(0, 0, 0, 0)
#         elements.append(cl)
#     if r == 1:
#         cl = Rect(random.randrange(0, 100),
#                   random.randrange(0, 100),
#                   random.randrange(0, 100),
#                   random.randrange(0, 100))
#         elements.append(cl)
#     if r == 2:
#         cl = Ellipse(random.randrange(0, 100),
#                   random.randrange(0, 100),
#                   random.randrange(0, 100),
#                   random.randrange(0, 100))
#         elements.append(cl)


# class TriangleChecker:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def is_triangle(self):
#         if (type(self.a) != int and type(self.a) != float) or self.a <= 0:
#             return 1
#         elif (type(self.b) != int and type(self.b) != float) or self.b <= 0:
#             return 1
#         elif (type(self.c) != int and type(self.c) != float) or self.c <= 0:
#             return 1
#         if self.a >= self.b + self.c or self.b >= self.a + self.c or self.c >= self.a + self.b:
#             return 2
#         else:
#             return 3
#
#
# a, b, c = '3', 4, 5
# print(type(a) == int)
# tr = TriangleChecker(a, b, c)
# print(tr.is_triangle())


# class Graph:
#     def __init__(self, data, is_show=True):
#         self.data = data[:]
#         self.is_show = is_show
#
#     def set_data(self, data):
#         self.data = data
#
#     def show_table(self):
#         if not self.is_show:
#             print("Отображение данных закрыто")
#         else:
#             print(' '.join(str(el) for el in self.data))
#
#     def show_graph(self):
#         if not self.is_show:
#             print("Отображение данных закрыто")
#         else:
#             print('Графическое отображение данных:', end=' ')
#             self.show_table()
#
#     def show_bar(self):
#         if not self.is_show:
#             print("Отображение данных закрыто")
#         else:
#             print('Столбчатая диаграмма:', end=' ')
#             self.show_table()
#
#     def set_show(self, fl_show):
#         self.is_show = fl_show
#
#
# data_graph = list(map(int, input().split()))
# gr = Graph(data_graph)
# gr.show_bar()
# gr.set_show(False)
# gr.show_table()


# class CPU:
#     def __init__(self, name, fr):
#         self.name = name
#         self.fr = fr
#
#
# class Memory:
#     def __init__(self, name, volume):
#         self.name = name
#         self.volume = volume
#
#
# class MotherBoard:
#     def __init__(self, name, cpu, *mem_slots):
#         self.name = name
#         self.cpu = cpu
#         self.total_mem_slots = 4
#         self.mem_slots = mem_slots[:self.total_mem_slots]
#
#     def get_config(self):
#         return [f"Материнская плата: {self.name}",
#         f"Центральный процессор: {self.cpu.name}, {self.cpu.fr}",
#         f"Слотов памяти: {self.total_mem_slots}",
#         'Память: ' + "; ".join(map(lambda x: f'{x.name} - {x.volume}', self.mem_slots))]
#
#
# mb = MotherBoard('Asus', CPU('Asus', 1333),
#                  Memory('Kingstone', 4000),
#                   Memory('Kingstone', 4000))
#
# print(mb.get_config())

# class Cart:
#     def __init__(self):
#         self.goods = []
#
#     def add(self, gd):
#         self.goods.append(gd)
#
#     def remove(self, indx):
#         self.goods.pop(indx)
#
#     def get_list(self):
#         return [f'{i.name}: {i.price}' for i in self.goods]
#
#
# class Table:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
#
# class TV:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
#
# class Notebook:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
#
# class Cup:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
#
# tv1 = TV("samsung", 1111)
# tv2 = TV("LG", 1234)
# table = Table("ikea", 2345)
# n1= Notebook("msi", 5433)
# n2 = Notebook("apple", 542)
# c = Cup("keepcup", 43)
#
# cart = Cart()
# cart.add(tv1)
# cart.add(tv2)
# cart.add(table)
# cart.add(n1)
# cart.add(n2)
# cart.add(c)


# class ListObject:
#     def __init__(self, data):
#         self.next_obj = None
#         self.data = data
#
#     def link(self, obj):
#         self.next_obj = obj
#
#
# lst_in = "foo bar baz foo1 bar1 baz1".split()
# head_obj = ListObject(lst_in[0])
# obj = head_obj
# for i in range(1, len(lst_in)):
#     obj_new = ListObject(lst_in[i])
#     obj.link(obj_new)
#     obj = obj_new

# class AbstractClass:
#     def __new__(cls, *args, **kwargs):
#         return "Ошибка: нельзя создавать объекты абстрактного класса"


# class SingletonFive:
#     count = 0
#     instance = None
#
#     def __new__(cls, *args, **kwargs):
#         if cls.count < 3:
#             cls.count += 1
#             return super().__new__(cls)
#         elif cls.count == 3:
#             cls.count += 1
#             cls.instance = super().__new__(cls)
#             return super().__new__(cls)
#         else:
#             cls.count += 1
#             return cls.instance
#
#     def __init__(self, name):
#         self.name = name
#
# objs = [SingletonFive(str(n)) for n in range(10)]
# print(objs)

# TYPE_OS = 1 # 1 - Windows; 2 - Linux вызываем другой класс через переделанный new
#
# class DialogWindows:
#     name_class = "DialogWindows"
#
#
# class DialogLinux:
#     name_class = "DialogLinux"
#
# class Dialog:
#     def __new__(cls, *args, **kwargs):
#         if TYPE_OS == 1:
#             d = super().__new__(DialogWindows)
#             setattr(d, 'name', args[0])
#             return d
#         else:
#             d = super().__new__(DialogLinux)
#             setattr(d, 'name', args[0])
#             return d


# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
#     def clone(self):
#         pt = Point(self.x, self.y)
#         return pt
#
#
# pt = Point(2, 3)
# pt_clone = pt.clone()
# print(pt_clone.__dict__)


# class Factory:
#     def build_sequence(self):
#         return []
#
#     def build_number(self, string):
#         return float(string)
# class Loader:
#     def parse_format(self, string, factory):
#         seq = factory.build_sequence()
#         for sub in string.split(","):
#             item = factory.build_number(sub)
#             seq.append(item)
#
#         return seq
#
#
# # эти строчки не менять!
# ld = Loader()
# s = input()
# res = ld.parse_format(s, Factory())

# from string import ascii_lowercase, digits
#
#
# class TextInput:
#     CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + ascii_lowercase
#     CHARS_CORRECT = CHARS + CHARS.upper() + digits
#
#     def __init__(self, name, size=10):
#         if self.check_name(name):
#             self.name = name
#             self.size = size
#
#     def get_html(self):
#         return f"<p class='login'>{self.name}: <input type='text' size={self.size} />"
#
#     @classmethod
#     def check_name(cls, name):
#         if len(name) < 3 or len(name) > 50:
#             raise ValueError("некорректное поле name")
#         else:
#             for i in name:
#                 if i not in cls.CHARS_CORRECT:
#                     raise ValueError("некорректное поле name")
#         return True
#
#
# class PasswordInput:
#     CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + ascii_lowercase
#     CHARS_CORRECT = CHARS + CHARS.upper() + digits
#
#     def __init__(self, name, size=10):
#         if self.check_name(name):
#             self.name = name
#             self.size = size
#
#     def get_html(self):
#         return f"<p class='password'>{self.name}: <input type='text' size={self.size} />"
#
#     @classmethod
#     def check_name(cls, name):
#         if len(name) < 3 or len(name) > 50:
#             raise ValueError("некорректное поле name")
#         else:
#             for i in name:
#                 if i not in cls.CHARS_CORRECT:
#                     raise ValueError("некорректное поле name")
#         return True
#
#
# class FormLogin:
#     def __init__(self, lgn, psw):
#         self.login = lgn
#         self.password = psw
#
#     def render_template(self):
#         return "\n".join(['<form action="#">', self.login.get_html(), self.password.get_html(), '</form>'])
#
#
# login = FormLogin(TextInput("Лоubyjbl"), PasswordInput("Пароль"))
# html = login.render_template()
# print(login)
# print(html)

# from string import ascii_lowercase, digits
# class CardCheck:
#     CHARS_FOR_NAME = ascii_lowercase.upper() + digits
#     @staticmethod
#     def check_card_number(number):
#         if type(number) != str:
#             return False
#         n = number.split('-')
#         if len(n) != 4:
#             return False
#         for i in n:
#             if len(i) != 4:
#                 return False
#             if not str.isdigit(i):
#                 return False
#         return True
#
#
#     @staticmethod
#     def check_name(name):
#         if type(name) != str:
#             return False
#         n = name.split()
#         if len(n) != 2:
#             return False
#         for i in n:
#             for j in set(i):
#                 if j not in CardCheck.CHARS_FOR_NAME:
#                     return False
#         return True


# class Video:
#     def create(self, name):
#         self.name = name
#
#     def play(self):
#         print(f"воспроизведение видео {self.name}")
#
#
# class YouTube:
#     videos = []
#
#     @classmethod
#     def add_video(cls, video: Video):
#         cls.videos.append(video)
#
#     @classmethod
#     def play(cls, index):
#         Video.play(cls.videos[index])
#
#
# v1, v2 = Video(), Video()
# v1.create('Python')
# v2.create('Python ООП')
# YouTube.add_video(v1)
# YouTube.add_video(v2)
# YouTube.play(0)
# YouTube.play(1)

# class Application:
#     def __init__(self, name, blocked=False):
#         self.name = name
#         self.blocked = blocked
#
#
# class AppStore:
#     def __init__(self):
#         self.apps = []
#
#     def add_application(self, app: Application):
#         self.apps.append(app)
#
#     def remove_application(self, app: Application):
#         self.apps.remove(app)
#
#     def block_application(self, app: Application):
#         if app in self.apps:
#             app.blocked = True
#
#     def total_apps(self):
#         return len(self.apps)

# class Message:
#     def __init__(self, text, fl_like=False):
#         self.text = text
#         self.fl_like = fl_like
#
#
# class Viber:
#     messages = []
#
#     @classmethod
#     def add_message(cls, msg):
#         cls.messages.append(msg)
#
#     @classmethod
#     def remove_message(cls, msg):
#         cls.messages.remove(msg)
#
#     @classmethod
#     def set_like(cls, msg: Message):
#         if msg in cls.messages:
#             if not msg.fl_like:
#                 msg.fl_like = True
#             else:
#                 msg.fl_like = False
#
#     @classmethod
#     def show_last_message(cls, count):
#         if count == 1:
#             print(cls.messages[-1])
#         else:
#             print(cls.messages[-1 * count: - 1])
#
#     @classmethod
#     def total_messages(cls):
#         return len(cls.messages)


# class Cell:
#     def __init__(self, around_mines=0, mine=False):
#         self.around_mines = around_mines
#         self.mine = mine
#         self.fl_open = False
#
#
# class GamePole:
#     def __init__(self, N, M):
#         self.N = N
#         self.pole = [[Cell() for i in range(self.N)] for i in range (self.N)]
#         self.M = M
#         self.init()
#
#     def init(self):
#         m = 0
#         while m < self.M:
#             i = random.randint(0, self.N - 1)
#             j = random.randint(0, self.N - 1)
#             if self.pole[i][j].mine:
#                 continue
#             self.pole[i][j].mine = True
#             m += 1
#
#         indx = (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)
#         for x in range(self.N):
#             for y in range(self.N):
#                 if not self.pole[x][y].mine:
#                     mines = sum((self.pole[x + i][y + j].mine for i, j in indx if 0 <= x + i < self.N and 0 <= y + j < self.N))
#                     self.pole[x][y].around_mines = mines
#
#     def show(self):
#         for row in self.pole:
#             print(*map(lambda x: '#' if not x.fl_open else x.around_mines if not x.mine else '*', row))
#
#
# pole_game = GamePole(10, 12)
# pole_game.show()


# class Server:
#     server_ip = 1
#
#     def __init__(self):
#         self.ip = Server.server_ip
#         self.buffer = []
#         Server.server_ip += 1
#         self.router = None
#
#     def send_data(self, data):
#         if self.router:
#             self.router.buffer.append(data)
#
#     def get_data(self):
#         b = self.buffer[:]
#         self.buffer.clear()
#         return b
#
#     def get_ip(self):
#         return self.ip
#
#
# class Router:
#     def __init__(self):
#         self.buffer = []
#         self.servers = {}
#
#     def link(self, server):
#         self.servers[server.ip] = server
#         server.router = self
#
#     def unlink(self, server):
#         s = self.servers.pop(server.ip, False)
#         if s:
#             s.router = None
#
#     def send_data(self):
#         for d in self.buffer:
#             if d.ip in self.servers:
#                 self.servers[d.ip].buffer.append(d)
#         self.buffer.clear()
#
#
# class Data:
#     def __init__(self, msg, ip):
#         self.data = msg
#         self.ip = ip


# class Clock:
#     def __init__(self, time=0):
#         self.__time = time
#     @classmethod
#     def __checktime(cls, tm):
#         return type(tm) == int and 0 <= tm < 100000
#
#     def get_time(self):
#         return self.__time
#
#     def set_time(self, tm):
#         if self.__checktime(tm):
#             self.__time = tm
#
#
# clock = Clock()
# clock.set_time('4530')
# print(clock.get_time())


# class Money:
#     def __init__(self, money):
#         self.__money = money
#
#     @classmethod
#     def __check_money(cls, money):
#         return type(money) is int and money >= 0
#
#     def set_money(self, money):
#         if self.__check_money(money):
#             self.__money = money
#
#     def get_money(self):
#         return self.__money
#
#     def add_money(self, mn):
#         self.__money += mn.get_money()


# class Book:
#     def __init__(self, author, title, price):
#         self.__author = author
#         self.__title = title
#         self.__price = price
#
#     def set_title(self, title):
#         self.__title = title
#
#     def set_author(self, author):
#         self.__author = author
#
#     def set_price(self, price):
#         self.__price = price
#
#     def get_title(self):
#         return self.__title
#
#     def get_author(self):
#         return self.__author
#
#     def get_price(self):
#         return self.__price


# class Line:
#     def __init__(self, x1, y1, x2, y2):
#         self.__x1 = x1
#         self.__x2 = x2
#         self.__y1 = y1
#         self.__y2 = y2
#
#     def set_coords(self, x1, y1, x2, y2):
#         self.__x1 = x1
#         self.__x2 = x2
#         self.__y1 = y1
#         self.__y2 = y2
#
#     def get_coords(self):
#         return self.__x1, self.__y1, self.__x2, self.__y2
#
#     def draw(self):
#         print(*[self.__x1, self.__y1, self.__x2, self.__y2])
#
#
# line = Line(1, 2, 3, 4)
# line.draw()


# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def get_coords(self):
#         return self.__x, self.__y
#
#
# class Rectangle:
#     def __init__(self, *args):
#         if len(args) == 4:
#             self.__sp = Point(args[0], args[1])
#             self.__ep = Point(args[2], args[3])
#         else:
#             self.__sp = args[0]
#             self.__ep = args[1]
#
#     def set_coords(self, sp, ep):
#         self.__sp = sp
#         self.__ep = ep
#
#     def get_coords(self):
#         return self.__sp, self.__ep
#
#     def draw(self):
#         print(f"Прямоугольник с координатами: {self.__sp.get_coords()} {self.__ep.get_coords()}")
#
#
# rect = Rectangle(0, 0, 20, 34)
# print(rect.get_coords())

from string import ascii_lowercase, digits


# class EmailValidator:
#     def __new__(cls, *args, **kwargs):
#         return None
#
#     CHARS_FOR_EMAIL = ascii_lowercase + ascii_lowercase.upper() + digits + '_' + '.'
#
#     def get_random_email(cls):
#         rand_email = ''.join(random.choice(cls.CHARS_FOR_EMAIL) for i in range(101))
#         rand_email += '@gmail.com'
#         return rand_email
#
#     @staticmethod
#     def __is_email_str(email):
#         return type(email) is str
#
#     @classmethod
#     def check_email(cls, email):
#         if EmailValidator.__is_email_str(email):
#             if any(char not in cls.CHARS_FOR_EMAIL + '@' for char in email):
#                 return False
#             if email.count('@') != 1:
#                 return False
#             dog_index = email.index('@')
#             if len(email[:dog_index]) > 100 or len(email[dog_index + 1:]) > 50:
#                 return False
#             if '.' not in email[dog_index + 1:]:
#                 return False
#             for i in range(len(email)):
#                 if email[i] == '.' and email[i + 1] == '.':
#                     return False
#             return True
#         else:
#             return False


# class Car:
#     def __init__(self, model):
#         self.__model = model
#
#     @property
#     def model(self):
#         return self.__model
#
#     @model.setter
#     def model(self, model):
#         if type(model) is str and 2 <= len(model) <= 100:
#             self.__model = model


class WindowDlg:
    def __init__(self, title, width, height):
        self.__title = title
        self.__width = width
        self.__height = height

    def show(self):
        print(f'{self.__title}: {self.__width}, {self.__height}')

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if type(width) is int and 0 <= width <= 10000:
            self.__width = width
            self.show()

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if type(height) is int and 0 <= height <= 10000:
            self.__height = height
            self.show()
























































