# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

x = int(input('Введите число x: '))
y = int(input('Введите число y: '))
z = int(input('Введите число z: '))

print(not (x or y or z) == (not x and not y and not z))

