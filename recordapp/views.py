from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse
from .models import Patient_info
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
            patient_form.save()
            patient_id = request.POST['patient_form']
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
    
        
        
    
    