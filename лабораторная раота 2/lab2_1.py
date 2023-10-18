money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
budget=money_capital+salary
k=0
while budget>=spend:
    budget = budget - spend
    spend+=increase*spend
    k+=1
    budget+=salary
print("Количество месяцев, которое можно протянуть без долгов:", k)
