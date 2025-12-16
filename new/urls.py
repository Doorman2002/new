from django.urls import path
from . import views
urlpatterns = [
    path("",views.Home,name="home"),
    path("about_medcore/",views.AboutCare,name="aboutCare"),
    path("mindcare/",views.MindCare,name="mindcare"),
    path("medverify/",views.MedVerify,name="medverify"),
    path("hospital_portal_signup/",views.SignUp,name="signup"),
    path("hospital_portal_login/",views.Login,name="login"),
    path("mindcare_dashboard/",views.MindcareDashboard,name="mindcareDashboard"),
    path("hospital_dashboard/",views.HospitalDashboard,name="HospitalDashboard"),
    path("patient_dashboard/",views.patientDashboard,name="patientDashboard"),
    path('medVerify_failed',views.failed,name="failed"),
    path('medVerify_success',views.success,name="success"),
    path('staff_login/',views.staffLogin,name="staffLogin"),
    path('staff_dashboard/',views.staffDashboard,name="staffDashboard"),
    path("logout/",views.Logout,name="Logout"),
    path("patient_signup/",views.PatientSignup,name="patientSignup"),
    path("patient_login/",views.PatientLogin,name="patientLogin")
]
