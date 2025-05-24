
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

def predict_commercial(account):
    consumption = account.get('consumption', {})
    monthly_consumptions = [v for k, v in sorted(consumption.items(), key=lambda x: int(x[0]))]
    
    # Проверка критериев для коммерческой недвижимости
    def is_commercial():
        # Шаг 1: Среднее потребление > 3000
        if monthly_consumptions:
            avg = sum(monthly_consumptions) / len(monthly_consumptions)
            if avg > 3000:
                return True

        # Шаг 2: Сезонные пики летом
        if len(monthly_consumptions) >= 8:
            summer_months = monthly_consumptions[5:8]  # июнь-август
            other_months = monthly_consumptions[:5] + monthly_consumptions[8:]
            if summer_months and other_months:
                summer_avg = sum(summer_months) / len(summer_months)
                other_avg = sum(other_months) / len(other_months)
                if summer_avg > 2 * other_avg:
                    return True

        # Шаг 3: Тип объекта
        if account.get('buildingType') in ['Прочий', 'Гараж', 'Многоквартирный']:
            return True

        # Шаг 4: Соотношение комнат и жильцов
        rooms = account.get('roomsCount', 0)
        residents = account.get('residentsCount', 0)
        if rooms >= 5 and residents <= 2:
            return True

        # Шаг 5: Аномалии потребления
        for i in range(1, len(monthly_consumptions)):
            prev = monthly_consumptions[i-1]
            curr = monthly_consumptions[i]
            if prev > 0 and (abs(curr - prev)/prev) > 5:  # 500%
                return True

        return False

    # Проверка критериев для жилой недвижимости
    def is_residential():
        # Шаг 1: Среднее потребление < 1500 (обновленный порог)
        if not monthly_consumptions:
            return False
        avg = sum(monthly_consumptions) / len(monthly_consumptions)
        if avg >= 1500:
            return False

        # Шаг 2: Стабильность потребления
        max_cons = max(monthly_consumptions)
        min_cons = min(monthly_consumptions)
        if min_cons == 0 or max_cons / min_cons > 1.5:
            return False

        # Шаг 3: Тип объекта
        if account.get('buildingType') != 'Частный':
            return False

        # Шаг 4: Соотношение жильцов
        rooms = account.get('roomsCount', 0)
        residents = account.get('residentsCount', 0)
        if rooms > 3 or residents < 3:
            return False

        # Шаг 5: Отсутствие аномалий
        for i in range(1, len(monthly_consumptions)):
            prev = monthly_consumptions[i-1]
            curr = monthly_consumptions[i]
            if curr == 0 or (prev > 0 and (abs(curr - prev)/prev) > 5):
                return False

        # Дополнительная проверка на большую площадь
        if account.get('totalArea', 0) > 500:
            return False

        return True

    # Итоговое решение
    if is_commercial():
        return "commercial"
    return "commercial" if not is_residential() else "non-commercial"


