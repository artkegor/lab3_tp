from singleton import DatabaseConnection
from factory_method import RoadLogistics, SeaLogistics
from abstract_factory import ModernFurnitureFactory, VictorianFurnitureFactory, RoomInterior
from builder import GamingPCBuilder, OfficePCBuilder, Director


def run_singleton_demo():
    print("=== 1. Паттерн Singleton (Одиночка) ===")
    db1 = DatabaseConnection()
    db2 = DatabaseConnection()

    db1.connect()
    print(f"Статус db2: {db2.status}")
    print(f"db1 и db2 — это один объект? {db1 is db2}\n")


def run_factory_method_demo():
    print("=== 2. Паттерн Factory Method (Фабричный метод) ===")
    road_delivery = RoadLogistics()
    sea_delivery = SeaLogistics()

    road_delivery.plan_delivery("Электроника")
    sea_delivery.plan_delivery("Контейнеры с одеждой")
    print()


def run_abstract_factory_demo():
    print("=== 3. Паттерн Abstract Factory (Абстрактная фабрика) ===")
    print("[Современный интерьер]")
    modern_room = RoomInterior(ModernFurnitureFactory())
    modern_room.describe()

    print("\n[Викторианский интерьер]")
    victorian_room = RoomInterior(VictorianFurnitureFactory())
    victorian_room.describe()
    print()


def run_builder_demo():
    print("=== 4. Паттерн Builder (Строитель) ===")
    gaming_builder = GamingPCBuilder()
    director = Director(gaming_builder)
    director.build_pc()
    print("Игровая сборка:", gaming_builder.get_result())

    office_builder = OfficePCBuilder()
    director = Director(office_builder)
    director.build_pc()
    print("Офисная сборка:", office_builder.get_result())
    print()


if __name__ == "__main__":
    run_singleton_demo()
    run_factory_method_demo()
    run_abstract_factory_demo()
    run_builder_demo()
