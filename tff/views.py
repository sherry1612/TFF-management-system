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
            department = getattr(user, "department", None)  # safe way to fetch data
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
    # Overview stats for Super Admin
    total_users = CustomUser.objects.count()
    total_requests = Request.objects.count()
    material_count = MaterialRequisition.objects.count()
    holiday_count = HolidayLeaveRequest.objects.count()
    appointment_count = AppointmentRequest.objects.count()

    return render(request, "admin/dashboard.html", {
        "user": user,
        "total_users": total_users,
        "total_requests": total_requests,
        "material_count": material_count,
        "holiday_count": holiday_count,
        "appointment_count": appointment_count,
    })

    
    #  MANAGE USERS 
@login_required(login_url="login")
def manage_users(request):
    users = CustomUser.objects.all()
    return render(request, "admin/manage_users.html", {"users": users})


#  VIEW ALL REQUESTS 
@login_required(login_url="login")
def all_requests(request):
    requests_list = Request.objects.all().order_by("-created_at")
    return render(request, "admin/all_requests.html", {"requests": requests_list})




@login_required(login_url="login")
def ICT_dashboard(request,pk):
    user = get_object_or_404(CustomUser, pk=pk)  # always the logged-in user
    material = MaterialRequisition.objects.filter(status="pending")
    holiday = HolidayLeaveRequest.objects.filter(status="pending")
    appointment = AppointmentRequest.objects.filter(status="pending")
    pending_requests = MaterialRequisition.objects.filter(status="pending")
    pending_requests_holiday = HolidayLeaveRequest.objects.filter(status="pending")
    pending_requests_appointment = AppointmentRequest.objects.filter(status="pending")


    print("DEBUG: Material count =", material.count())
    print("DEBUG: Pending ICT Requests =", pending_requests.count())
    print("DEBUG: holiday count =", holiday.count())
    print("DEBUG: Pending ICT Requests =", pending_requests.count())
    print("DEBUG: appointment count =", appointment.count())
    print("DEBUG: Pending ICT Requests =", pending_requests.count())

    return render(
        request,
        "ICT/admin/dashboard.html",
        {
            'user': user,
            "material": material,
            "holiday":holiday,
            "appointment":appointment,
            "pending_requests_appointment ":pending_requests_appointment,
            "pending_requests_holiday ":pending_requests_holiday, 
            "pending_requests": pending_requests
        }
    )
@login_required


def ict_request_material(request):
    if request.method == "POST":
        form = MaterialRequestForm(request.POST)
        if form.is_valid():
            material = form.save(commit=False)
            material.submitted_by = request.user
            material.type = "Material"
            material.save()
            return redirect('ict_member_dashboard')
    else:
        form = MaterialRequestForm()
    return render(request, 'request_material.html', {'form': form})

@login_required
def ict_request_holiday(request):
    if request.method == "POST":
        form = HolidayRequestForm(request.POST)
        if form.is_valid():
            holiday = form.save(commit=False)
            holiday.submitted_by = request.user
            holiday.type = "Holiday"
            holiday.save()
            return redirect('ict_member_dashboard')
    else:
        form = HolidayRequestForm()
    return render(request, 'request_holiday.html', {'form': form})

@login_required
def ict_request_appointment(request):
    if request.method == "POST":
        form = AppointmentRequestForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.submitted_by = request.user
            appointment.type = "Appointment"
            appointment.save()
            return redirect('ict_member_dashboard')
    else:
        form = AppointmentRequestForm()
    return render(request, 'request_appointment.html', {'form': form})

@login_required
def ict_request_detail(request, pk):
    req = get_object_or_404(Request, pk=pk)
    return render(request, 'request_detail.html', {'req': req})

@login_required
def ict_request_edit(request, pk):
    req = get_object_or_404(Request, pk=pk)
    if request.method == "POST":
        if req.status == "Pending":  # Only pending requests can be edited
            form = MaterialRequestForm(request.POST, instance=req) if req.type=="Material" else \
                   HolidayRequestForm(request.POST, instance=req) if req.type=="Holiday" else \
                   AppointmentRequestForm(request.POST, instance=req)
            if form.is_valid():
                form.save()
                return redirect('request_detail', pk=req.pk)
    else:
        form = MaterialRequestForm(instance=req) if req.type=="Material" else \
               HolidayRequestForm(instance=req) if req.type=="Holiday" else \
               AppointmentRequestForm(instance=req)
    return render(request, 'request_edit.html', {'form': form, 'req': req})

