from django.urls import path
from . import views

urlpatterns = [
    # Auth
    path("", views.login_view, name="login"),
    path("register/", views.register_view, name="register"),
    path("ICTregister/", views.ICTregister_view, name="ICTregister"),
    path("Procurementregister/", views.Procurementregister_view, name="Procurementregister"),
   path("Administrationregister/", views.Administrationregister_view, name="Administrationregister"),
    path("Hrregister/", views.Hrregister_view, name="Hrregister"),
    path("logout/", views.logout_view, name="logout"),

    # Core pages
    path("dashboard/<int:pk>/", views.dashboard, name="dashboard"),
    path("hr_dashboard/<int:pk>/", views.hr_dashboard, name="hr_dashboard"),
    path('ICT_dashboard/<int:pk>/', views.ICT_dashboard, name="ICT_dashboard"),
    path("procurement_dashboard/<int:pk>/", views.procurement_dashboard, name="procurement_dashboard"),
    path("administration_dashboard/<int:pk>/", views.administration_dashboard, name="administration_dashboard"),
    path("userhr_dashboard/<int:pk>/", views.userhr_dashboard, name="userhr_dashboard"),
    path('userICT_dashboard/<int:pk>/', views.userICT_dashboard, name="userICT_dashboard"),
    path("userprocurement_dashboard/<int:pk>/", views.userprocurement_dashboard, name="userprocurement_dashboard"),
    path("useradministration_dashboard/<int:pk>/", views.useradministration_dashboard, name="useradministration_dashboard"),

    path("requests_material/", views.request_material, name="request_material"),
    path("requests_holiday/", views.request_holiday, name="request_holiday"),
    path("requests_appointment/", views.request_appointment, name="request_appointment"),
    path("my-requests/", views.my_requests, name="my_requests"),
    path("requests/<int:pk>/", views.request_detail, name="request_detail"),
    path("requests/<int:pk>/edit/", views.request_edit, name="request_edit"),
    path("approvals/", views.approvals, name="approvals"),
    path("finance/", views.finance, name="finance"),
    path("profile/", views.profile, name="profile"),
]
