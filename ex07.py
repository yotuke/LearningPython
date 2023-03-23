"""
·······································dict和set···········································
1.dict全称dictionary，在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度。
2.set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。
  要创建一个set，需要提供一个list作为输入集合.
···························································································
"""
# dict
staffs = {'Tom': '0010', 'funny': '0011', 'ico': '0012'}
print(staffs)

# set
animals = set(['cat', 'dog', 'bird'])

print(animals)
print(type(animals))