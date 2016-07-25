import gspread
from oauth2client.service_account import ServiceAccountCredentials

from urllib.request import urlopen
from bs4 import BeautifulSoup

import time

JSON = 'conf/TodayNews.json'
URL_KRX = 'http://www.krx.co.kr/main/main.jsp'
URL_NEWS = 'http://www.yonhapnews.co.kr/advisory/2203000001.html'

class Data(object):
    def __init__(self):
        scope = ['https://spreadsheets.google.com/feeds']
        credentials = ServiceAccountCredentials.from_json_keyfile_name(JSON, scope)
        self.gc = gspread.authorize(credentials)

        self.kospi_price = ''
        self.kospi_ud = ''
        self.kosdaq_price = ''
        self.kosdaq_ud = ''

        self.news1_title = ''
        self.news1_text = ''
        self.news2_title = ''
        self.news2_text = ''

        self.saying_text = ''
        self.saying_author = ''
        return

    def get_kospi_price(self):
        return self.kospi_price

    def get_kospi_ud(self):
        return self.kospi_ud

    def get_kosdaq_price(self):
        return self.kosdaq_price

    def get_kosdaq_ud(self):
        return self.kosdaq_ud

    def get_news1_title(self):
        return self.news1_title

    def get_news1_text(self):
        return self.news1_text

    def get_news2_title(self):
        return self.news2_title

    def get_news2_text(self):
        return self.news2_text

    def get_saying_text(self):
        return self.saying_text

    def get_saying_author(self):
        return self.saying_author

    def craw_stoK(self):
        page = urlopen(URL_KRX).read()
        soup = BeautifulSoup(page, 'lxml')

        div = soup.find('div', attrs={'class':'intro-index'})

        spans = div.find_all('span')

        #print(t[3])
        self.kospi_price = spans[4].text
        self.kospi_ud = spans[5].text

        self.kosdaq_price = spans[10].text
        self.kosdaq_ud = spans[11].text

        #print(self.kospi_price, self.kospi_ud)
        #print(self.kosdaq_price, self.kosdaq_ud)
        return

    def select_stock(self):
        wks = self.gc.open('Stock').worksheet('KOSPI')
        count = int(wks.cell(1,1).value)
        index = 0

        for i in range(count):
            if wks.cell(i+2,1).value == time.strftime('%y.%m.%d'):
                index = i+2

        self.kospi_price = wks.cell(index,2).value
        self.kospi_ud = wks.cell(index,3).value


        wks = self.gc.open('Stock').worksheet('KOSDAQ')
        count = int(wks.cell(1,1).value)
        index = 0

        for i in range(count):
            if wks.cell(i+2,1).value == time.strftime('%y.%m.%d'):
                index = i+2

        self.kosdaq_price = wks.cell(index,2).value
        self.kosdaq_ud = wks.cell(index,3).value

        #print(self.kospi_price, self.kospi_ud)
        #print(self.kosdaq_price, self.kosdaq_ud)
        return

    def select_saying(self):

        wks = self.gc.open('Saying').worksheet(time.strftime('Saying'))
        count = int(wks.cell(1,1).value)

        for i in range(count):
            if wks.cell(i+2,1).value == time.strftime('%y.%m.%d'):
                index = i+2

        self.saying_text = wks.cell(index, 2).value
        self.saying_author = wks.cell(index, 3).value

        print(self.saying_text)
        print(self.saying_author)
        return

    def craw_news(self):
        page = urlopen(URL_NEWS).read()
        soup = BeautifulSoup(page, 'lxml')

        print(soup.find_all('li', attrs={'class':'section03'}))

        return

    def select_news(self):
        """"
        제목길이 36, 텍스트 길이 300
        """""
        wks = self.gc.open('TodayNews').worksheet(time.strftime('%y.%m.%d'))
        count = int(wks.cell(1,1).value)

        news_list = []
        for i in range(count):
            news = []
            news.append(wks.cell(i+2,1).value)
            news.append(wks.cell(i+2,2).value)
            #print(news[0])
            #print(news[1])
            news_list.append(news)

        self.news1_title = news_list[0][0]
        self.news1_text = news_list[0][1]
        self.news2_title = news_list[1][0]
        self.news2_text = news_list[1][1]
        return