from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Course, Student
from .forms import StudentRegistrationForm,CourseCreationForm

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/course_list.html', {'courses': courses})


def register_student(request, course_id):
    course = get_object_or_404(Course, id=course_id)

    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']

            if course.is_full():
                messages.error(request, "This course is already full.")
                return redirect('course_list')

            # Check if the student already exists
            student, created = Student.objects.get_or_create(email=email, defaults={'name': name})
            
            # Enroll student in course
            student.enrolled_courses.add(course)
            course.current_enrolled += 1
            course.save()

            messages.success(request, "Registration successful!")
            return redirect('course_list')
    else:
        form = StudentRegistrationForm(initial={'course_id': course_id})

    return render(request, 'courses/register_student.html', {'form': form, 'course': course})


def create_course(request):
    if request.method == 'POST':
        form = CourseCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Course created successfully!")
            return redirect('course_list')
    else:
        form = CourseCreationForm()

    return render(request, 'courses/create_course.html', {'form': form})