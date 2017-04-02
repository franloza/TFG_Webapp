from django import forms
from tfg_webapp.models import DataFile, ReportSettings

class DataFileForm(forms.ModelForm):
    class Meta:
        model = DataFile
        fields = ('data_file',)
