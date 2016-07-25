
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
        
        view.drawDate(str(time.strftime('%Y.%m.%d')))
        view.drawSaying()

        view.drawNews()
        title1 = '메이 "연내 브렉시트 통보 안해" 메르켈 "이해하나 끌어선 안돼"'
        text1 = '''영국의 유럽연합(EU) 탈퇴를 뜻하는 브렉시트 국민투표 이후 새로 선출된 영국의 테리사 메이 총리와 독일의 앙겔라 메르켈 총리가 20일(현지시간) 베를린에서 처음 만나 "연내 탈퇴 통보 불가"와 "이해하되 과도한 지체 불가"라는 서로의 입장을 다시 확인했다. 메이 총리는 이날 회담을 마치고 가진 공동기자회견에서 예민하고도 질서 있는 탈퇴 계획을 짜기 위해 이미 밝힌 대로 올해 안에 탈퇴 조항이 담긴 리스본 조약 50조를 발동하지 않는다는 것은 명확하다고 말했다.'''
        print(len(text1))
        view.drawNewsContents(title1, text1, None, None)

        view.drawPhone('010-8845-6548')
        view.drawName('티맥스소프트 최영선')

        view.save(str(time.strftime('%Y%m%d')))
        return










