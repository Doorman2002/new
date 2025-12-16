from django.contrib import admin
from .models import Hospital,Staff,Patient,Mind

# Register your models here.
admin.site.register(Hospital)
admin.site.register(Staff)
admin.site.register(Patient)
admin.site.register(Mind)