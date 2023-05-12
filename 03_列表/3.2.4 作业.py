# 3-4 嘉宾名单：邀请任何人一起共进晚餐（无论在世还是离世的），会邀请哪些人，创建一个列表，邀请这些人来晚餐
dinner_list = ['Dongju', 'Guy', 'Jonny', 'Jihua']
print("Hi " + dinner_list[0] + ", " + "I want to invite you to have dinner with me.")
print("Hi " + dinner_list[1] + ", " + "I want to invite you to have dinner with me.")
print("Hi " + dinner_list[2] + ", " + "I want to invite you to have dinner with me.")
print("Hi " + dinner_list[3] + ", " + "I want to invite you to have dinner with me.")

# 3-5 修改介宾名单：得知一位嘉宾来不了，需要邀请另一位
dinner_list = ['Dongju', 'Guy', 'Jonny', 'Jihua']
print(dinner_list[3] + " don't come.")
dinner_list[3] = 'Yifan'
print("Hi " + dinner_list[0] + ", " + "I want to invite you to have dinner with me.")
print("Hi " + dinner_list[1] + ", " + "I want to invite you to have dinner with me.")
print("Hi " + dinner_list[2] + ", " + "I want to invite you to have dinner with me.")
print("Hi " + dinner_list[3] + ", " + "I want to invite you to have dinner with me.")

# 3-6 添加嘉宾，想想还想邀请的三个嘉宾
dinner_list = ['Dongju', 'Guy', 'Jonny', 'Yifan']
dinner_list.insert(0, 'jack')
dinner_list.insert(5, 'David')
dinner_list.append('Jon')
print(dinner_list)

# 3-7 缩减名单：得知新购买的餐桌无法及时送达

print("I can only invite two person to have dinner")
popped_dinner_list = dinner_list.pop()
print("Sorry " + popped_dinner_list + ".")
popped_dinner_list = dinner_list.pop()
print("Sorry " + popped_dinner_list + ".")
popped_dinner_list = dinner_list.pop()
print("Sorry " + popped_dinner_list + ".")
popped_dinner_list = dinner_list.pop()
print("Sorry " + popped_dinner_list + ".")
popped_dinner_list = dinner_list.pop()
print("Sorry " + popped_dinner_list + ".")
print(dinner_list[0] + " you are still in my list.")
print(dinner_list[1] + " you are still in my list.")
del dinner_list[0]
del dinner_list[0]
print(dinner_list)


