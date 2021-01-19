from django.shortcuts import render
from django.http import HttpResponse
from .forms import InfoForm
from .models import Info

def index(request):
    all_info = Info.objects.all()
    return render(request, 'index.html', {'all_info':all_info} )

def create_port(request):
    form = InfoForm(request.POST, request.FILES)
    if form.is_valid():
        photo = form.cleaned_data.get('photo')
        first_name = form.data.get('first_name')
        last_name = form.data.get('last_name')
        address = form.data.get('address')
        about_me = form.data.get('about_me')
        interest = form.data.get('interest')
        phone_number = form.data.get('phone_number')
        high_school = form.data.get('high_school')
        high_school_gpa = form.data.get('high_school_gpa')
        university = form.data.get('university')
        department = form.data.get('department')
        faculty = form.data.get('faculty')
        university_gpa = form.data.get('university_gpa')
        info = Info(photo=photo, first_name=first_name, last_name=last_name, address=address,
        about_me=about_me, interest=interest,phone_number=phone_number, high_school=high_school,
        high_school_gpa=high_school_gpa, university=university, department=department, faculty=faculty,
        university_gpa=university_gpa)
        info.save()
    return render(request, 'create-port.html', {'form':form})
