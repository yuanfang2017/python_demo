# coding=<encoding name> 例如，可添加# coding=utf-8

# 迭代器

# 定义一个迭代器，依次返回1,3,5
def add():
    print 'test 1'
    yield 1
    print 'test 2'
    yield 3
    print 'test 3'
    yield 5

# 创建一个对象
a =add()
a.next()
a.next()
# 把函数改成generator后，我们基本上从来不会用next()来调用它，而是直接使用for循环来迭代
for a in add():
    print a

# 迭代器的意义：它是在for循环的过程中不断计算出下一个元素，并在适当的条件结束for循环



