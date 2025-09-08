from django import forms
from .models import *

class ProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ["email","username"]
    
class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ["type", "description"]



class MaterialRequestForm(forms.ModelForm):
    class Meta:
        model = MaterialRequisition
        fields = ["item_name", "quantity", "unit", "department", "purpose"]

        widgets = {
            "item_name": forms.TextInput(attrs={"class": "form-control", "required": True}),
            "quantity": forms.NumberInput(attrs={"class": "form-control", "min": 1, "required": True}),
            "unit": forms.TextInput(attrs={"class": "form-control", "placeholder": "L, pcs, box"}),
            "department": forms.Select(attrs={"class": "form-select", "required": True}),
            "purpose": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
        }


class HolidayRequestForm(forms.ModelForm):
    class Meta:
        model = HolidayLeaveRequest
        fields = ["start_date", "end_date", "reason"]

        widgets = {
            "start_date": forms.DateInput(attrs={"class": "form-control", "type": "date", "required": True}),
            "end_date": forms.DateInput(attrs={"class": "form-control", "type": "date", "required": True}),
            "reason": forms.Textarea(attrs={"class": "form-control", "rows": 3}),}
        
class AppointmentRequestForm(forms.ModelForm):
    class Meta:
        model = AppointmentRequest
        fields = ["date", "time", "with_whom", "purpose"]

        widgets = {
            "date": forms.DateInput(attrs={"class": "form-control", "type": "date", "required": True}),
            "time": forms.TimeInput(attrs={"class": "form-control", "type": "time", "required": True}),
            "with_whom": forms.TextInput(attrs={"class": "form-control", "placeholder": "Department/Person"}),
            "purpose": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
        }        