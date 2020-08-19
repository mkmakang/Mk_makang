import random
import xlrd
# 一、输出商品列表  用户输入序号 显示用户选中的商品
# 商品 li=["手机","电脑","鼠标垫","游艇"]
# a.允许用户添加商品
# b.用户输入序号显示内容
"""
li=["手机","电脑","鼠标垫","游艇"]
a=input("请输入你想加入的商品")
li.append(a)
b=int(input("请输入序号"))
print(li[b])
"""
# 二、转换
# a. 将字符串 s = "alex"转换为列表
# b. 将字符串s = "alex"转换为元组
# c. 将列表li = ["alex", "seven"]转换为元组
# d.将元组 tu = ("Alex", "seven")转换为列表
"""
s="alex"
print(list(s))
print(tuple(s))
li=["alex","seven"]
print(tuple(li))
tu=("Alex","seven")
print(list(tu))
"""
# 三、写代码，有如下列表，li=[“alex”,“eric”,“rain”],按照要求实现每一个功能

# a.计算列表长度并输出
# b.列表中追加元素"seven",并输出添加后的列表
# c.请在列表中的第一个位置插入元素"Tony"，并输出添加后的列表
# d.请修改列表中的第2个位置的元素为"Kelly"，并输出修改后的列表
# e.请删除列表中的元素"eric",并输出删除后的列表
# f.请删除列表中的第2个元素，并输出删除的元素的值和删除后的列表
# g.请删除列表中的第3个元素，并输出删除后的列表===用不同的方法，不能和上面的方法重复
# h.请删除列表中的第2至4个元素，并输出删除元素后的列表
# i.请将列表所有的元素反转，并输出反转后的列表
"""
li=["alex","eric","rain"]
print(len(li))
print(li)

li.append("seven")
print(li)

li.insert(0,"Tony")
print(li)

li[1]="kelly"
print(li)

li.remove("eric")
print(li)

print(li.pop(1))
print(li)

del li[2]
print(li)

li1=[1,2,3,4,5,6]
del li1[1:3]
print(li1)

li1.reverse()
print(li1)
"""
"""
# 四、写代码，有如下列表，li=[“hello”,“seven”,[“mon”,[“h”,“kelly”],“all”,123,446],按照要求实现每一个功能
# a.请根据索引输出"kelly"

li2=["hello","seven",["mon",["h","kelly"],"all",123,446]]
print(li2[2][1][1])
"""
"""
# 五、列举布尔值是False的所有值
print(bool(0))
print(bool(""))
print(bool([]))
print(bool(()))
print(bool(None))
print(bool({}))
"""
"""
num=int(input("请输入月份"))
if num in [1,2,3]:
    print("该月份属于春天")
elif num in [4,5,6]:
    print("该月份属于夏天")
elif num in [7,8,9]:
    print("该月份属于秋天")
else:
    print("该月份属于冬天")
"""

"""
year=int(input("请输入你的年份"))
if (year%4==0 and year%100!=0) or (year%400==0):
    print("该年为闰年")
else:
    print("该年不为闰年")
"""

