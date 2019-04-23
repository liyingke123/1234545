# class Person:
#     def __init__(self, name, weight):
#         self.name = name
#         self.weight = weight
#
#     def __str__(self):
#         return '我的名字叫%s 体重是%.2f' % (self.name, self.weight)
#
#     def run(self):
#         print('%s 爱跑步' % self.name)
#         self.weight -= 0.5
#
#     def eat(self):
#         print('%s 吃东西' % self.name)
#         self.weight += 1
#
#
# xx = Person('小明', 75.0)
# xx.run()
# xx.eat()
# print(xx)
#
# xm = Person('小美', 45.0)
# xm.run()
# xm.eat()
# print(xm)


# class Home:
#     def __init__(self, have, size, addr):
#         self.have = have
#         self.size = size
#         self.addr = addr
#         self.furniture_list = []
#
#     def __str__(self):
#         msn = '位于%s的%s的房子总面积为%s平方米.' % (self.addr, self.have, self.size)
#         msn += '房子里家具有%s' % str(self.furniture_list)
#         return msn
#
#     def Add_furniture(self, fitment):
#         self.furniture_list.append(fitment.get_name())
#
#
# class Bed:
#     def __init__(self, name):
#         self.name = name
#
#     def get_name(self):
#         return self.name
#
#
# class Refrigerator:
#     def __init__(self, name):
#         self.name = name
#
#     def get_name(self):
#         return self.name
#
#
# fangzi = Home('三室一厅', 120, '成都市-成华区-建设路')
# bed1 = Bed("双人床")
# fangzi.Add_furniture(bed1)
# refrigerator1 = Refrigerator('大一点的旧冰箱')
# fangzi.Add_furniture(refrigerator1)
# print(fangzi)

# class Person:
#     number = 0
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         Person.number = Person.number + 1
#         print(Person.number)
#
#     def __str__(self):
#         return '我的名字叫%s 年龄是%s' % (self.name, self.age)
#
#
# xm = Person('小明', 21)
# print(xm)
#
# xl = Person('小李', 22)
# print(xl)


# class Rectangle:
#     def __init__(self, long, wide):
#         self.long = long
#         self.wide = wide
#
#     def __str__(self):
#         msn = '周长为%s.' % (self.long * self.wide)
#         msn += '面积为%s' % (2 * (self.long + self.wide))
#         return msn
#
#     @classmethod
#     def func(cls):
#         pass
#
#
# rg = Rectangle(8, 6)
# print(rg)

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def input_information(self):
#         return '我的名字叫%s 年龄是%s' % (self.name, self.age)
#
#
# xm = Person('小明', 21)
# print(xm.input_information())
#
# xl = Person('小李', 22)
# print(xl.input_information())
#
#
# class Rectangle:
#     def __init__(self, long, wide):
#         self.long = long
#         self.wide = wide
#
#     def get_area(self):
#         msn = '周长为%s.' % (self.long * self.wide)
#         msn += '面积为%s' % (2 * (self.long + self.wide))
#         return msn
#
#
# rg = Rectangle(8, 6)
# print(rg.get_area())


# class Person(object):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def intr(self):
#         print('大家好 我是%s 今年 %s' % (self.name, self.age))
#
#
# class Programer(Person):
#     def __init__(self, name, age):
#         Person.__init__(self, name, age)
#
#     def study(self, programer):
#         print('%s 正在学习 %s编程' % (self.name, programer))
#
#     def intr(self, hobby):
#         Person.intr(self)
#         print('我喜欢 %s' % hobby)
#
#
# class language(Person):
#     def __init__(self, name, age):
#         super().__init__(name, age)
#
#     def study(self, language):
#         print('%s 正在学习 %s语言' % (self.name, language))
#
#     def intr(self):
#         super().intr()
#         print('我喜欢 游泳')
#
#
# class ProgramerLanguage(Programer, language):
#     def __init__(self, name, age):
#         Programer.__init__(self, name, age)
#         self.Program = ''
#         self.language = ''
#
#     def study(self, program, language):
#         self.proaram = program
#         self.language = language
#         print('%s 正在学习 %s 和 %s' % (self.name, self.Program, self.language))
#
#
# wang = Programer('小王', '21')
# wang.study('python')
# wang.intr('游戏')
#
# li = language('小李', '23')
# li.study('英语')
# li.intr()
#
# wei = ProgramerLanguage('小伟', 25)
# wei.study('python', '英语')
# wei.intr('钓鱼')


