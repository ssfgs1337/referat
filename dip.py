class Database(ABC):
    @abstractmethod
    def connect(self):
        pass  # Абстрактний метод для підключення

class PostgreSQLDatabase(Database):
    def connect(self):
        return "Connecting to PostgreSQL"