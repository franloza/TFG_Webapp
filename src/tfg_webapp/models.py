from __future__ import unicode_literals

import os

from django.db import models
from django.conf import settings
from multiselectfield import MultiSelectField


def generate_filename(self, filename):
    url = '{0}/{1}/{2}'.format('data_files', self.settings.user.profile.slug, filename)
    return url

class ReportSettings(models.Model):

    COLUMN_TYPES = (('Mean', 'Mean'),
              ('Std', 'Standard deviation'),
              ('Max', 'Maximum'),
              ('Min', 'Minimum'),
              ('MAGE', 'MAGE'))

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        primary_key=True,
        on_delete=models.CASCADE,
    )
    columns = MultiSelectField(choices=COLUMN_TYPES, default="Mean,Std,Max,Min,MAGE")


class DataFile(models.Model):
    settings = models.ForeignKey(ReportSettings)
    data_file = models.FileField(upload_to=generate_filename)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def filename(self):
        return os.path.basename(self.data_file.name)

    def __str__(self):
        return "{}". format(os.path.basename(self.data_file.name))


