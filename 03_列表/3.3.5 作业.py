# 3-8 5个渴望旅游的地方，条件如下：

visit_list = ['Tokyo', 'Kyoto', 'Osaka', 'Hokkaido', 'Sendai']

print(visit_list)               # 直接打印

print(sorted(visit_list))       # 使用sorted()按准许打印且不破坏顺序
print(visit_list)               # 再次打印核实顺序没发生变化

print(sorted(visit_list, reverse=True))  # 使用sorted按字母相反顺序打印且不破坏顺序
print(visit_list)               # 再次打印核实顺序没发生变化

visit_list.reverse()            # 使用reverse()修改原列表顺序
print(visit_list)

visit_list.reverse()            # 再次使用reverse()修改原列表顺序
print(visit_list)

visit_list.sort()               # 使用sort()永久修改列表按首字母顺序排列
print(visit_list)

visit_list.sort(reverse=True)   # 使用sort()永久修改列表按首字母相反顺序排列
print(visit_list)

# 3-9 len()应用
print(len(visit_list))