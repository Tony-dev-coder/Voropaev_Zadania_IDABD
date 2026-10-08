def solve(a, b):
    if a == 0 and b == 0:
        return 'Any'
    elif a == 0 and b != 0:
        return 'Error'
    else:
        return b / a
a = int(input('Введите параметр a: '))
b = int(input('Введите параметр b: '))
print(solve(a,b))