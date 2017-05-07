group = [
('Александр Скворцов', '1,1,1,1,1,1,1,0,1,0,1,0,0,1,0,1,1,0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0'),
('Андрей Рожко', '1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0'),
('Алексей Кулишенко ', '0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0'),
('Виталий Рыжков', '1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0'),
('Виталина Гавеля ', '1,1,1,1,1,1,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0'),
('Виктор Бурлаков', '1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0'),
('Виктор Горовой', '1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,0,1,0,0,0,0,0,0,0,0,0,0,0'),
('Надежда Симанович', '1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0'),
('Николай Марушевский', '1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0'),
('Андрей Кравчук', '1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0'),
('Екатерина Шадрина ', '1,1,1,1,1,1,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0'),
('Александр Малышев', '1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0'),
('Владимир Веренчук', '0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0')
]

# def print_full_names(group):
#     for student in group:
#         print(student[0])


# def print_reverse_names(group):
#     for student in group:
#         full_name = student[0] #строка в стьюдент
#         lst_full_name = full_name.split()
#         first_name = lst_full_name[0]
#         second_name = lst_full_name[1]
#         # rank = student[1]
#         # print(student[0])
#         print (second_name + " " + first_name)


# def print_ranks(group):
#     for student in group:
#         full_name = student[0] #строка в стьюдент
#         rank = student[1]
#         lst_rank = rank.split(",")
#         rank_total = sum ([int(x) for x in lst_rank]) #преобразование строки в число, sum только для чисел
#         print (full_name, rank_total)

def sort_by_surname(elem):
    return elem.split()[1]

def print_full_names_sorted(group):
    #1.Создать новый пустой список
    list = []
    for student in group:
        full_name = student[0] #строка в стьюдент
        lst_full_name = full_name.split()
        first_name = lst_full_name[0]
        second_name = lst_full_name[1]
        full_name2 = second_name + " " + first_name
        #2.Добавить в него полное имя
        result_list = list.append(full_name)
        #3.Отсортировать
    list.sort(key=sort_by_surname) #сортировка по фамилиям, создать новую функцию(стр41)
    for name in list:
        print(name)


# def print_ranks(group):
#     pass
#
# def get_ranks_sorted(group):
#     pass
#
# def print_top_n(students_rank, n):
#     pass

# print_full_names(group)
# print_reverse_names(group)
# print_ranks(group)
print_full_names_sorted(group)


for idx, elem in enumerate([1,2,3]):
    print(idx, elem)

l = [1,2,3]
