from abc import ABC, abstractmethod


class RangeService(ABC):
    @abstractmethod
    def is_value_in_range(self, value):
        pass


class Temperature(RangeService):
    lower_limit = 0
    higher_limit = 45

    @classmethod
    def is_value_in_range(cls, value):
        if value in range(cls.lower_limit, cls.higher_limit + 1):
            return True
        print(f'{cls.__name__} is out of range!')
        return False


class ChargeRate(RangeService):
    higher_limit = 0.8

    @classmethod
    def is_value_in_range(cls, value):
        if value > 0.8:
            print(f'{cls.__name__} is out of range!')
            return False
        return True


class StateOfCharge(RangeService):
    lower_limit = 20
    higher_limit = 80

    @classmethod
    def is_value_in_range(cls, value):
        if value in range(cls.lower_limit, cls.higher_limit + 1):
            return True
        print(f'{cls.__name__} is out of range!')
        return False


def battery_is_ok(temperature_value, state_of_charge_value, charge_rate_value):
    return Temperature.is_value_in_range(temperature_value) and \
           ChargeRate.is_value_in_range(charge_rate_value) and StateOfCharge.is_value_in_range(state_of_charge_value)


def test_battery_is_ok():
    assert (battery_is_ok(temperature_value=70, state_of_charge_value=20, charge_rate_value=0.8) is False)
    assert (battery_is_ok(temperature_value=45, state_of_charge_value=20, charge_rate_value=0.8) is True)
    assert (battery_is_ok(temperature_value=40, state_of_charge_value=10, charge_rate_value=0.8) is False)
    assert (battery_is_ok(temperature_value=40, state_of_charge_value=50, charge_rate_value=0.8) is True)
    assert (battery_is_ok(temperature_value=40, state_of_charge_value=30, charge_rate_value=1.0) is False)
    assert (battery_is_ok(temperature_value=40, state_of_charge_value=50, charge_rate_value=0.6) is True)


if __name__ == '__main__':
    test_battery_is_ok()
