# forms.py

from django import forms
from .models import Applicant

class ApplicantForm(forms.ModelForm):
    class Meta:
        model = Applicant
        fields = ['full_name', 'email', 'phone_number', 'resume_link', 'skills']
