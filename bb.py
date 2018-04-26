# coding=<encoding name> 例如，可添加# coding=utf-8
def function(name,age,gender='B',city='beijing'):
    print 'name:',name
    print 'age:',age
    print 'gender:',gender
    print 'city:',city

#有多个默认参数时，调用的时候，既可以按顺序提供默认参数，
# city参数由于没有提供，仍然使用默认值。
function('yuan',25)
function('wang',24,'k')

# 当不按顺序提供部分默认参数时，需要把参数名写上
function('yuan',25,city='tianjing')