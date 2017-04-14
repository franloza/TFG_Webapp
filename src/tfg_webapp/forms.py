from django import forms
from multiselectfield import MultiSelectFormField

from tfg_webapp.models import DataFile, ReportSettings


class DataFileForm(forms.ModelForm):
    class Meta:
        model = DataFile
        fields = ('data_file',)
        labels = {
            'data_file': ''
        }


class ColumnsForm(forms.Form):

    _COLUMNS = {'Mean', 'Std', 'Max', 'Min', 'MAGE'}

    def __init__(self, *args, **kwargs):
        super(ColumnsForm, self).__init__(*args, **kwargs)
        self.fields['columns'] = MultiSelectFormField(choices=ReportSettings.COLUMN_TYPES)

    def is_valid(self):
        return super(ColumnsForm, self).is_valid() and set(self.cleaned_data['columns']) <= self._COLUMNS

