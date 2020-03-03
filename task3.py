lst = input("Введите элементы через пробел: ").split(' ')

steps = int(input("Введите значение для элементов: "))
def shift(lst, steps):
    if steps < 0:
        steps = abs(steps)
        for i in range(steps):
            lst.append(lst.pop(0))
    else:
        for i in range(steps):
            lst.insert(0, lst.pop())
    print(lst)

shift(lst, steps)
# print(lst)