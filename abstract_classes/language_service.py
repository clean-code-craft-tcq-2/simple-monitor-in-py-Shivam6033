from abc import ABC, abstractmethod


class LanguageService(ABC):
    @abstractmethod
    def get_out_of_range_message(self):
        pass

    @abstractmethod
    def get_approaching_charge_peak_message(self):
        pass

    @abstractmethod
    def get_approaching_discharge_message(self):
        pass
