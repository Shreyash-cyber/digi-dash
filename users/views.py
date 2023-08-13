from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from .forms import *
from django.contrib.auth.decorators import login_required
from .models import Jsondata
from rest_framework.views import APIView
from rest_framework.response import Response


def my_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            remember_me = form.cleaned_data['remember_me']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                if not remember_me:
                    request.session.set_expiry(0)
                    return redirect('users:home')
                else:
                    request.session.set_expiry(1209600)
                    return redirect('users:home')
            else:
                return redirect('users:login')
        else:
            return redirect('users:login')
    else:
        form = LoginForm()
        return render(request, "login.html", {'form': form})
    

def home(request):
    json = Jsondata.objects.all()
    end_year = [str(data.end_year) for data in json]
    start_year = [str(data.start_year) for data in json]
    likelihood = [str(data.likelihood) for data in json]
    relevance = [str(data.relevance) for data in json]
    country = [str(data.country) for data in json]
    topic = [str(data.topic) for data in json]
    region = [str(data.region) for data in json]
    intensity = [str(data.intensity) for data in json]
    return render(request, 'home.html', {'json':json, 'end_year':end_year, 'start_year':start_year, 'likelihood':likelihood, 'relevance':relevance, 'country':country, 
                                         'topic':topic, 'region':region, 'intensity':intensity})


class chart_data(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        json = Jsondata.objects.all()
        end_year = [str(datas.end_year) for datas in json]
        start_year = [str(datas.start_year) for datas in json]
        likelihood = [str(datas.likelihood) for datas in json]
        relevance = [str(datas.relevance) for datas in json]
        country = [str(datas.country) for datas in json]
        topic = [str(datas.topic) for datas in json]
        region = [str(datas.region) for datas in json]
        intensity = [str(datas.intensity) for datas in json]
        data = {
            'end_year':end_year, 
            'start_year':start_year, 
            'likelihood':likelihood, 
            'relevance':relevance, 
            'country':country, 
            'topic':topic, 
            'region':region, 
            'intensity':intensity
        }
        return Response(data)

@login_required
def user_logout(request):
    logout(request)
    return redirect('users:login')