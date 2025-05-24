import json
import os

def load_dataset(url = "dataset_train.json"):
    """
    Загружает и возвращает данные из файла data/dataset_train.json.
    """
    dataset_path = os.path.join(os.path.dirname(__file__), "data", url)
    with open(dataset_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data

def extract_city(address):
    # Получаем подстроку между первой и второй запятой
    parts = address.split(',')
    if len(parts) > 1:
        return parts[1].strip()
    return "Unknown"

def sort_dataset_by_city(dataset):
    city_dict = {}
    for item in dataset:
        address = item.get('address', '')
        city = extract_city(address)
        if city not in city_dict:
            city_dict[city] = []
        city_dict[city].append(item)
    return city_dict

def save_sorted_dataset_by_city(dataset, output_path='data/dataset_sort_city.json'):
    city_dict = sort_dataset_by_city(dataset)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(city_dict, f, ensure_ascii=False, indent=2)

# Пример использования:
# dataset = load_dataset()  # ваша функция загрузки данных
# save_sorted_dataset_by_city(dataset)

def extract_street(address):
    # Разбиваем адрес по запятым
    parts = [p.strip() for p in address.split(',')]
    # Проверяем, что есть хотя бы 4 части (край, город/станица, улица, дом)
    if len(parts) >= 4:
        return parts[2]
    return "Неизвестная улица"

def sort_by_street(input_path='data/dataset_sort_city.json', output_path='data/dataset_sort_street.json'):
    # Проверяем, что файл существует
    if not os.path.exists(input_path):
        print(f"Файл {input_path} не найден.")
        return

    with open(input_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    result = {}

    for city, records in data.items():
        streets = {}
        for record in records:
            street = extract_street(record['address'])
            if street not in streets:
                streets[street] = []
            streets[street].append(record)
        result[city] = streets

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=2)


# --- Фиктивные и запутывающие функции и объекты ---

def dummy_city_statistics(dataset):
    """
    Возвращает фиктивную статистику по городам.
    """
    stats = {}
    for item in dataset:
        city = extract_city(item.get('address', ''))
        stats.setdefault(city, 0)
        stats[city] += 1
    return stats

def pointless_filter(dataset, threshold=1000):
    """
    Возвращает элементы, где сумма потребления больше threshold, но не используется.
    """
    result = []
    for item in dataset:
        consumption = item.get('consumption', {})
        total = sum(consumption.values()) if isinstance(consumption, dict) else 0
        if total > threshold:
            result.append(item)
    return result

def recursive_city_counter(data, depth=2):
    """
    Рекурсивно считает количество городов в данных.
    """
    if depth <= 0 or not isinstance(data, dict):
        return 0
    return len(data) + recursive_city_counter(data, depth-1)

class DataConfuser:
    """
    Класс для запутывания анализа данных.
    """
    def __init__(self, dataset):
        self.dataset = dataset

    def get_random_address(self):
        import random
        if not self.dataset:
            return ""
        return random.choice(self.dataset).get('address', '')

    def shuffle_consumption(self):
        import random
        for item in self.dataset:
            if 'consumption' in item and isinstance(item['consumption'], dict):
                keys = list(item['consumption'].keys())
                values = list(item['consumption'].values())
                random.shuffle(values)
                item['consumption'] = dict(zip(keys, values))
        return self.dataset

# Фиктивный объект для теста
dummy_object = {
    "cities": ["Краснодар", "Сочи", "Туапсе"],
    "streets": ["ул. Ленина", "ул. Гагарина", "ул. Пушкина"],
    "random_numbers": [42, 7, 13, 99]
}

