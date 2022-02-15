from abstract_classes.range_service import RangeService
from base_classes.charge_rate import ChargeRate
from base_classes.state_of_charge import StateOfCharge
from base_classes.temperature import Temperature
from lang_base_classes.english_language import EnglishLanguage
from lang_base_classes.german_language import GermanLanguage


def battery_is_ok(*args: RangeService):
    for battery_attributes in args:
        if not battery_attributes.is_value_in_range():
            battery_attributes.print_out_of_range_message()
            return False
        battery_attributes.warn_if_within_warning_tolerance()
    return True


def test_battery_is_ok():
    assert (battery_is_ok(Temperature(45, EnglishLanguage()), StateOfCharge(20, EnglishLanguage()),
                          ChargeRate(0.76, EnglishLanguage())) is True)
    assert (battery_is_ok(Temperature(45, GermanLanguage()), StateOfCharge(10, GermanLanguage()),
                          ChargeRate(0.76, GermanLanguage())) is False)
    assert (battery_is_ok(Temperature(50, GermanLanguage()), StateOfCharge(25, GermanLanguage()),
                          ChargeRate(0.80, GermanLanguage())) is False)
    assert (battery_is_ok(Temperature(20, EnglishLanguage()), StateOfCharge(25, EnglishLanguage()),
                          ChargeRate(1.00, EnglishLanguage())) is False)
    assert (battery_is_ok(Temperature(20, GermanLanguage()), StateOfCharge(25, GermanLanguage()),
                          ChargeRate(0.60, GermanLanguage())) is True)


if __name__ == '__main__':
    test_battery_is_ok()
