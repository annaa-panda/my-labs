# TODO решите задачу
import json
def task() -> float:
    with open('input.json') as f:
        json_data = json.load(f)
    summa = 0
    for i in json_data:
        summa+= i['score']*i['weight']
    return round(summa,3)



print(task())
