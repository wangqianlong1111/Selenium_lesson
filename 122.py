# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys #需要引入 keys 包
# import os,time
# driver = webdriver.Chrome()
# driver.get("http://www.baidu.com")
# time.sleep(3)
# driver.maximize_window() # 浏览器全屏显示
# driver.find_element(by_id)("user_name").clear()
# driver.find_element(by_id)("user_name").send_keys("fnngj")
# tab 的定位相相于清除了密码框的默认提示信息，等同上面的 clear()
# driver.find_element_by_id("user_name").send_keys(Keys.TAB)
# time.sleep(3)
# driver.find_element_by_id("user_pwd").send_keys("123456") #通过定位密码框，enter（回车）来代替登陆按钮
# driver.find_element_by_id("user_pwd").send_keys(Keys.ENTER)
# '''
# 也可定位登陆按钮，通过 enter（回车）代替 click()
# driver.find_element_by_id("login").send_keys(Keys.ENTER)
# '''
# time.sleep(3)
# driver.quit()
# 合并字符串
# fist_name = "ada"
# last_name = "lovelace"
# full_name = fist_name + " " + last_name
# print(full_name)

# 使用制表符或换行符来添加空白
# print("python")
# print('\tPython')
# print('Languages:\n\tpython\n\tC\n\tJavaScript')

# 列表
# biycles = ['trek', 'cannondale', 'redline', 'specialized']
# print(biycles[0])
# print(biycles[0].title())  # 首字母大写
# message = 'My first bicycle was a' + biycles[0].title() + '.'   # 第一辆自行车
# print(message)

# names = ['王风泽', '李腾', '郑健', '彭宇璇', '赵清']
# print(names[0] + ' 你好')
# print(names[1] + ' 你好')
# print(names[2] + ' 你好')
# print(names[3] + ' 你好')
# print(names[4] + ' 你好')
# texts = ['txt', 'the subway', 'bus']
# print(texts[0] + ' I would like to own a Honda motorcycle')
# print('names[1]: ', names[1])
# # 从第二位开始（包含）截取到倒数第二位（不包含）
# print('names[1:-2]: ', names[1:-2])
#
# print('第三个元素为 : ', names[2])
# names[2] = 2001
# print('更新后的第三个元素为 ：', names[2])
#
# names1 = ['Google', 'Runoob', 'Taobao']
# # 列表中增加Baidu
# names1.append('Baidu')
# print('更新后的列表 ：', names1)
# list = ['Google', 'Runoob', '1997', '2000']
# print('原始列表：', list)
#  删除第三个元素
# del list[2]
# print('删除第三个元素：', list)
# 组织列表
# cars = ['bmw', 'audi', 'toyota', 'subaru']
#  字母排序
# cars.sort()
#  字母相反排序
#  cars.sort(reverse=True)
# print(cars)
#  倒序(从尾到头)
# cars.reverse()
# print(cars)
# cars.reverse()
# print(cars)
# print("Here is the original list:")
# print(cars)
# print("\nHere is the original list")
# print(sorted(cars))  # 临时排序
# print("\nHere is the original list")
# print(cars)
# 练习3-8
# travel = ['biejin', 'shanghai', 'xian', 'qingdao', 'xiameng']
# print(travel)
# print(sorted(travel))
# print(travel)  # 按sorted()临时排序
# travel.reverse()
# print(travel)
# travel.reverse()
# print(travel)
# travel.sort()
# print(travel)
# travel.sort(reverse=True)
# print(travel)
# 第四章 操作列表
# 4.1遍历整个列表
# magicians = ['alice', 'david', 'carolina']
# for magician in magicians:
#     print(magician.title() + ',that was a great trick!')
#     print("I can't wait to see your next trick, " + magician.title() )
#     print("Thank you everyone. That was a great magic show!" + ".\n")
# 不必要的缩进
# message = "Hello python world"
#     print(message)

# 练习4-1
# pizzas = ['durian pazza', 'lads', 'dasdd']
# for pizza in pizzas:
#     print(pizza.title() + ',I like pepperoni pazza' )
# print("I really love pizza!")
#
# zoons = ['dog', 'cat', 'pig']
# for zoon in zoons:
#     print(zoon.title() + ',A dog would make a grear pet')
# print("Any of these animals would make a great pet!")


