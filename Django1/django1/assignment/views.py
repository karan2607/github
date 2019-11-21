from django.shortcuts import render
from . import forms
from django.http import HttpResponse
# Create your views here.

def home(request):
    var = {'home':' '}
    return render(request, 'assignment/home.html', context=var)

def about(request):
    var = {'about': ' '}
    return render(request, 'assignment/about.html', context=var)

def gallery(request):
    var = {'gallery': ' '}
    return render(request, 'assignment/gallery.html', context=var)

def signup(request):
    form = forms.FormSignup()
    if request.method == "POST":
        form = forms.FormSignup(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'assignment/signup.html', {'signup': form})

def form_view(request):
    form = forms.FormName()
    if request.method == "POST":
        form = forms.FormName(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'assignment/login.html', {'login': form})