@login_required
def ict_dashboard(request):
    # Only ICT admin can access
    if request.user.department != 'ICT' or request.user.is_staff == False:
        return redirect('dashboard')  # Or show error

    # Get ICT members
    ict_members = CustomUser.objects.filter(department='ICT', is_staff=False)

    # Get ICT member requests
    pending_requests = Request.objects.filter(member__department='ICT', status='Pending')

    context = {
        'ict_members': ict_members,
        'pending_requests': pending_requests
    }
    return render(request, 'dept/ict_dashboard.html', context)
@login_required
def approve_request(request, pk):
    
    if request.method == 'POST':
        req = get_object_or_404(MaterialRequisition, pk=pk)
        req.status = 'Approved'
        req.save()
    return redirect('ICT_dashboard',pk=pk)

@login_required
def reject_request(request,pk):
    if request.method == 'POST':
        req = get_object_or_404(MaterialRequisition, pk=pk)
        req.status = 'Rejected'
        req.save()
    return redirect('ICT_dashboard',pk=pk)

@login_required

def forward_request(request, pk):
    if request.method == 'POST':
        # Get the requisition object
        req = get_object_or_404(MaterialRequisition, pk=pk)

        # Get the selected destination from the form (name="v")
        next_department = request.POST.get('status')

        if next_department:
            req.next_department = next_department
            req.status = "Forwarded"  # or "In Review", "Sent", etc.

            req.save()

        return redirect('ICT_dashboard', pk=pk)
    # ===========================
#   HOLIDAY REQUEST ACTIONS
# ===========================
@login_required
def approve_holiday(request, pk):
    if request.method == 'POST':
        req = get_object_or_404(HolidayLeaveRequest, pk=pk)
        req.status = 'Approved'
        req.save()
    return redirect('ICT_dashboard', pk=pk)


@login_required
def reject_holiday(request, pk):
    if request.method == 'POST':
        req = get_object_or_404(HolidayLeaveRequest, pk=pk)
        req.status = 'Rejected'
        req.save()
    return redirect('ICT_dashboard', pk=pk)


@login_required
def forward_holiday(request, pk):
    if request.method == 'POST':
        req = get_object_or_404(HolidayLeaveRequest, pk=pk)
        next_department = request.POST.get('status')

        if next_department:
            req.next_department = next_department
            req.status = "Forwarded"
            req.save()

    return redirect('ICT_dashboard', pk=pk)


# ===============================
#   APPOINTMENT REQUEST ACTIONS
# ===============================
@login_required
def approve_appointment(request, pk):
    if request.method == 'POST':
        req = get_object_or_404(AppointmentRequest, pk=pk)
        req.status = 'Approved'
        req.save()
    return redirect('ICT_dashboard', pk=pk)


@login_required
def reject_appointment(request, pk):
    if request.method == 'POST':
        req = get_object_or_404(AppointmentRequest, pk=pk)
        req.status = 'Rejected'
        req.save()
    return redirect('ICT_dashboard', pk=pk)


@login_required
def forward_appointment(request, pk):
    if request.method == 'POST':
        req = get_object_or_404(AppointmentRequest, pk=pk)
        next_department = request.POST.get('status')

        if next_department:
            req.next_department = next_department
            req.status = "Forwarded"
            req.save()

    return redirect('ICT_dashboard', pk=pk)

@login_required
def ict_member_dashboard(request):
   requests = MaterialRequisition.objects.filter(user=request.user).order_by('-created_at')
   return render(request, "ICT/dashboard.html", {"requests": requests})

@login_required(login_url="login")
def procurement_dashboard(request,pk):
    user = get_object_or_404(CustomUser, pk=pk)  # always the logged-in user
    return render(request, "Procurement/admin/dashboard.html",{'user':user})


@login_required(login_url="login")
def hr_dashboard(request,pk):
    user = get_object_or_404(CustomUser, pk=pk) 
    department = user.department # always the logged-in user
    material = MaterialRequisition.objects.filter(status="pending",department=department)
    holiday = HolidayLeaveRequest.objects.filter(status="pending",department=department)
    appointment = AppointmentRequest.objects.filter(status="pending",department=department)
    pending_requests = MaterialRequisition.objects.filter(status="pending",department=department)
    pending_requests_holiday = HolidayLeaveRequest.objects.filter(status="pending",department=department)
    pending_requests_appointment = AppointmentRequest.objects.filter(status="pending",department=department)


    print("DEBUG: Material count =", material.count())
    print("DEBUG: Pending Hr Requests =", pending_requests.count())
    print("DEBUG: holiday count =", holiday.count())
    print("DEBUG: Pending Hr Requests =", pending_requests.count())
    print("DEBUG: appointment count =", appointment.count())
    print("DEBUG: Pending Hr Requests =", pending_requests.count())

    return render(
        request,
        "Hr/admin/dashboard.html",
        {
            'user': user,
            "material": material,
            "holiday":holiday,
            "appointment":appointment,
            "pending_requests_appointment ":pending_requests_appointment,
            "pending_requests_holiday ":pending_requests_holiday, 
            "pending_requests": pending_requests
        }
    )

