from PIL import Image, ImageFont, ImageDraw
import textwrap
import time

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

FONT_BOLD       = 'font/NotoSansCJKjp-Bold.otf'
FONT_REGU       = 'font/NotoSansCJKjp-Regular.otf'
FONT_THIN       = 'font/NotoSansCJKjp-Thin.otf'
FONT_MONO_BOLD  = 'font/NotoSansMonoCJKkr-Bold.otf'
FONT_MONO_REGU  = 'font/NotoSansMonoCJKkr-Regular.otf'

BG_COLOR = [BG_COLOR_MON, BG_COLOR_TUE, BG_COLOR_WED, BG_COLOR_THU, BG_COLOR_FRI]

HEIGHT_SECTION1 = 0
HEIGHT_SECTION2 = HEIGHT_SECTION1 + 150
HEIGHT_SECTION3 = HEIGHT_SECTION2 + 100 # 250
HEIGHT_SECTION4 = HEIGHT_SECTION3 + 610 # 760
HEIGHT_SECTION5 = HEIGHT_SECTION4 + 100 # 860
HEIGHT_SECTION6 = HEIGHT_SECTION5 + 810 # 1770
HEIGHT_SECTION7 = HEIGHT_SECTION6 + 150 # 1920

class  CardView(object):
    def __init__(self, today):
        self.img = Image.new('RGB', (1080, 1920), BG_COLOR_WHITE)
        self.draw = ImageDraw.Draw(self.img)
        self.pixel = self.img.load()
        self.bgcolor =  BG_COLOR[today]

        self.draw.rectangle(((0,HEIGHT_SECTION1), (1080,HEIGHT_SECTION2)), fill=self.bgcolor)
        self.draw.rectangle(((0,HEIGHT_SECTION2), (1080, HEIGHT_SECTION3)), fill=BG_COLOR_GRAY)
        self.draw.rectangle(((0,HEIGHT_SECTION4), (1080, HEIGHT_SECTION5)), fill=BG_COLOR_GRAY)
        self.draw.rectangle(((0,HEIGHT_SECTION6), (1080, HEIGHT_SECTION7)), fill=self.bgcolor)
        return


    def draw_icon(self, icon, x, y):
        img = Image.open(icon).resize((64,64))
        pixel = img.load()

        for i in range(img.size[0]):
            for j in range(img.size[1]):
                if pixel[i, j] != (0,0,0,0):
                    self.pixel[i + x, j + y] = (255,255,255,0)

    def draw_font(self, type, x, y, size, color, text):
        drawfont = ImageFont.truetype(type, size)
        self.draw.text((x, y), text, fill=color, font=drawfont)
        return


    def draw_stock(self, kospi_price, kospi_ud, kosdaq_price, kosdaq_ud):
        self.draw_icon(ICON_STOCK, 30, HEIGHT_SECTION1 + 15)
        color = BG_COLOR_WHITE
        self.draw_font(FONT_BOLD, 124, HEIGHT_SECTION1 + 15, 40, color, 'KOSPI')
        if '▼' in kospi_ud:
            color = COLOR_BLUE
        else:
            color = COLOR_RED
        self.draw_font(FONT_BOLD, 124 + 180, HEIGHT_SECTION1 + 15, 40, color, kospi_price)
        self.draw_font(FONT_BOLD, 124 + 370, HEIGHT_SECTION1 + 15 + 15, 30, color, kospi_ud)

        color = BG_COLOR_WHITE
        self.draw_font(FONT_BOLD, 124, HEIGHT_SECTION1 + 60 + 15, 40, color, 'KOSDAQ')
        if '▼' in kosdaq_ud:
            color = COLOR_BLUE
        else:
            color = COLOR_RED
        self.draw_font(FONT_BOLD, 124 + 180 + 35, HEIGHT_SECTION1 + 60 + 15, 40, color, kosdaq_price)
        self.draw_font(FONT_BOLD, 124 + 370, HEIGHT_SECTION1 + 60 + 15 + 15, 30, color, kosdaq_ud)


        return

    def draw_date(self, year, month, day):
        date = year+'년 ' + month + '월 ' + day + ''
        self.draw_font(FONT_BOLD, 800, HEIGHT_SECTION1 + 15, 40, BG_COLOR_WHITE, date)
        return

    def draw_date(self, date):
        self.draw_font(FONT_BOLD, 800, 20, 40, BG_COLOR_WHITE, date)
        return

    def draw_saying(self):
        self.draw_icon(ICON_SAYING, 30, HEIGHT_SECTION2 + 20)
        self.draw_font(FONT_BOLD, 124, HEIGHT_SECTION2 + 20, 40, BG_COLOR_WHITE, '오늘의 명언')

    def draw_saying_contents(self, text, author):
        filename = 'picture/saying/' + str(time.strftime('%Y%m%d')) + '.jpg'
        img = Image.open(filename).resize((1080, 610))
        pixel = img.load()

        for i in range(img.size[0]):
            for j in range(img.size[1]):
                self.pixel[i, j + HEIGHT_SECTION3] = pixel[i, j]

        #lines= self.get_multiline(FONT_MONO_REGU, 40, text, 1000)
        self.draw_font(FONT_MONO_BOLD, 50, HEIGHT_SECTION3 + 200, 40, BG_COLOR_WHITE, text)
        self.draw_font(FONT_MONO_BOLD, 50, HEIGHT_SECTION3 + 300, 40, BG_COLOR_WHITE, author)

        return

    def draw_news(self):
        self.draw_icon(ICON_NEWS, 30, HEIGHT_SECTION4 + 20)
        self.draw_font(FONT_BOLD, 124, HEIGHT_SECTION4 + 20, 40, BG_COLOR_WHITE, '오늘의 헤드라인 뉴스')
        return


    def get_multiline(self, type, size, text, limit):
        lines = []
        pos = 0
        font = ImageFont.truetype(type, size)

        while pos != len(text):
            line = ""
            while font.getsize(line)[0] < limit:
                if pos == len(text):
                    break;
                line += text[pos]
                pos += 1
                if line[0] == ' ':
                    line = line[1:]
            # print(line)
            lines.append(line)
        return lines

    def draw_news_contents(self, title1, contents1, title2, contents2):

        self.draw_font(FONT_MONO_BOLD, 30, HEIGHT_SECTION5 + 20, 35, BG_COLOR_BLACK, title1)

        lines= self.get_multiline(FONT_MONO_REGU, 32, contents1, 1000)
        for num, line in enumerate(lines, 1):
            self.draw_font(FONT_MONO_REGU, 30, HEIGHT_SECTION5 + 20 + 20 + 40 * num, 32, BG_COLOR_BLACK, line)

        self.draw_font(FONT_MONO_BOLD, 30, HEIGHT_SECTION5 + 20 + 400, 35, BG_COLOR_BLACK, title2)

        lines= self.get_multiline(FONT_MONO_REGU, 32, contents2, 1000)
        for num, line in enumerate(lines, 1):
            self.draw_font(FONT_MONO_REGU, 30, HEIGHT_SECTION5 + 20 + 400 + 20 + 40 * num, 32, BG_COLOR_BLACK, line)

        return

    def draw_phone(self, number):
        self.draw_icon(ICON_PHONE, 30, HEIGHT_SECTION6 + 15)
        self.draw_font(FONT_BOLD, 124, HEIGHT_SECTION6 + 15, 40, BG_COLOR_WHITE, number)
        return

    def draw_name(self, name):
        self.draw_font(FONT_BOLD, 124, HEIGHT_SECTION6 + 15 + 60, 40, BG_COLOR_WHITE, name)
        return

    def save_img(self, strtime):
        filename = 'TodayNews_' + strtime + '.png'
        self.img.save(filename)
        return