# class BaseClass(object):
#     def play(self):
#         print('Base is play!')
#
#
# class ClassA(BaseClass):
#     def play(self):
#         print('A is playing')
#
#
# class ClassB(BaseClass):
#     def play(self):
#         print('B is playing')
#
#
# class ClassC(ClassA, ClassB):
#     pass
#
#
# c = ClassC()
# c.play()


# class People(object):
#     def say(self):
#         print('people talk')
#
#
# class Pig(object):
#     def say(self):
#         print('pig talk')
#
#
# class Dog(object):
#     def say(self):
#         print('dog talk')
#
#
# def say_func(object):
#     object.say()
#
#
# xiaoming = People()
# henhen = Pig()
# wangwang = Dog()
#
# say_func(xiaoming)
# say_func(henhen)
# say_func(wangwang)


# class People(object):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def intr(self):
#         print('%s 的年龄是 %s' % (self.name, self.age))
#
#
# class Ticket(People):
#     def __init__(self, name, age):
#         People.__init__(self, name, age)
#
#     def buy_tickets(self, ticket):
#         print('价格为 %s' % (self.name, ticket))
#
#
# xm = Ticket('小明', 21)
# xm.buy_tickets('60')


# class School(object):
#     def __init__(self, student, teacher):
#         self.student = student
#         self.teacher = teacher
#


# class Person:
#     def __init__(self, name, achievement):
#         self.name = name
#         self.achievement = achievement
#
#     def information(self):
#         print('姓名是%s 成绩是%s' % self.name, self.achievement)
#
#
# xm = Person('小明', 98)
# print(xm)

# class Member(object):
#     def __init__(self, name, achievement):
#         self.name = name
#         self.achievement = achievement
#
#
# class Student(Member):
#     number = 0
#
#     def __init__(self, name, achievement):
#         Member.__init__(self, name, achievement)
#         Student.number = Student.number + 1
#         print(Student.number)
#
#     def input_information(self):
#         return '%s 成绩是%s' % (self.name, self.achievement)
#
#     def __del__(self):
#         Student.number -= 1
#         print(Student.number)
#
#
# class Teacher(Member):
#     number = 0
#
#     def __init__(self, name, achievement):
#         Member.__init__(self, name, achievement)
#         Teacher.number = Teacher.number + 1
#         print(Teacher.number)
#
#     def information(self):
#         return '%s 工资是%s' % (self.name, self.achievement)
#
#     def __del__(self):
#         Teacher.number -= 1
#         print(Teacher.number)
#
#
# xm = Student('小明', 98)
# print(xm.input_information())
#
# li = Teacher('李老师', 5000)
# print(li.information())
#
# wang = Teacher('王老师', 6000)
# print(wang.information())
#
# xh = Student('小红', 100)
# print(xh.input_information())
#
# oy = Teacher('欧阳老师', 7000)
# print(oy.information())
#
# del oy


# class Ticketing(object):
#     def __init__(self, age):
#         self.age = age
#
#     def get_price(self, week=True):
#         if week:
#             self.ratio = 1
#         else:
#             self.ratio = 1.2
#         if self.age <= 12:
#             self.discount = 0.5
#         elif self.age < 60:
#             self.discount = 1
#         elif self.age < 80:
#             self.discount = 0.5
#         else:
#             self.discount = 0
#
#         self.price = 120 * self.discount * self.ratio
#         return '价格为%s' % self.price
#
#
# xm = Ticketing(11)
# print(xm.get_price())
# xl = Ticketing(45)
# print(xl.get_price())
# xo = Ticketing(65)
# print(xo.get_price())
# xp = Ticketing(81)
# print(xp.get_price())

# class Bird(object):
#     def __init__(self, name, cry, fly):
#         self.name = name
#         self.cry = cry
#         self.fly = fly
#
#
# class Big_bird(Bird):
#     def __init__(self, name, cry, fly):
#         Bird.__init__(self, name, cry, fly)
#         self.name = name
#         self.cry = cry
#         self.fly = fly
#
#     def his_name(self):
#         return '它是%s鸟 它的叫声是%s 它是可以%s的' % (self.name, self.cry, self.fly)
#
#     def start_fly(self):
#         print('鸟在天上飞')
#
#
# class Penguin(Bird):
#     def __init__(self, name, cry, go):
#         Bird.__init__(self, name, cry, go)
#         self.name = name
#         self.cry = cry
#         self.go = go
#
#     def he_name(self):
#         return '它是%s 它的叫声是%s 但是它不会飞,它是用%s的' % (self.name, self.cry, self.go)
#
#     def start_fly(self):
#         print('企鹅不会飞，只会扑翅膀')
#
#
# niao = Big_bird('布谷', '布谷、布谷、布谷布谷！', '飞')
# print(niao.his_name())
# niao.start_fly()
# niao = Penguin('企鹅', '嘎嘎嘎', '走')
# print(niao.he_name())
# niao.start_fly()

