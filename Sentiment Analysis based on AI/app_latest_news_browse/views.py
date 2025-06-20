from django.shortcuts import render
from django.http import JsonResponse
import pandas as pd
from django.views.decorators.csrf import csrf_exempt

from operator import itemgetter
import numpy as np

from datetime import datetime, timedelta


#-- home page
def home(request):
    return render(request, "app_latest_news_browse/home.html")

#-- API: input category
@csrf_exempt
def api_query_keyword_cate_news(request):
    cate = request.POST['category']
    user_keywords = request.POST['input_keywords']
    user_keywords = user_keywords.split()
    cond='and'
    response = get_userkeyword_cate_latest_news(user_keywords, cate, cond)
    #print(response)
    return JsonResponse({"latest_news": response})

#-- API: input news_id, and then get news information
@csrf_exempt
def api_news_content(request):
    item_id = request.POST['item_id']
    content = get_news_content(item_id)
    # related = get_itemid_most_similar(item_id)
    # print(related)
    related=[]
    return JsonResponse({"news_content": content, "related_news": related})


import pandas as pd
import sqlalchemy
# Step 1: Connect to maria or mysql database
conn= sqlalchemy.create_engine('sqlite:///nownewsdata.sqlite3.db')

def get_duration_date(days=1):
    # What date is the last day?
    # end date: the date of the last record of news
    end_date = conn.execute("SELECT MAX(date) FROM now_news").fetchall()[0][0]
    days=1
    start_date_delta = (datetime.strptime(end_date, '%Y-%m-%d').date() - timedelta(days=days)).strftime('%Y-%m-%d')
    start_date_min = conn.execute("SELECT Min(date) FROM now_news").fetchall()[0][0]
    # set start_date as the larger one from the start_date_delta and start_date_min 開始時間選資料最早時間與周數:兩者較晚者
    start_date = max(start_date_delta,   start_date_min)
    # A time period of 4 weeks 
    #  "select * from now_news where date > '2020-02-12' AND date <= '2020-02-17'; "
    # statement = "select * from now_news where date > '{}' AND date <= '{}'".format(start_date, end_date)

    return start_date, end_date

def filter_database(query_keywords, cate, days=1):

    # Get start and end dates.
    start_date, end_date = get_duration_date(days)

    # query keywords
    qkey = ' '.join([w for w in query_keywords])
    
    # 過濾並隨機挑選數篇用於前端呈現
    if (query_keywords == []):
        statement = "select * from now_news where date > '{}' AND date <= '{}' AND category='{}' ORDER BY RAND() LIMIT 3".format(start_date, end_date, cate)
        #statement = "select * from now_news where date > '{}' AND date <= '{}' AND category='{}' ".format(start_date, end_date, cate)
    else:
        statement = "select * from now_news where MATCH(tokens_v2) AGAINST('{}' IN BOOLEAN MODE) AND date > '{}' AND date <= '{}' AND category='{}' ORDER BY RAND() LIMIT 3".format( qkey, start_date, end_date, cate)
    
    # query from database
    df_query = pd.read_sql_query(statement, conn)

    return df_query


#-- Given a category, get the latest news
def get_userkeyword_cate_latest_news(query_keywords, cate, cond):
    # get the last news (the latest news)

    df_query = filter_database(query_keywords, cate)
    print(df_query.shape)

    # 若檢索無內容回傳None在前端需用null來判斷
    # if (len(df_query)) == 0:
    #     return None

    # 抽樣在資料庫端進行即可
    # if len(df_query) >= 5:
    #     df_query = df_query.sample(3) # Sample only 5 pieces 若文章數不足會報錯!
    # else:
    #     df_query = df_query.tail(3) # Only latest 5 pieces
    
    items = []
    for i in range( len(df_query)):
        item_id = df_query.iloc[i].item_id    
        title = df_query.iloc[i].title
        content = df_query.iloc[i].content
        category = df_query.iloc[i].category
        link = df_query.iloc[i].link
        photo_link = df_query.iloc[i].photo_link
        # if photo_link value is NaN, replace it with empty string 
        if pd.isna(photo_link):
            photo_link=""

        news_info = {
            "item_id": item_id, 
            "category": category, 
            "title": title,
            "content": content, 
            "link": link,
            "photo_link": photo_link
        }

        items.append(news_info)
    
    return items

# -- Given a item_id, get document information
def get_news_content(item_id):
    
    # select article from database by item_id
    statement = "SELECT * FROM now_news where item_id='{}'".format(item_id)
    df_item = pd.read_sql_query(statement, conn)

    title = df_item.iloc[0].title   
    content = df_item.iloc[0].content
    category = df_item.iloc[0].category
    link = df_item.iloc[0].link
    date = df_item.iloc[0].date
    photo_link = df_item.iloc[0].photo_link
    # if photo_link value is NaN, replace it with empty string 
    if pd.isna(photo_link):
        photo_link=''

    news_info = {
        "item_id": item_id,
        "category": category,
        "title": title,
        "content": content,
        "link": link,
        "date": date,
        "photo_link": photo_link
    }

    return news_info

print("app Bert based news recommendation was loaded!")
