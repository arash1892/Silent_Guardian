from django.test import TestCase
from web_app.campaign_analyser import number_of_rev, banner_list_generator
import pandas as pd


class TestCampaignAnalyser(TestCase):

    def test_number_of_rev(self):
        test_list = [5, 4, 3, 2, 0, 0, 0, 0]
        test_series = pd.Series(test_list)
        result = number_of_rev(test_series)
        self.assertEqual(result, 4)

    def test_banner_list_generator(self):  # In this test, user has visited the 422 banner, instead we should show 164
        result = banner_list_generator(43, 10, [1, 2, 3, 4, 5, 6, 7, 8, 9, 422],[20,22])
        self.assertEqual(result, [190, 206, 163, 229, 277, 103, 398, 261, 231, 164])


