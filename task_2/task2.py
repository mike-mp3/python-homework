from abc import ABC, abstractmethod

# Определение интерфейса стратегии
class Strategy(ABC):
    @abstractmethod
    def process_data(self, data):
        pass

# Конкретная стратегия для обработки списков
class ListProcessingStrategy(Strategy):
    def process_data(self, data):
        if not isinstance(data, list):
            raise TypeError("Data must be a list")
        return {
            "max": max(data),
            "min": min(data),
            "sorted": sorted(data)
        }

# Конкретная стратегия для обработки словарей
class DictionaryProcessingStrategy(Strategy):
    def process_data(self, data):
        if not isinstance(data, dict):
            raise TypeError("Data must be a dictionary")
        return {
            "keys": list(data.keys()),
            "values": list(data.values()),
            "items": list(data.items())
        }

# Возможность добавления пользовательских стратегий
class CustomStrategy(Strategy):
    def process_data(self, data):
        return f"Custom processing of {type(data).__name__}: {data}"

# Центральный модуль обработки данных
class DataProcessor:
    def __init__(self, strategy: Strategy = None):
        self._strategy = strategy

    def set_strategy(self, strategy: Strategy):
        self._strategy = strategy

    def process_data(self, data):
        if not self._strategy:
            raise ValueError("Strategy is not set")
        return self._strategy.process_data(data)

# Пример использования
if __name__ == "__main__":
    # Данные для обработки
    list_data = [5, 2, 9, 1, 7]
    dict_data = {"a": 1, "b": 2, "c": 3}

    # Создание процессора
    processor = DataProcessor()

    # Обработка списка
    processor.set_strategy(ListProcessingStrategy())
    print("List Processing:", processor.process_data(list_data))

    # Обработка словаря
    processor.set_strategy(DictionaryProcessingStrategy())
    print("Dictionary Processing:", processor.process_data(dict_data))

    # Пример использования пользовательской стратегии
    processor.set_strategy(CustomStrategy())
    print("Custom Strategy:", processor.process_data("Some data"))