# for value in range(1, 6):
#     print(value)
# numbers = list(range(1,6))
# print(numbers)
# even_numbers = list(range(2, 11, 2))
# print(even_numbers)
#
# squares = []   # 赋予一个空列表
# for value in range(1, 11):   # 使用函数range()，遍历1~10的值
#     square = value**2        # 计算当前值的平方
#     squares.append(square)   # 将值放入squares末尾
#     squares.append(value**2)  # 直接平方
# print(squares)

# 练习4-3
# numerals = list(range(1, 1000001))
# for numeral in numerals:
#     print(numeral)
# print(max(numerals))
# print(sum(numerals))

# 通过给函数range() 指定第三个参数来创建一个列表，其中包含1~20的奇数
# values = list(range(1, 20, 2))
# for value in values:
#     print(value)

#  创建一个列表，其中包含3~30内能被3整除的数字
# values = list(range(3, 31, 3))
# for value in values:
#     print(value)

# 包含前10个整数（即1~10）的立方，再使用一个for 循 环将这些立方数都打印出来
# sq = []
# for value in range(1, 11):
#     value = value**3
#     sq.append(value)
# print(sq)

# 切片
# players = ['charles', 'martin', 'michael', 'florence', 'eli']
# for player in players[:3]:
#     print(player.title())

# 复制列表
# my_foods = ['pizza', 'falafel', 'carrot', 'cake']
# friend_foods = my_foods[:]
# my_foods.append('sas')
# friend_foods.append('2qs')
# print(my_foods)
# print(friend_foods)
# 练习4-10
# print("The first three items in the list are:")
# print(my_foods[:3])
# print("Three items from the middle of the list are:")
# print(my_foods[1:4])
# print("The last three items in the list are:")
# print(my_foods[2:])

#  元组
# tup2 = (1, 2, 3, 4, 6, 8, 7 )
# print(tup2[1:5])
# 创建一个新的元组只能通过连接组合
# tup1 = (12, 23, 45)
# tup2 = ('abd', 'hhz', 'zzc')
# tup3 = tup1 + tup2
# print(tup3)
# # 删除元组
# tup = (1, 2, 3, 4)
# print(tup)
#
# # del tup
# # print('删除后的元组 tup：')
# print(tup)
# tups = (20, 30)
# print("qwe:")
# for tup in tups:
#     print(tup)
# tups = (200, 32)
# for tup in tups:
#     print(tup)
# 练习4-13
# foods = ('atl', 'ccr', 'saa', 'add', 'ddd')
# for food in foods:
#     print(food)
#  food[0] = 'ada'
# foods = ('aaa', 'bbb', 'ccc', 'ddd', 'eee')
# for food in foods:
#     print(food)
# 字典
# dict1 = {'abc': 456}
# dict2 = {'abc': 123, 98.6: 37}
# dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
# print("dict['Name']: ", dict['Name'])
# print("dict['Age']: ",dict['Age'])
# print("dict[Class]: ",dict['Class'])
# dict['Age'] = 8
# dict['School'] = '菜鸟教程'
# print("dict['Age']: ",dict['Age'])
# print("dict[School]: ",dict['School'])
# print('字典长度: %d' % len(dict))


# 第五章 IF语句
# 检查当前的汽车名是否是'bmw'，如果是，就以全大写的方式打印它；否则就以首字母大写的方式打印
# cars = ['adui', 'bmw', 'subaru', 'toyota']
# for car in cars:
#     if car == 'bmw':
#         print(car.upper())
#     else:
#         print(car.title())
# 不相等输出print中的语句
# requested_topping = 'mushrooms'
# if requested_topping != 'anchovies':
#     print("Hold the anchovies!")

# answer = 17
# if answer != 42:
#     print("The is not the correct answer.Please try again!")
# 不包含 not in
# banned_users = ['andrew', 'carolina', 'david']
# user = 'marie'
# if user not in banned_users:
#     print(user.title() + ", you can post a response if you wish.")
# 5-1
# car = 'subaru'
# print("Is car == 'subaru'? I predict True.")
# print(car == 'subaru')
# print("\nIs car == 'audi'? I predict False.")
# print(car == 'audi')


# 5.3 if语句
# if后的条件不满足执行else下的语句
# age = 17
# if age >= 18:
#     print("You are old enough to vote!")
#     print("Have you registeered to vote yet?")
# else:
#     print("1111")
#     print("1122123132")

