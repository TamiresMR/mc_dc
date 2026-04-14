import datetime

class Car:
    def _init__(self, make, model, plate):
        self.make = make
        self.model = model
        self.plate = plate


class ParkedCar:
    def __init__(self, car: Car, entry_time: datetime, lost_ticket: bool = False):
        self.car = car
        self.entry_time = entry_time
        self.exit_time = None
        self.lost_ticket = lost_ticket

    def get_car_info(self):
        return f"{self.car.make} {self.car.model} ({self.car.plate})"
    
    def add_exit_time(self, exit_time: datetime):
        if self.entry_time.time() >= exit_time.time():
            raise ValueError("O horário de saída deve ser após o horário de entrada.")

        self.exit_time = exit_time
        return self.exit_time
        

    def add_lost_ticket(self):
        self.lost_ticket = True


    def calculate_fee(self):
        if self.lost_ticket:
            return 300.0

        duration = self.exit_time - self.entry_time
        hours = duration.total_seconds() / 3600

        if hours <= 0.5:
            return 0.0

        fee = hours * 5.0

        day = self.entry_time.weekday()
        if day == 5 or day == 6: 
            fee *= 0.8 

        inicio = datetime.time(22, 0)
        fim = datetime.time(6, 0)
        if (self.entry_time.time() >= inicio or self.entry_time.time() <= fim):
            fee -= 10.0

        fee = min(fee, 100.0)

        return fee if fee > 0 else 0.0
    
    