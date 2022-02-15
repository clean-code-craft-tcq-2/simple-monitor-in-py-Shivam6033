from abstract_classes.language_service import LanguageService


class EnglishLanguage(LanguageService):
    def get_out_of_range_message(self):
        return 'out of Range!!'

    def get_approaching_charge_peak_message(self):
        return 'Warning: Approaching discharge'

    def get_approaching_discharge_message(self):
        return 'Warning: Approaching charge-peak'
