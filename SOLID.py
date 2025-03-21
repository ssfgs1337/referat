# Реферат: Принципи SOLID

## 1. Принцип єдиної відповідальності (Single Responsibility Principle, SRP)

### Порушення
class Report:
    def __init__(self, data):
        self.data = data

    def calculate_statistics(self):
        # Логіка обчислень
        pass

    def format_report(self):
        # Форматування звіту
        pass

    def save_to_file(self):
        # Збереження до файлу
        pass
###Порушення:Клас `Report` виконує три різні завдання: обчислення статистики, форматування звіту та його збереження.Це порушує SRP.
### Вирішення
class ReportCalculator:
    def calculate(self, data):
        pass


class ReportFormatter:
    def format(self, data):
        pass


class ReportSaver:
    def save(self, formatted_data):
        pass

###Виправлення:Ми розділили обовязки на три окремі класи.

## 2. Принцип відкритості/закритості (Open/Closed Principle, OCP)
### Порушення
class Discount:
    def apply_discount(self, price, discount_type):
        if discount_type == "fixed":
            return price - 10
        elif discount_type == "percentage":
            return price * 0.9

###Порушення:Додавання нового типу знижки вимагає зміни існуючого коду.
### Вирішення (без абстракції)
class FixedDiscount:
    def apply(self, price):
        return price - 10


class PercentageDiscount:
    def apply(self, price):
        return price * 0.9

###Виправлення:Ми створили окремі класи для кожного типу знижки, що дозволяє розширювати систему без зміни існуючого коду.

## 3. Принцип підстановки Лісков (Liskov Substitution Principle, LSP)

### Порушення
class Bird:
    def fly(self):
        pass


class Penguin(Bird):
    def fly(self):
        raise Exception("Penguins can't fly!")
###Порушення:`Penguin` не може літати, що порушує очікувану поведінку `Bird`.
### Вирішення
class Bird:
    pass


class FlyingBird(Bird):
    def fly(self):
        pass


class Penguin(Bird):
    def swim(self):
        pass

###Виправлення: Ми створили окремі класи для літаючих і нелітаючих птахів.

## 4. Принцип розділення інтерфейсів (Interface Segregation Principle, ISP)
### Порушення

class Worker:
    def work(self):
        pass

    def eat(self):
        pass

###Порушення:Не всі робітники їдять, наприклад, роботи.
### Вирішення

class Workable:
    def work(self):
        pass


class Eatable:
    def eat(self):
        pass


class Human(Workable, Eatable):
    pass


class Robot(Workable):
    pass

###Виправлення:Ми розділили обов’язки між двома інтерфейсами.

## 5. Принцип інверсії залежностей (Dependency Inversion Principle, DIP)

### Порушення
class MySQLDatabase:
    def connect(self):
        pass


class UserService:
    def __init__(self):
        self.db = MySQLDatabase()

###Порушення: `UserService` залежить від конкретної реалізації бази даних.
### Вирішення

class Database(ABC):
    @abstractmethod
    def connect(self):
        pass


class MySQLDatabase(Database):
    def connect(self):
        pass


class UserService:
    def __init__(self, db: Database):
        self.db = db
### Виправлення: Використання абстракції `Database` дозволяє легко змінювати реалізацію бази даних.



###Порушення
class Worker:
    def work(self):
        pass
    def eat(self):
        pass
class Manager(Worker):
    def work(self):
        print("Менеджер працює")
    def eat(self):
        print("Менеджер їсть")
class Robot(Worker):
    def work(self):
        print("Робот працює")
    def eat(self):  # Порушення ISP, робот не їсть
        raise NotImplementedError("Робот не їсть")


### Вирішення
from abc import ABC, abstractmethod
class Workable(ABC):
    @abstractmethod
    def work(self):
        pass
class Eatable(ABC):
    @abstractmethod
    def eat(self):
        pass
class Manager(Workable, Eatable):
    def work(self):
        print("Менеджер працює")
    def eat(self):
        print("Менеджер їсть")
class Robot(Workable):
    def work(self):
        print("Робот працює")
