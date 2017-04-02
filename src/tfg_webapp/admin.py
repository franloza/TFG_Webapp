from __future__ import unicode_literals
from django.contrib import admin

from tfg_webapp.models import DataFile, ReportSettings


class DataFileInline (admin.StackedInline):
    model = DataFile


@admin.register(ReportSettings)
class ReportSettingsAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        if getattr(obj, 'user', None) is None:
            obj.user = request.user
        obj.save()
    def get_queryset(self, request):
        qs = super(ReportSettingsAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)
    def has_change_permission(self, request, obj=None):
        if not obj:
            return True
        return obj.user == request.user or request.user.is_superuser

    inlines = [
        DataFileInline,
    ]






