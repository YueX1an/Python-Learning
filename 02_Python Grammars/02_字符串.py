# 字符串是一系列字符，可以用单引号或者多引号
# 修改字符串的大小写
name = "ada lovelace"
print(name.title())
"""
方法title()出现在变量后面，name后的.让python对变量name执行方法title()指定的操作。每个方法后面都跟有一对()
title()作用是将首字母大写
"""
# 将所有字母大写或小写
name = "ada lovelace"
print(name.upper()) # 大写
print(name.lower()) # 小写



# 合并拼接字符串
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
print(full_name)
message = "hello," + " " + full_name.title() + "!"
print(message)
# python用“加号”来合并字符串



# 使用制表符\t或换行符\n来添加空白
print("python")
print("\tpython")
print("\npython")
print("languages:\nPython\nC\nJavaScript")
print("languages:\n\tPython\n\tC\n\tJavaScript")



# 删除空白 rstrip()，但只是一个操作
favorite_language = 'python '
print(favorite_language)
print(favorite_language.rstrip())
# 要永久删除空白，必须将删除操作的结果存回变量
favorite_language = 'python '
favorite_language = favorite_language.rstrip()
print(favorite_language)



# 使用字符串避免语法错误
"""
如在用单引号括起的变量中又包含单引号，就会导致错误
"""
message = "One of Python's strengths is its diverse community."
print(message)
# 单引号在双引号内部，Python可以正确理解字符串
"""
message = 'One of Python's strengths is its diverse community.'
print(message)     # 出现了三个单引号,所以报错
"""