import random
from datetime import datetime, timedelta

def generate_dates(start_date, end_date):
    """
    Генерирует список дат между указанными начальной и конечной датами.

    Параметры
    ----------
    start_date : str
        Начальная дата в формате ГГГГ-ММ-ДД.
    end_date : str
        Конечная дата в формате ГГГГ-ММ-ДД.

    Возвращает
    -------
    list
        Список дат (в виде строк в формате ГГГГ-ММ-ДД) между начальной и конечной датами.
    """

    start = datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.strptime(end_date, "%Y-%m-%d")
    date_list = [(start + timedelta(days=x)).strftime("%Y-%m-%d") for x in range((end - start).days + 1)]
    return date_list

def choose_city(cities):
    """
    Случайно выбирает город из списка городов.

    Параметры
    ----------
    cities : list
        Список названий городов.

    Возвращает
    -------
    str
        Случайно выбранный город из списка.
    """
    return random.choice(cities)

def generate_weather_data(temp_range, humidity_range, precipitation_range):
    """
    Генерирует случайные данные о погоде, включая температуру, влажность и осадки.

    Параметры
    ----------
    temp_range : tuple
        Кортеж (минимальная температура, максимальная температура), задающий диапазон температур.
    humidity_range : tuple
        Кортеж (минимальная влажность, максимальная влажность), задающий диапазон влажности.
    precipitation_range : tuple
        Кортеж (минимальное количество осадков, максимальное количество осадков), задающий диапазон осадков.

    Возвращает
    -------
    tuple
        Кортеж, содержащий случайно сгенерированные значения температуры, влажности и осадков.
    """
    temperature = random.uniform(*temp_range)
    humidity = random.uniform(*humidity_range)
    precipitation = random.uniform(*precipitation_range)
    return temperature, humidity, precipitation

def create_weather_data(start_date, end_date, cities, temp_range, humidity_range, precipitation_range):
    """
    Создает список словарей с данными о погоде для различных дат и городов.

    Параметры
    ----------
    start_date : str
        Начальная дата в формате ГГГГ-ММ-ДД.
    end_date : str
        Конечная дата в формате ГГГГ-ММ-ДД.
    cities : list
        Список названий городов.
    temp_range : tuple
        Кортеж (минимальная температура, максимальная температура), задающий диапазон температур.
    humidity_range : tuple
        Кортеж (минимальная влажность, максимальная влажность), задающий диапазон влажности.
    precipitation_range : tuple
        Кортеж (минимальное количество осадков, максимальное количество осадков), задающий диапазон осадков.

    Возвращает
    -------
    list
        Список словарей, каждый из которых представляет данные о погоде для конкретной даты и города.
    """
    weather_data = []
    for date in generate_dates(start_date, end_date):
        for city in cities:
            temperature, humidity, precipitation = generate_weather_data(temp_range, humidity_range, precipitation_range)
            weather_data.append({
                "date": date,
                "city": city,
                "temperature": round(temperature, 2),
                "humidity": round(humidity, 2),
                "precipitation": round(precipitation, 2)
            })
    return weather_data

# Пример использования
cities = ["CityA", "CityB", "CityC", "CityD", "CityE", "CityF", "CityG"]
temp_range = (10, 30)
humidity_range = (50, 90)
precipitation_range = (0, 10)

weather_data = create_weather_data("2024-11-01", "2024-11-05", cities, temp_range, humidity_range, precipitation_range)
weather_data[:35]


from functools import reduce

def FindTheParameter(data, p, date=False): #тут функция для сортировки города и его параметра
    grouped_data = {}
    for record in data:
        city = record["city"]
        if city not in grouped_data:
            grouped_data[city] = []
        if date == False:
            grouped_data[city].append(record[f"{p}"])
        else:
            grouped_data[city].append(record[f"{p}"])
            grouped_data[city].append(record['date'])


    return grouped_data

#считаем среднее
AverageTemperature = list(map(lambda city: {"city": city,
                            "AverageTemperature": sum(FindTheParameter(weather_data, 'temperature')[city]) / len(FindTheParameter(weather_data, 'temperature')[city])},
                            FindTheParameter(weather_data, 'temperature')
                            ))
print(f'Средняя температура в городах: \n {AverageTemperature}')

#считаем осадки
TotalPrecipitation = {
    city: reduce(lambda x, y: x + y, precipitation, 0)
    for city, precipitation in FindTheParameter(weather_data, 'precipitation').items()
}

print(f'Cумма осадков в городах: \n {TotalPrecipitation}')

#print(type(FindTheParameter(weather_data, 'humidity', True)))


# Функция для фильтрации данных по влажности
Humidity70 = list(
    map(
        lambda x: {"city": x["city"], "date": x["date"]},
        filter(
            lambda x: x["humidity"] > 70,
            weather_data
        )
    )
)


print(f'Города и даты с влажностью более 70%: \n {Humidity70}')
