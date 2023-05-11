# 在python中，第一个列表元素的索引为0，而不是1
# 大多数编程语言都是如此

bicycles = ['trek', 'cannon dale', 'redline', 'specialized']
print(bicycles[1])
print(bicycles[3])
# 运行结果 cannon dale, specialized 返回的是第二个和第四个

# Python为最后一个列表元素提供了特殊语法，索引指定为-1
print(bicycles[-1])
# 返回结果为 specialized
# -2为倒数第二个，以此类推

