from abc import ABC, abstractmethod


class Transport(ABC):

    @abstractmethod
    def deliver(self, cargo):
        pass


class Truck(Transport):

    def deliver(self, cargo):
        print(f"Доставка груза '{cargo}' по земле на грузовике.")


class Ship(Transport):

    def deliver(self, cargo):
        print(f"Доставка груза '{cargo}' по морю на корабле.")


class Logistics(ABC):

    @abstractmethod
    def create_transport(self) -> Transport:
        pass

    def plan_delivery(self, cargo):
        transport = self.create_transport()
        transport.deliver(cargo)


class RoadLogistics(Logistics):

    def create_transport(self) -> Transport:
        return Truck()


class SeaLogistics(Logistics):

    def create_transport(self) -> Transport:
        return Ship()


if __name__ == "__main__":
    road_delivery = RoadLogistics()
    sea_delivery = SeaLogistics()

    road_delivery.plan_delivery("Электроника")
    sea_delivery.plan_delivery("Контейнеры с одеждой")
