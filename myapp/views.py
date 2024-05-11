from django.shortcuts import render
from django.http import HttpResponse
from .forms import StudentForm
# Create your views here.

def home(request):

    if request.method =="POST":
        form = StudentForm(request.POST)
        if(form.is_valid()):
            first_name = form.cleaned_data["first_name"]
            return HttpResponse(f"Thank you , {first_name}")

    #GET
    context = {}
    context["form"] = StudentForm
    return render(request, 'students_form.html', context)