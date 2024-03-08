import sys

args = sys.argv[1:]

if len(args) == 0:
    print("Пожалуйста, укажите элементы массива в качестве аргументов командной строки.")
    sys.exit(1)

try:
    array = [int(x) for x in args]
except:
    print("Ошибка: Все элементы массива должны быть целыми числами.")
    sys.exit(1)

double = []

for i, num in enumerate(array):
    if num in array[i+1:] and num not in double:
        double.append(num)

if double:
    print("Повторяющиеся элементы:", double)
else:
    print("Повторяющихся элементов нет.")

new_array = [0 if num < 10 else 1 if num > 20 else num for num in array]

print("Исходный массив:", array)
print("Преобразованный массив:", new_array)
