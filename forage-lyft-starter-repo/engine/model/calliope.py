from abc import ABC, abstractmethod
from datetime import date, datetime

class Serviceable(ABC):
    @abstractmethod
    def needs_service(self) -> bool:
        pass

class Engine(Serviceable, ABC):
    def __init__(self, engine_type: str, capacity: int, manufacture_date: date, last_service_date: date):
        self.engine_type = engine_type
        self.capacity = capacity
        self.manufacture_date = manufacture_date
        self.last_service_date = last_service_date

    def check_health(self):
        pass

    def get_service_status(self) -> bool:
        pass

    def start(self):
        pass

    def stop(self):
        pass

    def change_engine_type(self, new_engine_type: str):
        self.engine_type = new_engine_type


class CapuletEngine(Engine):
    def __init__(self, last_service_date: date, current_mileage: int, last_service_mileage: int):
        super().__init__("Capulet Engine", 2000, date(2019, 1, 1), last_service_date)
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def needs_service(self) -> bool:
        return (self.current_mileage - self.last_service_mileage) > 30000 or self.get_service_status()


class SternmanEngine(Engine):
    def __init__(self, last_service_date: date, warning_light_on: bool):
        super().__init__("Sternman Engine", 1800, date(2020, 1, 1), last_service_date)
        self.warning_light_on = warning_light_on

    def needs_service(self) -> bool:
        return self.warning_light_on or self.get_service_status()


class WilloughbyEngine(Engine):
    def __init__(self, last_service_date: date, current_mileage: int, last_service_mileage: int):
        super().__init__("Willoughby Engine", 2200, date(2021, 1, 1), last_service_date)
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def needs_service(self) -> bool:
        return (self.current_mileage - self.last_service_mileage) > 60000 or self.get_service_status()
