# a = 10
# b = 2
#
# is_zero = b==0
#
# def is_zero (x):
#     return x==0
# if is_zero (b):
#     print ("Zero division error!")
# else:
#     result = a/b
#     print ("Result of a/b :", result)
#
#
# if b!=0:
#     result = a/b
#     print ("Result of a/b :", result)
# else:
#     print ("Zero division error")
#
# def is_zero(x):
#     return x==0
# def is_leap_year (year):
#     reminder = year %4
#     # return reminder == 0 можно делать так, чотбы не было тавтологии
#     # return not reminder %4
#     if reminder == 0:
#         return True
#     else:
#         return False
#
# print (is_leap_year(2017)) #является ли год высокостным(деление на 4)
#
#
# if is_zero (b):
#     print ("Zero division error!")
#  else:
#    result = a/b
#    print ("Result of a/b :", result)
#
# if not is_zero(b)
#  # if b!=0:
#     result = a/b
#     print ("Result of a/b :", result)
# else:
#      print ("Zero division error")


# word = " A word"
# c = word[0]
#
# if c=='a' or c=='A':
#     print ("Word starts with 'a' or 'A'")
# else:
#     print("Word doesn't start with 'a' or 'A'")

#
# x = 4
# y = 150
# # if x>=3 and x<=7 :
# if 3<= x <=7 or 100<= y <= 200:
#     print ("Inside")
# else:
#     print ("Outside")



print ("Привет, Богатырь!")
print ("1: > смерть найдёшь")
print ("2: > полцарства найдёшь")
print ("3: ^ коня потеряешь")
choice = int(input("Твой выбор [1...3]:"))

if choice == 1:
    print ("Сам виноват!")

elif choice == 2:
    print ("Bingo!")

elif choice ==3:
    print ("Лошадку жалко:(")

else:
# if choice <1 or choice > 3:
    print ("Учи матчасть!")



