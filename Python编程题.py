# 1、使用Python语言实现冒泡排序
#   思路：先取列表的第一个数字、依次跟后面的数字比较大小、如果第一个数字比后面大、则交换位置
#   利用下标来取值、第一个数字a依次从第一位取倒数第一位（把最后一位留给第二个数字b来取、好做比较）
#   第二个数字b依次从第二位取到最后一位、以此类推、当把列表中数字取完、结果就出来了

"""
a=[19,14,45,28,57,29,65,52,85,45]
for i in range(len(a)):
    for j in range(1,len(a)):
        if a[j]>a[j-1]:
            a[j],a[j-1]=a[j-1],a[j]
print(a)
"""

# 2、编写一个函数完成十进制到二进制、八进制、十六进制的转化

"""
def run(data,jinzhi):
    a = [0,1,2,3,4,5,6,7,8,9,"A","B","C","D","E","F"]
    b = []
    while True:
        shang = data//jinzhi
        yushu = data%jinzhi
        b = b + [yushu]
        if shang == 0:
            break
        data = shang
    b.reverse()
    for i in b :
        print(a[i],end="")
run(data=int(input("请输入一个数字")),jinzhi=int(input("请输入进制")))
"""

# 3、利用条件运算符的嵌套来完成此题：学习成绩大于90分的同学用A来表示、60-89分之间的同学用B表示、60分以下的用C表示

"""
a = int(input("请输入你要查询的学生成绩"))
if a >= 90:
    print("该学生的成绩等级为：A")
elif a >= 60 and a <=89 :
    print("该学生的成绩等级为：B")
else:
    print("该学生的成绩等级为：C")
"""

# 4、编写函数、判断一个数字是否为素数、是则返回字符串YES、否则返回字符串NO

"""
def su(num):
    if num<2:
        print("该%d不符合素数的定义"%num)
    elif num == 2:
        print("该%d是素数"%num)
    else:
        for i in range(2,num):
            if num%i == 0:
                print("NO")
            else:
                print("YES")
su(num=int(input("请输入一个数字")))
"""

# 5、自己定义一个异常类、继承Exception类、捕获下面的过程：判断input()输入的字符串长度是否小于5、如果小于5、
#    比如输入长度为3则输出：“The input is of length 3,expecting at least 5”，大于5输出"print success"

"""
class Err(Exception):
    def __init__(self,m):
        self.m=m
    def liu(self):
        if len(self.m)<5:
            return ("The input is of length %d,expecting at least 5"%len(self.m))
        if len(self.m)>5:
            return 'print success'

n=input("请输入一组字符串")
try:
    raise Err(n)
except Err as e:
    print(e.liu())
"""