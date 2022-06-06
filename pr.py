x = 5
y = 10
print(y > x * x or y >= 2 * x and x < y)
# Условия if else
# A = int(input("Время, которое рекомендовали спать"))
# B =  int(input("Время, которое является вредным для сна"))
# H = int(input("Сколько сейчас спите?"))
# if H>=A and H<B:
#     print("Это нормально")
# else:
#     if H>B:
#         print("Пересып")
#     else:
#         print("Недосып")

n = int(input())
if n%4!=0:
    print("Обычный")
else:
    if n%100==0:
        if n%400==0:
            print("Високосный")
        else:
            print("Обычный")

    else:
         print("Високосный")