# if elif else 语句
# elif 它仅在前面的测试未通过 时才会运行
age = 12
# if age < 4:
#     print("Your admission cost is $0.")
# elif age < 18:
#     print("Your admission cost is $5.")
# else:
#     print("Your admission cost is $10.")
# if age < 4:
#     price = 0
# elif age < 18 :
#     price = 5
# else:
#     price = 10
# print("Your admission cost is $" + str(price) + ".")
# age = 12
# if age < 4:
#     price = 0
# elif age < 18:
#     price = 5
# elif age < 65:
#     price = 10
# else:
#     price = 5
# print("11111 $" + str(price) + ".")   # str()作用是转换字符串

# requested_toppings = ['mushrooms', 'extra cheese']
# if 'mushrooms' in requested_toppings:
#     print("Adding mushrooms.")
# if 'pepperoni' in requested_toppings:
#     print("Adding pepperoni.")
# if 'extra cheese' in requested_toppings:
#     print("Adding extra cheese.")
# print("\nFinished making your pizza!")

#   练习5-8
# lbiaos = ['a', 'b', 'c', 'd', 'admin']
# for lbiao in lbiaos:
#      if lbiao == "admin":
#          print('Hello admin,thank you for logging in again')
#      else:
#          print("Hello "+lbiao+",thank you for logging in again")
# 练习 5-9 如果为空，就打印消息We need to find some users!
# ads = []
# if ads:
#     for ad in ads:
#         print("aaa" + ad + ".")
# else:
#     print("We need to find some users!")

# 练习5-10
# current_users = ['a1', 'A2', 'a3', 'D4', 'a5']
# new_users = ['a1', 'b2', 'c3', 'd4', 'E5']
# for new_user in new_users:
#     for current_user in current_users:
#         if new_user.lower() == current_user.lower():
#             print(new_user + " has already been used")
#             print("please input new username")
#             break
#         elif current_user == 'a5':
#             print(new_user + " is not being used")
# 练习 5-11  在循环中使用一个if-elif-else 结构，以打印每个数字对应的序数。输出应为1st 、2nd 、3rd 、4th 、5th 、6th
# nums = list(range(1, 10))
# for num in nums:
#     if num == 1:
#         print(str(num)+"st")
#     elif num == 2:
#         print(str(num)+"nd")
#     elif num == 3:
#         print(str(num)+"rd")
#     else:
#         print(str(num)+"th")

# 第六章字典
# 添加键-值对
# alien_0 = {'color': 'green', 'points': 5}
# new_points = alien_0['points']
# print("You just earned " + str(new_points) + "points!")
# print(alien_0)
# alien_0['x_points'] = 0
# alien_0['y_points'] = 25
# print(alien_0)

#  创建空字典
# alien_0 = {}
#
# alien_0['color'] = 'green'
# alien_0['points'] = '5'
# print(alien_0)

# 修改字典中的值
# alien_0 = {'color': 'green'}
# print("The alien is " + alien_0['color'] + ".")
# alien_0['color'] = 'yellow'
# print("The alien is now " + alien_0['color'] + ".")

# alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
# print("Original x_position: " + str(alien_0['x_position']))
# #  向右移动外星人
# #  根据外星人当前速度决定将其移动多远
# if alien_0['speed'] == 'slow':
#     x_increment = 1
# elif alien_0['speed'] == 'medium':
#     x_increment = 2
# else:
#     #  这个外星人的速度一定很快
#     x_increment = 3
# alien_0['x_position'] = alien_0['x_position'] + x_increment
# print("New x_position: " + str(alien_0['x_position']))

# alien_0 = {'color': 'green', 'points': 5}
# print(alien_0)
# del alien_0["color"]
# print(alien_0)

# adsr_1 = {
#     'sdad': 'ww',
#     'sddd': 'wa',
#     'wers': 'dd',
# }
# print("sddd is adsr " + adsr_1['sddd'].title() + ".")

#  练习6-1
# naem_1 = {'fist_name': 'zhang', 'last_name': 'san', 'age': '18', 'city': 'shanghai'}
# print(naem_1)
# name = 'tom'
# age = 20
# info = '我叫%s,年龄是%s' % (name, age)
# print(info)


