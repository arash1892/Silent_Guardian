from django.shortcuts import render
import pandas as pd
from datetime import datetime
from django.http import HttpResponse

# Create your views here.
#
clicks_1 = pd.read_csv("Data/1/clicks_1.csv")
conversion_1 = pd.read_csv("Data/1/conversion_1.csv")
impressions_1 = pd.read_csv("Data/1/impressions_1.csv")


def index(request, campaign_id=1):
    request_minute = datetime.now().minute
    page_dict = {"pages": x}
    return render(request, 'image_temp.html', context=page_dict)
