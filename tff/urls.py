from django.urls import path
from . import views

urlpatterns = [
    # Auth
    path("", views.login_view, name="login"),
    path("register/", views.register_view, name="register"),
    path("ICTregister/", views.ICTregister_view, name="ICTregister"),
    path('ict/dashboard/', views.ict_member_dashboard, name='ict_member_dashboard'),
    #path('ict/request/material/', views.ict_request_material, name='request_material'),
    path('ict/request/holiday/', views.ict_request_holiday, name='request_holiday'),
    path('ict/request/appointment/', views.ict_request_appointment, name='request_appointment'),
    path('ict/request/<int:pk>/', views.request_detail, name='request_detail'),   # ✅ single detail
    path('ict/request/<int:pk>/edit/', views.request_edit, name='request_edit'), # ✅ single edit
    path('ict/request/<int:pk>/', views.ict_request_detail, name='request_detail'),
    path('ict/request/<int:pk>/edit/', views.ict_request_edit, name='request_edit'),
    path("Procurementregister/", views.Procurementregister_view, name="Procurementregister"),
    path("Administrationregister/", views.Administrationregister_view, name="Administrationregister"),
    path("Hrregister/", views.Hrregister_view, name="Hrregister"),
    path("logout/", views.logout_view, name="logout"),

    # Core pages
    path("dashboard/<int:pk>/", views.dashboard, name="dashboard"),
    path("manage-users/", views.manage_users, name="manage_users"),
    path("all-requests/", views.all_requests, name="all_requests"),
    path("hr_dashboard/<int:pk>/", views.hr_dashboard, name="hr_dashboard"),
    path('ICT_dashboard/<int:pk>/', views.ICT_dashboard, name="ICT_dashboard"),
    path("procurement_dashboard/<int:pk>/", views.procurement_dashboard, name="procurement_dashboard"),
    path("administration_dashboard/<int:pk>/", views.administration_dashboard, name="administration_dashboard"),
    path("userhr_dashboard/<int:pk>/", views.userhr_dashboard, name="userhr_dashboard"),
    path('userICT_dashboard/<int:pk>/', views.userICT_dashboard, name="userICT_dashboard"),
    path("userprocurement_dashboard/<int:pk>/", views.userprocurement_dashboard, name="userprocurement_dashboard"),
    path("useradministration_dashboard/<int:pk>/", views.useradministration_dashboard, name="useradministration_dashboard"),

    path("requests_material/<int:pk>/", views.request_material, name="request_material"),
    path("requests_holiday/<int:pk>/", views.request_holiday, name="request_holiday"),
    path("requests_appointment/<int:pk>/", views.request_appointment, name="request_appointment"),
    path("my-requests/", views.my_requests, name="my_requests"),
    path("requests/<int:pk>/", views.request_detail, name="request_detail"),
    path("requests/<int:pk>/edit/", views.request_edit, name="request_edit"),
    path("approvals/", views.approvals, name="approvals"),
    path("finance/", views.finance, name="finance"),
    path("profile/", views.profile, name="profile"),
    path("update_material_req/<int:pk>/",views.update_material_req,name="update_material_req"),
    path("update_holiday_req/<int:pk>/",views.update_holiday_req,name="update_holiday_req"),
    path("update_appointment_req/<int:pk>/",views.update_appointment_req,name="update_appointment_req"),
    path('approve/<int:pk>/', views.approve_request, name='approve_request'),
    path('reject/<int:pk>/', views.reject_request, name='reject_request'),
    path('forward/<int:pk>/', views.forward_request, name='forward_request'),
path('approve_holiday/<int:pk>/', views.approve_holiday, name='approve_holiday'),
path('reject_holiday/<int:pk>/', views.reject_holiday, name='reject_holiday'),
path('forward_holiday/<int:pk>/', views.forward_holiday, name='forward_holiday'),
path('approve_appointment/<int:pk>/', views.approve_appointment, name='approve_appointment'),
path('reject_appointment/<int:pk>/', views.reject_appointment, name='reject_appointment'),
path('forward_appointment/<int:pk>/', views.forward_appointment, name='forward_appointment'),
]
