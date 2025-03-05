class Invoice:
    def __init__(self, customer, items):
        self.customer = customer
        self.items = items  # Список товарів у рахунку

    def calculate_total(self):
        return sum(item['price'] * item['quantity'] for item in self.items)  # Обчислення загальної суми

class InvoicePrinter:
    def print_invoice(self, invoice: Invoice):
        print(f"Invoice for {invoice.customer}: {invoice.calculate_total()} USD")  # Відповідає лише за друк