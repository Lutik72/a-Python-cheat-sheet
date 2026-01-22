# САМОСТОЯТЕЛЬНАЯ РАБОТА 1
# №2
# print("Введите трехзначное число")
# num = int(input())
# digit3 = num % 10
# digit2 = (num % 100) // 10
# digit1 = num // 100
# summ = digit1 + digit2 + digit3
# print("Сумма чисел =", summ)
# ---
# №4
# print("Введите общее количество журавликов")
# s = int(input())
# petya = s/6
# sergey = petya
# katya = (petya + sergey) * 2
# print("Маша сделала", katya, "журавликов")
# print("Петя сделал", petya, "журавликов")
# print("Сережа сделал", sergey, "журавликов")
# ---
# №6. Счастливый билет
# print("Введите номер билета")
# n = int(input())
# digit1 = n // 100000
# digit2 = (n % 100000) // 10000
# digit3 = (n % 10000) // 1000

# digit4 = (n % 1000) // 100
# digit5 = (n % 100) // 10
# digit6 = n % 10

# if 99999 < n <= 999999:
#     if digit1 + digit2 + digit3 == digit4 + digit5 + digit6:
#         print("Ваш билет счастливый :)")
#     else:
#         print("Увы :(")
# else:
#     print("некорректный номер билета")
# ---
# №8.Дольки шоколадки
# n, m, k = int(input()), int(input()), int(input())

# if k < n * m:

#     if k % m == 0:
#         print("YES")
#     elif k % n == 0:
#         print("YES")
#     else:
#         print("NO")
# else:
#     print("NO")