@login_required
def approve_request(request, pk):
    
    if request.method == 'POST':
        req = get_object_or_404(MaterialRequisition, pk=pk)
        req.status = 'Approved'
        req.save()
    return redirect('Hr_dashboard',pk=pk)

@login_required
def reject_request(request,pk):
    if request.method == 'POST':
        req = get_object_or_404(MaterialRequisition, pk=pk)
        req.status = 'Rejected'
        req.save()
    return redirect('Hr_dashboard',pk=pk)

@login_required

def forward_request(request, pk):
    if request.method == 'POST':
        # Get the requisition object
        req = get_object_or_404(MaterialRequisition, pk=pk)

        # Get the selected destination from the form (name="v")
        next_department = request.POST.get('status')

        if next_department:
            req.next_department = next_department
            req.status = "Forwarded"  # or "In Review", "Sent", etc.

            req.save()

        return redirect('Hr_dashboard', pk=pk)
    # ===========================
#   HOLIDAY REQUEST ACTIONS
# ===========================
@login_required
def approve_holiday(request, pk):
    if request.method == 'POST':
        req = get_object_or_404(HolidayLeaveRequest, pk=pk)
        req.status = 'Approved'
        req.save()
    return redirect('Hr_dashboard', pk=pk)


@login_required
def reject_holiday(request, pk):
    if request.method == 'POST':
        req = get_object_or_404(HolidayLeaveRequest, pk=pk)
        req.status = 'Rejected'
        req.save()
    return redirect('Hr_dashboard', pk=pk)


@login_required
def forward_holiday(request, pk):
    if request.method == 'POST':
        req = get_object_or_404(HolidayLeaveRequest, pk=pk)
        next_department = request.POST.get('status')

        if next_department:
            req.next_department = next_department
            req.status = "Forwarded"
            req.save()

    return redirect('Hr_dashboard', pk=pk)


# ===============================
#   APPOINTMENT REQUEST ACTIONS
# ===============================
@login_required
def approve_appointment(request, pk):
    if request.method == 'POST':
        req = get_object_or_404(AppointmentRequest, pk=pk)
        req.status = 'Approved'
        req.save()
    return redirect('Hr_dashboard', pk=pk)


@login_required
def reject_appointment(request, pk):
    if request.method == 'POST':
        req = get_object_or_404(AppointmentRequest, pk=pk)
        req.status = 'Rejected'
        req.save()
    return redirect('Hr_dashboard', pk=pk)


@login_required
def forward_appointment(request, pk):
    if request.method == 'POST':
        req = get_object_or_404(AppointmentRequest, pk=pk)
        next_department = request.POST.get('status')

        if next_department:
            req.next_department = next_department
            req.status = "Forwarded"
            req.save()
    return redirect('Hr_dashboard', pk=pk)    
    

@login_required(login_url="login")
def administration_dashboard(request,pk):
    user = get_object_or_404(CustomUser, pk=pk)  # always the logged-in user
 
   
    return render(request, "Administration/admin/dashboard.html",{'user':user})

@login_required(login_url="login")
def userICT_dashboard(request, pk):
    user = get_object_or_404(CustomUser, pk=pk)  # always the logged-in user
    
    material = MaterialRequisition.objects.filter(user=user)
    holiday = HolidayLeaveRequest.objects.filter(user=user)
    appointment = AppointmentRequest.objects.filter(user=user)

    print("DEBUG: Dashboard for user =", user.username)
    print("DEBUG: Material count =", material.count())
    print("DEBUG: Holiday count =", holiday.count())
    print("DEBUG: Appointment count =", appointment.count())

    return render(request, "ICT/ictmember dashboard.html", {
        'user': user,
        'material': material,
        'holiday': holiday,
        'appointment': appointment
    })

@login_required(login_url="login")
def userprocurement_dashboard(request,pk):
    user = get_object_or_404(CustomUser, pk=pk)  # always the logged-in user
    material = MaterialRequisition.objects.filter(user=user)
    holiday = HolidayLeaveRequest.objects.filter(user=user)
    appointment = AppointmentRequest.objects.filter(user=user)

    print("DEBUG: Dashboard for user =", user.username)
    print("DEBUG: Material count =", material.count())
    print("DEBUG: Holiday count =", holiday.count())
    print("DEBUG: Appointment count =", appointment.count())

    
   
    return render(request, "Procurement/procurementmember dashboard.html",{
        'user': user,
        'material': material,
        'holiday': holiday,
        'appointment': appointment

    })


