from datetime import datetime
from pprint import pprint

from modules.bmw import BMW
from modules.ford import Ford


def main():
    new_ford = Ford(color='blue', manufacturer_country='usa',
                    max_fuel=1000, current_fuel=69, is_cabriolet=True)
    new_bmw = BMW(color='red', manufacturer_country='germany',
                  max_fuel=200, current_fuel=10,
                  wheel_heater_subscription_until=datetime(2023, 10, 10))

    print(new_bmw < new_ford)
    new_bmw.fill_fuel(2)
    new_bmw.fill_fuel(5)
    new_bmw.fill_fuel(10)
    new_bmw.fill_fuel(1)
    new_bmw.fill_fuel(1)
    new_bmw.fill_fuel(2)
    new_bmw.fill_fuel(7)
    new_bmw.fill_fuel(8)
    new_bmw.fill_fuel(1)
    new_bmw.fill_fuel(20)
    print('_' * 100)
    print(vars(new_ford))
    print('_' * 100)
    print(vars(new_bmw))
    print('_' * 100)

    pprint(new_bmw.get_last_fills(10))

    new_bmw.fill_fuel(20000)
    print(new_bmw < new_ford)

    print(repr(new_bmw))
    print(repr(new_ford))


if __name__ == '__main__':
    main()