# alist.sort()
# print(alist)
# print(alist[::-1])

#  冒泡排序---升序
#  找n-1较大值：两两相邻元素比对，大往后移
# alist = [9, 2, 6, 0, 8]
# for i in range(0, len(alist)-1):  # (0,3)总共4个元素，3次比较
#     #  每一次较大值怎么去找---相邻比较
#     #  i=0 j=4-1-i==(0,3) 0 1 2  ; i =1 j=4-1-2== (0,2)== 0 1 ; i=2 j=4-1-2==(0,1)== 0
#     for j in range(0,len(alist)-1-i):
#         # if 前者>后者:
#         if alist[j] > alist[j+1]:
#             alist[j], alist[j+1] = alist[j+1], alist[j]
# print(alist)
# ald = [3, 5, 7, 2]
# newList = []
# print(min(ald))
# newList.append(min(ald))
#  第三方库
'''
1- where pip 
2- pip install selenium
3- pip uninstall selenium
4- pip show selenium 
import requests

# 6-3遍历字典
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
    }
    '''
# for key, value in user_0.items():
#     print("\nKey: " + key)
#     print("\nValue: " + value)
# for name in user_0.keys():
#     print(name.title())

# 6-4 嵌套
# alien_0 = {'color': 'green', 'points': 5}
# alien_1 = {'color': 'yellow', 'points': 10}
# alien_2 = {'color': 'red', 'points': 15}
# aliens = [alien_0, alien_1, alien_2]
# for alien in aliens:
#     print(alien)

# # 创建一个空列表存储外星人
# aliens = []
# # 创建30人绿色的外星人
# for aline_number in range(30):
#     new_aline = {'color': 'green', 'points': 5, 'speed': 'slow'}
#     aliens.append(new_aline)
#     # 显示前五个外星人
# for alien in aliens[:5]:
#     print(alien)
# print("...")
# # 显示创建了多少个外星人
# print("Total number of aliens: " + str(len(aliens)))
# python爬虫教程
# a = 1
# b = 1
# print(id(a))
# print(id(b))
# 第3集 课堂作业
# a = 10
# print(a)
# a += 10
# print(a)
#
# b = 10
# b -= 10
# print(b)
#
# c = 10
# c //= 3
# print(c)
#
# d = 10
# d %= 3
# print(d)

"""
7、编程程序检查用户注册的电子邮箱是否合法
"""
# e = input("请输入您的邮箱：")
# if len(e) < 11:        #判断是否是10个以上字符
#     print("必须在10个字符以上")
# else:
#     if e.count("@")!=1 or e.endswith("@") or e.startswith("@") :  #判断@是否有且仅有一个
#         print("有且仅有1个@，且@不打头，不结尾")
#     else :
#         if e.count(".")<1 or e.endswith(".") or e.startswith(".") or e.find(".") <= e.find("@") + 1:
#             print('至少有1个“.”，且“.”在@后面一个字符之后，且“.”不能打头和结尾')
#         else:
#              i = e.find("@")  # 调用字符串对象e的find方法，查找指定子字符串出现的位置
#              print(f"用户名为：{e[:i]}")
#              print(f"域名为：{e[i:]}")

# 菜鸟教程 循环语句

# break 语句可以跳出 for 和 while 的循环体。如果你从 for 或 while 循环中终止，任何对应的循环 else 块将不执行。
# continue 语句被用来告诉 Python 跳过当前循环块中的剩余语句，然后继续进行下一轮循环。

# n = 5
# while n > 0:
#     n -= 1
#     if n ==2:
#         continue
#     print(n)
# print('循环结束')

# for letter in 'Runoob':
#     if letter == 'b':
#         break
#     print('当前字母为：', letter)
# var = 10
# while var > 0:
#     print('当前变量值为：', var)
#     var = var-1
#     if var == 5:
#         break
# print("Good bye")

# for letter in 'Runoob':
#     if letter == 'o':     # 字母为o时跳过
#         continue
#     print('当前字母为：', letter)
# var = 10
# while var > 0:
#     print('当前变量值为：', var)
#     var = var-1
#     if var == 5:          # 变量为5时跳过
#         continue
# print("Good bye")

