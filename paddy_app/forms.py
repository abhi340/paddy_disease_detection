from django import forms
from django.contrib.auth.models import User
from .models import UserProfile, DiseaseDetection
import os

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    phone = forms.CharField(max_length=15, required=False)
    address = forms.CharField(widget=forms.Textarea, required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match")
        return cleaned_data

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = DiseaseDetection
        fields = ['image', 'temperature', 'humidity', 'location']

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image:
            # Check file extension
            ext = os.path.splitext(image.name)[1].lower()
            if ext not in ['.jpg', '.jpeg', '.png', '.webp']:
                raise forms.ValidationError("Unsupported file extension. Please use JPG, PNG, or WEBP.")
            
            # Check file size (e.g., limit to 10MB)
            if image.size > 10 * 1024 * 1024:
                raise forms.ValidationError("File size too large. Please upload an image smaller than 10MB.")
        return image
