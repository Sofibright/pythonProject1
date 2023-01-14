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

# n = int(input())
# if n%4!=0:
#     print("Обычный")
# else:
#     if n%100==0:
#         if n%400==0:
#             print("Високосный")
#         else:
#             print("Обычный")
#
#     else:
#          print("Високосный")

# import math
# a = int(input())
# b = int(input())
# c = int(input())
# p = ((a+b+c)/2)
# S = math.sqrt(p*(p-a)*(p-b)*(p-c))
# print(S)


# a = int(input())
# if a>-15 and a<= 12:
#     print("True")
# else:
#     if (a>=14 and a<=17):
#         print("True")
#     else:
#         if a>19:
#             print("True")
#         else:
#             print("False")
# i = 0
# while i <= 10:
#     i = i + 1
#     if i > 7:
#         i = i + 2
#         print(i)

# a = int(input())
# s = 0
# while a != 0:
#     s += a
#     a = int(input())
# print(s)


# aa = int(input())
# bb = int(input())
# a = aa
# b = bb
#
# if b > a:
#     a, b = b, a
# while a % b != 0:
#     r = a % b
#     d = a // b
#     a = b
#     b = r
# t = aa * bb // b
# print(t)


# while True:
#     i = int(input())
#     if i < 10:
#         continue
#     if i > 100:
#         break
#     print(i)

# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())

# for i in range(c, d + 1):
#     print(i, end="\t")
# print()
#
# for i in range(c, d + 1):
#     print(j)
#     for j in range(a, b+1):
#
#         print(j*i, end="\t")
#     print()

# for i in range(a, b + 1):
#     print(i, end="\t")
# print()
# for i in range(a, b + 1):
#     print(i)
#     for j in range(c, d+1):
#         print(j)
#         print(j*i, end="\t")
#     print()

# s = 'abcdefghijk'
# res = s[3:6]
# res = s[:6]
# res = s[3:]
# res = s[::-1]
# res = s[-3:]
# res = s[:-6]
# res = s[-1:-10:-2]

s = input()
