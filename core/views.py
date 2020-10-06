from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout
from django.views.generic import ListView, DetailView, View
from .models import *


# Create your views here.
def login(request):
    return render(request, 'login.html')


@login_required
def list(request):
    restaurants = Restaurant.objects.all()
    context = {'restaurants': restaurants}
    return render(request, 'list.html', context)


def logout(request):
    auth_logout(request)
    return redirect('/')


def products(request):
    context = {
        'restaurants': Restaurant.objects.all()
    }
    return render(request, "products.html", context)


class HomeView(ListView):
    model = Restaurant
    paginate_by = 8
    template_name = "list.html"


class ItemDetailView(DetailView):
    model = Restaurant
    template_name = "product.html"
