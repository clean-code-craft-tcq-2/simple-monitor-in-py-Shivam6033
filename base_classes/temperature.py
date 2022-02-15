from abstract_classes.language_service import LanguageService
from abstract_classes.range_service import RangeService


class Temperature(RangeService):
    lower_limit = 0
    higher_limit = 45
    warning_tolerance = 0.05

    def __init__(self, value, language: LanguageService):
        self.value = value
        self.language = language

    def is_value_in_range(self):
        if self.value in range(self.lower_limit, self.higher_limit + 1):
            return True
        return False

    def print_out_of_range_message(self):
        print(f'Temperature {self.language.get_out_of_range_message()}')

    def warn_if_within_warning_tolerance(self):
        lower_limit_tolerance = int(self.lower_limit + self.higher_limit * self.warning_tolerance)
        higher_limit_tolerance = int(self.higher_limit - self.higher_limit * self.warning_tolerance)
        if self.value in range(self.lower_limit, lower_limit_tolerance + 1):
            print(f'Temperature {self.language.get_approaching_discharge_message()}')
        if self.value in range(higher_limit_tolerance, self.higher_limit):
            print(f'Temperature {self.language.get_approaching_charge_peak_message()}')
