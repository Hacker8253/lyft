from abc import ABC, abstractmethod
from datetime import date


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
