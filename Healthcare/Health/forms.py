from django.forms import ModelForm
# from django.contrib.auth.forms import UserCreationForm
from .models import Doctor,Patient,Medical_Report,Extra_Values
from django.contrib.auth.models import User




# class RegisterForm(UserCreationForm):
#     email = forms.EmailField(required=True)
# #     # profile_image = forms.FileField()
#     # type_user = forms.ChoiceField(choices=[('Pa')],required=True)


#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']

class DoctorCreationForm(ModelForm):
    class Meta:
        model = Doctor
        fields = ["Name","email","mobile_number","Profile_pic","Date_of_birth","street","city","state","country","Experience","Position","Profession","About_me","Education_from"]

class PatientCreationForm(ModelForm):
    class Meta:
        model = Patient
        fields = ["user_name","profile_pic","Date_of_birth","user_relationship","father_name","mother_name","street","city","state","country"]

class MedicalReportForm(ModelForm):
    class Meta:
        model = Medical_Report
        fields = ["Report_name","Hospital","Patient_name","Doctor_name","Date_of_scan","Date_of_recieved","Blood_pressure","Sugar_level"]

class ExtraValuesForm(ModelForm):
    class Meta:
        model = Extra_Values
        fields = ["parameter_name","parameters_value"]
         