# 1、使用while循环和for循环,求1～100之间所有偶数之和(至少一种方法)
# while循环
"""
s=0
n=2
while n<=100:
    s+=n
    n+=2
print(s)
"""
# for循环
"""
方法一
s=0
for i in range(0,101,2):
    s+=i
print(s)
方法二
s=0
for i in range(0,101):
    if i%2==0:
        s+=i
print(s)
"""
# 2、 使用while循环和for循环输出1 2 3 4 5 6     8 9 10(至少一种方法)
# while循环
"""
n=0
s=1
while n!=7:
    if n<7:
        n+=s
        print(n)
    elif n>7:
        n+=s
        print(n)
    else:
        print("")
"""
# for循环
"""
for i in range(1,11):
    if i==7:
        continue
    else:
        print(i,end="  ")
"""
# 3、使用for循环,求1-100的所有数的和
"""
s=0
for i in range(0,101):
    s+=i
print(s)
"""
# 4、输入1到100之间的偶数:
"""
for i in range(0,101,2):
    print(i)
"""
# 5、用户登陆（三次机会重试），用户名为:abc；密码为123
# 方法一
"""
for i in range(3):
    a=input("请输入用户名")
    b=input("请输入密码")
    if a=="abc" and b=="123":
        print("登陆成功")
        break
    else:
        print("用户名或密码输入错误")
"""
# 方法二
"""
n=1
while n<=3:
    a=input("请输入你的用户名")
    b=input("请输入你的密码")
    if a=="abc" and  b=="123":
        print("登陆成功")
        break
    else:
        n+=1
        print("用户名或密码输入错误")
"""
# 6、有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
"""
n=0
for a in range(1,5):
    for b in range(1,5):
        for c in range(1,5):
            if a!=b and a!=c and b!=c:
                print(a,b,c)
                n+=1
print("总共能组成",n)
"""
# 7、输入三个整数x,y,z，请把这三个数由小到大输出。
"""
x=int(input("请输入一个数字"))
y=int(input("请输入一个数字"))
z=int(input("请输入一个数字"))
a=[x,y,z]
a.sort()
print(a)
"""
# 8、将一个列表的数据复制到另一个列表中。使用两种方法
"""
# 列表如下所示list1 = [11,22,33,44]
list1 = [11,22,33,44]
list2 = [55,66,77,88]
# 方法一
# list1.extend(list2)
# print(list1)
# 方法二
# list1=list2.copy()
# print(list1)
"""
# 9、按相反的顺序输出列表的值。a = ['one', 'two', 'three']
"""
a = ['one', 'two', 'three']
a.reverse()
print(a)
"""
# 10、有如下值集合[11,22,33,44,55,66,77,88,99,90], 将所有大于66的值保存至字典的第一个key中，
# 将小于66值保存至第二个key的值中。
"""
li = [11,22,33,44,55,66,77,88,99,90]
dic = {}
n = []
m = []
for i in li:
        if i > 66:
                n.append(i)
        if i < 66:
                m.append(i)
dic.update(key1 = m, key2 = n)
print(dic)
"""
# 11、一行代码实现两个变量进行交换
"""
a=10
b=20
a,b=b,a
print(a,b)
"""

