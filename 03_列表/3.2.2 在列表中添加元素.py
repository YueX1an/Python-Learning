# 1.在列表末尾添加元素

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)

"""
方法append()将'ducati'添加到了列表的末尾而不影响其他元素
可以创建一个空列表，用一系列的append()语句添加元素
"""

motorcycles = []
print(motorcycles)
motorcycles.append('honda')
print(motorcycles)
motorcycles.append('yamaha')
print(motorcycles)
motorcycles.append('suzuki')
print(motorcycles)

"""
这种创建列表的方法非常常见，因为要等程序运行之后才知道用户在程序中存储哪些数据
为控制用户，可以首先创建一个空列表，用于存储用户将要输入的值
然后将用户提供的每个新值附加到列表中
"""

# 2.在列表中任意位置添加元素

motorcycles = ['honda', 'yamaha', 'suzuki']

motorcycles.insert(0, 'ducati')
print(motorcycles)

"""
值'ducati'被插入到了列表开头，方法insert(A, 'B'), A处为列表插入的位置，B为插入的内容
"""