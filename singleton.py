class DatabaseConnection:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.status = "Отключено"
        return cls._instance

    def connect(self):
        self.status = "Подключено к БД"
        print("Соединение с базой данных установлено.")


if __name__ == "__main__":
    db1 = DatabaseConnection()
    db2 = DatabaseConnection()

    db1.connect()

    print(f"Статус db2: {db2.status}")
    print(f"db1 и db2 — это один объект? {db1 is db2}")
