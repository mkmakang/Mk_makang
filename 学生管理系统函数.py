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
    add_dict = {}
    add_name=input("请输入您要增加的学生姓名")
    add_sex=input("请输入你要增加的学生性别")
    add_tel=input("请输入你要增加的学生电话号码")
    add_dict["name"] = add_name
    add_dict["sex"] = add_sex
    add_dict["tel"] = add_tel
    studentInfos.append(add_dict)
    print(studentInfos)


def del_stu():
    m = int(input("请输入你要删除的学生信息的序号"))
    del studentInfos[m-1]
    print(studentInfos)


def mod_stu():
    n = int(input("请输入你要修改的学生信息的序号"))-1
    mod_name = input("请输入你要修改的学生姓名")
    mod_sex = input("请输入你要修改的学生性别（男/女）")
    mod_tel = input("请输入你要修改的学生电话")
    mod_dict = studentInfos[n]
    mod_dict["name"] = mod_name
    mod_dict["sex"] = mod_sex
    mod_dict["tel"] = mod_tel
    print(studentInfos)


def show_stu():
    print("=" * 50)
    print("学生信息如下")
    print("=" * 50)
    print("序号   姓名  性别  手机号")
    num = 1
    for i in studentInfos:
        print("%d %s %s %s"%(num,i.get("name"),i.get("sex"),i.get("tel")))
        num+=1


def main():
    while True:
        a=menu()
        if a == 1:
            add_stu()
        if a == 2:
            del_stu()
        if a == 3:
            mod_stu()
        if a == 4:
            show_stu()
        if a == 0:
            break
main()