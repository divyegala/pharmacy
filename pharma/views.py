from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from pharma.models import Staff,Doctor,Medicines,Nonmedicine, Location
from django.forms.models import model_to_dict
import requests
from json import loads


# Create your views here.
def index(request):
    return render(request, 'pharma/home.html')


def doctor(request):
    doctors=Doctor.objects.all()
    context = {'doctors': doctors, 'site': 'Our'}
    print context
    return render(request,'pharma/doctor.html', context)


def medicine(request):
    medicines = Medicines.objects.all()
    context = {'medicines': medicines, 'site': 'Our'}
    return render(request, 'pharma/medicine.html', context)


def nonmedicine(request):
    nonmedicines = Nonmedicine.objects.all()
    context = {'nonmedicines': nonmedicines, 'site': 'Our'}
    return render(request, 'pharma/nonmedicine.html', context)


def staff(request):
    staffs = Staff.objects.all()
    context = {'staffs': staffs, 'site': 'Our'}
    return render(request, 'pharma/staff.html', context)


def dispdocs(request, site):
    location = get_object_or_404(Location, loc=site)
    url = "http://" + location.ip + ":8000/get_doctor/"
    req = requests.get(url)
    context = loads(req.text.decode('utf-8'))
    context['site'] = site
    print context
    return render(request, 'pharma/doctor.html', context)


def dispmeds(request, site):
    location = get_object_or_404(Location, loc=site)
    url = "http://" + location.ip + ":8000/get_medicine/"
    req = requests.get(url)
    context = loads(req.text.decode('utf-8'))
    context['site'] = site
    print context
    return render(request, 'pharma/medicine.html', context)


def dispnonmeds(request, site):
    location = get_object_or_404(Location, loc=site)
    url = "http://" + location.ip + ":8000/get_non_medicine/"
    req = requests.get(url)
    context = loads(req.text.decode('utf-8'))
    context['site'] = site
    print context
    return render(request, 'pharma/nonmedicine.html', context)


def dispstaff(request, site):
    location = get_object_or_404(Location, loc=site)
    url = "http://" + location.ip + ":8000/get_staff/"
    req = requests.get(url)
    context = loads(req.text.decode('utf-8'))
    context['site'] = site
    print context
    return render(request, 'pharma/staff.html', context)


def get_doctor(request):
    data_dict = dict()
    data_dict["doctors"] = list()
    for d in Doctor.objects.all():
        data_dict["doctors"].append(model_to_dict(d))
    return JsonResponse(data_dict)


def get_medicine(request):
    data_dict = dict()
    data_dict["medicines"] = list()
    for m in Medicines.objects.all():
        data_dict["medicines"].append(model_to_dict(m))
    return JsonResponse(data_dict)


def get_non_medicine(request):
    data_dict = dict()
    data_dict["nonmedicines"] = list()
    for n in Nonmedicine.objects.all():
        data_dict["nonmedicines"].append(model_to_dict(n))
    return JsonResponse(data_dict)


def get_staff(request):
    data_dict = dict()
    data_dict["staffs"] = list()
    for s in Staff.objects.all():
        data_dict["staffs"].append(model_to_dict(s))
    return JsonResponse(data_dict)