# import math
#
#
# class Point(object):
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def getX(self):
#         return self.x
#
#     def getY(self):
#         return self.y
#
#
# class Line(Point):
#     def __init__(self, P0, P1):
#         Point.__init__(self, P0, P1)
#         self.x = p1.getX() - p0.getX()
#         self.y = p1.getY() - p0.getY()
#         self.len = math.sqrt(self.x * self.x + self.y * self.y)
#
#     def getlen(self):
#         return self.len
#
#
# p0 = Point(4, 11)
# p1 = Point(10, 3)
# Line = Line(p0, p1)
# print(Line.getlen())


# class Box:
#     number = 0
#
#     def __init__(self, length, height, width):
#         self.length = length
#         self.height = height
#         self.width = width
#         Box.number = Box.number + 1
#         print(Box.number)
#
#     def volume(self):
#         return '体积为%s' % (self.length * self.height * self.width)
#
#
# rectangle = Box(3, 4, 5)
# print(rectangle.volume())
# rectangle = Box(7, 8, 9)
# print(rectangle.volume())
# rectangle = Box(9, 1, 8)
# print(rectangle.volume())
# rectangle = Box(6, 2, 9)
# print(rectangle.volume())
# rectangle = Box(5, 9, 1)
# print(rectangle.volume())
#
#
# class Automobile(object):
#     def __init__(self, vehicle_type, brand, daily_rent):
#         self.vehicle_type = vehicle_type
#         self.brand = brand
#         self.daily_rent = daily_rent
#
#
# class BuickGLB(Automobile):
#     def __init__(self, vehicle_type, brand, daily_rent):
#         Automobile.__init__(self, vehicle_type, brand, daily_rent)
#         self.daily_rent = 600
#
#     def cost(self, days):
#         self.rent = self.daily_rent * days
#         print('价格为%d' % self.rent)
#
#
# class Bmw(Automobile):
#     def __init__(self, vehicle_type, brand, daily_rent):
#         Automobile.__init__(self, vehicle_type, brand, daily_rent)
#         self.daily_rent = 500
#
#     def cost(self, days):
#         self.rent = self.daily_rent * days
#         print('价格为%d' % self.rent)
#
#
# class RedFlag(Automobile):
#     def __init__(self, vehicle_type, brand, daily_rent):
#         Automobile.__init__(self, vehicle_type, brand, daily_rent)
#         self.daily_rent = 300
#
#     def cost(self, days):
#         self.rent = self.daily_rent * days
#         print('价格为%d' % self.rent)
#
#
# class GoldenCup(Automobile):
#     def __init__(self, vehicle_type, brand, daily_rent):
#         Automobile.__init__(self, vehicle_type, brand, daily_rent)
#         self.daily_rent = 800
#
#     def cost(self, days):
#         self.rent = self.daily_rent * days
#         print('价格为%d' % self.rent)
#
#
# class DoldenDragon(Automobile):
#     def __init__(self, vehicle_type, brand, daily_rent):
#         Automobile.__init__(self, vehicle_type, brand, daily_rent)
#         self.daily_rent = 1500
#
#     def cost(self, days):
#         self.rent = self.daily_rent * days
#         print('价格为%d' % self.rent)
#
#
# xm = BuickGLB('汽车', '别克GLB', 600)
# xm.cost(2)
# xl = Bmw('汽车', '宝马550i', 500)
# xl.cost(3)
# xo = RedFlag('汽车', '红旗1', 300)
# xo.cost(5)
# xp = GoldenCup('汽车', '金杯', 700)
# xp.cost(3)
# xq = DoldenDragon('汽车', '金龙', 1500)
# xq.cost(4)

