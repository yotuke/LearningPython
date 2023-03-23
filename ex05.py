"""
·······································list和tuple·········································
1.list是一种有序的集合，可以随时添加和删除其中的元素.      list = []
2.tuple和list非常类似，但是tuple一旦初始化就不能修改.    tuple = ()
···························································································
"""

# list
animals = ['dog', 'cat', 'pig', 'monkey', 'rabbit']
print(type(animals))
print(animals)
print(len(animals))
print(animals[0], animals[1])
animals.sort()
print(animals)

# 元组(tuple)一旦初始化完成，只能读里面的到数据
fruits = ('apple', 'pear', 'banana', 'grape')
print(type(fruits))
print(fruits)
