# x = 0
#
# while x <= 100:
#     if x%2==0:
#         print ("x=", x)
#     x = x + 1
#
# x = 0

# while x<=3000:
#     if x%4==0 and x%100!=0 or x%400==0:
#         print  ("x =", x)
#     x = x + 1
#
#
# sum = 0
# while x<=3:
#     print ("x =", x)
#     sum = sum + x
#     x = x + 1
#
#
# print ("Summa =", sum)


# sum = 0
# while x<=100:
#
#         print ("x =", x)
#         sum = sum + x
#         x = x + 2
#
# print ("Summa =", sum)

# Возведение в квадрат и сумма квадратов всех чисел в диапазоне 100-200
# sum = 0
# x = 100
# while x<=200:
#     print ("x**2 =", x**2)
#     sum = sum + x**2
#     x = x + 1
# print ("Summa = ", sum)

#
# for x in range (-100, 100, 2):
#     print ("x = ", x)
#
# for x in "Monthy Python":
#         print("x = ", x)
#
# for x in [1, 22, -13]:
#             print("x = ", x)

# x = 0
# while x<100:
#     print ("x =", x)
#     x = x + 1
#
# for x in range (0, 100): #чётко знаешь количесвто шагов
#     print ("x = ", x)
#
#
#
# for x in range (100, 201, 2):
#     print ("x = ", x)
#
# for x in range (100, 201):
#     if x%2 == 0:
#         print ("x = ", x)

s = "Plhdskjbskjbvsk, Kljsbnkjblbnjk"
total_lower_symbols = 0
total_UPPER_symbols = 0
total = 0
for c in s:
    if c.islower():
        print (c)
        total_lower_symbols = total_lower_symbols + 1
    if c.isupper():
        print (c)
        total_UPPER_symbols = total_UPPER_symbols + 1
    if c.isspace():
        print(c)
        total = total + 1
print("total_lower_symbols", total_lower_symbols)
print("total_UPPER_symbols", total_UPPER_symbols)
print("total", total)