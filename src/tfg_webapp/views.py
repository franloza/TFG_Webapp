import codecs
import tempfile

from django.http import HttpResponse
from django.shortcuts import redirect
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

from lib.glycemic_patterns.glycemic_patterns.model.Model import Model, DataFormatException
from tfg_webapp.forms import ColumnsForm
from tfg_webapp.models import ReportSettings, DataFile
from tfg_webapp.settings.base import BASE_DIR, MEDIA_ROOT
from . import forms
from os.path import join
from os import sep

import logging


logger = logging.getLogger("project")

class HomePage(generic.TemplateView):
    template_name = "home.html"


class AboutPage(generic.TemplateView):
    template_name = "about.html"


class ReportPage(LoginRequiredMixin, generic.TemplateView):

    template_name = "tfg_webapp/report.html"
    http_method_names = ['get', 'post']

    def get(self, request, *args, **kwargs):
        user = self.request.user
        if "data_file_form" not in kwargs:
            kwargs["data_file_form"] = forms.DataFileForm()

        # Add report settings to the page documents for the list page
        try:
            report_settings = ReportSettings.objects.get(user=user)
            kwargs["data_files"] = DataFile.objects.filter(settings=report_settings)
            kwargs["columns_form"] = ColumnsForm()
            kwargs["checked_columns"] = report_settings.columns
        except ReportSettings.DoesNotExist:
            pass
        except DataFile.DoesNotExist:
            pass

        return super(ReportPage, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):

        user = self.request.user
        settings = ReportSettings.objects.get(user=user)
        if "upload_file" in request.POST:
            data_file = DataFile(settings=settings)
            data_file = forms.DataFileForm(request.POST, request.FILES, instance=data_file)

            if not data_file.is_valid():
                messages.error(request, "There was a problem with the form. "
                               "Please check the details.")
                data_file = DataFile(settings=settings)
                data_file_form = forms.DataFileForm(instance=data_file)
                return super(ReportPage, self).get(request, data_file_form=data_file_form)

            # Forms is fine. Time to save!
            data_file.save()
            messages.success(request, "Data file uploaded")
            logger.info('{} has uploaded a data file')
            return redirect("report")
        elif "generate_report" in request.POST:
            columns = request.POST.getlist("columns")
            if columns and not forms.ColumnsForm(request.POST).is_valid():
                messages.error(request, "There was a problem with the feature selection."
                                        "Please check the details.")
                return redirect("report")
            settings.columns = columns
            settings.save()

            # Generate report
            data_files = DataFile.objects.filter(settings=settings)
            filepaths = [join(BASE_DIR, *(data_file.data_file.url.split(sep))) for data_file in data_files]
            if filepaths:
                metadata = {"Patient_Name": user.name,
                            "UUID": user.profile.slug}
                try:
                    trees = Model(filepaths, metadata=metadata)
                except DataFormatException as e:
                    messages.error(request, '{} .Please, upload a different data file'.format(e))
                    return redirect("report")

                trees.fit(columns)
                report = trees.generate_report(output_path=join(MEDIA_ROOT, 'trees'), to_file=False)

                # Creating http response
                response = HttpResponse(report, content_type='application/pdf')
                response['Content-Disposition'] = 'filename="report.pdf"'
                messages.success(request, "Report has been generated successfully")
                return response
            else:
                messages.error(request, "It is necessary to upload a datafile before generating a report")
                return redirect("report")




    def delete_datafile(request,  *args, **kwargs):
        pk =  kwargs["pk"]
        df = DataFile.objects.get(pk=pk)
        user = request.user
        settings = ReportSettings.objects.get(user=user)
        if(df.settings == settings):
            df.delete()
            messages.success(request, "Data file deleted")
            logger.info('{} has deleted a data file')
        else:
            messages.error(request, "There was a problem deleting the file. Try again")
        return redirect("report")




