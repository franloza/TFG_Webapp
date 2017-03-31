from __future__ import unicode_literals

import os

from django.db import models
from profiles.models import Profile


def generate_filename(self, filename):
    url = '{0}/{1}/{2}'.format('data_files', self.settings.profile.slug, filename)
    return url


class ReportSettings(models.Model):
    profile = models.OneToOneField(
        Profile,
        on_delete=models.CASCADE,
    )


class DataFile(models.Model):
    settings = models.ForeignKey(ReportSettings)
    data_file = models.FileField(upload_to=generate_filename)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{}". format(str(self.data_file.file.name))

    def filename(self):
        return os.path.basename(self.data_file.name)
