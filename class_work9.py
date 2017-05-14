dict_planets = {'earth': 345778, 'mars': 47789, 'venus': 4679339}
dict_planets_2 = {'earth': (345778, 894202), 'saturn': (98097007, 7897608), 'mars': (47789, 898902), 'venus': (4679339, 238000)}

employee_1 = {"name":"Alex",  "salary": 10000, "dep": "Sales", "bonus":200}
employee_2 = {"name":"Nick", "salary": 20000, "dep": "Sales"}
employee_3 = {"name":"Sue",  "salary": 50000, "dep": "IT", "bonus":500}
employee_4 = {"name":"Phil", "salary": 5000,  "dep": "BoardOfDirectors", "bonus":10000}
employees = [employee_1, employee_2, employee_3, employee_4]

# def get_value_by_key(key):
#     return dict_planets[key]
#
# for key in sorted(dict_planets, key = get_value_by_key):
#     print (key, "->", dict_planets)
#
# for key in sorted(dict_planets.keys(), key = dict_planets.get):
#     print (key, "->", dict_planets)


dict_vocab_en_es = {
                    'world':'mundo',
                    'language': 'idioma',
                    'see you later': 'hasta la vista'
                    }

# def get_word_by_key(key):
#     return dict_vocab_en_es[key]

# # for key in sorted(dict_vocab_en_es,key =get_word_by_key):
# #     print(key, "->", dict_vocab_en_es)
#
# for key in sorted(dict_vocab_en_es.keys(),key =dict_vocab_en_es.get):
#     print(key, "->", dict_vocab_en_es)



# def get_value_by_key(key):
#     return dict_planets_2[key]

# for key in sorted(dict_planets_2.keys(), key = dict_planets_2.get):
#     print(key, "->", dict_planets_2[key])
#

# for key in sorted(dict_planets_2.keys(), reverse = True):
#     print(key, "->", dict_planets_2[key])


# for key in sorted(dict_vocab_en_es.keys(), reverse = True):
#      print(key, "->", dict_vocab_en_es[key])

# for key in sorted(dict_vocab_en_es.keys(), key = dict_vocab_en_es.get, reverse=True):#ортировка по значению
#     print(key, "->", dict_vocab_en_es[key])

# for key in sorted(dict_planets.keys(), key = dict_planets.get, reverse=True):#ортировка по значению
#     print(key, "->", dict_planets[key])
#
# for key in sorted(dict_planets.keys(), key = dict_planets.get):#ортировка по значению
#     print(key, "->", dict_planets[key])


# for key in sorted(employees.keys([1]), key = employees.get):#ортировка по значению
#     print(key, "->", employees[key])



# f = open("D:\\test4242.txt", mode = "w")
# f.write("abc")
# f.close()
#
#
# f = open(r"D:\\test4242.txt", mode = "r")#r-трактовка как строки
# s = f.read()
# print(s)
# f.close()
#
# f = open("D:\\test4242.txt", mode = "a")
# s = f.write("ghbdtn")
# print(s)
# f.close()

# d = {}
# f = open("D:\\war_peace.txt", mode = "r")
# s = f.read().lower()
#
#
# # print(s[:100])
#
# for c in s:
#     if ord(c) in range(ord("а"), ord("я")+1):
#         if c in d:
#             d[c] += 1
#         else:
#             d[c] = 1
# # print(d)
# for key in sorted(d.keys(),key = d.get, reverse= True):
#     normalized_length = int(d[key]/5000)
#     print("%s -> \t%s:\t%s" %(key, d[key], normalized_length*"*"))
# f.close()


# dict_planets = {'earth': 345778, 'mars': 47789, 'venus': 4679339}
# dict_planets_2 = {'earth': (345778, 894202), 'saturn': (98097007, 7897608), 'mars': (47789, 898902), 'venus': (4679339, 238000)}
#
# def get_value_by_key(key):
#    return dict_planets_2[key][1]#сортировка по второму значению в в значении
#
# for key in sorted(dict_planets_2.keys(), key = dict_planets_2.get):
#     print(key, "->", dict_planets_2[key])

def foo(dict):
    # print (dict)
    return dict['salary']
for elem in sorted(employees, key = foo):
    print(elem["name"], elem["salary"])


# def foo(dict):
#     # print (dict)
#     return dict['dep']
# print ("Before:", employees)
# employees.sort(key=foo, reverse = True)
# print ("After:", employees)
#
# for elem in sorted(employees, key=foo):
#     print(elem["name"],":", elem["dep"])

#по бонусу, у ника нет бонуса = 0
# def foo(dict):
#     return dict.get('bonus', 0)#функция гэт-()
# print ("Before:", employees)
employees.sort(key=lambda dict: dict.get('bonus', 0), reverse = True)
print ("After:", employees)

# lambda dict: dict.get('bonus', 0)