# 十一题
# class Student(object):
#     def __init__(self, student_id, name, age, achievement):
#         self.__student_id = student_id
#         self.__name = name
#         self.__age = age
#         self.__achievement = achievement
#         self.__level = "优等生"
#
#     def get_student_id(self):
#         return '学号为%s' % self.__student_id
#
#     def get_name(self):
#         return '名字为%s' % self.__name
#
#     def get_age(self):
#         return '年龄为%s' % self.__age
#
#     def get_achievement(self):
#         return '成绩为%s' % self.__achievement
#
#     def get_level(self):
#         if self.__achievement >= 80:
#             return '优等生'
#         elif self.__achievement >= 60:
#             return '中等生'
#         else:
#             return '差等生'
#
#     @property
#     def level(self):
#         return self.__level
#
#     @level.setter
#     def level(self, val):
#         self.__level = val
#
#     @level.deleter
#     def level(self):
#         del self.__level
#
#
# xiaoming = Student('12', '小明', 18, 59)
# print(xiaoming.get_name())
# print(xiaoming.get_age())
# print(xiaoming.get_student_id())
# print(xiaoming.get_achievement())
# print(xiaoming.get_level())
# xiaoming.Student = ('13', '小强', 17, 80)
# print(xiaoming.Student)
# del xiaoming.level
# print(xiaoming.level)


# 十二题
# class Computer(object):
#     def __init__(self, host, monitor, mouse):
#         self.host = host
#         self.monitor = monitor
#         self.mouse = mouse
#
#     def cost(self):
#         self.rent = self.host.price + self.monitor.price + self.mouse.price
#         return self.rent
#
#
# class Equipment(object):
#     def __init__(self, brand, price):
#         self.brand = brand
#         self.price = price
#
#     def get_brand(self):
#         return '品牌为%s' % self.brand
#
#     def get_price(self):
#         return '价格为%s' % self.price
#
#
# class Host(Equipment):
#     def __init__(self, brand, price, Power_supply):
#         Equipment.__init__(self, brand, price)
#         self.__Power_supply = Power_supply
#
#     def get_PowerSupply(self):
#         return '电源%s' % self.__Power_supply
#
#
# class Monitor(Equipment):
#     def __init__(self, brand, price, Resolving_power):
#         Equipment.__init__(self, brand, price)
#         self.__Resolving_power = Resolving_power
#
#     def get_ResolvingPower(self):
#         return '分辨率为%s' % self.__Resolving_power()
#
#
# class Mouse(Equipment):
#     def __init__(self, brand, price, wired):
#         Equipment.__init__(self, brand, price)
#         self.__wired = wired
#
#     def get_wired(self):
#         return '鼠标是%s鼠标' % self.__wired
#
#
# mouses = Mouse('逻辑', 200, '有线')
# monitors = Monitor('联盟', 800, '1680x1050')
# hosts = Host('金马', 600, '有')
# print(mouses.price + monitors.price + hosts.price)


# 十三题
# from fd import *
# func()
#
#
# class Box:
#     number = 0
#
#     def __init__(self, length, height, width, color):
#         self.length = length
#         self.height = height
#         self.width = width
#         self._color = color
#         self.state = 0
#         Box.number = Box.number + 1
#         print(Box.number)
#
#     def get_volume(self):
#         self.__volume = self.length * self.height * self.width
#         return self.__volume
#
#     def operation(self):
#         if self.state == 1:
#             print('处于打开状态,不能再次打开')
#         else:
#             print('处于关闭状态，可以打开')
#             self.state = 1
#
#     def operations(self):
#         if self.state == 0:
#             print('处于关闭状态,不能再次关闭')
#         else:
#             print('处于打开状态,可以关闭')
#             self.state = 0
#
#
# rectangle = Box(3, 4, 5, 'blue')
# print(rectangle.get_volume())
# print(rectangle._color)
# rectangle = Box(7, 8, 9, 'red')
# print(rectangle.get_volume())
# print(rectangle._color)
# rectangle = Box(9, 1, 8, 'orange')
# print(rectangle.get_volume())
# print(rectangle._color)
# rectangle = Box(6, 2, 9, 'black')
# print(rectangle.get_volume())
# print(rectangle._color)
# rectangle = Box(5, 9, 1, 'pink')
# print(rectangle.get_volume())
# print(rectangle._color)
# print(rectangle.operation())
# print(rectangle.operation())
# print(rectangle.operations())
# print(rectangle.operations())


