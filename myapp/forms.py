from django import forms

COURSES = (
    ("BS-CS","Computer Science"),
    ("BS-DS","Data Science"),
    ("BS-IS","Information Systems"),
    ("BS-IT","Information Technology")
)
class StudentForm(forms.Form):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    age = forms.IntegerField(required=True)
    email = forms.EmailField(required=True)
    course = forms.ChoiceField(choices = COURSES, required=True)