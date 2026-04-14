import pytest
import datetime
from app.cars import Car, ParkedCar

def test_exit_time_validation():
    car = Car()
    car.make = "Toyota"
    car.model = "Corolla"
    car.plate = "XYZ1234"

    entry_time = datetime.datetime(2026, 3, 31, 10, 0, 0)

    parked_car = ParkedCar(car, entry_time)

    with pytest.raises(ValueError):
        parked_car.add_exit_time(entry_time)

    parked_car = ParkedCar(car, entry_time)

    with pytest.raises(ValueError):
        parked_car.add_exit_time(entry_time - datetime.timedelta(minutes=1))

    parked_car = ParkedCar(car, entry_time)
    parked_car.add_exit_time(entry_time + datetime.timedelta(minutes=1))

    assert parked_car.exit_time is not None

test_exit_time_validation()