from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# class customuser(AbstractUser):
#     Type_user = (
#         ('PATIENT', 'patient'),
#         ('DOCTOR', 'doctor'),

#     )
#     # interests = models.CharField(max_length=200, null=True, editable=True)
#     type_user = models.CharField(max_length=20,choices  = Type_user,null=True)
#     email = models.EmailField(unique=True, null=True, editable=True)


# class Address(models.Model):
#     street = models.CharField(max_length=30)
#     city = models.CharField(max_length=30)
#     state = models.CharField(max_length=30)
#     country =  m
# dels.CharField(max_length=30)

#     def __str__(self):
#         return self.street


class Doctor(models.Model):
    host = models.OneToOneField(User, on_delete=models.CASCADE)
    Name = models.CharField(max_length=30)
    Profile_pic = models.ImageField(upload_to='', null=True, default="doctor.png")
    Date_of_birth = models.DateField(null=True)

    street = models.CharField(max_length=100)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    country = models.CharField(max_length=30)  

    Experience = models.PositiveIntegerField()
    Position = models.CharField(max_length=30)
    Profession = models.CharField(max_length=100)
    About_me = models.TextField(max_length=500)
    Education_from = models.CharField(max_length=100)
    email = models.EmailField(blank= False)
    mobile_number = models.IntegerField(blank = True)
 

class Patient(models.Model):
    host = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    user_name = models.CharField(max_length=30)
    profile_pic = models.ImageField(upload_to='', null=True, default="avater.svg")
    Date_of_birth = models.DateField(null=True)
    user_relationship = models.CharField(max_length=30)
    father_name = models.CharField(max_length=30)
    mother_name = models.CharField(max_length=30)
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    country = models.CharField(max_length=30)  

    def __str__(self):
        return self.user_name


class Medical_Report(models.Model):
    host = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    person = models.ForeignKey(Patient,on_delete=models.CASCADE,null=True)
    description = models.TextField(max_length=300,default="None ")

    Report_name = models.CharField(max_length=100)    
    Hospital = models.CharField(max_length=100)
    Patient_name = models.CharField(max_length=100)
    Doctor_name = models.CharField(max_length=100)
    Date_of_scan = models.DateTimeField()
    Date_of_recieved = models.DateTimeField()
    doctor_prescription= models.TextField(max_length=300,default="None ")
    Blood_pressure = models.IntegerField()
    Sugar_level = models.IntegerField()

    def __str__(self):
        return self.Report_name

class Extra_Values(models.Model):
    Extra_parameters = models.ForeignKey(Medical_Report,on_delete= models.CASCADE,null=True)
    parameter_name = models.CharField(max_length=100)
    parameters_value = models.CharField(max_length=100)
