from django.shortcuts import render, HttpResponse,redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Course, RCourse, Caraousel, Comment

# Create your views here.
def index(request):
    rcourses = RCourse.objects.all()
    caraousel = Caraousel.objects.all()
    return render(request, 'index.html', {'rcourses': rcourses, 'caraousel': caraousel})


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
            
def LogoutPage(request):
    logout(request)
    messages.success(request, "You have been successfully logged out.")
    return redirect('login')

def CoursesPage(request):
    courses = Course.objects.all()
    return render(request, 'courses.html', {'courses': courses})

def watch_course(request, course_title):
    course = get_object_or_404(RCourse, title=course_title)
    comments = Comment.objects.filter(course=course)  # If you have a Comment model
    context = {
        'course': course,
        'comments': comments,
    }
    return render(request, 'watch_course.html', context)


def add_comment(request, course_title):
    course = get_object_or_404(RCourse, title=course_title)

    if request.method == 'POST':
        text = request.POST.get('comment_text')

        if request.user.is_authenticated:
            username = request.user.username
            Comment.objects.create(course=course, text=text, username=username)

    return redirect('watch_course', course_title=course.title)




