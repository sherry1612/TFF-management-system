from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout, login
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib.auth.models import User
from .models import Request  
from .forms import RequestForm  
from .models import *
from .forms import *
from django.contrib import messages



# ---- Auth ----
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user:
            auth_login(request, user)
            messages.success(request, f"Welcome back, {user.username}!")
            request.session['CustomUser_id'] = user.id
            # ✅ redirect based on department field
            department = getattr(user, "department", None)  # safe way to fetch
            
            if department == "AdministrationAdmin":
              return redirect("administration_dashboard",pk=user.pk)
            elif department == "Administration":
              return redirect("useradministration_dashboard",pk=user.pk)
            elif department == "ProcurementAdmin":
                return redirect("procurement_dashboard",pk=user.pk)
            elif department == "Procurement":
                return redirect("userprocurement_dashboard",pk=user.pk)
            elif department == "FinanceAdmin":
                return redirect("finance_dashboard",pk=user.pk)
            elif department == "Finance":
                return redirect("userfinance_dashboard",pk=user.pk)
            elif department == "HRAdmin":
                return redirect("hr_dashboard",pk=user.pk)
            elif department == "HR":
                return redirect("userhr_dashboard",pk=user.pk)
            elif department == "ICTAdmin":
                return redirect("ICT_dashboard",pk=user.pk)
            elif department == "ICT":
                return redirect("userICT_dashboard",pk=user.pk)
            elif department == "admin":
                return redirect("dashboard",pk=user.pk)
            else:
                return redirect("dashboard",pk=user.pk)  # fallback if no department

        messages.error(request, "Invalid credentials")
    return render(request, "auth/login.html")

from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib import messages

User = get_user_model()

def register_view(request):
    if request.method == "POST":
        full_name = request.POST.get("full_name")
        department = request.POST.get("department")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        username = request.POST.get("username")
        password = request.POST.get("password")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect("register")

        user = User(
            full_name=full_name,
            department=department,
            email=email,
            phone=phone,
            username=username,
        )
        user.set_password(password)  # hash password
        user.save()

        messages.success(request, "Account created! You can log in now.")
        return redirect("login")

    return render(request, "admin/register.html")

def ICTregister_view(request):
    if request.method == "POST":
        full_name = request.POST.get("full_name")
        department = request.POST.get("department")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        username = request.POST.get("username")
        password = request.POST.get("password")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect("register")

        user = User(
            full_name=full_name,
            department=department,
            email=email,
            phone=phone,
            username=username,
        )
        user.set_password(password)  # hash password
        user.save()

        messages.success(request, "Account created! You can log in now.")
        return redirect("login")

    return render(request, "ICT/admin/ICTregister.html")

def Hrregister_view(request):
    if request.method == "POST":
        full_name = request.POST.get("full_name")
        department = request.POST.get("department")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        username = request.POST.get("username")
        password = request.POST.get("password")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect("register")

        user = User(
            full_name=full_name,
            department=department,
            email=email,
            phone=phone,
            username=username,
        )
        user.set_password(password)  # hash password
        user.save()

        messages.success(request, "Account created! You can log in now.")
        return redirect("login")

    return render(request, "HR/admin/Hrregister.html")

def Procurementregister_view(request):
    if request.method == "POST":
        full_name = request.POST.get("full_name")
        department = request.POST.get("department")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        username = request.POST.get("username")
        password = request.POST.get("password")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect("register")

        user = User(
            full_name=full_name,
            department=department,
            email=email,
            phone=phone,
            username=username,
        )
        user.set_password(password)  # hash password
        user.save()

        messages.success(request, "Account created! You can log in now.")
        return redirect("login")

    return render(request, "Procurement/admin/Procurementregister.html")

def Administrationregister_view(request):
    if request.method == "POST":
        full_name = request.POST.get("full_name")
        department = request.POST.get("department")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        username = request.POST.get("username")
        password = request.POST.get("password")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect("register")

        user = User(
            full_name=full_name,
            department=department,
            email=email,
            phone=phone,
            username=username,
        )
        user.set_password(password)  # hash password
        user.save()

        messages.success(request, "Account created! You can log in now.")
        return redirect("login")

    return render(request, "Administration/admin/Administrationregister.html")





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
def dashboard(request,pk):
    user = get_object_or_404(CustomUser, pk=pk) 
    
    return render(request, "admin/dashboard.html",{'user':user})


@login_required(login_url="login")
def ICT_dashboard(request,pk):
    user = get_object_or_404(CustomUser, pk=pk)  # always the logged-in user
    
    
    return render(request, "ICT/admin/dashboard.html",{'user':user} )

