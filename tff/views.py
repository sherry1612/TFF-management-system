from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout, login
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib.auth.models import User


# ---- Auth ----
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user:
            auth_login(request, user)
            messages.success(request, "Welcome back!")
            return redirect("dashboard")
        messages.error(request, "Invalid credentials")
    return render(request, "auth/login.html")

def register_view(request):
    # NOTE: This is a simple placeholder; integrate with your CustomUser later.
    if request.method == "POST":
        messages.success(request, "Registration submitted (demo). You can now login.")
        return redirect("login")
    return render(request, "auth/register.html")


# def login_view(request):
#     if request.method == "POST":
#         username = request.POST.get("username")   # from form
#         password = request.POST.get("password")

#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect("dashboard")  # redirect to dashboard page
#         else:
#             messages.error(request, "Invalid credentials")
#             return redirect("login")

#     return render(request, "login.html")





# def register_view(request):
#     if request.method == "POST":
#         full_name = request.POST.get("full_name")
#         department = request.POST.get("department")
#         email = request.POST.get("email")
#         phone = request.POST.get("phone")
#         username = request.POST.get("username")
#         password = request.POST.get("password")

#         if User.objects.filter(username=username).exists():
#             messages.error(request, "Username already exists")
#             return redirect("register")

#         # Create user with hashed password
#         user = User.objects.create_user(username=username, email=email, password=password)
#         user.first_name = full_name   # store full name in first_name field
#         user.save()

#         messages.success(request, "Registration successful! Please login.")
#         return redirect("login")

#     return render(request, "register.html")

def logout_view(request):
    auth_logout(request)
    return redirect("login")

# ---- Core Pages ----
@login_required(login_url="login")
def dashboard(request):
    # demo data
    stats = {"all": 8, "pending": 3, "approved": 4, "completed": 1}
    requests_list = [
        {"type": "Material", "department": "Procurement", "status": "Pending", "submitted": timezone.now().date()},
        {"type": "Holiday", "department": "HR", "status": "Approved", "submitted": timezone.now().date()},
        {"type": "Appointment", "department": "Administration", "status": "Completed", "submitted": timezone.now().date()},
    ]
    return render(request, "dashboard.html", {"stats": stats, "requests_list": requests_list})

@login_required(login_url="login")
def request_material(request):
    if request.method == "POST":
        messages.success(request, "Material request submitted (demo).")
        return redirect("my_requests")
    return render(request, "requests/request_material.html")

@login_required(login_url="login")
def request_holiday(request):
    if request.method == "POST":
        messages.success(request, "Holiday leave request submitted (demo).")
        return redirect("my_requests")
    return render(request, "requests/request_holiday.html")

@login_required(login_url="login")
def request_appointment(request):
    if request.method == "POST":
        messages.success(request, "Appointment request submitted (demo).")
        return redirect("my_requests")
    return render(request, "requests/request_appointment.html")

@login_required(login_url="login")
def my_requests(request):
    my_requests = [
        {"type": "Material", "status": "Pending", "submitted": timezone.now().date()},
        {"type": "Holiday", "status": "Approved", "submitted": timezone.now().date()},
    ]
    return render(request, "my_requests.html", {"my_requests": my_requests})

@login_required(login_url="login")
def approvals(request):
    approvals = [
        {"type": "Material", "requester": "Asha", "status": "Waiting Approval"},
        {"type": "Appointment", "requester": "Jonas", "status": "Waiting Approval"},
    ]
    return render(request, "approvals.html", {"approvals": approvals})

@login_required(login_url="login")
def finance(request):
    finance_items = [
        {"type": "Material", "amount": "350,000 TZS", "status": "To Pay"},
    ]
    return render(request, "finance.html", {"finance_items": finance_items})

@login_required(login_url="login")
def profile(request):
    if request.method == "POST":
        messages.success(request, "Profile updated (demo).")
        return redirect("profile")
    return render(request, "profile.html")

