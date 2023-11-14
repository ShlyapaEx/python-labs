from datetime import datetime

import pytest

from lab_3.modules.bmw import BMW
from lab_3.modules.car import Car
from lab_3.modules.ford import Ford


@pytest.fixture
def new_ford():
    cool_ford = Ford(color='blue', manufacturer_country='usa',
                     max_fuel=1000, current_fuel=69, is_cabriolet=True)
    yield cool_ford
    cool_ford.fuel_fills_history.clear()


@pytest.fixture
def new_bmw():
    cool_bmw = BMW(color='red', manufacturer_country='germany',
                   max_fuel=200, current_fuel=10,
                   wheel_heater_subscription_until=datetime(2023, 10, 10))
    yield cool_bmw
    cool_bmw.fuel_fills_history.clear()


def test_overfill_fuel(new_bmw: BMW):
    new_bmw.fill_fuel(new_bmw.max_fuel + 1)
    assert new_bmw.current_fuel == new_bmw.max_fuel


def test_overloaded_compare(new_bmw: BMW, new_ford: Ford):
    assert new_bmw < new_ford


def test_fuel_history(new_bmw: BMW):
    fills_count = 5
    for i in range(fills_count):
        new_bmw.fill_fuel(i)
    assert len(new_bmw.get_last_fills()) == fills_count


def test_fill_diesel(new_ford: Ford):
    fills_count = 5
    for i in range(fills_count):
        new_ford.fill_fuel(i, "diesel")
    assert len(new_ford.get_last_fills()) == fills_count


def test_fill_bad_fuel(new_ford: Ford):
    with pytest.raises(Exception):
        new_ford.fill_fuel(5, "Wood")
