# TODO решите задачу
import json

def task() -> float:

    json_file_path = 'input.json'

    total_sum = 0.0 # Переменная для суммы

    with open(json_file_path, 'r') as file:
        data = json.load(file) # Чтение данных из файла


    for item in data:
        score = item.get("score", 0)
        weight = item.get("weight", 0)
        total_sum += score * weight  # Считаем произведение и добавляем к общей сумме


    return round(total_sum, 3) # сумма, округленная до 3 знаков после запятой


print(task())
