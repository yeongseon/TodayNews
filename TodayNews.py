
import gspread
from oauth2client.service_account import ServiceAccountCredentials

from urllib.request import urlopen
from bs4 import BeautifulSoup

from view import CardView
import time

JSON = 'conf/TodayNews.json'


class CardNews(object):
    def __init__(self):


        scope = ['https://spreadsheets.google.com/feeds']
        credentials = ServiceAccountCredentials.from_json_keyfile_name(JSON, scope)
        self.gc = gspread.authorize(credentials)

        wks = self.gc.open('Saying').worksheet('Saying')
        saying = wks.cell(2,2).value
        who = wks.cell(2,3).value

        return

    def draw(self):
        view = CardView(1)
        view.drawStock()
        #view.drawDate(str(time.strftime('%Y')), str(time.strftime('%m')), str(time.strftime('%d')))
        view.drawDate(str(time.strftime('%Y.%m.%d')))
        view.drawSaying()

        view.drawNews()
        view.drawNewsContents(None, None, None, None)

        view.drawPhone('010-8845-6548')
        view.drawName('티맥스소프트 최영선')

        view.save(str(time.strftime('%Y%m%d')))
        return










