# coding=<encoding name> 例如，可添加# coding=utf-8
# 迭代
# 定义一个dict集合出来
a = {'a':10,'b':20,'c':30,'d':40}
# 迭代 key
for key in a:
     print key


# 迭代value
for values in a.itervalues():
    print values

# 迭代 key,values
for key,vakues in a.iteritems():
    print key,values

# 发现迭代出来是无序的，，

# 判断一个对象是否可迭代
from collections import Iterable
print isinstance('abc',Iterable)
print isinstance(123,Iterable)
print isinstance([1,2,3],Iterable)
