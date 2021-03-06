from django.shortcuts import render, HttpResponse
from datetime import datetime
import random
from web_app.campaign_analyser import banner_list_generator, banner_clicked
from web_app.models import User_Banners_Visited, User_Banner_Clicked

# Create your views here.


def index(request, campaign_id=1):
    request_minute = datetime.now().minute
    banners_visited = request.session.get('banner_visited', [])
    if not request.session.session_key:
        request.session.save()
    banners_clicked = banner_clicked(request.session.session_key)
    shown_banners = banner_list_generator(campaign_id, request_minute, banners_visited, banners_clicked)
    shown_banners = random.sample(shown_banners, len(shown_banners))  # In order to show banners randomly
    banner_numbers_dict = {}
    for x in range(len(shown_banners)):
        banner_numbers_dict[x] = shown_banners[x]
    response = render(request, 'image_temp.html', context={'data': banner_numbers_dict})
    request.session['banner_visited'] = shown_banners
    User_Banners_Visited.objects.create(user_id_session=request.session.session_key, banners_visited=shown_banners,
                                        campaign_visited=campaign_id, time_visited=datetime.now())
    return response


def redirection(request, banner_id=1):
    User_Banner_Clicked.objects.create(user_id_session=request.session.session_key, banner_clicked=banner_id)
    return HttpResponse("redirecting to customer website...")
