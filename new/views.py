from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Hospital,Staff,Patient,Mind
from django.contrib.auth.hashers import check_password,make_password
import time

# Create your views here.
def Home(request):
    return render(request,"index.html")

def AboutCare(request):
    return render(request,"aboutCare.html")

def MindCare(request):
    if request.method=="POST":
        name=request.POST.get("name")
        age=request.POST.get("age")
        social_worker=request.POST.get("social_worker")
        mental_illness=request.POST.get("condition")
        severity=request.POST.get("severity")
        note=request.POST.get("notes")
        if Mind.objects.filter(name=name).exists():
            messages.error(request,"This client has been registered already")
            time.sleep(2)
            return redirect("mindcare")
        else:
            Mind.objects.create(
                name=name,
                age=age,
                socialworker=social_worker,
                mentalillness=mental_illness,
                conditionseverity=severity,
                additionalnote=note
            )
            messages.success(request,"Information has been stored")
            time.sleep(3)
            return redirect("mindcareDashboard")
    return render(request,"mindCare.html")

def MindcareDashboard(request):
    user=Mind.objects.all()
    context={
        "user":user
    }
    return render(request,"mindcareDashboard.html",context)

def MedVerify(request):
    return render(request,"medverify.html")

def SignUp(request):
    if request.method=="POST":
        name=request.POST.get("hospital")
        email=request.POST.get("email")
        password=request.POST.get("password")
        con_password=request.POST.get("confirm_password")

        if password != con_password:
            messages.error(request,"****Password does not match****")
            return redirect("signup")
        else:
            if Hospital.objects.filter(email=email).first():
                messages.success(request,"You have an Acccount")
                time.sleep(2)
                return redirect("login")
            

            Hospital.objects.create(
                name=name,
                email=email,
                password=make_password(password)
            )
            
            messages.success(request,"Account created successfully")
            time.sleep(3)
            return redirect("login")

    return render(request,"signup.html")


def Login(request):
    if request.method=="POST":
        email=request.POST.get("email")
        password=request.POST.get("password")
        if Hospital.objects.filter(email=email).first():
            user=Hospital.objects.get(email=email)
            
            
            if check_password(password,user.password):
                messages.success(request,"Login successfull")
                request.session["hospital_id"]=user.id
                time.sleep(3)
                return redirect("HospitalDashboard")
        else:
            messages.error(request,"Account does not exist")
            return redirect("login")
    return render(request,"login.html")

def HospitalDashboard(request):
    user=request.session.get("hospital_id")
    if user==None:
        return redirect("login")
    hospital=Hospital.objects.all()
    pts=Patient.objects.all()
    staff=Staff.objects.all()
    context={
        "hospital":hospital,
        "patient":pts,
        "staff":staff
    }
   
    return render(request,"hospitalDashboard.html",context)


def failed(request):
    return render(request,"medverifyFailed.html")

def success(request):
    return render(request,"medverifySuccess.html")

def staffLogin(request):
    if request.method=="POST":
        staff=Staff.objects.all()
        id=request.POST.get("staff_id")
        if staff.filter(uniqueid=id).exists():
            messages.success(request,"You will be rredircted Shortly")
            request.session["staff_id"]=id
            # staff_info=Staff.objects.filter(unique_id=id).first()


            time.sleep(3)
            return redirect("staffDashboard")
        else:
            messages.error(request,"ID not found")
            time.sleep(2)
            return redirect("staffLogin")
    return render(request,"staffLogin.html")

def staffDashboard(request):
    staff=request.session.get("staff_id")
    if staff==None:
        return redirect("staffLogin")
    else:
        # staff_data=staff_info
        staff_id=Staff.objects.filter(uniqueid=staff).first()
        context={
            "s":staff_id
        }
        pass
    return render(request,"staffDashboard.html",context)
def Logout(request):
    request.session["hospital_id"]=None
    return redirect("home")
    # return render(request,"logout.html")

def PatientLogin(request):
    
    if request.method=="POST":
        email=request.POST.get("email")
        password=request.POST.get("password")
        user=Patient.objects.filter(email=email).first()
        if user:
            validate=check_password(password,user.password)
            if validate:
                request.session["patient"]=user.id
                messages.success(request,"You will be redirected soon")
                time.sleep(4)
                # pts_id=user.id?
                return redirect("patientDashboard")
            else:
                messages.error(request,"Password is Incorrect")
                time.sleep(4)
                return redirect("patientLogin")
        else:
            messages.error(request,"Account does not Exist")
            time.sleep(4)
            return redirect("PatientSignup")
        
    return render(request,"patientlogin.html")


def PatientSignup(request):
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        phone=request.POST.get("num")
        password=request.POST.get("password")
        con_password=request.POST.get("confirm_password")

        user=Patient.objects.filter(email=email).first()
        if user:
            messages.error(request,"Account exists")
            time.sleep(3)
            return redirect("patientLogin")
        
        if password != con_password:
            messages.error(request,"Password does not match")
            return redirect("patientSignup")
        
        else:
            Patient.objects.create(
                name=name,
                email=email,
                phonenumber=phone,
                password=make_password(password)
            )
            messages.success(request,"Account Created Successfully")
            time.sleep(3)
            return redirect("patientDashboard")


    return render(request,"patientsignup.html")


def patientDashboard(request):
    patient_id=request.session.get("patient")
    if patient_id==None:
        return redirect("patientLogin")
    patient = Patient.objects.filter(id=patient_id).first()
    context={
        "patient":patient
    }
    # pts_info=pts_id
    return render(request,"patientDashboard.html",context)