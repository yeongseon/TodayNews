from PIL import Image, ImageFont, ImageDraw

import gspread
from oauth2client.service_account import ServiceAccountCredentials

from urllib.request import urlopen
from bs4 import BeautifulSoup

import time

JSON = 'conf/TodayNews.json'

COLOR0 = (255, 255, 255) # white
COLOR1 = (0, 0, 0) # black
COLOR2 = (59, 56, 56) # dark gray
COLOR3 = (118, 113, 113) # gray

COLOR4 = (237, 125, 40) #
COLOR5 = (216, 86, 51) # orange
COLOR6 = (70, 93, 114) # blue
COLOR7 = (149, 56, 58) # red

URL = "http://www.yonhapnews.co.kr/home09/7091000000.html?query=%ED%97%A4%EB%93%9C%EB%9D%BC%EC%9D%B8"

class CardNews(object):
    def __init__(self):
        self.im = Image.new('RGB',(1080,1920),COLOR0)
        self.dr = ImageDraw.Draw(self.im)
        self.pixelmap = self.im.load()

        scope = ['https://spreadsheets.google.com/feeds']
        credentials = ServiceAccountCredentials.from_json_keyfile_name(JSON, scope)
        self.gc = gspread.authorize(credentials)

        return

    def draw_section1(self):
        self.dr.rectangle(((0,0), (1080,200)), fill=COLOR5)

        # get KOSPI, KOSDAQ
        return

    def draw_section2(self):
        self.dr.rectangle(((0, 200), (1080, 300)), fill=COLOR3)

        img = Image.open('icon/saying.png')
        img = img.resize((64, 64))

        pixels = img.load()

        for i in range(img.size[0]):
            for j in range(img.size[1]):
                # print(pixels[i,j])
                if pixels[i,j] != (0, 0, 0, 0):
                    self.pixelmap[i+ 40, j + 220] = (255, 255, 255, 0)

        font = ImageFont.truetype('font/NotoSansCJKjp-Bold.otf', 40)
        self.dr.text((150, 220), '오늘의 명언', fill=COLOR0, font=font)

        img = Image.open('picture/1.jpg')
        img = img.resize((1080, 610))
        # img.show()
        pixels = img.load()

        for i in range(img.size[0]):
            for j in range(img.size[1]):
                # print(pixels[i,j])
                self.pixelmap[i ,j + 300] = pixels[i, j]

        wks = self.gc.open('TodayNews').worksheet('Saying')
        saying = wks.cell(2,2).value
        who = wks.cell(2,3).value

        font = ImageFont.truetype('font/NotoSansCJKjp-Medium.otf', 60)
        self.dr.text((50, 520), saying, fill=COLOR0, font=font)
        self.dr.text((50, 620), who, fill=COLOR0, font=font)



        return

    def draw_section3(self):
        self.dr.rectangle(((0, 910), (1080, 1010)), fill=COLOR3)

        img = Image.open('icon/news.png')
        img = img.resize((64, 64))

        pixels = img.load()

        for i in range(img.size[0]):
            for j in range(img.size[1]):
                # print(pixels[i,j])
                if pixels[i,j] != (0, 0, 0, 0):
                    self.pixelmap[i+ 40, j + 930] = (255, 255, 255, 0)

        font = ImageFont.truetype('font/NotoSansCJKjp-Bold.otf', 40)
        self.dr.text((150, 930), '오늘의 헤드라인 뉴스', fill=COLOR0, font=font)


        return

    def draw_section4(self):
        self.dr.rectangle(((0, 1820), (1080, 1920)), fill=COLOR5)


        img = Image.open('icon/phone.png')
        img = img.resize((64, 64))

        pixels = img.load()

        for i in range(img.size[0]):
            for j in range(img.size[1]):
                # print(pixels[i,j])
                if pixels[i,j] != (0, 0, 0, 0):
                    self.pixelmap[i+ 40,j + 1840] = (255, 255, 255, 0)

        font = ImageFont.truetype('font/NotoSansCJKjp-Bold.otf', 40)
        self.dr.text((150, 1840), '010-8845-6548', fill=COLOR0, font=font)

        font = ImageFont.truetype('font/NotoSansCJKjp-Bold.otf', 40)
        self.dr.text((900, 1840), '최영선', fill=COLOR0, font=font)

        return


    def save(self):
        filename = 'TodayNews_' + str(time.strftime('%Y%m%d')) + '.png'
        self.im.save(filename)
        return

    def __del__(self):
        return









