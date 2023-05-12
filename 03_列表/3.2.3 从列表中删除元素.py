# 1.使用del语句删除（知道位置）

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

del motorcycles[0]
print(motorcycles)

""" 输出结果
['honda', 'yamaha', 'suzuki']
['yamaha', 'suzuki']
del语句删除后，便无法再访问
"""

# 2.使用pop()删除元素

"""
有时，要将元素从列表删除，并借着用它的值，如需要获取刚被射杀的外星人x和y的坐标以便在相应的位置获得爆炸效果
在web应用中，将用户从活跃成员列表中删除，并将其加入到非活跃成员列表中
pop()可删除列表末尾的元素，并让你接着用。列表就像一个栈，删除列表末尾元素相当于弹出栈顶元素
"""

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

popped_motorcycle = motorcycles.pop()          # 从这个列表中弹出一个值，并将其存储到变量popped_motorcycle中
print(motorcycles)                             # 打印这个列表，核实从其中删除了一个值
print(popped_motorcycle)                       # 打印弹出的值，证明我们依然可以访问删除的值

""" 输出结果
['honda', 'yamaha', 'suzuki']
['honda', 'yamaha']
suzuki
"""

"""
方法pop()起作用方式，假设列表中的摩托车是按购买时间存储的，就可使用pop()打印一条消息，指出最后购买的是哪款摩托车
"""

motorcycles = ['honda', 'yamaha', 'suzuki']

last_owned = motorcycles.pop()
print("The last motorcycle I owned was a " + last_owned + ".")

""" 输出结果
The last motorcycle I owned was a suzuki.
"""

# 3.弹出列表中任意元素

"""
事实上可以用pop()来删除列表中任意位置的元素，只需要括号中指定要删除的元素索引即可
"""

motorcycles = ['honda', 'yamaha', 'suzuki']

first_owned = motorcycles.pop(0)
print('The first motorcycle I owned was a ' + first_owned.title() + '.')

""" 输出结果
The first motorcycle I owned was a Honda.
"""

# 4.根据值删除元素

"""
有时候，不知道删除元素的位置，但知道数值，可使用方法remove()
"""

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

motorcycles.remove("ducati")
print(motorcycles)

""" 输出结果
['honda', 'yamaha', 'suzuki', 'ducati']
['honda', 'yamaha', 'suzuki']
"""

"""
使用remove()删除元素时，也可接着使用它的值
"""

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

too_expensive = 'ducati'                         # 将要删除的元素存储到变量 too_expensive 中
motorcycles.remove(too_expensive)                # 接下来使用这个变量告诉Python将哪个值从列表中删除了
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")      # 结果显示删除的元素还存储在 too_expensive 变量中

""" 输出结果

A Ducati is too expensive for me.
"""

""" 注意！！
方法remove()只删除第一个特定值，要删除的值可能在列表中多次出现
此时需要借用循环语句来判断列表中的该元素是否全部被remove()方法删除了，第7章将继续学习
"""
