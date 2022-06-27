from django.contrib import admin


# from django.http import HttpResponseRedirect
from django.urls import path
from django.shortcuts import redirect
from import_export import resources
from import_export.admin import ExportMixin, ImportMixin
# from django.contrib import messages
# from django_object_actions import DjangoObjectActions
# from django.urls import reverse
# from admin_tools.menu import items, Menu
from django.contrib import admin
from import_export.fields import Field
from import_export.forms import ImportForm, ConfirmImportForm

from .models import *
# from import_export.admin import ImportExportMixin
# from import_export.admin import ImportExportActionModelAdmin
# from import_export.admin import ImportExportModelAdmin
from django import forms
from import_export.formats import base_formats



# Register your models here.
# admin.site.register(Klasa)
# admin.site.register(Oryginal)
# admin.site.register(Ocena)
# admin.site.register(Kandydat)

#
# class MyMenu(Menu):
#     def __init__(self, **kwargs):
#         super(MyMenu, self).__init__(**kwargs)
#         self.children += [
#             items.MenuItem('Home', reverse('admin:index')),
#             items.AppList('Applications'),
#             items.MenuItem('Multi level menu item',
#                 children=[
#                     items.MenuItem('Child 1', '/foo/'),
#                     items.MenuItem('Child 2', '/bar/'),
#                 ]
#             ),
#         ]




class CustomImportForm(ImportForm):
    author = forms.ModelChoiceField(
        queryset=Kandydat.objects.all(),
        required=True)

class CustomConfirmImportForm(ConfirmImportForm):
    author = forms.ModelChoiceField(
        queryset=Kandydat.objects.all(),
        required=True)






class KlasaAdmin(admin.ModelAdmin):
    list_display = ['name']
    

admin.site.register(Klasa, KlasaAdmin)



class OryginalAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

admin.site.register(Oryginal, OryginalAdmin)



class OcenaAdmin(admin.ModelAdmin):
    list_display = ['ocena']


admin.site.register(Ocena, OcenaAdmin)




class KandydatResources(resources.ModelResource):

    family_name = Field(attribute="family_name", column_name="Nazwisko")
    second_name1 = Field(attribute="second_name1", column_name='Imię1')
    second_name2 = Field(attribute="second_name2", column_name='Imię2')
    pesel = Field(attribute="pesel" ,  column_name = "Pesel")
    suma_pkt = Field(attribute="suma_pkt", column_name="Pkt")
    class Meta:
        model = Kandydat
        # skip_unchanged = True
        # report_skipped = True
        fields = ('family_name','second_name1','second_name2','pesel','suma_pkt','document')






class KandydatAdmin(ExportMixin, admin.ModelAdmin):
    change_list_template = "admin/licznik/kandydat/kandydat_changelist.html"

    list_display = ['family_name','second_name1', 'document', 'clas', 'suma_pkt','pesel']
    search_fields = ['family_name', 'pesel','document__name','second_name1','second_name2']
    list_filter = ['document', 'clas','internat']
    resource_class = KandydatResources
    list_per_page = 20


    def get_export_formats(self):

        formats = (
            base_formats.CSV,
            base_formats.XLS,

        )
        return [f for f in formats if f().can_export()]



    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('wp/', self.import2),

        ]
        return my_urls + urls


    def import2(request, queryset):
        from django.http import HttpResponseRedirect
        return HttpResponseRedirect(f'/zestawienie/')



    def f_pesel(self,nr):
        if len(nr) == 11:
            for char in list(nr):
                if char.isdigit():
                    status = True
                else:
                    status = False
                    break
        else:
            status = False
        return status


    def response_add(self, request, obj, post_url_continue=None):
        if obj.f_pesel(obj.pesel) == True:
            msg = "Dodano kandydata"
        else:
            msg = ""

        self.message_user(request, msg, level=messages.SUCCESS)
        return self.response_post_save_add(request, obj)

    def response_change(self, request, obj, post_url_continue=None):
        if obj.f_pesel(obj.pesel) == True:
            msg = f"Dokonano zmian {obj.family_name} {obj.second_name1}"

        else:
            msg = ""
        messages.add_message(request, messages.INFO, msg)
        return self.response_post_save_add(request, obj)



    def save_model(self, request, obj, form, change):
        if obj.f_pesel(obj.pesel) == False:
            messages.add_message(request, messages.ERROR, 'Błędny pesel')

            return redirect('/admin/licznik/kandydat/')

        super(KandydatAdmin, self).save_model(request, obj, form, change)


admin.site.register(Kandydat, KandydatAdmin)
