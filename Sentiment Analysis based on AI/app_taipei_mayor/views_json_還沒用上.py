from django.http import JsonResponse
import pandas as pd
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json

def load_data_pk():
    global data
    # Read data from file:
    data = json.load( open( "app_taipei_mayor/dataset/pk_taipei_mayor_election.json" ) )

# load pk data
load_data_pk()

print(data)

def home(request):
    return render(request,'app_taipei_mayor/home.html')


# csrf_exempt is used for POST
# 單獨指定這一支程式忽略csrf驗證
@csrf_exempt
def api_get_taipei_mayor_data(request):

    return JsonResponse(data)

print('app_leaderboard was loaded!')
