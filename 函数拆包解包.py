def func1(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

print(func1(1, 2, 3, 4))

# res = [1, 2, 3, 4]
# print(func1(*res))


def func2(a, b, c):
    print(a, b, c)


z = {'a': 7, 'b': 8, 'c': 9}  # 字典数据
func2(**z)  # 字典解包  通过 **对字典进行解包


def func3(**args):
    for key, value in args.items():
        print(key, value)


func3(**z)
func3(**{'a': 7, 'b': 8, 'c': 9})

def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)


person('Michael', 30)
person('Adam', 45, gender='M', job='Engineer')

