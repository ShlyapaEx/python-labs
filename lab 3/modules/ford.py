from typing import overload
from modules.car import Car
from datetime import datetime


class Ford(Car):

    is_cabriolet: bool

    def __init__(self, color: str, manufacturer_country: str,
                 max_fuel: int, current_fuel: int, is_cabriolet: bool):
        super().__init__(color, manufacturer_country, max_fuel, current_fuel)
        self.is_cabriolet = is_cabriolet

    def fill_fuel(self, intake_fuel: int, fuel_type: str = 'gasoline'):
        free_fuel_space = self.max_fuel - self.current_fuel
        if intake_fuel > free_fuel_space:
            intake_fuel = free_fuel_space

        self.current_fuel += intake_fuel
        current_datetime = datetime.now()

        self.fuel_fills_history.append({'Дата заправки': current_datetime.date().strftime('%d/%m/%Y'),
                                        'Время заправки': current_datetime.time().strftime('%H:%M:%S'),
                                        'Количество залитых литров': intake_fuel,
                                        'Тип топлива': fuel_type})

        return self.current_fuel

    # def test(self):
    #     self.fill_fuel(10)
    #     self.fill_fuel(20, 'diesel')
