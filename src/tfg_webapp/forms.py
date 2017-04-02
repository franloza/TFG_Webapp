from django import forms
from multiselectfield import MultiSelectFormField, MultiSelectField

from tfg_webapp.models import DataFile, ReportSettings

class DataFileForm(forms.ModelForm):

    class Meta:
        model = DataFile
        fields = ('data_file',)
        labels = {
            'data_file': ''
        }



class ColumnsForm(forms.Form):
   def __init__(self, *args, **kwargs):
       super(ColumnsForm, self).__init__(*args, **kwargs)
       self.fields['columns'] = MultiSelectFormField(choices=ReportSettings.COLUMN_TYPES)

