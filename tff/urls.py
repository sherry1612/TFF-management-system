from django.urls import path
from . import views

urlpatterns = [
    # Auth
    path("login/", views.login_view, name="login"),
    path("register/", views.register_view, name="register"),
    path("logout/", views.logout_view, name="logout"),

    # Core pages
    path("", views.dashboard, name="dashboard"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("requests/material/", views.request_material, name="request_material"),
    path("requests/holiday/", views.request_holiday, name="request_holiday"),
    path("requests/appointment/", views.request_appointment, name="request_appointment"),
    path("my-requests/", views.my_requests, name="my_requests"),
    path("approvals/", views.approvals, name="approvals"),
    path("finance/", views.finance, name="finance"),
    path("profile/", views.profile, name="profile"),
]
