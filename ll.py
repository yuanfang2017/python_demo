# coding=<encoding name> 例如，可添加# coding=utf-8

# 创建一个类
class Student(object):
    def __init__(self,name,age):  # 绑定两个属性 name，age
        self.name = name
        self.age = age
    def print_age(self):       # 定义一个输出内容的方法
        print '%s: %s' % (self.name, self.age)

    def get_age(self):
        if self.age<20:
            print '未成年'
        elif self.age <=30:
            print '而立之年'
        else:
            print '中年'


bart = Student('hello!',23)
print bart.name
bart.print_age()
bart.get_age()



