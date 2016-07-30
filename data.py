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

        self.custom_size = 0
        self.custom_name = ''
        self.custom_phone = ''
        self.custom_job = ''

        self.kospi_price = ''
        self.kospi_ud = ''
        self.kosdaq_price = ''
        self.kosdaq_ud = ''

        self.news1_title = ''
        self.news1_text = ''
        self.news2_title = ''
        self.news2_text = ''
        self.news_list = []

        self.saying_text = ''
        self.saying_author = ''

        self.book_num = 0
        self.book_name = ''
        self.book_author = ''
        self.book_text = ''

        self.movie_num = 0
        self.movie_name = ''
        self.movie_summary = ''
        self.movie_director = ''
        self.movie_actor = ''
        self.movie_text = ''

        return

    def get_custom_name(self):
        return self.custom_name

    def get_custom_phone(self):
        return self.custom_phone

    def get_custom_job(self):
        return self.custom_job

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

    def get_news_list(self):
        return self.news_list

    def get_saying_text(self):
        return self.saying_text

    def get_saying_author(self):
        return self.saying_author

    def get_book_num(self):
        return self.book_num

    def get_book_name(self):
        return self.book_name

    def get_book_author(self):
        return self.book_author

    def get_book_text(self):
        return self.book_text

    def get_movie_num(self):
        return self.movie_num

    def get_movie_name(self):
        return self.movie_name

    def get_movie_summary(self):
        return self.movie_summary

    def get_movie_director(self):
        return self.movie_director

    def get_movie_actor(self):
        return self.movie_actor

    def get_movie_text(self):
        return self.movie_text

    def get_custom_size(self):
        wks = self.gc.open('Custom').worksheet('Custom')
        self.custom_size = int(wks.cell(1,1).value)
        return self.custom_size

    def select_peple(self, number):
        wks = self.gc.open('Custom').worksheet('Custom')
        self.custom_name = wks.cell(number +2, 1).value
        self.custom_phone = wks.cell(number +2, 2).value
        self.custom_job = wks.cell(number +2, 3).value
        return

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


        try:
            wks = self.gc.open('Stock').worksheet('KOSPI')
        except:
            wks = self.gc.open('Stock').add_worksheet('KOSPI', 1, 4)
            wks.update_cell(1, 1, 0)

        count = int(wks.cell(1,1).value)
        if count == 0:
            wks.add_rows(1)
            wks.update_cell(2, 1, time.strftime('%y.%m.%d'))
            wks.update_cell(2, 2, self.kospi_price)
            wks.update_cell(2, 3, self.kospi_ud)
            wks.update_cell(1, 1, count+1)
        else:
            if wks.cell(count+1, 1).value == time.strftime('%y.%m.%d'):
                pass
            else:
                wks.add_rows(1)
                wks.update_cell(count+2, 1, time.strftime('%y.%m.%d'))
                wks.update_cell(count+2, 2, self.kospi_price)
                wks.update_cell(count+2, 3, self.kospi_ud)
                wks.update_cell(1, 1, count+1)


        try:
            wks = self.gc.open('Stock').worksheet('KOSDAQ')
        except:
            wks = self.gc.open('Stock').add_worksheet('KOSDAQ', 1, 4)
            wks.update_cell(1, 1, 0)

        count = int(wks.cell(1,1).value)
        if count == 0:
            wks.add_rows(1)
            wks.update_cell(2, 1, time.strftime('%y.%m.%d'))
            wks.update_cell(2, 2, self.kosdaq_price)
            wks.update_cell(2, 3, self.kosdaq_ud)
            wks.update_cell(1, 1, count+1)
        else:
            if wks.cell(count+1, 1).value == time.strftime('%y.%m.%d'):
                pass
            else:
                wks.add_rows(1)
                wks.update_cell(count+2, 1, time.strftime('%y.%m.%d'))
                wks.update_cell(count+2, 2, self.kosdaq_price)
                wks.update_cell(count+2, 3, self.kosdaq_ud)
                wks.update_cell(1, 1, count+1)

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

        #print(self.saying_text)
        #print(self.saying_author)
        return

    def select_book(self):

        wks = self.gc.open('Book').worksheet(time.strftime('Book'))
        count = int(wks.cell(1,1).value)

        if wks.cell(count+1, 1).value == time.strftime('%y.%m.%d'):
            self.book_num = count
            self.book_name = wks.cell(count+1, 2).value
            self.book_author = wks.cell(count+1, 3).value
            self.book_text = wks.cell(count+1, 4).value
        else:
            wks.update_cell(count+2, 1, time.strftime('%y.%m.%d'))
            wks.update_cell(1, 1, count+1)

    def select_movie(self):

        wks = self.gc.open('Movie').worksheet(time.strftime('Movie'))
        count = int(wks.cell(1,1).value)

        if wks.cell(count+1, 1).value == time.strftime('%y.%m.%d'):
            self.movie_num = count
            self.movie_name = wks.cell(count+1, 2).value
            self.movie_summary = wks.cell(count+1, 3).value
            self.movie_director = wks.cell(count+1, 4).value
            self.movie_actor = wks.cell(count+1, 5).value
            self.movie_text = wks.cell(count+1, 6).value
        else:
            wks.update_cell(count+2, 1, time.strftime('%y.%m.%d'))
            wks.update_cell(1, 1, count+1)

    def craw_news(self):
        page = urlopen(URL_NEWS).read()
        soup = BeautifulSoup(page, 'lxml')

        #for li in soup.find_all('li', attrs={'class':'section03'}):
        #    if time.strftime('%Y%m%d') in li.find('a')['href']:
        #        print(li.find('a')['href'])

        url = soup.find('li', attrs={'class':'section03'}).find('a')['href']

        page = urlopen(url).read()
        soup = BeautifulSoup(page, 'lxml')

        article = soup.find('div', attrs={'class':'article'})

        index = 0
        news_list = []
        title = ''
        text = ''
        flag = 0
        for p in article.find_all('p'):
            if '■' in p.text:
                title = str(p.text).replace('■','').lstrip().rstrip()
                flag = 1
            if flag == 1:
                text = str(p.text).lstrip().rstrip()
                news = []
                news.append(title)
                news.append(text)
                news_list.append(news)

                flag = 0

        #for news in news_list:
        #    print(news[0])
        #    print(news[1])

        row = len(news_list)

        try:
            wks = self.gc.open('TodayNews').worksheet(time.strftime('%y.%m.%d'))
        except:
            wks = self.gc.open('TodayNews').add_worksheet(time.strftime('%y.%m.%d'), row+1, 2)

        wks.update_cell(1, 1, row)

        for i, news in enumerate(news_list, 2):
            wks.update_cell(i, 1, news[0])
            wks.update_cell(i, 2, news[1])
            # print(len(news[1]))

        return

    def select_news_list(self):
        wks = self.gc.open('TodayNews').worksheet(time.strftime('%y.%m.%d'))
        count = int(wks.cell(1,1).value)

        for i in range(count):
            title = wks.cell(i+2, 1).value
            if len(title) < 40:
                #print(title)
                self.news_list.append(title)

        return

    def select_news(self):
        """"
        제목길이 36, 텍스트 길이 300 이
        """""
        wks = self.gc.open('TodayNews').worksheet(time.strftime('%y.%m.%d'))
        count = int(wks.cell(1,1).value)

        news_list = []
        for i in range(count):
            news = []

            title = wks.cell(i+2,1).value
            text = wks.cell(i+2,2).value
            if len(title) < 36 and len(text) < 320:
                if '오늘' in text:
                    continue
                else:
                    news.append(title)
                    news.append(text)
                    #print(news[0])
                    #print(news[1])
                    news_list.append(news)

        self.news1_title = news_list[0][0]
        self.news1_text = news_list[0][1]
        self.news2_title = news_list[1][0]
        self.news2_text = news_list[1][1]
        return