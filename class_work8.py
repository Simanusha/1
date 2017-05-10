dict_vocab_en_es = {
                    'world':'mundo', #ключ:значение
                    'language': 'idioma',
                    'See you later': 'Hasta la vista'
                    }

print (dict_vocab_en_es["world"])#только поиск по ключу, нельзя наоборот

capitals = {
            'United Kingdom':'London',
            'Ukraine':'Kiev',
            'Germany':'Berlin'
            }
print(capitals["United Kingdom"])

#consist = {
            #'Computer':['keyboard', 'monitor', 'mouse'],
            #'Phone':['sensor', 'microphone', 'sound']}
#print(consist["Phone"][2])

capitals['Georgia'] = 'Tbilisi' #добавление в список
print(capitals)
#del capitals['Georgia'] #удаление
#print(capitals)

#consist = {"Coca-Cola":["Fanta", "Sprite"]}#строка
#consist ['Coca-Cola'] = 'Fanta', 'Sprite'
#print(consist)
#consist ['Coca-Cola'].append ('Coca-Cola')#append к строке
#print(consist)


#if 'Georgia' in capitals:#проверять только в ключах
    #del capitals['Georgia']
#print(capitals)


# for key, value in capitals.items():#цикл, построчно перебор, каждая итерация-вывод ключа, значенияб пары
#     print("%s -> %s" % (key, value))


employee_1 = {"name":"Alex",  "salary": 10000, "dep": "Sales", "bonus":200}
employee_2 = {"name":"Nick", "salary": 20000, "dep": "Sales"}
employee_3 = {"name":"Sue",  "salary": 50000, "dep": "IT", "bonus":500}
employee_4 = {"name":"Phil", "salary": 5000,  "dep": "BoardOfDirectors", "bonus":10000}
#Добавление в словарь
employee_1 ["address"] = {"city":"Odessa", "street":"Deribas", "number":"12"}#:-словарь
employee_2 ["address"] = {"city":"Kiev", "street":"Stepovaya", "number":"26"}
employee_3 ["address"] = {"city":"Paris", "street":"la Fima", "number":"39"}
employee_4 ["address"] = {"city":"Koln", "street":"Bunde", "number":"58"}

# print(employee_1)
# print(employee_2)
# print(employee_3)
# print(employee_4)


s = {"London", "Paris"}
s1 = {"Paris", "Kiev"}
#print(s&s1)#амперсант- находит одинаковые значения

#print (employee_2.get("bonus", 100))

employees = [employee_1, employee_2, employee_3, employee_4]

salary = employee_1["salary"]# увеличиваем зарпалату в 1.5 раза
salary = salary*1.5
employee_1["salary"] = salary#вносим назад
#print(employee_1)
#employee_1["salary"] = employee_1["salary"]*1.5

#for employee in employees:
    #employee["salary"] = employee["salary"]*1.5
   # employee["salary"] *=1.5
#print(employees)

symbols = {code: chr(code) for code in range(10000+1)}
print(symbols)

for key in symbols:
    print("%s -> %s" % key(symbols, key) )
