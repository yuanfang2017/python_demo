# coding=<encoding name> 例如，可添加# coding=utf-8

# 定义一个student类
class Student(object):
    def get_score(self):
        return self._score
    def set_score(self,value):
        if not isinstance(value,int):
            raise ValueError('score must be an integer')
        if value <0 or value> 100:
            raise  ValueError('score must between 0-100!')
        self._score = value

s = Student()
s1 = Student()
s.set_score(33)
print s.get_score()
s1.set_score(990)
s1.get_score()