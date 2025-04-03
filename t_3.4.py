class Phone:
    type: str = "Смартфон"
    manufacturer: str = "Китай"

    def __init__(self, model: str, os: str, color: str, ram: int, rom: int, frequency: int) -> None:
        self.model = model
        self.os = os
        self.color = color
        self.ram = ram
        self.rom = rom
        self.frequency = frequency

    def __add__(self, mem: int) -> str:
        if isinstance(mem, int) and 0 < mem <= 6:
            self.ram += mem
            self.rom -= mem
        else:
            raise ValueError("Недопустимое значение расширения оперативной памяти!")
        return f"Новое количество оперативной памяти у {self.model}: {self.ram} ГБ.\nНовое количество постоянной памяти у {self.model}: {self.rom} ГБ."

    def get_model(self) -> str:
        return self.model

    def is_android(self) -> bool:
        return self.os == "Android"

    def get_color(self) -> str:
        return self.color

    def set_frequency(self, frequency: int) -> None:
        self.frequency = frequency


phone_1 = Phone("POCO C61", "Android", "зелёный", 3, 64, 90)
phone_2 = Phone("Apple iPhone 15 Pro", "iOS", "серый", 8, 256, 120)
phone_3 = Phone("Tecno SPARK GO 1", "Android", "зелёный", 3, 64, 120)


print(phone_1.get_model())
print(phone_2.get_model())
print(phone_3.get_model())

print(phone_1.is_android())
print(phone_2.is_android())
print(phone_3.is_android())

print(phone_1.get_color())
print(phone_2.get_color())
print(phone_3.get_color())

phone_1.set_frequency(75)
print(phone_1.frequency)
phone_2.set_frequency(90)
print(phone_2.frequency)
phone_3.set_frequency(60)
print(phone_3.frequency)

print(phone_1 + 1)
print(phone_2 + 4)
print(phone_3 + 2)