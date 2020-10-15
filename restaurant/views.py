from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout
from django.views.generic import ListView, DetailView, View
from .models import *


# Create your views here.


class HomeView(ListView):
    model = Restaurant
    paginate_by = 8
    template_name = "restaurant/list.html"


class RestaurantDetailView(DetailView):
    model = Restaurant
    template_name = "restaurant/details.html"