# 1、输入一个人名，如果字典中有这个人输出人名对应的城市
"""
places={'张三':['上海','广州','深圳'],'李四':['九寨沟','张家界','张家口']}
a=input("请输入名字")
for i in places:
    if a==i:
        print(places[a])
"""
"""
places={'张三':['上海','广州','深圳'],'李四':['九寨沟','张家界','张家口']}
a=input("请输入名字")
for i in places:
    if a==i:
        print(places.setdefault(i))
"""
# 2、求阶乘
"""
a=int(input("请输入一个数字"))
for i in range(1,a):
   a*=i
print(a)
"""
# 3、从键盘输入一个字符串，将小写字母都转换成大写字母，将字符串以列表的形式输出
"""
a="HellOpyTHon"
print(a.upper())
print(list(a))
"""
"""
a=input("请输入一个字符串")
l=[]
for i in a:
    if i.isdigit()==True:
        l.append(i)
    else:
        l.append(i.upper())
print(l)
"""
# 4、随机输入一个八位以内的整数，求它是几位数，然后逆序打印其他数字
"""
a=(input("请随机输入一个八位以内的整数"))
b=len(a)
if b<=8:
    print(b)
    c=list(a)
    c.reverse()
    print(c)
else:
    print("大于八位数")
"""
# 5、猜年龄游戏
# 要求：
# 1.允许用户最多尝试3次，3次都没猜对的话，就直接退出，如果猜对了，打印恭喜信息并退出
# 2.猜的数字给定要求：1----18之间的整数
"""
a = random.randint(1,18)
print(a)
for i in range(3):
    b = int(input("请输入1——18之间的整数"))
    if b!=a:
        print("对不起，你猜错了")
        continue
    else:
        print("恭喜你答对了")
        break
"""
# 5、猜年龄游戏升级版(选做)
# 要求：
# 允许用户最多尝试3次
# 每尝试3次后，如果还没猜对，就问用户是否还想继续玩，如果回答Y或y, 就继续让其猜3次，以此往复，如果回退答N或n，就出程序
# 如果猜对了，就直接退出
"""
a=random.randint(1,18)
print(a)
b =  "y"
while b=="y" or b=="Y":
    for i in range(3):
        b=int(input("请随机输入一个1——18的整数"))
        if b!=a:
            print("对不起猜错了")
            continue

        else:
            print("恭喜你答对了")
            break
    b = input("是否继续游戏===是/y   不是/n")
"""
#6、 冒泡排序
# 变量如下：
# list01 = [5,65,41,1,32,8,9,89,670]
"""
list01 = [5,65,41,1,32,8,9,89,670]
for i in range(len(list01)):
   for j in range(1,len(list01)):
      if list01[j]>list01[j-1]:
         list01[j],list01[j-1]=list01[j-1],list01[j]
print(list01)
"""
# 7、打印一个等腰三角形
# 需求分析：
# 行数 6
# 空格数 5 4 3 2 1
# 星星数 1 3 5 7 9 11
"""
for i in range(6):
    for j in range(5-i):
        print(" ",end=" ")
    for g in range(2*i+1):
            print("g",end=" ")
    print()
 """
# 8、打印一个矩形
# 需求分析 ：
# 行数 6
# 空格数 0
# 星星数 6 6 6 6 6 6
"""
for i in range(6):
    for j in range(6):
        print("*",end=" ")
    print()
    """
# 9、打印一个直角三角形
# 需求分析
# 行数 6
# 空格数 0
# 星星数 1 2 3 4 5 6
"""
for i in range(1,7):
    for j in range(i):
        print("*",end=" ")
    print()
"""

"""
for i in range(1,10):
    for j in range(i):
        print("❤",end=" ")
    print()
"""

"""
# 1.编写一个名为collatz()的函数,它有一个名为number的参数
#如果参数是偶数,那么collatz()就打印出number//2
#如果number是奇数,collatz()就打印3*number+1
def collatz(number):
    if number%2==0:
        print(number//2)
    else:
        print(3*number+1)
collatz(int(input("请输入一个数字")))

# 2.使用匿名函数对多个数字求和，形参不能给死。
num=lambda *args:sum(args)
print(num(1,23,456,7890,9,87,654,3210))

# 3、写函数，检查传入字典的每一个value的长度,如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。
def run(**kwargs):
    for i,v in kwargs.items():
        if len(v)>2:
            kwargs[i]=v[0:2]
    return kwargs   
print(run(name="makang",age="1002",sex="nan"))
"""


