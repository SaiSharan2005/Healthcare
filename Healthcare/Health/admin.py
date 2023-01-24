from django.contrib import admin
from .models import Patient,Doctor,Medical_Report,Extra_Values
# Register your models here.
admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Medical_Report)
admin.site.register(Extra_Values)

