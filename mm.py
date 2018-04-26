# coding=<encoding name> 例如，可添加# coding=utf-8

# 定义一个特殊的__slots__变量，来限制该class能添加的属性

# 定义一个类
class Student(object):
    __slots__ = ('name','age')   # 用tuple定义允许绑定的属性名称，要用单引号括起来

# 实例化一个对象
s = Student()
s.name = 'hello'
s.age =78