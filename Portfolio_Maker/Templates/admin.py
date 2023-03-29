from django.contrib import admin
from .models import Offer,Detail
from django.contrib.admin.sites import site
from Services.models import Portfolio,Resume
import csv,io
from django.http import HttpResponse,FileResponse
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
# Register your models here.

class Admin_Offer(admin.ModelAdmin):
    model = Offer
    fields = [ 'Offer_id', 'Offer', 'Offer_value', 'Start_date','End_date' ]
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

admin.site.register(Offer,Admin_Offer),

class Admin_Temp_Detail(admin.ModelAdmin):
    model = Detail
    fields = [ 'Temp_Cat', 'Temp_Type', 'Temp_name', 'Temp_cat','Temp_type','Temp_date','Temp_img1','Temp_img2','Temp_img3','Temp_des','Temp_price','Temp_file','Temp_active','Temp_offer' ]
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
    

admin.site.register(Detail,Admin_Temp_Detail),
class Admin_Temp_Detail(admin.ModelAdmin):
    model = Portfolio
    fields = [ 'Portfolio_id', 'Template', 'User']
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
admin.site.register(Portfolio,Admin_Temp_Detail),

class Admin_Temp_Detail(admin.ModelAdmin):
    model = Resume
    fields = [ 'Resume_id', 'Template', 'User']
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
admin.site.register(Resume,Admin_Temp_Detail)