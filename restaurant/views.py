from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout
from django.views.generic import ListView, DetailView, View
from .models import *


# Create your views here.
def login(request):
    return render(request, 'restaurant/login.html')


@login_required
def list(request):
    restaurants = Restaurant.objects.all()
    context = {'restaurants': restaurants}
    return render(request, 'restaurant/list.html', context)


def logout(request):
    auth_logout(request)
    return redirect('/')


class HomeView(ListView):
    model = Restaurant
    paginate_by = 8
    template_name = "restaurant/list.html"


class RestaurantDetailView(DetailView):
    model = Restaurant
    template_name = "restaurant/details.html"
