from django.shortcuts import render
from .forms import StudentForm
# Create your views here.

def home(request):
    context = {}
    context["form"] = StudentForm
    return render(request, 'students_form.html', context)