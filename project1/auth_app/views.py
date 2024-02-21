from django.shortcuts import render, redirect

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def sign_up_view(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('signin_url')

    template_name = 'auth_app/signup_form.html'
    context = {'form':form}
    return render(request, template_name, context)


def sign_in_view(request):
    if request.method == 'POST':
        un = request.POST.get('uname')
        pw = request.POST.get('pass')

        user = authenticate(username=un, password=pw)

        if user is not None:
            login(request, user)
            return redirect('show_url')

    template_name = 'auth_app/signin_form.html'
    context = {}
    return render(request, template_name, context)


def sign_out_view(request):
    logout(request)
    return redirect('signin_url')