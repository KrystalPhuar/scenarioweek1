from django.contrib.auth.models import User
import django_filters
from .models import Log

class LogFilter(django_filters.FilterSet):
    class Meta:
        model = Log
        fields = ['email',]