def predict_commercial(account):
    consumption = account.get('consumption', {})
    monthly_consumptions = [v for k, v in sorted(consumption.items(), key=lambda x: int(x[0]))]
    
    # Проверка критериев для коммерческой недвижимости
    def is_commercial():
        # Шаг 1: Среднее потребление > 3000
        if monthly_consumptions:
            avg = sum(monthly_consumptions) / len(monthly_consumptions)
            if avg > 3000:
                return True

        # Шаг 2: Сезонные пики летом
        if len(monthly_consumptions) >= 8:
            summer_months = monthly_consumptions[5:8]  # июнь-август
            other_months = monthly_consumptions[:5] + monthly_consumptions[8:]
            if summer_months and other_months:
                summer_avg = sum(summer_months) / len(summer_months)
                other_avg = sum(other_months) / len(other_months)
                if summer_avg > 2 * other_avg:
                    return True

        # Шаг 3: Тип объекта
        if account.get('buildingType') in ['Прочий', 'Гараж', 'Многоквартирный']:
            return True

        # Шаг 4: Соотношение комнат и жильцов
        rooms = account.get('roomsCount', 0)
        residents = account.get('residentsCount', 0)
        if rooms >= 5 and residents <= 2:
            return True

        # Шаг 5: Аномалии потребления
        for i in range(1, len(monthly_consumptions)):
            prev = monthly_consumptions[i-1]
            curr = monthly_consumptions[i]
            if prev > 0 and (abs(curr - prev)/prev) > 5:  # 500%
                return True

        return False
    

    # Проверка критериев для жилой недвижимости
    def is_residential():
        # Шаг 1: Среднее потребление < 1500 (обновленный порог)
        if not monthly_consumptions:
            return False
        avg = sum(monthly_consumptions) / len(monthly_consumptions)
        if avg >= 1500:
            return False

        # Шаг 2: Стабильность потребления
        max_cons = max(monthly_consumptions)
        min_cons = min(monthly_consumptions)
        if min_cons == 0 or max_cons / min_cons > 1.5:
            return False

        # Шаг 3: Тип объекта
        if account.get('buildingType') != 'Частный':
            return False

        # Шаг 4: Соотношение жильцов
        rooms = account.get('roomsCount', 0)
        residents = account.get('residentsCount', 0)
        if rooms > 3 or residents < 3:
            return False

        # Шаг 5: Отсутствие аномалий
        for i in range(1, len(monthly_consumptions)):
            prev = monthly_consumptions[i-1]
            curr = monthly_consumptions[i]
            if curr == 0 or (prev > 0 and (abs(curr - prev)/prev) > 5):
                return False

        # Дополнительная проверка на большую площадь
        if account.get('totalArea', 0) > 500:
            return False

        return True

    # Итоговое решение
    if is_commercial():
        return "commercial"
    return "commercial" if not is_residential() else "non-commercial"

def predict_commercial(account):
    consumption = account.get('consumption', {})
    monthly_consumptions = [v for k, v in sorted(consumption.items(), key=lambda x: int(x[0]))]
    
    # Проверка критериев для коммерческой недвижимости
    def is_commercial():
        # Шаг 1: Среднее потребление > 3000
        if monthly_consumptions:
            avg = sum(monthly_consumptions) / len(monthly_consumptions)
            if avg > 3000:
                return True

        # Шаг 2: Сезонные пики летом
        if len(monthly_consumptions) >= 8:
            summer_months = monthly_consumptions[5:8]  # июнь-август
            other_months = monthly_consumptions[:5] + monthly_consumptions[8:]
            if summer_months and other_months:
                summer_avg = sum(summer_months) / len(summer_months)
                other_avg = sum(other_months) / len(other_months)
                if summer_avg > 2 * other_avg:
                    return True

        # Шаг 3: Тип объекта
        if account.get('buildingType') in ['Прочий', 'Гараж', 'Многоквартирный']:
            return True

        # Шаг 4: Соотношение комнат и жильцов
        rooms = account.get('roomsCount', 0)
        residents = account.get('residentsCount', 0)
        if rooms >= 5 and residents <= 2:
            return True

        # Шаг 5: Аномалии потребления
        for i in range(1, len(monthly_consumptions)):
            prev = monthly_consumptions[i-1]
            curr = monthly_consumptions[i]
            if prev > 0 and (abs(curr - prev)/prev) > 5:  # 500%
                return True

        return False

    # Проверка критериев для жилой недвижимости
    def is_residential():
        # Шаг 1: Среднее потребление < 1500 (обновленный порог)
        if not monthly_consumptions:
            return False
        avg = sum(monthly_consumptions) / len(monthly_consumptions)
        if avg >= 1500:
            return False

        # Шаг 2: Стабильность потребления
        max_cons = max(monthly_consumptions)
        min_cons = min(monthly_consumptions)
        if min_cons == 0 or max_cons / min_cons > 1.5:
            return False

        # Шаг 3: Тип объекта
        if account.get('buildingType') != 'Частный':
            return False

        # Шаг 4: Соотношение жильцов
        rooms = account.get('roomsCount', 0)
        residents = account.get('residentsCount', 0)
        if rooms > 3 or residents < 3:
            return False

        # Шаг 5: Отсутствие аномалий
        for i in range(1, len(monthly_consumptions)):
            prev = monthly_consumptions[i-1]
            curr = monthly_consumptions[i]
            if curr == 0 or (prev > 0 and (abs(curr - prev)/prev) > 5):
                return False

        # Дополнительная проверка на большую площадь
        if account.get('totalArea', 0) > 500:
            return False

        return True

    # Итоговое решение
    if is_commercial():
        return "commercial"
    return "commercial" if not is_residential() else "non-commercial"