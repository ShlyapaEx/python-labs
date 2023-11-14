from datetime import datetime
from lab_3.modules.car import Car


class BMW(Car):
    wheel_heater_subscription_until: datetime

    def __init__(self, color: str, manufacturer_country: str,
                 max_fuel: int, current_fuel: int,
                 wheel_heater_subscription_until: datetime):
        super().__init__(color, manufacturer_country, max_fuel, current_fuel)
        self.wheel_heater_subscription_until = wheel_heater_subscription_until
