from abstract_classes.language_service import LanguageService


class GermanLanguage(LanguageService):
    def get_out_of_range_message(self):
        return 'außerhalb des Bereichs!!'

    def get_approaching_charge_peak_message(self):
        return 'Warnung: Naht an Entladung'

    def get_approaching_discharge_message(self):
        return 'Warnung: Ladespitze nähert sich '
