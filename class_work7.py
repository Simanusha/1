# def do_action (f, a, b, c):
#     return f( a, b, c)
#
# def add(a, b):
#     return a+b
#
# def mult(a, b):
#     return a*b
#
# print (do_action(mult, 2, 3))


# lst = ['aaaz', 'bb', 'ccc', 'd']
# def reversed_sort(elem):
#     return elem
#     lst = lst.sort(key=reversed_sort)
#     print (lst)



# dist = [2,4,7,8,4,11,10,12] сортировка относительно 9
# my_position = 9
#
# def diff_dist(elem):
#     return abs(elem - my_position)
# dist.sort(key = diff_dist)
# print (dist)

#сортировка по фимилии
# s = ['Александр Малышев', 'Александр Скворцов', 'Алексей Кулишенко', 'Андрей Кравчук', 'Андрей Рожко', 'Виктор Бурлаков', 'Виктор Горовой', 'Виталий Рыжков', 'Виталина Гавеля', 'Владимир Веренчук', 'Екатерина Шадрина', 'Надежда Симанович', 'Николай Марушевский']
#
# def surname_sort(elem):
#     return elem.split()[1] + "" + elem.split()[0]   #[::-1]
# s.sort (key = surname_sort)
# print (s)


# table = [[1,2,3], [4,5,6], [7,8,9]]
#         #[1,2,3,4,5,6,7,8,9],  #таблица умножения
#          #[1,2,3,4,5,6,7,8,9],
#          #[1,2,3,4,5,6,7,8,9]]
#
# def print_table(table):
#     for line in table:
#         for elem in line:
#             print(elem, end=" ")
#         print()
#
#     table [0][1] = 42
#     print(table)
#
# def fill_random_table(table):
#     import random
#     for idx1, line in enumerate(table):
#         for idx2, elem in enumerate(line):
#             table[idx1] [idx2] = random.randint(1,50)  #можем записать любое значение
# print_table(table)
# fill_random_table(table)
# print_table(table)

#прямая таблица
# table =[[0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0]
#         ]
#
# def print_table(table):
#     for line in table:
#         for elem in line:
#             print(elem, end="\t")
#         print()
#
#
# def fill_random_table(table):
#     import random
#     for idx1, line in enumerate(table):
#         for idx2, elem in enumerate(line):
#             table[idx1][idx2] = (idx1+1)*(idx2+1)
#
# def fill_piphagor_table_reversed(table):
#     import random
#     for idx1, line in enumerate(table):
#         for idx2, elem in enumerate(line):
#             table[idx1][idx2] = (idx1 + 1) * (idx2 + 1)
#
# print_table(table)
# fill_random_table(table)
# print_table(table)
#
# # обратная таблица
# table =[[0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0]
#         ]
#
# def print_table(table):
#     for line in table:
#         for elem in line:
#             print(elem, end="\t")
#         print()
#
#
# def fill_random_table(table):
#     import random
#     for idx1, line in enumerate(table):
#         for idx2, elem in enumerate(line):
#             table[idx1][idx2] = (idx1+1)*(idx2+1)
#
# def fill_piphagor_table_reversed(table):
#     import random
#     for idx1, line in enumerate(table):
#         for idx2, elem in enumerate(line):
#             table[idx1][idx2] = (len(line)-idx1)*(len(line)-idx2)
#
# print_table(table)
# print()
# fill_random_table(table)
# print()
# fill_piphagor_table_reversed(table)
# print()
# print_table(table)


# table = [[0 for i in range(10)] for j in range(10)] #нет связи между внутр циклами
# table[0][0] = 42
# print(table)


#кортежи
# def foo():
#     return 1, 2
#
# a, b = foo()
# print(a)
# print(b)

# def foo(*args):
#     print(type(args))  #tuple
#     print(args)
# foo = 1,2,3
# print (foo)