#编写一个学生管理系统，要求如下。**
#1. 使用自定义函数，完成对程序的模块化。
#2. 学生信息至少包含：姓名、性别及手机号。
#3. 该系统具有的功能：添加、删除、修改、显示、退出系统。
#设计思路如下
#1. 提示用户选择功能操作。
#2. 获取用户选择的功能。
#3. 根据用户的选择，分别调用不同的函数，执行相应的功能。
# 1.  新建一个列表，用来保存学生所有信息。
# 2.  定义打印功能菜单的函数。
# 3.  定义添加学生信息的函数。
# 4.  定义删除学生信息的函数。
# 5.  定义修改学生信息的函数。
# 6.  定义显示学生信息的函数。
# 7.  在主函数中执行不同的功能。
# 8.  调用main函数。
"""
studentInfos = []
def menu():
    print("="*50)
    print("  学生管理系统")
    print("1.添加学生信息")
    print("2.删除学生信息")
    print("3.修改学生信息")
    print("4.显示所有学生信息")
    print("0.退出系统")
    print("="*50)
    choice = int(input("请输入你要执行的操作"))
    return choice

def add_stu():
    add_dict={}
    name = input("请输入增加的学生姓名")
    sex = input("请输入增加的学生性别")
    tel = input("请输入增加的学生电话")
    add_dict["name"] = name
    add_dict["sex"] = sex
    add_dict["tel"] = tel
    studentInfos.append(add_dict)
    print(studentInfos)

def del_stu():
    del_num = int(input("请输入你要删除的序号"))-1
    studentInfos.pop(del_num)
    print(studentInfos)

def mod_stu():
	stu_id = int(input("请输入要修改的序号：")) - 1
	new_name = input("请输入新的学生名字：")
	new_sex = input("请输入新的学生性别(男/女)：")
	new_tel = input("请输入新的学生电话：")
	newInfo = {}
	newInfo["name"] = new_name
	newInfo["sex"] = new_sex
	newInfo["phone"] = new_tel
	studentInfos[stu_id] = newInfo

def show_stu():
    print("="*50)
    print("学生信息如下")
    print("="*50)
    print("序号   姓名  性别  手机号")
    num = 1
    for a in studentInfos:
        print("%d %s %s %s"%(num,a.get("name"),a.get("sex"),a.get("tel")))
        num+=1

def main():
    while True:
        a = menu()
        if a == 1:
            add_stu()
        elif a == 2:
            del_stu()
        elif a == 3:
            mod_stu()
        elif a == 4:
            show_stu()
        elif a == 0:
            break

main()
"""


# 0629 作业
'''
# 一、输出商品列表，用户输入序号，显示用户选中的商品。
# 商品   li = ["手机", "电脑", "鼠标垫", "游艇" ]
# a. 允许用户添加商品
# b. 用户输入序号显示内容
li = ["手机","电脑","鼠标垫","游艇"]
a = input("请输入你想加入的商品")
li.append(a)
print(li)
b = int(input("请输入商品的序号"))-1
print(li[b])
'''

'''
# 二、转换
# a. 将字符串 s = "alex"转换为列表
# b. 将字符串s = "alex"转换为元组
# c. 将列表li = ["alex", "seven"]转换为元组
# d.将元组 tu = ("Alex", "seven")转换为列表
s = "alex"
print(list(s))
a = "alex"
print(tuple(a))
li = ["alex", "seven"]
print(tuple(li))
tu = ("Alex", "seven")
print(list(tu))
'''

'''
# 三、写代码，有如下列表，li=[“alex”,“eric”,“rain”],按照要求实现每一个功能
# a.计算列表长度并输出
# b.列表中追加元素"seven",并输出添加后的列表
# c.请在列表中的第一个位置插入元素"Tony"，并输出添加后的列表
# d.请修改列表中的第2个位置的元素为"Kelly"，并输出修改后的列表
# e.请删除列表中的元素"eric",并输出删除后的列表
# f.请删除列表中的第2个元素，并输出删除的元素的值和删除后的列表
# g.请删除列表中的第3个元素，并输出删除后的列表===用不同的方法，不能和上面的方法重复
# h.请删除列表中的第2至4个元素，并输出删除元素后的列表
# i.请将列表所有的元素反转，并输出反转后的列表
li=["alex","eric","rain"]
print(len(li))
li.append("seven")
print(li)
li.insert(0,"Tony")
print(li)
li[1]="Kelly"
print(li)
li.remove("eric")
print(li)
print(li.pop(1))
print(li)
del li[2]
print(li)
li1=["alex","eric","rain","123","456","789"]
del li1[1:4]
print(li1)
li1.reverse()
print(li1)
'''

