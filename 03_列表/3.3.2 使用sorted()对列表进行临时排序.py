# 要保留原来的排序顺序，同时以特定的顺序呈现他们，可使用函数sorted()，从而达到不影响原来排序的目的
cars = ['BYD', 'BMW', 'Benz', 'Toyota']
print("Here is the original list: ")
print(cars)

print("\nHere is the sorted list: ")
print(sorted(cars))

print("\nHere is the original list: ")
print(cars)

# 如果要临时的相反排序，可向函数sorted()传递参数 reverse=Ture