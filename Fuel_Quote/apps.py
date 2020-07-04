from django.apps import AppConfig


class Fuel_quoteConfig(AppConfig):
    name = 'Fuel_quote'

    def ready(self):
        import Fuel_quote.signals
