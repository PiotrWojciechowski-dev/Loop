import django_filters
from django import forms
from .models import Report

REPORT_CHOICES = [
    ('Language', 'Language'),
    ('Violence', 'Violence'),
    ('Spam', 'Spam'),
    ('Harassment', 'Harassment'),
    ('Terrorism', 'Terrorism'),
    ('Hate Speech', 'Hate Speech'),
    ('Unauthorized Sales', 'Unauthorized Sales')
]

    
class ReportFilter(django_filters.FilterSet):
    report = django_filters.ChoiceFilter(
      choices=REPORT_CHOICES,
      widget=forms.Select(
          attrs={
              'class': 'form-control form-control-lg',
          }
      )
  )

    class Meta:
        model = Report
        fields = ['report']