import pytest
import datetime

from app.cars import Car, ParkedCar

def test_lost_ticket():
    car = Car()
    car.make = "Toyota"
    car.model = "Corolla"
    car.plate = "BBB1111"

    entry_time = datetime.datetime(2026, 3, 31, 10, 0, 0)

    parked_car = ParkedCar(car, entry_time)
    parked_car.add_exit_time(entry_time + datetime.timedelta(hours=2))

    normal_fee = parked_car.calculate_fee()

    parked_car.add_lost_ticket()

    lost_ticket_fee = parked_car.calculate_fee()

    assert normal_fee != 300.0
    assert lost_ticket_fee == 300.0

test_lost_ticket()
