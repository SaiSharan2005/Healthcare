from django.shortcuts import render,redirect
from .forms import DoctorCreationForm,PatientCreationForm
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .models import Patient

# Create your views here.

def home(request):
    return render(request,"Health/home.html")

def sign_up(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        print(form)
        if form.is_valid():
            user=form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request,user)
            return redirect('type_user')

    context = {"form":form}
    return render(request ,"Health/sign_up.html",context)

def log_in(request):
    if request.method =="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            pass
    return render(request,'Health/log_in.html')

def log_out(request):
    logout(request)
    return redirect('home')

def type_user(request):
    if request.method =="POST":
        choice = request.POST.get('image')
        if choice == 'doctor':
            return redirect('doctor_form')
        if choice == 'patient':
            return redirect('patient_form')
        print(choice)

    return render(request,"Health/type_user.html")
def doctor_form(request):
    form = DoctorCreationForm()
    if request.method == "POST":
        form = DoctorCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit = False)
            user.host = request.user
            user.save()
            return redirect('home')
    context={'form':form}
    return render(request,'Health/doctor_form.html',context)

def patient_form(request):
    form = PatientCreationForm()
    if request.method == "POST":
        # form.host = request.user
        form = PatientCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit = False)
            user.host= request.user
            user.save()
            return redirect('home')

    context={'form':form}
    return render(request,'Health/doctor_form.html',context)

def choice_acc(request):
    form = Patient.objects.filter(host = request.user)
    # print(data)
    context = {"form":form}
    return render(request,"Health/choice_acc.html",context)