@login_required(login_url="login")
def userhr_dashboard(request,pk):
    user = get_object_or_404(CustomUser, pk=pk)  # always the logged-in user
    
    material = MaterialRequisition.objects.filter(user=user)
    holiday = HolidayLeaveRequest.objects.filter(user=user)
    appointment = AppointmentRequest.objects.filter(user=user)

    print("DEBUG: Dashboard for user =", user.username)
    print("DEBUG: Material count =", material.count())
    print("DEBUG: Holiday count =", holiday.count())
    print("DEBUG: Appointment count =", appointment.count())

    return render(request, "Hr/hrmember dashboard.html", {
        'user': user,
        'material': material,
        'holiday': holiday,
        'appointment': appointment
    })


@login_required(login_url="login")
def useradministration_dashboard(request,pk):
    user = get_object_or_404(CustomUser, pk=pk)  # always the logged-in user
 
   
    return render(request, "Administration/dashboard.html",{'user':user})

@login_required(login_url="login")
def request_material(request,pk):
    user = get_object_or_404(CustomUser, pk=pk)  # always the logged-in user


    if request.method == "POST":
        form = MaterialRequestForm(request.POST)
        if form.is_valid():
            requisition = form.save(commit=False)
            requisition.user = request.user
            requisition.save()
            messages.success(request, "Material Requisition submitted successfully!")
            return redirect("request_material")  # redirect to same page or a list view
    else:
        form = MaterialRequestForm()

    return render(request, "requests/request_material.html", {"form": form,"user":user})


@login_required(login_url="login")
def request_holiday(request,pk):
    user = get_object_or_404(CustomUser, pk=pk)  # always the logged-in user

    if request.method == "POST":
        form = HolidayRequestForm(request.POST)
        if form.is_valid():
            leave_request = form.save(commit=False)
            leave_request.user = request.user
            leave_request.save()
            messages.success(request, "Holiday Leave Request submitted successfully!")
            return redirect("request_holiday")  # redirect to same page or leave list
    else:
        form = HolidayRequestForm()

    return render(request, "requests/request_holiday.html", {"form": form,"user":user})

@login_required(login_url="login")
def request_appointment(request,pk):
    user = get_object_or_404(CustomUser, pk=pk)  # always the logged-in user

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

    
    return render(request, "requests/request_appointment.html", {"form": form,"user":user})

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
    req = get_object_or_404(Request, pk=pk, user=request.user)   # ✅ changed 'requester' → 'user'
    return render(request, "request_detail.html", {"req": req})


@login_required
def request_edit(request, pk):     # NEW (edit if pending)
    req = get_object_or_404(Request, pk=pk, user=request.user)   # ✅ secure query (only own requests)

    if req.status != "Pending":  # ✅ only allow editing pending
        messages.error(request, "You can only edit requests that are Pending.")
        return redirect("request_detail", pk=req.pk)

    if request.method == "POST":
        form = RequestForm(request.POST, instance=req)   # ✅ reuse generic RequestForm
        if form.is_valid():
            form.save()
            messages.success(request, "Request updated successfully.")
            return redirect("request_detail", pk=req.pk)   # ✅ redirect to detail after save
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

    return render(request, "profile.html", {"form": form})@login_required

def update_material_req(request, pk):
    material_req = get_object_or_404(MaterialRequisition, pk=pk)

    if request.method == 'POST':
        form = MaterialRequestForm(request.POST, instance=material_req)
        if form.is_valid():
            form.save()
            # log the update
            messages.success(request, "✅ Material request updated successfully.")

            return redirect('update_material_req', pk=pk)
        

    else:
        form = MaterialRequestForm(instance=material_req)

    return render(request, 'update_material_req.html', {'form': form, 'material_req': material_req})



def update_holiday_req(request, pk):
    holiday_req = get_object_or_404(HolidayLeaveRequest, pk=pk)

    if request.method == 'POST':
        form = HolidayRequestForm(request.POST, instance=holiday_req)
        if form.is_valid():
            form.save()
            # log the update
            messages.success(request, "✅ Holiday request updated successfully.")

            return redirect('update_holiday_req', pk=pk)
        

    else:
        form = HolidayRequestForm(instance=holiday_req)

    return render(request, 'update_holiday_req.html', {'form': form, 'holiday_req': holiday_req})

def update_appointment_req(request, pk):
    appointment_req = get_object_or_404(AppointmentRequest, pk=pk)

    if request.method == 'POST':
        form = AppointmentRequestForm(request.POST, instance=appointment_req)
        if form.is_valid():
            form.save()
            # log the update
            messages.success(request, "✅ Appointment request updated successfully.")

            return redirect('update_appointment_req', pk=pk)
        

    else:
        form = AppointmentRequestForm(instance=appointment_req)

    return render(request, 'update_appointment_req.html', {'form': form, 'appointment_req': appointment_req})


