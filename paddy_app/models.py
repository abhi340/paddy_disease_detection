from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, blank=True)
    address = models.TextField(blank=True)
    is_authorized = models.BooleanField(default=False)
    
    def __str__(self):
        return self.user.username

class DiseaseDetection(models.Model):
    DISEASE_CHOICES = [
        ('Leaf Blast', 'Leaf Blast'),
        ('Sheath Blight', 'Sheath Blight'),
        ('Bacterial Blight', 'Bacterial Blight'),
        ('Brown Spot', 'Brown Spot'),
        ('Healthy', 'Healthy'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='paddy_images/', max_length=255)
    temperature = models.FloatField(help_text="Temperature in Celsius", null=True, blank=True)
    humidity = models.FloatField(help_text="Humidity percentage", null=True, blank=True)
    location = models.CharField(max_length=255, blank=True)
    detected_disease = models.CharField(max_length=100, choices=DISEASE_CHOICES, blank=True)
    confidence = models.FloatField(default=0.0)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.detected_disease} - {self.created_at}"

class FriendRequest(models.Model):
    from_user = models.ForeignKey(User, related_name='sent_requests', on_delete=models.CASCADE)
    to_user = models.ForeignKey(User, related_name='received_requests', on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Accepted', 'Accepted'), ('Rejected', 'Rejected')], default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.from_user.username} to {self.to_user.username}"