'''
# 四、写代码，有如下列表，li=["hello","seven",["mon",["h","kelly"],"all",123,446]],按照要求实现每一个功能
# a.请根据索引输出"kelly"
li=["hello","seven",["mon",["h","kelly"],"all",123,446]]
print(li[2][1][1])
'''

'''
# 五、列举布尔值是False的所有值
print(bool(0))
print(bool(""))
print(bool([]))
print(bool(()))
print(bool(None))
print(bool({}))
print(bool(set()))
'''

'''
# 1、使用while循环和for循环,求1～100之间所有偶数之和(至少一种方法)
# 方法一：
num = 0
n = 0
while n <= 100:
    num+=n
    n+=2
print(num)
# 方法二：
m = 0
i = 0
for i in range(0,101,2):
    m+=i
print(m)
'''

'''
# 2、使用while循环和for循环输出1 2 3 4 5 6     8 9 10(至少一种方法)
# 方法一：
for i in range(1,11):
    if i == 7:
        continue
    else:
        print(i,end=" ")
        '''

'''
# 3、使用for循环,求1-100的所有数的和
m=0
for i in range(1,101):
    m+=i
print(m)
'''

'''
# 4、输入1到100之间的偶数
for i in range(2,101,2):
    print(i)
'''

'''
# 5、用户登陆（三次机会重试），用户名为:abc；密码为123
for i in range(3):
    a = input("请输入你的用户名")
    b = int(input("请输入你的密码"))
    if a == "abc" and b == 123:
        print("恭喜你输入成功")
        break
    else:
        print("对不起，你的输入有误")
        continue
'''

'''
# 六、有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
n=0
for a in range(1,5):
    for b in range(1,5):
        for c in range(1,5):
            if a!=b and a!=c and b!=c:
                print(a,b,c)
                n+=1
print("总共能组成",n)
'''

'''
# 七、输入三个整数x,y,z，请把这三个数由小到大输出
x = int(input("请输入一个整数"))
y = int(input("请输入一个整数"))
z = int(input("请输入一个整数"))
a = [x,y,z]
a.sort()
print(a)
'''

'''
# 八、将一个列表的数据复制到另一个列表中。使用两种方法
# 列表如下所示list1 = [11,22,33,44]
list1 = [11,22,33,44]
# 方法一：
list2 = [123,456,789]
list2 = list1.copy()
print(list2)
# 方法二：
list3 = [33,22,11]
list3.append(list1)
print(list3)
'''

'''
# 九、按相反的顺序输出列表的值。a = ['one', 'two', 'three']
a = ['one', 'two', 'three']
a.reverse()
print(a)
'''

'''
# 十、有如下值集合[11,22,33,44,55,66,77,88,99,90], 将所有大于66的值保存至字典的第一个key中，
# 将小于66值保存至第二个key的值中
li = [11,22,33,44,55,66,77,88,99,90]
dic = {}
m = []
n = []
for i in li:
    if i > 66:
        n.append(i)
    if i < 66:
        m.append(i)
dic.update(key1=m, key2=n)
print(dic)
'''

"""
old_file_name = input("请输入你要拷贝的文件")
a = open(old_file_name,"r",encoding="utf8")
b = old_file_name.rfind(".")
c = old_file_name[:b]
d = old_file_name[b:]
new_file_name = c +"拷贝"+ d
print(new_file_name)
e = open(new_file_name,"w",encoding="utf8")
m = a.readlines()
for i in m:
    print(i)
    e.write(i)
a.close()
e.close()
"""

