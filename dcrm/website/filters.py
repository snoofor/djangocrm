import django_filters
from .models import Record

class RecordFilter(django_filters.FilterSet):
    class Meta:
        model = Record
        fields = {'first_name': ['contains'],
                  'last_name': ['contains'], 
                  'city': ['contains']}
