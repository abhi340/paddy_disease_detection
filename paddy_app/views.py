from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegistrationForm, ImageUploadForm
from .models import UserProfile, DiseaseDetection, FriendRequest
from .utils import predict_paddy_disease
import os

def home(request):
    return render(request, 'paddy_app/home.html')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            # Create user profile
            UserProfile.objects.create(
                user=user, 
                phone=form.cleaned_data['phone'], 
                address=form.cleaned_data['address']
            )
            # Log the user in and show message
            login(request, user)
            messages.info(request, "Account created. Please wait for an administrator to authorize your access.")
            return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request, 'paddy_app/register.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        u = request.POST.get('username')
        p = request.POST.get('password')
        user = authenticate(request, username=u, password=p)
        if user is not None:
            # Check if user is authorized
            try:
                profile = UserProfile.objects.get(user=user)
                if profile.is_authorized or user.is_staff:
                    login(request, user)
                    messages.success(request, f"Welcome back, {u}!")
                    return redirect('home')
                else:
                    messages.error(request, "Your account is pending authorization by an administrator.")
            except UserProfile.DoesNotExist:
                if user.is_staff:
                    login(request, user)
                    return redirect('home')
                messages.error(request, "User profile not found. Please contact support.")
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, 'paddy_app/login.html')

@login_required
def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                detection = form.save(commit=False)
                detection.user = request.user
                detection.save()
                
                # Perform prediction
                image_path = detection.image.path
                disease, conf = predict_paddy_disease(image_path)
                
                if "Error" in disease:
                    messages.error(request, f"Detection failed: {disease}")
                else:
                    detection.detected_disease = disease
                    detection.confidence = conf
                    detection.save()
                    messages.success(request, f"Detection complete! Found: {disease}")
                
                return redirect('results')
            except Exception as e:
                messages.error(request, f"An unexpected error occurred: {str(e)}")
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field.capitalize()}: {error}")
    else:
        form = ImageUploadForm()
    return render(request, 'paddy_app/upload.html', {'form': form})

@login_required
def authorize_users(request):
    if not request.user.is_staff:
        messages.error(request, "Access Denied: Admin privileges required.")
        return redirect('home')
    
    unauthorized_users = UserProfile.objects.filter(is_authorized=False)
    
    if request.method == 'POST':
        profile_id = request.POST.get('profile_id')
        action = request.POST.get('action')
        profile = UserProfile.objects.get(id=profile_id)
        
        if action == 'approve':
            profile.is_authorized = True
            profile.save()
            messages.success(request, f"User {profile.user.username} approved.")
        elif action == 'reject':
            messages.warning(request, f"User {profile.user.username} rejected.")
            
        return redirect('authorize_users')
        
    return render(request, 'paddy_app/authorize.html', {'profiles': unauthorized_users})

@login_required
def results(request):
    user_detections = DiseaseDetection.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'paddy_app/results.html', {'detections': user_detections})

@login_required
def search_users(request):
    query = request.GET.get('q', '')
    if query:
        users = UserProfile.objects.filter(user__username__icontains=query).exclude(user=request.user)
    else:
        users = []
    return render(request, 'paddy_app/search.html', {'users': users, 'query': query})

@login_required
def send_request(request, to_user_id):
    from django.contrib.auth.models import User
    to_user = User.objects.get(id=to_user_id)
    FriendRequest.objects.get_or_create(from_user=request.user, to_user=to_user)
    return redirect('search_users')

@login_required
def view_requests(request):
    requests = FriendRequest.objects.filter(to_user=request.user, status='Pending')
    return render(request, 'paddy_app/requests.html', {'requests': requests})