"""
# 1、写函数，检查传入字典的每一个value的长度,如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。
# 实参如下:x='12', y='345', c='bywgh'
def run(**kwargs):
    for k,v in kwargs.items():
        if len(v) > 2:        
            kwargs[k] = v[0:2]
    return kwargs
print(run(x="12",y="345",c="bywgh"))

# 1、从键盘输入一个字符串，将小写字母全部转换成大写字母，然后输出到一个磁盘文件"test"中保存。
a = input("请输入一个字符串")
b = a.upper()
print(b)
c = open("test.txt","w",encoding="utf8")
c.write(b)
c.close()

# 2、有两个磁盘文件A和B,各存放一行字母,要求把这两个文件中的信息合并(按字母顺序排列), 输出到一个新文件C中。
a = open("Awenjian.txt","r",encoding="utf8")
x = a.read()
b = open("Bwenjian.txt","r",encoding="utf8")
y = b.read()

c = open("Cwenjian.txt","w",encoding="utf8")
d = list(x+y)
d.sort()
print(d)
m = " ".join(d)
print(m)
c.write(m)
a.close()
b.close()
c.close()
"""

"""
import sys
# 模拟轮盘抽奖游戏
# 轮盘分为三部分: 一等奖, 二等奖和三等奖;
# 轮盘转的时候是随机的,
# 如果范围在[0,0.08)之间,代表一等奖,
# 如果范围在[0.08,0.3)之间,代表2等奖,
# 如果范围在[0.3, 1.0)之间,代表3等奖,

# 模拟本次活动1000人参加, 模拟游戏时需要准备各等级奖品的个数.

counter = 0#计数器
T1 = 0 #一等奖个数
T2 = 0 #二等奖个数
T3 = 0 #三等奖个数

# 查看Python对递归函数设置是有默认值
# sys.getrecursionlimit()

# 更改咱们的递归函数的默认值
sys.setrecursionlimit(1600)


def lunpan():
	import random
	global T1, T2, T3
	global counter
	a = random.random()  # 随机产生一个从0-1的数字
	if counter <= 1594:
		if 0 <= a and a < 0.08:
			T1 = T1 + 1
			counter += 1
		elif 0.08 <= a and a < 0.3:
			T2 = T2 + 1
			counter += 1
		else:
			T3 = T3 + 1
			counter += 1
		# 递归函数
		lunpan()
	else:
		print("====轮盘模拟游戏结果====")
		print("一等奖需要准备%d个\n二等奖需要准备%d个\n三等奖需要准备%d个\n" % (T1, T2, T3))
lunpan()
"""

# from pymysql import *
# conn = connect(user="root", password="root", host="192.168.1.6", port=3306, database="ywjmk", charset="utf8")
# sor = conn.cursor()
# class Student():
#     def menu(self):
#         print("*"*40)
#         print("[1] 查看所有学生信息")
#         print("[2] 插入数据")
#         print("[3] 删除学生")
#         print("[4] 查看班级对应哪些学生")
#         print("[5] 退出")
#         print("*"*40)
#         num = int(input("请输入你要操作的序号"))
#         return num
# class Sql():
#     def show_stu(self):
#         try:
#             sql = """
#             select * from students
#             """
#             sor.execute(sql)
#             show_a = sor.fetchall()
#             print("序号  姓名  年龄  身高  性别  班级")
#             for i in show_a:
#                 print(i[0],i[1],i[2],i[3],i[4],i[5])
#         except Exception as show_b:
#             print(show_b)
#     def add_stu(self):
#         new_name = input("请输入你要增加的学生姓名")
#         new_age = input("请输入你要增加的学生年龄")
#         new_height = input("请输入你要增加的学生身高")
#         new_gender = input("请输入你要增加的学生性别")
#         new_cls_name = input("请输入你要增加的学生班级")
#         try:
#             sql = """
#             insert into students(name,age,height,gender,cls_name) values(%s,%s,%s,%s,%s)
#             """
#             parm = (new_name,new_age,new_height,new_gender,new_cls_name)
#             sor.execute(sql,parm)
#             conn.commit()
#         except Exception as add_a:
#             print(add_a)
#             conn.rollback()
#     def del_stu(self):
#         id = int(input("请输入你要删除的序号"))
#         try:
#             sql = """
#             delete from students where id = %s
#             """
#             sor.execute(sql,id)
#             conn.commit()
#         except Exception as del_a:
#             print(del_a)
#             conn.rollback()
#     def sele_cls(self):
#         cls_name = input("请输入你要查询的班级")
#         try:
#             sql = """
#             select name from students where cls_name = %s
#             """
#             sor.execute(sql,cls_name)
#             x = sor.fetchall()
#             print(x)
#         except Exception as sele_a:
#             print(sele_a)
#             conn.rollback()
#
# class Main():
#     while True:
#         s = Student()
#         k = Sql()
#         n = s.menu()
#         if n == 1:
#             k.show_stu()
#         elif n == 2:
#             k.add_stu()
#         elif n == 3:
#             k.del_stu()
#         elif n == 4:
#             k.sele_cls()
#         elif n == 5:
#             break
#
# if __name__ == '__main__':
#     m = Main()
# sor.close()
# conn.close()


