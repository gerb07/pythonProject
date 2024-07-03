first = input('введите любое первое число:')
second = input('введите второе любое число:')
third = input('введите любое третье число:')

if first == second and third == second:
    print(3)
elif first == second or second == third or third == first:
    print(2)
else:
    print(0)