# 十四题
# class Box:
#     number = 0
#
#     def __init__(self, length, height, width, color):
#         self.length = length
#         self.height = height
#         self.width = width
#         self._color = color
#         self.state = 0
#         self.face = {'red': 1, 'orange': 2, 'yellow': 3, 'pink': 4, 'cyan': 5, 'blue': 6}
#         Box.number = Box.number + 1
#         print(Box.number)
#
#     @property
#     def color(self):
#         return self._color
#
#     def __call__(self, *args, **kwargs):
#         self.__volume = self.length * self.height * self.width
#         return '体积为%d' % self.__volume
#
#     def operation(self):
#         if self.state == 1:
#             print('处于打开状态,不能再次打开')
#         else:
#             print('处于关闭状态，可以打开')
#             self.state = 1
#
#     def operations(self):
#         if self.state == 0:
#             print('处于关闭状态,不能再次关闭')
#         else:
#             print('处于打开状态,可以关闭')
#             self.state = 0
#
#
# rectangle = Box(3, 4, 5, 'blue')
# print(rectangle())
# print(rectangle._color)
# print(rectangle.face.get('red'))
# rectangle = Box(7, 8, 9, 'red')
# print(rectangle())
# print(rectangle._color)
# rectangle = Box(9, 1, 8, 'orange')
# print(rectangle())
# print(rectangle._color)
# rectangle = Box(6, 2, 9, 'black')
# print(rectangle.__call__())
# print(rectangle._color)
# rectangle = Box(5, 9, 1, 'pink')
# print(rectangle())
# print(rectangle._color)
# print(rectangle.operation())
# print(rectangle.operation())
# print(rectangle.operations())
# print(rectangle.operations())
# dice = Box.get_dice()
# print(dice.face.get('red'))


# 十五题
# class Dice:
#     face = {'red': 1, 'orange': 2, 'yellow': 3, 'pink': 4, 'cyan': 5, 'blue': 6}
#
#     @staticmethod
#     def noodles(color1, color2):
#         noodles = Dice.face.get(color1) + Dice.face.get(color2)
#         return noodles
#
#     @classmethod
#     def get_dice(cls):
#         return cls()
#
#
# dice = Dice.get_dice()
# print(dice.face.get('red'))
# print(dice.noodles('red', 'blue'))


# 十六题
# class MyFile:
#     def __init__(self, file):
#         self.file = file
#
#     @property
#     def file(self):
#         return self.file
#
#     @file.setter
#     def file(self, val):
#         self.file = val
#
#     @file.deleter
#     def file(self):
#         del self.file
#         f.close()
#
#
# f = open('Temp', 'w')
# del f


# 十八题
# class Operation(int):
#     def __new__(cls, arg=0):
#         if isinstance(arg, str):
#             all = 0
#             for each in arg:
#                 all += ord(each)
#             arg = all
#         return int.__new__(cls, arg)
#
#
# print(Operation(123))

# 十九题
# class Operation:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def conuct_operation(self):
#         for i in self.a:
#             if i in self.b:
#                 self.a = self.a.replace(i, "")
#         return self.a
#
#
# xiaoming = Operation('Welcome to Beijing', 'c')
# print(xiaoming.conuct_operation())


# 二十题
# class MyStr(str):
#     def __add__(self, other):
#         return other
#
#
# a = MyStr("a")
# b = MyStr("b")
# print(a+b)


# # 二十一题
# class Word:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def obtain_operation(self):
#         return len(self.a) == len(self.b)
#
#     def obtain_operations(self):
#         return len(self.a[0:2]) == len(self.b)
#
#
# xiaoming = Word('afjkf', 'asafdf')
# print(xiaoming.obtain_operation())
# xiaoming1 = Word('ni hao', 'asdfgh')
# print(xiaoming1.obtain_operations())


# class Stack(object):
#     def __init__(self):
#         self.item = []
#         self.max = max
#
#     def is_empty(self):
#         return self.item == []
#
#     def pop(self):
#         self.item.pop()
#
#     def push(self):
#         self.item.pop()
#
#     def top(self):
#         return self.item[self.bottom()-1]
#
#     def bottom(self):
#         return len(self.item)
#
#
# if __name__ == '__main__':
#     stack = Stack()
#     print(stack.is_empty())
#     stack.push()
#     stack.push()
#     stack.push()
#     print(stack.is_empty())
#     print(stack.pop)
#     print(stack.bottom())
#     print()


import tkinter as tk
top = tk.Tk()
top.title("防碰撞测试")
top.geometry("600x600")
top.resizable(width=True, height=False)
top.mainloop()

