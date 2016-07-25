from PIL import Image, ImageFont, ImageDraw

BG_COLOR_BLACK  = (0,0,0)
BG_COLOR_WHITE  = (255,255,255)
BG_COLOR_GRAY   = (118,113,113)
BG_COLOR_WHITE1 = (237,229,226)
COLOR_RED       = (234,67,53)
COLOR_GREEN     = (52,168,83)
COLOR_BLUE      = (66,133,244)

BG_COLOR_MON = (252,168,79)
BG_COLOR_TUE = (184,127,2)
BG_COLOR_WED = (65,177,147)
#BG_COLOR_THU = (65,83,37)
BG_COLOR_THU = (124,142,50)
BG_COLOR_FRI = (103,54,83)

ICON_BOOK   = 'icon/book.png'
ICON_MOVIE  = 'icon/movie.png'
ICON_PHONE  = 'icon/phone.png'
ICON_STOCK  = 'icon/stock.png'
ICON_SAYING = 'icon/saying.png'
ICON_NEWS   = 'icon/news.png'

FONT_BOLD = 'font/NotoSansCJKjp-Bold.otf'
FONT_

BG_COLOR = [BG_COLOR_MON, BG_COLOR_TUE, BG_COLOR_WED, BG_COLOR_THU, BG_COLOR_FRI]

class  CardView(object):
    def __init__(self, today):
        self.img = Image.new('RGB', (1080, 1920), BG_COLOR_WHITE)
        self.draw = ImageDraw.Draw(self.img)
        self.pixel = self.img.load()
        self.bgcolor =  BG_COLOR[today]

        self.draw.rectangle(((0,0), (1080,200)), fill=self.bgcolor)
        self.draw.rectangle(((0,200), (1080, 300)), fill=BG_COLOR_GRAY)
        self.draw.rectangle(((0,910), (1080, 1010)), fill=BG_COLOR_GRAY)
        self.draw.rectangle(((0,1720),(1080, 1920)), fill=self.bgcolor)
        return


    def drawIcon(self, icon, x, y):
        img = Image.open(icon).resize((64,64))
        pixel = img.load()

        for i in range(img.size[0]):
            for j in range(img.size[1]):
                if pixel[i, j] != (0,0,0,0):
                    self.pixel[i + x, j + y] = (255,255,255,0)

    def drawFont(self, type, x, y, size, color, text):
        drawfont = ImageFont.truetype(type, size)
        self.draw.text((x, y), text, fill=color, font=drawfont)
        return


    def drawStock(self):
        self.drawIcon(ICON_STOCK, 30, 30)
        self.drawFont(FONT_BOLD, 124, 30, 40, BG_COLOR_WHITE, 'KOSPI  2,010,34')
        self.drawFont(FONT_BOLD, 124, 110, 40, BG_COLOR_WHITE, 'KOSDAQ 2,010,34')
        return

    def drawDate(self, year, month, day):
        date = year+'년 ' + month + '월 ' + day + ''
        self.drawFont(FONT_BOLD, 800, 30, 40, BG_COLOR_WHITE, date)
        return

    def drawDate(self, date):
        self.drawFont(FONT_BOLD, 800, 20, 40, BG_COLOR_WHITE, date)
        return

    def drawSaying(self):
        self.drawIcon(ICON_SAYING, 30, 220)
        self.drawFont(FONT_BOLD, 124, 220, 40, BG_COLOR_WHITE, '오늘의 명언')
        return

    def drawNews(self):
        self.drawIcon(ICON_NEWS, 30, 930)
        self.drawFont(FONT_BOLD, 124, 930, 40, BG_COLOR_WHITE, '오늘의 헤드라인 뉴스')
        return

    def drawNewsContents(self, title1, contents1, title2, contents2):
        # 50 byte if size 35
        self.drawFont(FONT_BOLD, 10, 1010, 35, BG_COLOR_BLACK,
                      '12345678901234567890123456789012345678901234567890')
        return

    def drawPhone(self, number):
        self.drawIcon(ICON_PHONE, 30, 1750)
        self.drawFont(FONT_BOLD, 124, 1750, 40, BG_COLOR_WHITE, number)
        return

    def drawName(self, name):
        self.drawFont(FONT_BOLD, 124, 1830, 40, BG_COLOR_WHITE, name)
        return

    def save(self, strtime):
        filename = 'TodayNews_' + strtime + '.png'
        self.img.save(filename)
        return