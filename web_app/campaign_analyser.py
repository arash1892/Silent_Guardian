import pandas as pd

clicks_1 = pd.read_csv("Data/1/clicks_1.csv")


def number_of_rev(series):
    m = 0
    for x in series:
        if x != 0:
            m += 1
        else:
            break
    return m


def banner_list_generator(camp_id, minute, banners_visited):
    # Loading dataset
    if minute < 15:
        clicks_1 = pd.read_csv("Data/1/clicks_1.csv")
        conversion_1 = pd.read_csv("Data/1/conversions_1.csv")
        impressions_1 = pd.read_csv("Data/1/impressions_1.csv")
    elif (minute > 14) & (minute < 30):
        clicks_1 = pd.read_csv("Data/2/clicks_2.csv")
        conversion_1 = pd.read_csv("Data/2/conversions_2.csv")
        impressions_1 = pd.read_csv("Data/2/impressions_2.csv")
    elif (minute > 29) & (minute < 45):
        clicks_1 = pd.read_csv("Data/3/clicks_3.csv")
        conversion_1 = pd.read_csv("Data/3/conversions_3.csv")
        impressions_1 = pd.read_csv("Data/3/impressions_3.csv")
    else:
        clicks_1 = pd.read_csv("Data/4/clicks_4.csv")
        conversion_1 = pd.read_csv("Data/4/conversions_4.csv")
        impressions_1 = pd.read_csv("Data/4/impressions_4.csv")

    total_1 = pd.merge(clicks_1, conversion_1, how='left', on='click_id')
    # Creating sorted series of banners based on revenues
    banner_rev = total_1[total_1['campaign_id'] == camp_id].groupby('banner_id')['revenue'].sum().sort_values(
        ascending=False)
    revenue_banners_num = number_of_rev(banner_rev)
    banner_rev_only = banner_rev[:revenue_banners_num].index

    # Creating sorted series of banners based on clicks
    banner_click = total_1[total_1['campaign_id'] == camp_id].groupby('banner_id')['click_id'].count().sort_values(
        ascending=False)[:10]
    click_banners_num = number_of_rev(banner_click)
    banner_click_only = banner_click[:click_banners_num].index

    # Creating list of banners for each campaign, regardless of click or revenue
    banners_list = impressions_1[impressions_1['campaign_id'] == camp_id]['banner_id'].index

    if revenue_banners_num >= 10:
        banners_tobe_shown = []
        for banner in banner_rev_only:
            if banner not in banners_visited:
                banners_tobe_shown.append(banner)
                if len(banners_tobe_shown) == 10:
                    break
        if len(banners_tobe_shown) < 10:
            for banner in banner_click_only:
                if banner not in banners_visited:
                    banners_tobe_shown.append(banner)
                    if len(banners_tobe_shown) == 10:
                        break
            if len(banners_tobe_shown) < 10:
                for banner in banners_list:
                    if banner not in banners_visited:
                        banners_tobe_shown.append(banner)
                        if len(banners_tobe_shown == 10):
                            break
        return banners_tobe_shown

    if (revenue_banners_num < 10) and (revenue_banners_num > 4):
        banners_tobe_shown = []
        #Fill the list with most revenue in that campaign
        for banner in banner_rev_only:
            if banner not in banners_visited:
                banners_tobe_shown.append(banner)
                if len(banners_tobe_shown) == revenue_banners_num:
                    break
        #If not fulled, fill with most clicked in that campaign
        if len(banners_tobe_shown) < revenue_banners_num:
            for banner in banner_click_only:
                if banner not in banners_visited:
                    banners_tobe_shown.append(banner)
                    if len(banners_tobe_shown) == revenue_banners_num:
                        break
            if len(banners_tobe_shown) < revenue_banners_num:
                for banner in banners_list:
                    if banner not in banners_visited:
                        banners_tobe_shown.append(banner)
                        if len(banners_tobe_shown == revenue_banners_num):
                            break
        return banners_tobe_shown

    if revenue_banners_num < 5:
        banners_tobe_shown = []
        for banner in banner_rev_only:
            if banner not in banners_visited:
                banners_tobe_shown.append(banner)
                if len(banners_tobe_shown) == 5:
                    break
        if len(banners_tobe_shown) < 5:
            for banner in banner_click_only:
                if banner not in banners_visited:
                    banners_tobe_shown.append(banner)
                    if len(banners_tobe_shown) == 5:
                        break
            if len(banners_tobe_shown) < 5:
                for banner in banners_list:
                    if banner not in banners_visited:
                        banners_tobe_shown.append(banner)
                        if len(banners_tobe_shown == 5):
                            break
        return banners_tobe_shown


