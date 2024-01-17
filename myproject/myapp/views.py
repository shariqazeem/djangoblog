from django.shortcuts import render, HttpResponse,redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import RCourse, Caraousel, Comment, ImageModel, Video
from django.http import HttpResponse, JsonResponse
from .forms import ApplicantForm
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail


@csrf_exempt
# Create your views here.
def index(request):
    recommended_courses = RCourse.objects.filter(recommended=True)
    caraousel = Caraousel.objects.all()  # Retrieve the first image from the Caraousel model
    return render(request, 'index.html', {'recommended_courses': recommended_courses, 'caraousel': caraousel})


@csrf_exempt
def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username') 
        password = request.POST.get('password') 
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, "Invalid Credentials")
            return redirect('login')
    
    return render(request, 'login.html')


@csrf_exempt
def SignupPage(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username is already taken.")
            elif User.objects.filter(email=email).exists():
                messages.error(request, "Email is already taken.")
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                messages.success(request, "You have successfully registered. Please log in.")
                return redirect('login')  # Redirect to the login page on successful registration
        else:
            messages.error(request, "Password and confirm password do not match.")
    
    # Render the signup page for GET requests as well
    return render(request, 'signup.html')

@csrf_exempt    
def LogoutPage(request):
    logout(request)
    messages.success(request, "You have been successfully logged out.")
    return redirect('login')

def CoursesPage(request):
    all_courses = RCourse.objects.filter(recommended=False)
    return render(request, 'courses.html', {'all_courses': all_courses})

def playlist_page(request, course_title):
    course = get_object_or_404(RCourse, title=course_title)
    video_urls = course.get_video_urls()  # Fetch all video URLs
    context = {
        'course': course,
        'video_urls': video_urls,
    }
    return render(request, 'watch_course.html', context)

def watch_course(request, course_title):
    course = get_object_or_404(RCourse, title=course_title)
    comments = Comment.objects.filter(course=course)
    videos = course.videos.all()  # Get associated videos for the course
    context = {
        'course': course,
        'comments': comments,
        'videos': videos,  # Pass the videos queryset to the template
    }
    return render(request, 'watch_course.html', context)




def video_detail(request, video_id):
    video = Video.objects.get(id=video_id)
    comments = Comment.objects.filter(video=video)

    # Check if the user is authenticated
    is_authenticated = request.user.is_authenticated

    context = {
        'video': video,
        'course': video.course,
        'comments': comments,
        'is_authenticated': is_authenticated,  # Include this variable
    }
    return render(request, 'video_detail.html', context)


@csrf_exempt
def add_comment(request):
    if request.method == 'POST':
        comment_text = request.POST.get('comment_text')
        video_id = request.POST.get('video_id')
        course_id = request.POST.get('course_id')
        
        if request.user.is_authenticated:
            username = request.user.username
            
            try:
                if video_id:
                    video = get_object_or_404(Video, pk=video_id)
                    Comment.objects.create(video=video, text=comment_text, username=username)
                    return redirect('video_detail', video_id=video.id)
                elif course_id:
                    course = get_object_or_404(RCourse, pk=course_id)
                    Comment.objects.create(course=course, text=comment_text, username=username)
                    return redirect('watch_course', course_title=course.title)
                else:
                    return HttpResponse("Invalid request. Missing video_id or course_id.")
            except Exception as e:
                return HttpResponse(f"Error creating the comment: {str(e)}")
        
    return HttpResponse("Invalid request or user not authenticated.")




def ContactPage(request):
    image = ImageModel.objects.first()
    return render(request, 'contact.html',{'image':image})

def WorkWithUsPage(request):
    return render(request, 'workwithus.html')

@csrf_exempt
def apply_now(request):
    if request.method == 'POST':
        form = ApplicantForm(request.POST)
        if form.is_valid():
            applicant = form.save()  # Save the data to the database

            # Send an email to the applicant
            applicant_subject = 'Confirmation: Your Job Application has been submitted'
            applicant_message = f'Thank you for submitting your job application, {applicant.full_name}! Your application has been received. We will review it and contact you if necessary.'

            send_mail(applicant_subject, applicant_message, 'shariqshaukat786@example.com', [applicant.email])

            # Send an email with the form data to yourself
            admin_subject = 'New Job Application'
            admin_message = f'Name: {applicant.full_name}\nEmail: {applicant.email}\nPhone: {applicant.phone_number}\nSkills: {applicant.skills}\nResume Link: {applicant.resume_link}'

            # Use your own email address for both 'from' and 'to'
            send_mail(admin_subject, admin_message, 'shariqshaukat786@example.com', ['shariqshaukat786@gmail.com'])

            # Redirect to a success page or do something else
            return render(request, 'workwithus.html')

    else:
        form = ApplicantForm()
    return render(request, 'workwithus.html', {'form': form})


def BlogPage(request):
    return render(request, 'blog.html')



