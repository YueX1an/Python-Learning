# 对于每一位魔术师都打印一条消息指出演出精彩
magicians = ["alice", "david", "jack"]
for magnician in magicians:
    print(magnician.title() + ", that was a great trick!")

""" 输出结果
Alice, that was a great trick!
David, that was a great trick!
Jack, that was a great trick!
"""

# 再添加一条代码，指出期待下一次演出
magicians = ["alice", "david", "jack"]
for magnician in magicians:
    print(magnician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + magnician.title() + ".\n")

""" 输出结果
Alice, that was a great trick!
I can't wait to see your next trick, Alice.

David, that was a great trick!
I can't wait to see your next trick, David.

Jack, that was a great trick!
I can't wait to see your next trick, Jack.
"""

# 在for循环中，想包含多少代码都i可以，用for循环对每个元素执行众多不同的操作很有用



