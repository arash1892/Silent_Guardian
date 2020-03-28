from django.shortcuts import render
import pandas as pd
from datetime import datetime
import random
from web_app.campaign_analyser import number_of_rev
from django.http import HttpResponse

# Create your views here.
# Adding
clicks_1 = pd.read_csv("Data/1/clicks_1.csv")
conversion_1 = pd.read_csv("Data/1/conversions_1.csv")
impressions_1 = pd.read_csv("Data/1/impressions_1.csv")
total_1 = pd.merge(clicks_1, conversion_1, how='left', on='click_id')


def index(request, campaign_id=1):
    print(request.session.get('num_visits', 0) + 1)
    request_minute = datetime.now().minute
    if request_minute < 60:
        page_dict = {}
        banner_nums = total_1[total_1['campaign_id'] == campaign_id].groupby('banner_id')['revenue'].sum().sort_values(
            ascending=False)
        if number_of_rev(banner_nums) > 10:
            if request.session['num_visits'] % 2 == 1:
                banner_nums = banner_nums.index[:10]
            else:
                banner_nums = banner_nums.index[10:20]
            banner_nums = random.sample(list(banner_nums), len(list(banner_nums)))
            for x in range(len(banner_nums)):
                page_dict[x] = banner_nums[x]
            response = render(request, 'image_temp.html', context={'data': page_dict})
            request.session['num_visits'] = request.session.get('num_visits', 0) + 1
            request.session['banner_visited'] = banner_nums
            print(request.session['banner_visited'])
            return response
