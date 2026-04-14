import pytest
import datetime

from app.cars import Car, ParkedCar

def test_night_discount():
    car = Car()
    car.make = "Toyota"
    car.model = "Corolla"
    car.plate = "DEF5678"

    entry_time2 = datetime.datetime(2026, 3, 31, 22, 0)
    parked_car2 = ParkedCar(car, entry_time2)
    parked_car2.add_exit_time(entry_time2 + datetime.timedelta(hours=3))

    fee2 = parked_car2.calculate_fee()

    entry_time1 = datetime.datetime(2026, 3, 31, 21, 59)
    parked_car1 = ParkedCar(car, entry_time1)
    parked_car1.add_exit_time(entry_time1 + datetime.timedelta(hours=3))

    fee1 = parked_car1.calculate_fee()

    assert fee2 < fee1

test_night_discount()