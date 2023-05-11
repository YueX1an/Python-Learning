# 可使用其他变量一样使用列表中的各个值

bicycle = ['trek', 'cannon dale', 'redline', 'specialized']
message = "My first bike was a " + bicycle[0].title() + "."
print(message)

# 返回结果为 My first bike was a Trek.
# 我们使用 bicycle[0] 的值生成了一个句子，并将其存储在变量message中
# 输出的是一个简单的句子