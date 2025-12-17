from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
# class CustomUser(AbstractUser):
#     username = models.CharField(max_length=150, unique=True)
#     email = models.EmailField(unique=True)

#     USERNAME_FIELD = 'username'
#     REQUIRED_FIELDS = ['email']

#     def __str__(self):
#         return self.username
    
class Hospital(models.Model):
    name=models.TextField(blank=False,null=False)
    email=models.EmailField(blank=False,null=False,unique=True)
    password=models.CharField(max_length=100)

class Staff(models.Model):
    staff=models.ForeignKey(Hospital,on_delete=models.CASCADE,null=True)

    name=models.TextField(blank=False,null=False)
    email=models.EmailField(blank=False,null=False,unique=True)
    phonenumber=models.IntegerField(blank=False,null=False)
    occupation=models.TextField(blank=False,null=False)
    uniqueid=models.CharField(blank=False,null=False)
    datejoined=models.CharField(blank=False,null=False)
    empstat=models.CharField()
    dept=models.CharField(blank=False,null=False)

class Patient(models.Model):
    user = models.ForeignKey(Hospital, on_delete=models.CASCADE, null=True)
    appointmentdate = models.CharField(blank=False, null=False, default="2025/12/16")
    appointmentstaff = models.CharField(blank=False, null=False, default="staff")
    appointmentpurpose = models.CharField(blank=False, null=False, default="checkup")
    name = models.TextField(blank=False, null=False)
    Age = models.IntegerField(blank=False, null=False, default=0)
    condition = models.TextField(blank=False, null=False, default="N/A")
    drug = models.TextField(blank=False, null=False, default="N/A")
    vitalpulse = models.CharField(blank=False, null=False, default="N/A")
    vitaltemp = models.CharField(blank=False, null=False, default="N/A")
    vitalpain = models.CharField(blank=False, null=False, default="N/A")
    vitalbp = models.CharField(blank=False, null=False, default="N/A")
    vitalresp = models.CharField(blank=False, null=False, default="N/A")
    inputin = models.CharField(blank=False, null=False, default="0")
    inputout = models.CharField(blank=False, null=False, default="0")
    waterbalance = models.CharField(blank=False, null=False, default="0")
    docnotes = models.CharField(blank=False, null=False, default="N/A")
    status = models.CharField(blank=False, null=False, default="N/A")
    bill = models.CharField(blank=False, null=False, default="0")
    labtest = models.CharField(blank=False, null=False, default="N/A")
    labdate = models.CharField(blank=False, null=False, default="N/A")
    labresult = models.CharField(blank=False, null=False, default="Pending")
    labnotes = models.CharField(blank=False, null=False, default="N/A")
    medhistory = models.TextField(blank=False, null=False, default="N/A")
    appointment = models.TextField(blank=False, null=False, default="N/A")
    email = models.EmailField(unique=True, blank=False, null=False, default="user@example.com")
    phonenumber = models.CharField(max_length=12, default="0000000000")
    password = models.CharField(blank=False, null=False, default="password")
    datebill = models.CharField(blank=False, null=False, default="N/A")
    billstatus = models.CharField(blank=False, null=False, default="Pending")
    drugtime = models.CharField(blank=False, null=False, default="N/A")
    dosage = models.CharField(blank=False, null=False, default="N/A")
    prescriber = models.TextField(blank=False, null=False, default="N/A")


# class Patient(models.Model):
#     appointment_date=models.CharField(blank=False,null=False,default="2025/12/16")
#     appointment_staff=models.CharField(blank=False,null=False,default="staff")
#     appointment_purpose=models.CharField(blank=False,null=False,default="checkup")
#     name=models.TextField(blank=False,null=False)
#     Age=models.IntegerField(blank=False,null=False)
#     condition=models.TextField(blank=False,null=False)
#     drug=models.TextField(blank=False,null=False)
#     vital_pulse=models.CharField(blank=False,null=False)
#     vital_temp=models.CharField(blank=False,null=False) 
#     vital_pain=models.CharField(blank=False,null=False)
#     vital_bp=models.CharField(blank=False,null=False)
#     vital_resp=models.CharField(blank=False,null=False)
#     input_in=models.CharField(blank=False,null=False)
#     input_out=models.CharField(blank=False,null=False)
#     water_balance=models.CharField(blank=False,null=False)
#     doc_notes=models.CharField(blank=False,null=False)
#     status=models.CharField(blank=False,null=False)
#     bill=models.CharField(blank=False,null=False)
#     lab_test=models.CharField(blank=False,null=False)
#     lab_date=models.CharField(blank=False,null=False)
#     lab_result=models.CharField(blank=False,null=False)
#     lab_notes=models.CharField(blank=False,null=False)
#     med_history=models.TextField(blank=False,null=False)
#     appointment=models.TextField(blank=False,null=False)
#     email=models.EmailField(unique=True,blank=False,null=False)
#     phone_number=models.CharField(max_length=12)
#     password=models.CharField(blank=False,null=False)
#     date_bill=models.CharField(blank=False,null=False)
#     bill_status=models.CharField(blank=False,null=False)
#     drug_time=models.CharField(blank=False,null=False)
#     dosage=models.CharField(blank=False,null=False)
#     prescriber=models.TextField(blank=False,null=False)

class Mind(models.Model):
    name=models.TextField(blank=False,null=False)
    age=models.IntegerField(blank=False,null=False)
    socialworker=models.TextField(blank=False,null=False)
    mentalillness=models.TextField(blank=False,null=False)
    conditionseverity=models.TextField(blank=False,null=False)
    additionalnote=models.TextField(blank=False,null=False)

