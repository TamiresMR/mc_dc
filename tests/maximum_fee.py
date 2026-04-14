import pytest
import datetime

from app.cars import Car, ParkedCar

def test_maximum_fee():
    car = Car()
    car.make = "BMW"
    car.model = "g70"
    car.plate = "AAA9999"

    entry_time = datetime.datetime(2026, 3, 31, 10, 0, 0)

    parked_car = ParkedCar(car, entry_time)
    parked_car.add_exit_time(entry_time + datetime.timedelta(hours=30))

    fee = parked_car.calculate_fee()

    assert fee == 100.0


test_maximum_fee()