users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений
students = {
    "Общее количество": 0,
    "Уникальные посещения": 0
}
kol = len(users)
unique =len(set(users))
students["Общее количество"] = kol
students["Уникальные посещения"] = unique
print(students)