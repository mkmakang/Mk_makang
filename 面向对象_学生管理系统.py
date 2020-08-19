from pymysql import *
class Mysql():
    def __init__(self):
        self.conn = conn = connect(user="root", password="root", host="192.168.1.6", port=3306, database="ywjmk", charset="utf8")
        self.sor = self.conn.cursor()

    def __del__(self):
        self.sor.close()
        self.conn.close()

    def execute_sql(self,sql="",parm=()):
        self.sor.execute(sql,parm)
        if "select" in sql:
            ret = self.sor.fetchall()
        else:
            self.conn.commit()
            ret = []
        return ret


class Student(Mysql):
    @staticmethod
    def menu():
        print("*" * 50)
        print("[1] 查看所有学生信息")
        print("[2] 插入数据")
        print("[3] 删除学生")
        print("[4] 查看班级对应哪些学生")
        print("[5] 退出学生系统")
        print("*" * 50)
        choice = int(input("请输入您要执行的操作"))
        return choice

    def show_stu(self):
        sql = """
            select * from students
        """
        try:
            x = self.execute_sql(sql = sql)
            print("序号  姓名  年龄  身高  性别  班级")
            for i in x:
                print(i[0], i[1], i[2], i[3], i[4], i[5])
        except Exception as e:
            print(e)

    def add_stu(self):
        new_name = input("请输入你要增加的学生姓名")
        new_age = input("请输入你要增加的学生年龄")
        new_height = input("请输入你要增加的学生身高")
        new_gender = input("请输入你要增加的学生性别")
        new_cls_name = input("请输入你要增加的学生班级")
        sql = """
            insert into students(name,age,height,gender,cls_name) values(%s,%s,%s,%s,%s)
        """
        parm = (new_name,new_age,new_height,new_gender,new_cls_name)
        try:
            self.execute_sql(sql = sql,parm = parm)
        except Exception as e:
            print(e)
            self.conn.rollback()

    def del_stu(self):
        id = int(input("请输入你要删除的序号"))
        sql = """
            delete from students where id = %s
        """
        parm = id
        try:
            self.execute_sql(sql = sql,parm = parm)
        except Exception as e:
            print(e)
            self.conn.rollback()

    def sele_cls(self):
        cls_name = input("请输入你要查询的班级")
        sql = """
            select name from students where cls_name = %s
        """
        parm = cls_name
        try:
            show_one = self.execute_sql(sql = sql,parm = parm)
            print(show_one)
        except Exception as e:
            print(e)


class Main():
    while True:
        s = Student()
        n = s.menu()
        if n == 1:
            s.show_stu()
        elif n == 2:
            s.add_stu()
        elif n == 3:
            s.del_stu()
        elif n == 4:
            s.sele_cls()
        elif n == 5:
            break

if __name__ == '__main__':
    m = Main()