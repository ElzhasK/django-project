from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Student, Instructor, Grades
from .forms import StudentForm, RegistrationForm, LoginForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import permission_required, login_required
from django.contrib import messages


def sdudent(request):
    return render(request, 'sdudent.html')

def result(request):
    student_id = request.GET['student_id']
    firstname = request.GET['firstname']
    lastname = request.GET['lastname']
    faculty = request.GET['faculty']
    gpa = request.GET['gpa']
    return render(request, 'result.html', {'student_id' : student_id, 'firstname' : firstname, 'lastname' : lastname, 'faculty' : faculty, 'gpa' : gpa})

def index(request):
    return render(request, 'index.html')

def show_result(request, pk):
    grades = get_object_or_404(Grades, pk=pk)
    student_info = get_object_or_404(Student, pk=pk)
    return render(request, 'show_result.html', {'student_info': student_info, 'grades':grades})

def search(request):
    if request.method == "POST":
        searched = request.POST['searched']
        students = Student.objects.filter(firstname__contains = searched)
        return render(request, 'search.html', {'searched':searched, 'students':students})
    else:
        return render(request, 'search.html', {})

def members(request):
    mystudents = Student.objects.all().values()
    myinstructors = Instructor.objects.all().values()
    template = loader.get_template('all_members.html')
    context = {'mystudents':mystudents, 'myinstructors':myinstructors}

    return HttpResponse(template.render(context, request))


def home(request):
    students = Student.objects.all()
    context = {'students': students}
    return render(request, 'home.html', context)

@permission_required('sdudent.add_student', raise_exception=True)
def create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = StudentForm()
    context = {'form': form}
    return render(request, 'create.html', context)

@permission_required('sdudent.change_student', raise_exception=True)
def update(request, id):
    student = Student.objects.get(id=id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = StudentForm(instance=student)
    context = {'form': form}
    return render(request, 'update.html', context)
    

@permission_required('sdudent.delete_student', raise_exception=True)
def delete(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('home')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'registration.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                form.add_error(None, 'Invalid login credentials.')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'profile.html', context)



