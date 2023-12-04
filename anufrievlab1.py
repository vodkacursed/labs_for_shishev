def task_1():
    numbers = input("Введите список чисел через пробел: ").split()
    number = int(input("Введите число: "))
    result = [int(x) for x in numbers if int(x) < number]
    print("Числа меньше", number, ":", result)

def task_2():
    string = input("Введите строку: ")
    if string == string[::-1]:
        print("Это палиндром")
    else:
        print("Это не палиндром")

def task_3():
    number = int(input("Введите число: "))
    if is_prime(number):
        print("Это простое число")
    else:
        print("Это не простое число")

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def task_4():
    array1 = input("Введите элементы первого массива через пробел: ").split()
    array2 = input("Введите элементы второго массива через пробел: ").split()
    result = list(set([int(x) for x in array1 if x in array2]))
    print("Элементы, которые входят в оба массива:", result)

while True:
    print("\nВыберите задачу:")
    print("1. Найти числа меньше заданного.")
    print("2. Проверить, является ли строка палиндромом.")
    print("3. Определить, является ли число простым.")
    print("4. Найти элементы, входящие в оба массива.")
    print("0. Выйти из программы.")

    choice = input("Введите номер задачи или 0 для выхода: ")

    if choice == '1':
        task_1()
    elif choice == '2':
        task_2()
    elif choice == '3':
        task_3()
    elif choice == '4':
        task_4()
    elif choice == '0':
        print("Программа завершена.")
        break
    else:
        print("Некорректный ввод. Попробуйте снова.")
