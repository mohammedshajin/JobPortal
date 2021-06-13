from django.db.models import fields
import django_filters
from .models import *
from django_filters import CharFilter


class JobFilter(django_filters.FilterSet):
    title = CharFilter(field_name="title", lookup_expr='icontains')

    class Meta:
        model = Job
        fields = ("title", "location", "salary", "experience", "jobtype" )

class JFilter(django_filters.FilterSet):
    title = CharFilter(field_name="title", lookup_expr='icontains')

    class Meta:
        model = Job
        fields = ("title", "location")
