a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
c = int(input('Введите третье число:'))

union = (a, b, c)

for i in union:
    if i in range(1, 51):
        print(i)
