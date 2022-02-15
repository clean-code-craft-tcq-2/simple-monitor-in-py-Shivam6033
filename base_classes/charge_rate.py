from abstract_classes.language_service import LanguageService
from abstract_classes.range_service import RangeService


class ChargeRate(RangeService):
    higher_limit = 0.80
    warning_tolerance = 0.05

    def __init__(self, value, language: LanguageService):
        self.value = value
        self.language = language

    def is_value_in_range(self):
        if self.value > self.higher_limit:
            return False
        return True

    def print_out_of_range_message(self):
        print(f'Charge Rate {self.language.get_out_of_range_message()}')

    def warn_if_within_warning_tolerance(self):
        higher_limit_tolerance = self.higher_limit - self.higher_limit * self.warning_tolerance
        warning_range = []
        while higher_limit_tolerance < self.higher_limit:
            warning_range.append(higher_limit_tolerance)
            higher_limit_tolerance = higher_limit_tolerance + 0.01
        if self.value in warning_range:
            print(f'Charge Rate {self.language.get_approaching_charge_peak_message()}')

