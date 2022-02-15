from abc import ABC, abstractmethod


class RangeService(ABC):
    @abstractmethod
    def is_value_in_range(self):
        pass

    @abstractmethod
    def warn_if_within_warning_tolerance(self):
        pass

    @abstractmethod
    def print_out_of_range_message(self):
        pass