# 1、输入一行字符，分别统计出其中的英文字母、空格、数字和其他字符的个数
"""
a = input("请输入一串字符串")
m = 0
n = 0
x = 0
y = 0
for i in a :
    if i.isspace():
        m+=1
    elif i.isdigit():
        n+=1
    elif i.isalpha():
        x+=1
    else:
        y+=1
print("该字符串有%d个空格，有%d个数字，有%d个英文字符，有%d个其他字符"%(m,n,x,y))
"""
# 2、编写一个函数完成十进制到二进制、八进制、十六进制的转化
"""
def run2():
    n = int(input("请输入一个数字"))
    b = []
    while True:
        m = n//2
        x = n%2
        b = b + [x]
        if m == 0:
            break
        n = m
    b.reverse()
    print("该数字转换为二进制为：")
    for i in b:
        print(i,end="")
run2()
"""
"""
def run8():
    n = int(input("请输入一个数字"))
    b = []
    while True:
        m = n//8
        x = n%8
        b = b + [x]
        if m == 0:
            break
        n = m
    b.reverse()
    print("该数字转换为八进制为：")
    for i in b:
        print(i,end="")
run8()
"""
"""
def run16():
    n = int(input("请输入一个数字"))
    b = []
    while True:
        m = n//16
        x = n%16
        b = b + [x]
        if m == 0:
            break
        n = m
    b.reverse()
    print("该数字转换为十六进制为：")
    for i in b:
        print(i,end="")
run16()
"""
# 3、从键盘输入一个字符串，将小写字母全部转换为大写字母，然后输出到一个磁盘文件“test”中保存
"""
a = input("请输入你要输入的字符串")
b = a.upper()
f = open("test.txt","w",encoding="utf8")
f.write(b)
f.close()
"""
# 4、利用条件运算符的嵌套来完成此题：学习成绩大于等于90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示
"""
a = int(input("请输入你要查询的学生成绩"))
if a >= 90:
    print("该学生的成绩等级为：A")
elif a >= 60 and a <=89 :
    print("该学生的成绩等级为：B")
else:
    print("该学生的成绩等级为：C")
"""
# 5、编写函数，判断一个数字是否为素数，是则返回字符串YES，否则返回字符串NO。
"""
def run():
    a = int(input("请输入一个数字"))
    for i in range(2,a):
        if a % i == 0:
            print("NO")
            break
    if a == i+1:
        print("NO")
run()
"""



# data = xlrd.open_workbook('C:\\Users\\Administrator\\Desktop\\name_list.xlsx')
# table = data.sheet_by_name("NAME")
# print (table.col_values(0)[1:])

# import re
# a = re.findall('\d+','33abcd112')
# print(a)


class Err(Exception):
    def __init__(self,m):
        self.m = m
    def liu(self):
        if  len(self.m)<5:
            return ("The input is of length %d,excepting at least 5"%len(self.m))
        if len(self.m)>5:
            return "print success"

n = input("请输入一串字符串")

try:
    raise Err(n)
except Err as e:
    print(e.liu())

import math

math.