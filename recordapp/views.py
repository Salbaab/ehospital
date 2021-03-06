from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse
from .models import Patient_info,Rank,Address, Next_of_kin, Unit, patient_pic
from .forms import Patient_info_form

# Create your views here.
def record_home(request):
    patient_form = Patient_info_form()
    context ={'patient_form':patient_form}
    return render(request, 'recordapp/home.html', context)

def add_patient(request): 
    if request.method =="POST":
        patient_form = Patient_info_form(request.POST)
        if patient_form.is_valid():
            patient=patient_form.save()
            rank = Rank(personal_info = patient)
            rank.save()
            address = Address(personal_info = patient)
            address.save()
            nok = Next_of_kin(personal_info = patient)
            nok.save()
            unit = Unit(personal_info = patient)
            unit.save()
            pic = patient_pic(personal_info = patient)
            pic.save()
        return redirect('recordapp:success')
    else: 
        patient_form = Patient_info_form()    
        context ={'patient_form':patient_form}
        return render(request, 'recordapp/home.html', context)
    
def patient_details(request, pk):
    patient_details = Patient_info.objects.get(id=pk)
    context = {'patient_details' : patient_details}
    template_name = 'recordapp/pateint_details.html'
    return render(request, template_name, context)
def success(request):
    return render(request, 'recordapp/success.html', { })
    
        
        
    
    