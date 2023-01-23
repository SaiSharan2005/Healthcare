from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name = "home"),
    path('sign_up/',views.sign_up,name = "sign_up"),
    path('log_in/',views.log_in,name = "log_in"),
    path('log_out/',views.log_out,name = "log_out"),
    path('type_user/',views.type_user,name = "type_user"),
    path('doctor_form/',views.doctor_form,name = "doctor_form"),
    path('patient_form/',views.patient_form,name = "patient_form"),
    path('choice_acc/',views.choice_acc,name = "choice_acc"),




    # path('/views',views.)
]