from abc import ABC, abstractmethod


class Chair(ABC):

    @abstractmethod
    def sit_on(self):
        pass


class ModernChair(Chair):

    def sit_on(self):
        print("Вы сидите на минималистичном современном стуле.")


class VictorianChair(Chair):

    def sit_on(self):
        print("Вы сидите на старинном викторианском кресле.")


class Table(ABC):

    @abstractmethod
    def put_on(self):
        pass


class ModernTable(Table):

    def put_on(self):
        print("Вещи лежат на стеклянном современном столе.")


class VictorianTable(Table):

    def put_on(self):
        print("Вещи лежат на резном деревянном викторианском столе.")


class FurnitureFactory(ABC):

    @abstractmethod
    def create_chair(self) -> Chair:
        pass

    @abstractmethod
    def create_table(self) -> Table:
        pass


class ModernFurnitureFactory(FurnitureFactory):

    def create_chair(self) -> Chair:
        return ModernChair()

    def create_table(self) -> Table:
        return ModernTable()


class VictorianFurnitureFactory(FurnitureFactory):

    def create_chair(self) -> Chair:
        return VictorianChair()

    def create_table(self) -> Table:
        return VictorianTable()


class RoomInterior:

    def __init__(self, factory: FurnitureFactory):
        self.chair = factory.create_chair()
        self.table = factory.create_table()

    def describe(self):
        self.chair.sit_on()
        self.table.put_on()


if __name__ == "__main__":
    print("--- Современный интерьер ---")
    modern_room = RoomInterior(ModernFurnitureFactory())
    modern_room.describe()

    print("\n--- Викторианский интерьер ---")
    victorian_room = RoomInterior(VictorianFurnitureFactory())
    victorian_room.describe()
