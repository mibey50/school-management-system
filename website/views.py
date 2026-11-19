from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import StudentForm
from .models import Student


def home(request):
    return render(request, 'website/home.html')


def student_list(request):
    students = Student.objects.all()
    return render(request, 'website/students.html', {'students': students})


def register_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registered successfully!')
            return redirect('register')
    else:
        form = StudentForm()

    return render(request, 'website/register.html', {'form': form})