import pytest
import datetime

from app.cars import Car, ParkedCar

def test_30_minutes_boundary():
    car = Car()
    car.make = "Toyota"
    car.model = "Corolla"
    car.plate = "ABC1234"

    entry_time = datetime.datetime(2026, 3, 31, 10, 0, 0)

    parked_car = ParkedCar(car, entry_time)
    parked_car.add_exit_time(entry_time + datetime.timedelta(minutes=29))

    fee = parked_car.calculate_fee()

    assert fee == 0.0

    parked_car = ParkedCar(car, entry_time)
    parked_car.add_exit_time(entry_time + datetime.timedelta(minutes=30))

    fee = parked_car.calculate_fee()

    assert fee == 0.0

    parked_car = ParkedCar(car, entry_time)
    parked_car.add_exit_time(entry_time + datetime.timedelta(minutes=31))

    fee = parked_car.calculate_fee()

    assert fee > 0.0

test_30_minutes_boundary()