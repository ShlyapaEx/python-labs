from datetime import datetime


class Car:
    color: str
    manufacturer_country: str
    max_fuel: int
    current_fuel: int

    fuel_fills_history = []

    def __init__(self, color: str, manufacturer_country: str,
                 max_fuel: int, current_fuel: int):
        self.color = color
        self.manufacturer_country = manufacturer_country
        self.max_fuel = max_fuel
        self.current_fuel = current_fuel

    def fill_fuel(self, intake_fuel: int):
        free_fuel_space = self.max_fuel - self.current_fuel
        if intake_fuel > free_fuel_space:
            intake_fuel = free_fuel_space

        self.current_fuel += intake_fuel
        current_datetime = datetime.now()

        self.fuel_fills_history.append(
            {'Дата заправки': current_datetime.date().strftime('%d/%m/%Y'),
             'Время заправки': current_datetime.time().strftime('%H:%M:%S'),
             'Количество залитых литров': intake_fuel})

        return self.current_fuel

    def get_last_fills(self, last_fills_count: int = 10):
        return self.fuel_fills_history[-min(last_fills_count,
                                            len(self.fuel_fills_history)):]

    def __lt__(self, other):
        return self.current_fuel < other.current_fuel

    def __repr__(self) -> str:
        return f'Country: {self.manufacturer_country} | Fuel: {self.current_fuel}/{self.max_fuel} | Color: {self.color}'
