from django.shortcuts import render, redirect
from .forms import DoctorCreationForm, PatientCreationForm, MedicalReportForm, ExtraValuesForm
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .models import Patient, Doctor, Medical_Report, Extra_Values

# Create your views here.


def home(request):
    try:
        if Doctor.objects.get(host=request.user) is not None:
            return redirect('doctor_profile')
            # print("i am in doctoe")
    except:
        pass
    try:
        if Patient.objects.filter(host=request.user) is not None:
            return redirect('choice_acc')
    except:
        pass

    return render(request, "Health/home.html")


def sign_up(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        print(form)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('type_user')

    context = {"form": form}
    return render(request, "Health/sign_up.html", context)


def log_in(request):
    if request.method == "POST":
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        print(username + "   "+password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            pass
    return render(request, 'Health/log_in.html')


def log_out(request):
    logout(request)
    return redirect('home')


def type_user(request):
    if request.method == "POST":
        choice = request.POST.get('image')
        if choice == 'doctor':
            return redirect('doctor_form')
        if choice == 'patient':
            return redirect('patient_form')
        print(choice)

    return render(request, "Health/type_user.html")


def doctor_form(request):
    form = DoctorCreationForm()
    if request.method == "POST":
        form = DoctorCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.host = request.user
            user.save()
            return redirect('doctor_profile')
    context = {'form': form}
    return render(request, 'Health/doctor_form.html', context)


def doctor_profile(request):
    form = Doctor.objects.get(host=request.user)
    context = {"form": form}
    return render(request, 'Health/doctor_profile.html', context)


def patient_form(request):
    form = PatientCreationForm()
    if request.method == "POST":
        # form.host = request.user
        form = PatientCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.host = request.user
            user.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'Health/doctor_form.html', context)


def patient_profile(request, pk):
    form = Patient.objects.get(user_name=pk)
    medical_report = Medical_Report.objects.filter(person=form)

    context = {"form": form, "medical_report": medical_report}
    return render(request, 'Health/patient_profile.html', context)


def choice_acc(request):
    form = Patient.objects.filter(host=request.user)

    context = {"form": form}
    return render(request, "Health/choice_acc.html", context)


def medical_report(request, pk):
    form_basic = MedicalReportForm()
    form_extra = ExtraValuesForm()
    patient = Patient.objects.get(user_name=pk)

    # print("dsaf")
    if request.method == "POST":
        print("POST")
        form_basic = MedicalReportForm(request.POST)
        # form_extra = ExtraValuesForm(request.POST)
        if form_basic.is_valid():
            basic = form_basic.save(commit=False)
            basic.person = patient
            basic.host = request.user
            basic.save()
            # medical_report = Medical_Report.objects.get(Report_name = basic.Report_name)

            # form = form_extra.save(commit=False)
            # form.Extra_parameters = medical_report
            # form.save()
            return redirect("/extra_form/"+basic.Report_name)
            # return render(request,"Health/extra_medi_form.html")
    # else:
    #     form_basic = MedicalReportForm(request.POST)
    #     form_basic = ExtraValuesForm(request.POST)
    context = {"form_basic": form_basic}
    return render(request, "Health/medical_form.html", context)


def extra_fields_med(request, pk):
    form_entry = ExtraValuesForm()
    form_data = Medical_Report.objects.get(Report_name=pk)
    form = Extra_Values.objects.filter(Extra_parameters=form_data)
    # patient = Patient.objects.get(person=form_basic.)
    # print("Fuck it works")
    # print(form)
    if request.method == "POST":
        form_entry = ExtraValuesForm(request.POST)
        if form_entry.is_valid():
            form_before = form_entry.save(commit=False)
            form_before.Extra_parameters = form_data
            form_before.save()
            if request.POST.get("choice") is not None:
                return redirect("home")

    context = {"form": form, "form_data": form_data, "form_entry": form_entry}
    return render(request, "Health/extra_medi_field.html", context)
    # medical_data =

    # if request.method =="POST":
    #     form = ExtraValuesForm(request.POST)
    #     if form.is_valid():
    #         form.


def medical_form_view(request, pk):
    data_medi = Medical_Report.objects.get(id=int(pk))
    extra_data_medi = Extra_Values.objects.filter(Extra_parameters=data_medi)
    # print(data_medi)
    context = {"data_medi": data_medi, "extra_data_medi": extra_data_medi}
    return render(request, "Health/medical_form_view.html", context)


def consult_doctor(request):
    all_doc = Doctor.objects.all()
    context={"all_doc":all_doc}
    return render(request,"Health/Consult_Doctor.html",context)