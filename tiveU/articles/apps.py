from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class ArticlesConfig(AppConfig):
    name = 'tiveU.articles'
    verbose_name = _('Articles')
