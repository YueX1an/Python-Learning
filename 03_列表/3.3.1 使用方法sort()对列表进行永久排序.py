# 假设有一个汽车列表，需要按照首字母排序
# 方法sort()永久秀嘎了列表元素的排列方式，无法恢复
cars = ['BYD', 'BMW', 'Benz', 'Toyota']
cars.sort()
print(cars)

# 还可以按与首字母相反的顺序排列，向sort()方法传递参数reverse=Ture
cars = ['BYD', 'BMW', 'Benz', 'Toyota']
cars.sort(reverse=True)
print(cars)