@login_required(login_url="login")
def procurement_dashboard(request,pk):
    user = get_object_or_404(CustomUser, pk=pk)  # always the logged-in user

    
   
    return render(request, "Procurement/admin/dashboard.html",{'user':user})


@login_required(login_url="login")
def hr_dashboard(request,pk):
    user = get_object_or_404(CustomUser, pk=pk)  # always the logged-in user

   
    return render(request, "Hr/admin/dashboard.html",{'user':user})

@login_required(login_url="login")
def administration_dashboard(request,pk):
    user = get_object_or_404(CustomUser, pk=pk)  # always the logged-in user
 
   
    return render(request, "Administration/admin/dashboard.html",{'user':user})

@login_required(login_url="login")
def userICT_dashboard(request,pk):
    user = get_object_or_404(CustomUser, pk=pk)  # always the logged-in user
    
    
    return render(request, "ICT/dashboard.html",{'user':user} )

@login_required(login_url="login")
def userprocurement_dashboard(request,pk):
    user = get_object_or_404(CustomUser, pk=pk)  # always the logged-in user

    
   
    return render(request, "Procurement/dashboard.html",{'user':user})


@login_required(login_url="login")
def userhr_dashboard(request,pk):
    user = get_object_or_404(CustomUser, pk=pk)  # always the logged-in user

   
    return render(request, "Hr/dashboard.html",{'user':user})

@login_required(login_url="login")
def useradministration_dashboard(request,pk):
    user = get_object_or_404(CustomUser, pk=pk)  # always the logged-in user
 
   
    return render(request, "Administration/dashboard.html",{'user':user})

@login_required(login_url="login")
def request_material(request):
    


    if request.method == "POST":
        form = MaterialRequisitionForm(request.POST)
        if form.is_valid():
            requisition = form.save(commit=False)
            requisition.user = request.user
            requisition.save()
            messages.success(request, "Material Requisition submitted successfully!")
            return redirect("request_material")  # redirect to same page or a list view
    else:
        form = MaterialRequisitionForm()

    return render(request, "requests/request_material.html", {"form": form})


@login_required(login_url="login")
def request_holiday(request):
    
    if request.method == "POST":
        form = HolidayLeaveRequestForm(request.POST)
        if form.is_valid():
            leave_request = form.save(commit=False)
            leave_request.user = request.user
            leave_request.save()
            messages.success(request, "Holiday Leave Request submitted successfully!")
            return redirect("request_holiday")  # redirect to same page or leave list
    else:
        form = HolidayLeaveRequestForm()

    return render(request, "requests/request_holiday.html", {"form": form})

@login_required(login_url="login")
def request_appointment(request):
    if request.method == "POST":
        form = AppointmentRequestForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.user = request.user
            appointment.save()
            messages.success(request, "Appointment Request submitted successfully!")
            return redirect("request_appointment")  # could also redirect to a list page
    else:
        form = AppointmentRequestForm()

    
    return render(request, "requests/request_appointment.html", {"form": form})

@login_required(login_url="login")
def my_requests(request):
    my_requests = Request.objects.filter(user=request.user)
    my_requests = [
        {"type": "Material", "status": "Pending", "submitted": timezone.now().date()},
        {"type": "Holiday", "status": "Approved", "submitted": timezone.now().date()},
    ]
    return render(request, "my_requests.html", {"my_requests": my_requests})
@login_required
def request_detail(request, pk):   # NEW (view only)
    req = get_object_or_404(Request, pk=pk, requester=request.user)
    return render(request, "request_detail.html", {"req": req})


@login_required
def request_edit(request, pk):     # NEW (edit if pending)
    req = get_object_or_404(Request, pk=pk, requester=request.user)

    if req.status != "Pending":  # lock editing if not pending
        messages.error(request, "You can only edit requests that are Pending.")
        return redirect("request_detail", pk=req.pk)

    if request.method == "POST":
        form = RequestForm(request.POST, instance=req)
        if form.is_valid():
            form.save()
            messages.success(request, "Request updated successfully.")
            return redirect("request_detail", pk=req.pk)
    else:
        form = RequestForm(instance=req)

    return render(request, "request_edit.html", {"form": form, "req": req})

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
    try:
        if request.method == "POST":
            form = ProfileForm(request.POST, instance=request.user)

            if form.is_valid():
                form.save()
                messages.success(request, "✅ Profile updated successfully.")
                return redirect("profile")
            else:
                # Debug: print form errors in terminal
                print("❌ Form errors:", form.errors)
                messages.error(request, "There were errors in the form.")
        else:
            form = ProfileForm(instance=request.user)

    except Exception as e:
        print("⚠️ Error in profile view:", str(e))  # Debugging
        messages.error(request, f"Something went wrong: {e}")
        form = ProfileForm(instance=request.user)

    return render(request, "profile.html", {"form": form})