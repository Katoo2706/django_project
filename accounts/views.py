from django.shortcuts import render, redirect
from django.contrib import messages, auth  # Display dynamic message
from django.contrib.auth.models import User

from contacts.models import Contact

# Create your views here.

def login(request):
    # Log in
    if request.method == 'POST':
        username = request.POST['username']
        username = username.lower()
        password = request.POST['password']

        user = auth.authenticate(username=username,
                                 password=password)

        if user:
            auth.login(request, user)
            messages.success(request, 'Log in successfully')
            return redirect('dashboard')
        else:
            messages.error(request, 'Username or password is wrong')
            return redirect('login')

    return render(request, 'accounts/login.html')


def register(request):
    # register
    if request.method == "POST":
        # Get from value
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        username = username.lower()
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # Check if passwords match
        if password == password2:
            # Check if existing user
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username is taken")
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, "Email is taken")
                    return redirect('register')
                else:
                    user = User.objects.create_user(
                        username=username,
                        password=password,
                        email=email,
                        first_name=first_name,
                        last_name=last_name
                    )
                    # Login register user
                    # auth.login(request, user)
                    # messages.success(request, "Successful registration")
                    # return redirect('index')
                    user.save()
                    messages.success(request, "Successful registration, you can log in now")
                    return redirect('login')
        else:
            messages.error(request, "Passwords do not match")
            redirect('register')
        messages.error(request, 'Testing error message')
        return redirect('register')
    else:
        return render(request, 'accounts/register.html')


def logout(request):
    # logout
    if request.method == "POST":
        auth.logout(request)
        messages.success(request, "You are now logged out")
        return redirect('index')


def dashboard(request):
    user_contact = Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)

    context = {
        'contacts': user_contact
    }
    return render(request, 'accounts/dashboard.html',
                  context)
