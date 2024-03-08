s = input("Введите строку: ")
r_count = 0
words = s.split()
capital_s = ""
for word in words:
    if word:
        r_count += 1
        capital_s += word.capitalize() + " "

print("Преобразованная строка:", capital_s.strip())
print("Количество замен:", r_count)


