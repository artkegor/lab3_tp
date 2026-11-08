from abc import ABC, abstractmethod


class Computer:

    def __init__(self):
        self.cpu = None
        self.ram = None
        self.gpu = None

    def __str__(self):
        return f"ПК [Процессор: {self.cpu}, ОЗУ: {self.ram}, Видеокарта: {self.gpu}]"


class ComputerBuilder(ABC):

    @abstractmethod
    def set_cpu(self):
        pass

    @abstractmethod
    def set_ram(self):
        pass

    @abstractmethod
    def set_gpu(self):
        pass

    @abstractmethod
    def get_result(self) -> Computer:
        pass


class GamingPCBuilder(ComputerBuilder):

    def __init__(self):
        self.pc = Computer()

    def set_cpu(self):
        self.pc.cpu = "Intel Core i9"

    def set_ram(self):
        self.pc.ram = "32 GB DDR5"

    def set_gpu(self):
        self.pc.gpu = "NVIDIA RTX 4090"

    def get_result(self) -> Computer:
        return self.pc


class OfficePCBuilder(ComputerBuilder):

    def __init__(self):
        self.pc = Computer()

    def set_cpu(self):
        self.pc.cpu = "Intel Core i3"

    def set_ram(self):
        self.pc.ram = "8 GB DDR4"

    def set_gpu(self):
        self.pc.gpu = "Встроенная графика"

    def get_result(self) -> Computer:
        return self.pc


class Director:

    def __init__(self, builder: ComputerBuilder):
        self.builder = builder

    def build_pc(self):
        self.builder.set_cpu()
        self.builder.set_ram()
        self.builder.set_gpu()


if __name__ == "__main__":
    gaming_builder = GamingPCBuilder()
    director = Director(gaming_builder)
    director.build_pc()
    print("Игровая сборка:", gaming_builder.get_result())

    office_builder = OfficePCBuilder()
    director = Director(office_builder)
    director.build_pc()
    print("Офисная сборка:", office_builder.get_result())