# age = int(input("请输入你家狗狗的年龄："))
# print('')
# if age <= 0:
#     print('逗我')
# elif age == 1:
#     print('等于14岁')
# elif age == 2:
#     print('等于22')
# elif age > 2:
#     human = 22 + (age - 2)*5
#     print('人类年龄：', human)
# input("点击enter退出")


# 函数
# def greet_user(username):
#     '''显示简单的问候语'''
#     print('Hello, '+ username.title() + "!")
#
# greet_user('jesse')
# 练习8-1 编写一个名为display_message() 的函数， 它打印一个句子， 指出你在本章学的是什么。
# 调用这个函数， 确认显示的消息正确无误
# def display_message():
#     print('function')
#
# display_message()
# 练习8-2 编写一个名为favorite_book() 的函数， 其中包含一个名为title 的形参。 这个函数打印一条消息，
# 如One of my favorite books isAlice in Wonderland 。 调用这个函数， 并将一本图书的名称作为实参传递给它。
# def favorite_book(title, price):
#     print('One of my favorite books is： ' + title)
#
# favorite_book('java程序设计','')
'''
if True:
    print('true')
else:
    print('false')
数字有四种类型：整数，布尔型，浮点数，复数
int(整数)，如 111
bool(布尔)，True
float(浮点数)，如 1.23
complex(复数)，如 1+2j



print()
'''
'''
# 列表
list = ['abcd', 786 , 2.23, 'runoob', 70.2]
tinylist = [123, 'runoob']
print(list)
print(list[0])
print(list[1:3])
print(list[2:])
print(tinylist * 2)
print(list + tinylist)

def reversewords(input):
    inputwords = input.split(" ")

    inputwords=inputwords[-1::-1]

    output = ' '.join(inputwords)

    return output

if __name__=="__main__":
    input = 'I like runoob'
    rw = reversewords(input)
    print(rw)


元组：与列表类似，不同之处在于元组元素不能修改
tuple = ('abcd', 786 , 2.23, 'runoob', 70.2)
tinytuple = (123, 'runoob')
print(tuple)
print(tuple[0])
print(tuple[1:3])
print(tuple[2:])
print(tinytuple * 2)
print(tinytuple + tuple)
# 条件判断
age = 20
if age >= 6:
    print('teenager')
elif age >= 18:
    print('adult')
else:
    print('kid')


s = input('birth:')
birth = int(s)
if birth < 2000:
    print('00前')
else:
    print('00后')


height = 1.75
weight = 80.5
bmi = weight/(height * height)
if bmi < 18.5:
    print('过轻')
elif 18.5 <= bmi <25:
    print('正常')
elif 25 <= bmi < 28:
    print('肥胖')
else:
    print('严重肥胖')
'''
'''
# 循环
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)


sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum = sum + x
print(sum)

sum = 0
for x in range(101):
    sum = sum + x
print(sum)

sum = 0
n = 99
while n > 0:
    sum = sum +n
    n = n-2
print(sum)

L = ['Bart', 'Lisa', 'Adam']
for Ls in L:
    print('Hello,', Ls + '!')

# 提前退出循环
n = 1
while n <= 100:
    if n > 10:  # 当n = 11时，条件满足，执行break语句
        break   # break语句会结束当前循环
    print(n)
    n = n + 1
print('END')

n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0:  # 如果n是偶数，执行continue语句
        continue    # continue语句会直接继续下一轮循环，后续的print()语句不会执行
    print(n)
'''

