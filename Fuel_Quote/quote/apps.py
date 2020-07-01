from django.apps import AppConfig

class QuoteformConfig(AppConfig):
    name = 'quoteForm'

    def ready(self):
    	import quote.signals
