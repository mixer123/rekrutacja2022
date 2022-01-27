import csv

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template import RequestContext
from django.urls import reverse
from django.views import generic

from .models import *
from django.db.models import Count
from django.shortcuts import redirect

from .models import Upload
from .forms import UploadForm
from django.shortcuts import render
# Create your views here.
import os




def starting_page(request):

    return render(request, 'licznik/index.html')


def admin_page(request):
    return redirect('/admin/')

@login_required(login_url='admin-page')
def zestawienie(request):
    all_klas = Klasa.objects.all()
    all_document = Oryginal.objects.all()
    all_kandydat = Kandydat.objects.all()
    il_document = Kandydat.objects.values('document').annotate(Count('id'))
    il_document = Kandydat.objects.all().select_related('document').select_related('clas')
    il_document_groupby = Kandydat.objects.all().select_related('document').select_related('clas')

    kand_docum = Kandydat.objects.values('clas','document').annotate(m=Count('document')).values('clas__name','m','document__name')
    return render(request, 'licznik/zestawienie.html', {'kand_docum': kand_docum})

def error(request):
    return render(request, 'licznik/error.html')


@login_required(login_url='login')
def uploadfile(request):
    try:
        Upload.objects.all().delete()
        list_oc = []
        for i in Ocena.objects.all():
            list_oc.append(i.ocena)
        ocena_min = sorted(list_oc)[0]
        ocena_id=Ocena.objects.get(ocena=ocena_min)
        dir = 'media/'

        for f in os.listdir(dir):
            os.remove(os.path.join(dir, f))
        # Handle file upload
        if request.method == 'POST':
            form = UploadForm(request.POST, request.FILES)
            if form.is_valid():
                docfile = Upload(file = request.FILES['docfile'])
                docfile.save()
                firstfile = Upload.objects.all()[0].file

                with open('media/' + str(firstfile), newline='') as csvfile:
                     spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
                     for row in spamreader:
                           row_strip_0=row[0].strip()
                           row_strip_1 = row[1].strip()
                           row_strip_2 = row[2].strip()
                           row_strip_3 = str(row[3].strip())
                           kandydat = Kandydat(family_name=row_strip_0,
                                         second_name1=row_strip_1,
                                         second_name2=row_strip_2,
                                         pesel=row_strip_3,
                                         j_pol_egz=0,
                                         mat_egz=0,
                                         suma_pkt=0,
                                         j_obcy_egz=0,
                                         j_pol_oc=ocena_id,
                                         mat_oc=ocena_id,
                                         biol_oc=ocena_id,
                                         inf_oc=ocena_id,
                                         )

                           kandydat.save()

                return redirect('/')
        else:
            form = UploadForm() # A empty, unbound form
    except IndexError:
        return redirect('/error/')

    # Load documents for the list page
    documents = Upload.objects.all()

    # Render list page with the documents and the form
    return render(request, 'licznik/uploadfile.html',  {'documents': documents, 'form': form})
