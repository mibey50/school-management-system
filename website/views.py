from django.shortcuts import render,redirect
from .models import Student
from .forms import StudentForm

def student_list(request):
    students = Student.objects.all()

    return render(request, 'students.html', {
        'students': students
    })

def register_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = StudentForm()

    return render(request, 'website/register.html', {
        'form': form
    })
