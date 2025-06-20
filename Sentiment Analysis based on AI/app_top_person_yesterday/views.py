from django.shortcuts import render
import pandas as pd

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


def home(request):
    return render(request, 'app_top_person_yesterday/home.html')

# csrf_exempt is used for POST
# 單獨指定這一支程式忽略csrf驗證
@csrf_exempt
def api_get_yestopPerson(request):

    cate = request.POST.get('news_category')

    chart_data, wf_pairs = get_category_yestopPerson_db(cate, topk=5)

    # print(chart_data)
    response = {'chart_data':  chart_data,
                'wf_pairs': wf_pairs,
                }
    return JsonResponse(response)


import pandas as pd
import sqlalchemy

conn= sqlalchemy.create_engine('sqlite:///nownewsdata.sqlite3.db')


def get_category_yestopPerson_db(cate, topk):

    statement = "SELECT top_keys FROM yesterdaytopperson where category='{}'".format(cate)
    result = conn.execute(statement).fetchone()
    wf_pairs = eval(result[0])[0:topk]

    words = [w for w, f in wf_pairs]
    freqs = [f for w, f in wf_pairs]
    chart_data = {
        "category": cate,
        "labels": words,
        "values": freqs}
        
    return chart_data, wf_pairs  # chart_data is for charting

print("昨日誰最大-載入成功!")

