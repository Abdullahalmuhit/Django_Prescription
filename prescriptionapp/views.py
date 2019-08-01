from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.http import HttpResponse
from .models import Prescription

# Create your views here.
def index(request):

    return render(request, 'index.html')

def create(request):
    # print(request.POST)
    # p_name = request.GET['name']
    # gen = request.GET['gender']
    # age = request.GET['age']
    # number = request.GET['number']
    # date = request.GET['date']
    # doctor_prefarance = request.GET['doctor_prefarance']
    # details = request.GET['details']
    # pressure = request.GET['bp']
    # pulse = request.GET['pulse']
    # #treatment = request.GET['treatment']
    # guide = request.GET['day']
    # medicine = request.GET['save']
        print(request.POST)
        name=request.GET['name']
        gender=request.GET['gender']
        number=request.GET['number']
        age=request.GET['age']
        date=request.GET['date']
        doctor_prefarance=request.GET['doctor_prefarance']
        details=request.GET['details']
        test=request.GET['selected']
        bp=request.GET['bp']
        pulse=request.GET['pulse']
        treatment=request.GET['treatment']
        guid=request.GET['guid']
        #medicine=request.GET['medicine']
        store=Prescription(patient_name=name, gender=gender, age=age, phone=number, prescription_date=date,
                                    doctor_Preference=doctor_prefarance, description=details, treatment=treatment,
                                    blood_pressure=bp, pulse= pulse, guide=guid, test=test)
        store.save()
        return redirect('index')
