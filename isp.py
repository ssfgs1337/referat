from abc import ABC, abstractmethod

class Workable(ABC):
    @abstractmethod
    def work(self):
        pass  # Загальний інтерфейс для роботи

class Maintainable(ABC):
    @abstractmethod
    def maintain(self):
        pass  # Окремий інтерфейс для обслуговування