from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class CurrencyConfig(AppConfig):
    name = 'sw_currency'
    verbose_name = _('Валюти')


default_app_config = 'sw_currency.CurrencyConfig'



