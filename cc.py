# coding=<encoding name> 例如，可添加# coding=utf-8
# 可变参数

def function(*numbers):
    sum = 0
    for n in numbers:
        sum = sum +n*n
    print sum

aa = [1,2,3]
function(*aa)

# 总结。定义可变参数和定义list或tuple参数相比，
# 仅仅在参数前面加了一个*号。在函数内部，参数numbers接收到的是一个tuple
# 因此，函数代码完全不变。但是，调用该函数时，可以传入任意个参数，包括0个参数：