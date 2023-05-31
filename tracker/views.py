from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def index(request):
    return render(request, 'tracker/index.html')

def test(request):
    return render(request, 'tracker/test.html')

def login_view(request):
    message = ''
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('main'))
        else:
            return render(request, 'tracker/login.html', {'message': 'Invalid credentials'})
    return render(request, 'tracker/login.html', {'message': message})

def logout_view(request):
    pass

def main(request):
    if not request.user.is_authenticated:
         return HttpResponseRedirect(reverse("login", message="Please login first"))
    return render(request, 'tracker/main.html')

def signup(request):
    if request.method == 'POST':
        """username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        """
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('main'))  # Redirect to a success page
    else:
        form = UserCreationForm()
    return render(request, 'tracker/signup.html', {
        'form': form})