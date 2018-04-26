# coding=<encoding name> 例如，可添加# coding=utf-8

# 返回函数

# 写一个求和的函数demo

# def function(*x):
#     sum = 0
#     for n in x:
#         sum = sum +x
#     return  sum

# 把function 作为函数返回
def myfunction(*x):
    def function():
        sum = 0
        for n in x:
            sum = sum + n
        return sum
    return function
f = myfunction(1,2,3,4,5,6)

