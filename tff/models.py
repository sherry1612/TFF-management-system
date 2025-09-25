from django.contrib.auth.models import AbstractUser
from django.db import models

# Custom user model
class CustomUser(AbstractUser):
    full_name = models.CharField(max_length=255)
    department = models.CharField(
        max_length=50,
        choices=[
            ('Administration', 'Administration'),
            ('Procurement', 'Procurement'),
            ('Finance', 'Finance'),
            ('HR', 'HR'),
            ('ICT', 'ICT'),
        ]
    )
    phone = models.CharField(max_length=15, blank=True, null=True)
ROLE_CHOICES = [
    ("super_admin", "Super Admin"),
    ("dept_admin", "Department Admin"),
    ("member", "Member"),
]

role = models.CharField(max_length=20, choices=ROLE_CHOICES, default="member")
def __str__(self):
         return f"{self.username} ({self.role})"
        


# Request model must be top-level
class Request(models.Model):
    REQUEST_TYPES = [
        ('Material', 'Material'),
        ('Holiday', 'Holiday'),
        ('Appointment', 'Appointment'),
    ]

    user = models.ForeignKey('tff.CustomUser', on_delete=models.CASCADE)
    type = models.CharField(max_length=50, choices=REQUEST_TYPES)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='Pending')

    def __str__(self):
        return f"{self.user.username} - {self.type}"


class MaterialRequisition(models.Model):
    DEPARTMENT_CHOICES = [
        ("Procurement", "Procurement"),
        ("Finance", "Finance"),
        ("ICT", "ICT"),
        ("Administration", "Administration"),
        ("forwarded", "Forwarded to Finance"),
        ("paid", "Paid by Finance"),
        ("not_paid", "Not Paid by Finance"),
    ]

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="requisitions")
    item_name = models.CharField(max_length=200)
    quantity = models.PositiveIntegerField()
    unit = models.CharField(max_length=50, blank=True, null=True)
    department = models.CharField(max_length=50, choices=DEPARTMENT_CHOICES)
    purpose = models.TextField(blank=True, null=True)
    
    status = models.CharField(
        max_length=20,
        choices=[("Pending", "Pending"), ("Approved", "Approved"), ("Rejected", "Rejected")],
        default="Pending"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.item_name} - {self.user.username}"

class HolidayLeaveRequest(models.Model):
    STATUS_CHOICES = [
        ("Pending", "Pending"),
        ("Approved", "Approved"),
        ("Rejected", "Rejected"),
    ]

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="holiday_requests")
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="Pending")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} | {self.start_date} to {self.end_date}"
    
class AppointmentRequest(models.Model):
    STATUS_CHOICES = [
        ("Pending", "Pending"),
        ("Approved", "Approved"),
        ("Rejected", "Rejected"),
    ]

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="appointments")
    date = models.DateField()
    time = models.TimeField()
    with_whom = models.CharField(max_length=200, blank=True, null=True)  # Department/Person
    purpose = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="Pending")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Appointment with {self.with_whom or 'N/A'} on {self.date} at {self.time}"    