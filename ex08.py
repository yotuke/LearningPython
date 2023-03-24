# python中的函数

"""
python定义函数语句如下:
····························
    def 函数名（参数）:
        ..代码块..
        return 返回值
····························
Tips:
1.python函数不指定参数类型
2.python的返回值可以是多个，并且将多个返回值存储到一个元组中返回
3.python的参数类型有：必选参数、默认参数、可变参数和关键字参数
    默认参数: def power(x, n=2),如果只传入一个参数x【power（4）】, n默认为 2.默认参数一般放在参数列表的最后面.默认参数要指向不变参数
    可变参数: def  calc(*para)，可变参数就是传入的参数个数是可变的，这些可变参数在函数调用时自动组装为一个tuple。
    关键字参数:关键字参数允传入任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict

"""


# 必选参数
def hello(name):
    print("hi!", name)


# hello("Tom")


# 默认参数
def power(x, n=2):
    result = 1
    while n > 0:
        result = result * x
        n = n - 1
    return result


# print(power(7))


# 可变参数
def calc(*param):
    for i in param:
        print(i)


# 关键字参数
def person(**key):
    print(key)


# 将 age = 1 这种带变量名和值的参数封装成字典存入可变参数中
person(name='jack', city='he fei')
