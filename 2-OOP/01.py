'''
定义一个学生类，用来定义学生
'''
# 定义一个空的类
class Student():
    pass

# 定义一个对象
mingyue = Student()

# 定义一个类，用来听python的学生
class pystudent():
    # 用None给不确定的值赋值
    name = None
    age = 18
    course = "Python"

    # 需要注意！1
    # 1.def dohomework的缩进层级
    # 2.系统默认有一个self函数
    def dohomework(self):
        print("i am doing homework")
        return None

# 实例化一个叫yueyue的学生
yueyue = pystudent()
