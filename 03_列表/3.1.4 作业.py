# 3-1 打印每个朋友的名字
name = ['David', 'Jane', 'Alice']
message = "My friends are " + name[0].title() + ", " +name[1].title() + " and " + name[-1].title() + "."
print(message)
# My friends are David, Jane and Alice.

# 3-2 问候语
greeting1 = "hello " + name[0].title() + "."
greeting2 = "hello " + name[1].title() + "."
greeting3 = "hello " + name[2].title() + "."
print(greeting1)
print(greeting2)
print(greeting3)

# 3-3 交通出行偏爱方式
transportations = ['subway', 'bus', 'walk', 'bike']
message1 = "When I catch my time, I choose to go school by " + transportations[0].title() + ", " + "but if I have enough time, I choose to go school by " + transportations[-1].title() + "."
print(message1)
# When I catch my time, I choose to go school by Subway, but if I have enough time, I choose to go school by Bike.