# 创作的绝大多数列表都是动态的，意味着列表创建后，将随着系统运行增删元素
# 例如，创作一个外星人射击游戏，被射杀的外星人移出列表，也有新外星人不断加入
# 修改列表元素与访问

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

# 轶可修改列表的任意位置