# coding=<encoding name> 例如，可添加# coding=utf-8
# 参数--关键字
def function(name,age,**kk):
    print 'name:',name
    print 'age:',age
    print kk

function('kfc',23,city='biejing')

function('kfc',23,denger='M')

# 总结 ，可变参数允许你传入0个或任意个参数，
# 这些可变参数在函数调用时自动组装为一个tuple。
# 而关键字参数允许你传入0个或任意个含参数名的参数，
# 这些关键字参数在函数内部自动组装为一个dict。