'''
# 十六进制函数调用
n1 = 255
n2 = 1000
print(hex(n1))
print(hex(n2))


# -*- coding: utf-8 -*-
# 自定义函数绝对值
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x
print(my_abs(-99))
# pass空函数用法
def nop():
    pass
if age >= 18:
    pass


def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x

import math
def move(x, y, step, angle=0):
    nx = x + step * marh.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny
# 调用平方函数
def power(x):
    return x * x
print(power(5))
# 调用x的n次方函数
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
print(power(5, 7))
print(power(5))


# 调用注册的函数
def enroll(name, gender, age = 6, city ='Beijing'):   # 默认年龄和城市
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)
enroll('Sarah', 'f')
print(enroll)

def add_end(L=[]):
    L.append('END')
    return L
    add_end([1, 2, 3])
print(add_end)



# 可变参数a平方 + b平方 + c平方 
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
print(calc(1, 2, 3))
# 加一个*号，把list或tuple的元素变成可变参数传进去：
nums = [1, 2, 3, 4, 5, 6]
print(calc(*nums))
# 关键字参数 kw
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)
person('Michael', 30, job='beijing')
print(person)



def person(name, age, **kw):
    if 'city' in kw:

        pass
    if 'job' in kw:
        pass
    print('name:', name, 'age:', age, 'other:', kw)
person('Jack',
       24,
       city='Beijing',
       addr='Chaoyang',
       zipcode=123456)

# 命名关键字参数
def person(name, age, **kw):
    if 'city' in kw:
        # 有city参数
        pass
    if 'job' in kw:
        # 有job参数
        pass
    print('name:', name, 'age:', age, 'other:', kw)
person('Jack', 24, city='Beijing', addr='Chaoyang', zipcode=123456)
print(person)


# 关键字参数**kw不同，命名关键字参数需要
# 一个特殊分隔符*，*后面的参数被视为命名关键字参数
def person(name, age, *, city='beijing', job):
    print(name, age, city, job)
person('jack', 24, job='engineer' )
print(person)

# 参数组合
def f1(a, b, c=0, *args, **kw):
    print('a=', a, 'b=', b, 'c=', c, 'args =',
          args, 'kw=', kw)
def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d,
          'kw =', kw)
f1(1, 2, 3, 'a', 'b', x=99)
print(f1)

# 练习--失败
def mul(x, y):
    res = x
    for n in y:
        res = res *n
    return res
print('mul(690, 30) =', mul(690,30))


def fact(n):
    if n==1:
        return 1
    return n * fact(n-1)

print(fact(100))


# 递归函数

def fact(n):
    if n==1:
        return 1
    return n * fact(n-1)
print(fact(10))


# 练习---递归函数
def move(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
    else:
        move(n-1, a, c, b)
        move(1, a, b, c)
        move(n-1, b, a, c)
move(4, 'A', 'B', 'C')



0
# 高级特性 
L = []
n = 1
while n <= 99:
    L.append(n)
    n = n+2
print(n)

# 取前三元素
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
r = []
n = 3
for i in range(n):   # n的值赋予i
    r.append(L[i])   # r更新后的列表
print(r)             # 输出前三个元素


L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print(L[-2:])


# 切片
L = list(range(100))
print(L)
print(L[10:20])   # 前11——20个数
print(L[:10:2])   # 前10个数，每两个取一个
print(L[::5])   # 所有数，每5个取一个
print(L[:])   # 复制一个list

# 练习
# 1.传入一个参数，判断该参数的长度是否为0，如果是，直接返回该参数；
#
# 2.如果长度不为0，循环判断该参数的首部是否有空格，如果有空格，去掉空格，再判断字符串的长度是否为0，如果是，直接返回字符串
#
# 3.还要循环判断该参数的尾部是否有空格，
# 如果有空格，去掉空格，再判断字符串的长度是否为0，如果是，直接返回字符串
#
# 4.返回该参数
def trim(s):
    if len(s) == 0:
        return s
    else:
        while(s[0]==' '):
            s = s[1:]
            if len(s) == 0:
                return s
        while(s[-1]==' '):
            s = s[:-1]
            if len(s) == 0:
                return s
        return s
print(trim(' abc '),len(trim(' abc ')))

# 迭代
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key)
for ch in 'ABC':
    print(ch)

for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)
for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)

# 练习未完成。。。


# 列表生成式
x = [x * x for x in range(1, 11)]
print(x)


# 循环
L = []
for x in range(1, 11):
    L.append(x * x)
print(L)

# 生成器
x = [x * x for x in range(1, 10)]
print(x)

g = (x * x for x in range(10))
for n in g:
    print(n)


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'
print(fib(6))
# 定义函数
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x
print(my_abs(-99))
if age >= 18:
    pass
def nop():
    pass


# 函数的参数
def power(x):
    return x * x
print(power(888))

# x 的 n 次方，也可修改n的值为默认值
# 比如n=5,直接输入power(5)就是5的5次方
def power(x, n):
    s = 1
    while n > 0:
        n = n -1
        s = s * x
    return s
print(power(5, 100))

# 年龄和城市设置为默认参数
def enroll(name, gender, age=6, city='beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)
print(enroll('Bob', 'M', '7'))

# 先定义一个函数，传入一个list，添加一个END再返回
def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L
print(add_end())


# 可变参数
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
print(calc(1, 2, 3, 4))

# 命名关键字参数
def person(name, age, *, city, job):
    print(name, age, city, job)
print(person('jack', 24, city='beijing', job='engineer'))

# 参数组合
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args,
          'kw =', kw)
def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d,
          'kw =', kw)
print(f1(1 ,2))
print(f1(1, 2, c=3))
print(f1(1, 2, 3, 'a', 'b'))
print(f1(1, 2, 3, 'a', 'b', x=99))
print(f2(1, 2, d=99, ext=None))

# Python的函数具有非常灵活的参数形态，既可以实现简单的调用，
# 又可以传入非常复杂的参数。
# 默认参数一定要用不可变对象，如果是可变对象，程序运行时会
# 有逻辑错误！要注意定义可变参数和关键字参数的语法：
# *args是可变参数，args接收的是一个tuple；
# **kw是关键字参数，kw接收的是一个dict。
# 以及调用函数时如何传入可变参数和关键字参数的语法：
# 可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或
# tuple，再通过*args传入：func(*(1, 2, 3))；关键字参数既可以
# 直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入
# ：func(**{'a': 1, 'b': 2})。
# 使用*args和**kw是Python的习惯写法，当然也可以用其他参数名，
# 但最好使用习惯用法。
# 命名的关键字参数是为了限制调用者可以传入的参数名，
# 同时可以提供默认值。
# 定义命名的关键字参数在没有可变参数的情况下不要忘了写分隔符*
# ，否则定义的将是位置参数。

# 递归函数
def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)
print(fact(100))


# 尾递归函数
def fact(n):
    return fact_iter(n, 1)
def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)
print(fact_iter(6, 1))


# 高级特性-切片
# 练习
def trim(s):
    if len(s) == 0:
        return s
    else:
        while s[0] == " ":
            s = s[1:]
        while s[-1] == " ":
            s = s[:-1]
        return s
print(trim(" sdasda "),len(trim(" sdasda ")))


# 迭代
d = {'a': 1, 'b': 2, 'c': 3}
for ch in 'ABC':
    print(ch)
from collections.abc import Iterable
isinstance('abc', Iterable)

# 列表生成器
L = [x * x for x in range(1, 11) if x % 2 == 0]
print(L)
d = {'x': 'A', 'y': 'B', 'z': 'C'}
for k, v in d.items():
    print(k, '=', v)


L = ['Hello', 'World', 'IBM', 'Apple']
[s.lower() for s in L]

[x if x % 2 == 0 else -x for x in range(1, 11)]

def fib(max):
	n, a, b = 0, 0, 1
	while n < max:
		yield b
		a, b = b, a+b
		n = n + 1
	reyurn
f = fib(6)
print(f)

# 高阶函数
def add(x, y, f):
    return f(x) + f(y)
print(add(-5, 6, abs))


# map/reduce
def f(x):
    return x * x
r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(list(r))


L = []
for n in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
    L.append(f(n))
print(L)


# 练习网站上的题目
# a+b
def cxz(a, b):
    return a + b
print(cxz(1, 4))

# 列表排序
L = [8, 2, 50, 3]
print(sorted(L))

# 字符串逆序（字符串逆向）
a = 'xydz'
print(a[::-1])

# 字典
a = {'1': '1', '2': '2', '3': '3'}
print(",".join(a.keys()))

# 输出字符奇数位置的字符串
a = '123456789'
print(a[::2])

# 求解100以内的所有素数（除了1和它本身以外不再有其他因数的自然数）
a = []
for i in range(2, 100):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        a.append(i)
print((' '.join(str(i) for i in a)))

# 求矩形面积
def zds(a, b):
    nx = a * b
    ny = a * 2 + b * 2
    return nx, ny
# print(zds(3, 8))

# 求中位数
L.sort()
a = int(len(L)/2)    # a 取整列表L的长度除2，3.5还是输出3
if len(L) % 2 == 0:  # 如果为偶数
    print(round((L[a] + L[a-1])/2,1))# 1代表小数点位数
else:                # 为奇数
    print(L[a])      # 四舍五入

# 光棍的悲伤
# bin()代表返回一个整数int，
# .count统计字符串里某个字符或子字符串出现的次数
print(bin(a).count("1"))

# python之光
import this

# 单身情歌
a = 'asafasfaLOVe'
if 'love' in a.lower():  # 判断love在a中
    # a.lower()将a所有大写字符转换为小写后生成的字符串
    print('LOVE')
else:
    print('SINGLE')

# 判断三角形
if (a + b > c and a + c > b and b + c > a):
    print('YES')
else:
    print('NO')

#  将序列中的元素以指定的字符连接生成一个新的字符串
str.join(sequence)
L = ['asd', 'sda', 'asf']
print("".join(L))

# 判断是否为环文
s = 'abcde'
t = 'cdeab'
if (s + s).find(t) >= 0 and len(s) == len(s):
    print('环文')
else:
    print('不是环文')

# 嵌套循环
x = 52
if x > 10:
    print("Above ten,")
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")

# 函数 函数是一种仅在调用时运行的代码块。
# 可以将数据（称为参数）传递到函数中。
# 函数可以把数据作为结果返回
# 调用函数：如需调用函数，请使用函数名称后跟括号
def my_function():
  print("Hello from a function")

my_function()

# 参数：信息可以作为参数传递给函数。
# 参数在函数名后的括号内指定。
# 可以根据需要添加任意数量的参数，只需用逗号分隔即可。
# 下面的例子有一个带参数（fname）的函数。
# 当调用此函数时，我们传递一个名字，在函数内部使用它来打印全名
def my_function(fname):
  print(fname + " Gates")

my_function("Bill")
my_function("Steve")
my_function("Elon")

# 默认参数值
def my_function(country = "China"):
  print("I am from " + country)
my_function('Bill')
my_function("123")

# 以 List 传参
# 您发送到函数的参数可以是任何数据类型
# （字符串、数字、列表、字典等）
# 并且在函数内其将被视为相同数据类型。
# 例如，如果您将 List 作为参数发送，它到达函数时仍将是 List列表
def my_function(food):
    for x in food:
        print(x)

fsdasd = ["wdaswd", "asda", "asdwqwr"]
my_function(fsdasd)

#
def my_function(x):
    return 5 * x * x
print(my_function(3))

# 递归函数
def tri_recursion(k):
  if(k>0):
    result = k+tri_recursion(k-1)
    print(result)
  else:
    result = 0
  return result

tri_recursion(6)
# k=1,result=1
# k=2,result=2+1
# k=3,result=3+tri(2)=3+3
# k=4,result=4+tri(3)=4+6
# k=5,result=5+tri(4)=5+10
# K=6,result=6+tri(5)=6+15

# 类/对象
class MyClass:
  x = 7
p1 = MyClass()
print(p1.x)

# __init__()函数
# 所有类都有一个名为 __init__() 的函数，
# 它始终在启动类时执行。
# 使用 __init__() 函数将值赋给对象属性，
# 或者在创建对象时需要执行的其他操作。
# 创建名为 Person的类，使用 __init__()函数为 name和 age赋值
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
p1 = Person("Bill",62)
print(p1.name)
print(p1.age)

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def myfunc(self):
    print("Hello my name is " + self.name)
p1 = Person("Bill", 63)
p1.myfunc()
class Student(object):
  def __init__(self, name, score):
    self.name = name
    self.score = score

# 打开一个txt文件
with open('C:/Users/Administrator/Desktop/记录.txt', 
          'r', encoding = 'utf-8') as f:
    print(f.read())

# 访问限制（无法从外部访问实例变量.__name和实例变量.__score）
class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score
    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))
# 报错        
bart = Student('asdas', 89)
print(bart.__name)

class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score
    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))
    def get_name(self):
        return self.__name
    def get_score(self):
        return self.score
    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')
    def get_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 60:
            return 'B'
        else:
            retuen 'C'

# 继承和多态
class Animal(object):
    def run(self):
        print('Animal is running...')
class Dog(Animal):
    def run(self):
        print('Dog is running...')
    def eat(self):
        print('Eating meat...')
class Cat(Animal):
    def run(self):
        print('Cat is running...')

dog = Dog()
dog.run()
cat = Cat()
cat.run()

'''
class Student(object):
    def __init__(self, name):
        self.name = name
s = Student('Bob')
s.score = 90







































