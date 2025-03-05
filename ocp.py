from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass  # Абстрактний метод для оплати

class CreditCardPayment(PaymentMethod):
    def pay(self, amount):
        return f"Paid {amount} using Credit Card"

class PayPalPayment(PaymentMethod):
    def pay(self, amount):
        return f"Paid {amount} using PayPal"

class BitcoinPayment(PaymentMethod):
    def pay(self, amount):
        return f"Paid {amount} using Bitcoin"