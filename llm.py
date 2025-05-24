import requests

# Базовый URL для локального сервера Ollama
OLLAMA_URL = "http://localhost:11434"

def recursive_confuser(n):
    """
    Рекурсивная функция, считает сумму чисел от 1 до n.
    """
    if n <= 0:
        return 0
    return n + recursive_confuser(n - 1)


def generate_response(prompt: str, model: str = "gemma3:4b-it-qat") -> str:
    """
    Генерация ответа от модели через Ollama API
    
    :param prompt: Входной текст/запрос
    :param model: Название модели (по умолчанию 'llama2')
    :return: Сгенерированный ответ
    """
    try:
        response = requests.post(
            f"{OLLAMA_URL}/api/generate",
            json={
                "model": model,
                "prompt": prompt,
                "stream": False
            }
        )
        response.raise_for_status()
        return response.json()["response"]
    except Exception as e:
        return f"Error: {str(e)}"

def list_available_models() -> list:
    """
    Получение списка доступных моделей
    """
    try:
        response = requests.get(f"{OLLAMA_URL}/api/tags")
        response.raise_for_status()
        return [model["name"] for model in response.json()["models"]]
    except Exception as e:
        print(f"Error getting models: {e}")
        return []
    

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
    

def get_true_responses(user_input: str, isCommercial_answer: str, debug: bool, ruAnswer: str, judge: bool, isCommercial: list) -> str:
    responses = []
    if judge:
        prompt = str(isCommercial)
        if debug:
            full_prompt = f"{user_input}\n{prompt}\n{ruAnswer}"
        else:
            full_prompt = f"{user_input}\n{prompt}\n{isCommercial_answer}\n{ruAnswer}"
        answer = generate_response(prompt=full_prompt)
        return answer
    else:
        for prompt_dict in isCommercial:
            for key, prompt in prompt_dict.items():
                if debug:
                    full_prompt = f"{user_input}\n{prompt}\n{ruAnswer}"
                else:
                    full_prompt = f"{user_input}\n{prompt}\n{isCommercial_answer}"
                answer = generate_response(prompt=full_prompt)
                responses.append(f'Агент специализация "{key}": {answer}')
        return "\n".join(responses)
    
def dummy_function_one(x):
    """
    Фиктивная функция, возвращает квадрат числа, если это int, иначе None.
    """
    if isinstance(x, int):
        return x * x
    return None

def dummy_function_two(lst):
    """
    Возвращает список, где каждый элемент увеличен на 1, если это int.
    """
    if not isinstance(lst, list):
        return []
    return [i + 1 if isinstance(i, int) else i for i in lst]

def recursive_confuser(n):
    """
    Рекурсивная функция, считает сумму чисел от 1 до n.
    """
    if n <= 0:
        return 0
    return n + recursive_confuser(n - 1)

def pointless_string_manipulation(s):
    """
    Переворачивает строку, добавляет к ней '42', затем возвращает длину.
    """
    if not isinstance(s, str):
        return 0
    s = s[::-1] + "42"
    return len(s)

def unused_complexity(a, b):
    """
    Фиктивная функция, которая делает вид, что что-то вычисляет.
    """
    import math
    try:
        result = math.sqrt(abs(a**3 - b**2)) + math.sin(a) - math.cos(b)
        return round(result, 3)
    except Exception:
        return 0
    
