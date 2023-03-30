from django.contrib import admin
from django.contrib.admin.sites import site
from .models import contact,feedback
import csv,io
from django.http import HttpResponse,FileResponse
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch

# Register your models here.

class Admin_contact(admin.ModelAdmin):
    model = contact
    fields = [ 'name', 'email', 'subject', 'message' ]
    actions = ['export_as_csv']

    def export_as_csv(self,request,queryset):
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response    

    export_as_csv.short_description = 'Export as csv'

    
admin.site.register(contact,Admin_contact)
admin.site.register(feedback)