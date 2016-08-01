from PIL import Image, ImageFont, ImageDraw
import textwrap
import time

BG_COLOR_BLACK  = (0,0,0)
BG_COLOR_WHITE  = (255,255,255)
BG_COLOR_GRAY   = (118,113,113)

'''
COLOR_RED       = (234,67,53)
COLOR_GREEN     = (52,168,83)
COLOR_BLUE      = (66,133,244)

BG_COLOR_MON = (148,122,99)
BG_COLOR_TUE = (166,86,69)
BG_COLOR_WED = (114,158,161)
BG_COLOR_THU = (82,84,73)
BG_COLOR_FRI = (131,128,73)
'''

COLOR_RED       = (187,26,44)
COLOR_BLUE      = (16,68,167)
BG_COLOR_BOOK   = (33,44,64)

BG_COLOR_MON = (148,120,57)
BG_COLOR_TUE = (230,133,52)
BG_COLOR_WED = (239,178,12)
BG_COLOR_THU = (196,183,138)
BG_COLOR_FRI = (77,81,96)

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
FONT_HANNA      = 'font/BMHANNA_11yrs_ttf.ttf'
FONT_JUA        = 'font/BMJUA_ttf.ttf'
FONT_DOHYEON    = 'font/BMDOHYEON_ttf.ttf'

BG_COLOR = [BG_COLOR_MON, BG_COLOR_TUE, BG_COLOR_WED, BG_COLOR_THU, BG_COLOR_FRI, BG_COLOR_TUE]

SECTION3_WIDTH = 810
SECTION4_WIDTH = 610

HEIGHT_SECTION1 = 0
HEIGHT_SECTION2 = HEIGHT_SECTION1 + 150
HEIGHT_SECTION3 = HEIGHT_SECTION2 + 100 # 250
HEIGHT_SECTION4 = HEIGHT_SECTION3 + SECTION3_WIDTH # 760
HEIGHT_SECTION5 = HEIGHT_SECTION4 + 100 # 860
HEIGHT_SECTION6 = HEIGHT_SECTION5 + SECTION4_WIDTH # 1770
HEIGHT_SECTION7 = HEIGHT_SECTION6 + 150 # 1920

class  CardView(object):
    def __init__(self, today):
        self.img = Image.new('RGBA', (1080, 1920), BG_COLOR_WHITE)
        self.draw = ImageDraw.Draw(self.img)
        self.pixel = self.img.load()
        self.bgcolor =  BG_COLOR[today]
        self.bgcolor2 = (int((BG_COLOR[today][0]+255)/2),
                         int((BG_COLOR[today][1]+255)/2),
                         int((BG_COLOR[today][2]+255)/2))

        self.draw.rectangle(((0,HEIGHT_SECTION1), (1080,HEIGHT_SECTION2)), fill=self.bgcolor)
        self.draw.rectangle(((0,HEIGHT_SECTION2), (1080, HEIGHT_SECTION3)), fill=BG_COLOR_GRAY)
        self.draw.rectangle(((0,HEIGHT_SECTION3), (1080, HEIGHT_SECTION4)), fill=self.bgcolor2)
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

    def draw_photo(self, icon, x, y):
        img = Image.open(icon).resize((128, 128))
        pixel = img.load()

        for i in range(img.size[0]):
            for j in range(img.size[1]):
                if pixel[i, j] != (0,0,0,0):
                    self.pixel[i + x, j + y] = pixel[i, j]

    def draw_font(self, type, x, y, size, color, text):
        drawfont = ImageFont.truetype(type, size)
        self.draw.text((x, y), text, fill=color, font=drawfont)
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

    def get_multilne2(self, type, text, width, height):
        size = 40
        lines = self.get_multiline(type, size, text, width)
        while len(lines) * (size+10) > height:
            lines = self.get_multiline(type, size, text, width)
            size -= 1
        return size, lines

    def get_font_size1(self, type, text, width, height):
        size = 35
        font = ImageFont.truetype(type, size)
        flag = 1

        while flag:
            for line in text.split('\n'):
                if font.getsize(line)[0] > width:
                    size -= 1
                    continue
            if len(text.split('\n')) * (size + 10) > height:
                size -= 1
                continue
            flag = 0
        return size

    def get_font_size(self, type, size, text):
        font = ImageFont.truetype(type, size)
        return font.getsize(text)[0]

    def draw_stock(self, kospi_price, kospi_ud, kosdaq_price, kosdaq_ud):
        self.draw_icon(ICON_STOCK, 30, HEIGHT_SECTION1 + 35)
        color = BG_COLOR_WHITE
        self.draw_font(FONT_DOHYEON, 124, HEIGHT_SECTION1 + 15, 45, color, 'KOSPI')
        if '▼' in kospi_ud:
            color = COLOR_BLUE
        else:
            color = COLOR_RED
        self.draw_font(FONT_DOHYEON, 124 + 180, HEIGHT_SECTION1 + 15, 45, color, kospi_price)
        self.draw_font(FONT_DOHYEON, 124 + 400, HEIGHT_SECTION1 + 15 + 15, 30, color, kospi_ud)

        color = BG_COLOR_WHITE
        self.draw_font(FONT_DOHYEON, 124, HEIGHT_SECTION1 + 60 + 15, 45, color, 'KOSDAQ')
        if '▼' in kosdaq_ud:
            color = COLOR_BLUE
        else:
            color = COLOR_RED
        self.draw_font(FONT_DOHYEON, 124 + 180 + 35, HEIGHT_SECTION1 + 60 + 15, 45, color, kosdaq_price)
        self.draw_font(FONT_DOHYEON, 124 + 400, HEIGHT_SECTION1 + 60 + 15 + 15, 30, color, kosdaq_ud)
        return

    def draw_date(self, year, month, day):
        date = year+'년 ' + month + '월 ' + day + ''
        self.draw_font(FONT_DOHYEON, 800, HEIGHT_SECTION1 + 15, 40, BG_COLOR_WHITE, date)
        return

    def draw_date(self, date):
        self.draw_font(FONT_DOHYEON, 800, 20, 45, BG_COLOR_WHITE, date)
        return

    def draw_book_contents(self, num, book, author, text):
        self.draw_icon(ICON_BOOK, 30, HEIGHT_SECTION2 + 20)
        #self.draw_font(FONT_DOHYEON, 124, HEIGHT_SECTION2 + 30, 40, BG_COLOR_WHITE, '오늘의 책소개')
        self.draw_font(FONT_DOHYEON, 124, HEIGHT_SECTION2 + 30, 40, BG_COLOR_WHITE, book)

        '''
        self.draw_font(FONT_DOHYEON, 124, HEIGHT_SECTION2 + 30, 40, BG_COLOR_WHITE, book)개
        width = self.get_font_size(FONT_DOHYEON, 40, book)
        self.draw_font(FONT_DOHYEON, 124 + width + 30, HEIGHT_SECTION2 + 40, 30, BG_COLOR_WHITE, author)
        '''

        filename = 'picture/book/' + num + '.jpg'
        #img = Image.open(filename).resize((198*3, 295*3))
        #img = Image.open(filename).resize((482, 737))
        img = Image.open(filename).resize((543, 810))
        pixel = img.load()

        for i in range(img.size[0]):
            for j in range(img.size[1]):
                self.pixel[i, j + HEIGHT_SECTION3] = pixel[i, j]

        #self.draw_font(FONT_DOHYEON, 320, HEIGHT_SECTION3 + 60, 40, BG_COLOR_WHITE, book)
        self.draw_font(FONT_DOHYEON, 560, HEIGHT_SECTION3 + 20, 40, BG_COLOR_WHITE, author)


        #lines= self.get_multiline(FONT_JUA, 33, text, 480)
        #for num, line in enumerate(lines, 0):
        #    self.draw_font(FONT_JUA, 560, HEIGHT_SECTION3 + 100 + 45*num, 33, BG_COLOR_BOOK, line)

        size, lines = self.get_multilne2(FONT_JUA, text, 480, 710)
        for num, line in enumerate(lines, 0):
            self.draw_font(FONT_JUA, 560, HEIGHT_SECTION3 + 100 + (size+10)*num, size, BG_COLOR_BOOK, line)


        return

    def draw_movie_contents(self, num, name, summary, director, actor, text):
        self.draw_icon(ICON_MOVIE, 30, HEIGHT_SECTION2 + 20)
        #self.draw_font(FONT_DOHYEON, 124, HEIGHT_SECTION2 + 30, 40, BG_COLOR_WHITE, '오늘의 영화소개')
        self.draw_font(FONT_DOHYEON, 124, HEIGHT_SECTION2 + 30, 40, BG_COLOR_WHITE, name)

        filename = 'picture/movie/' + num + '.jpg'
        '''
        img = Image.open(filename).resize((1080, 1920))
        img = img.crop((0, 0, 1080, HEIGHT_SECTION4-HEIGHT_SECTION3))
        pixel = img.load()
        for i in range(img.size[0]):
            for j in range(img.size[1]):
                self.pixel[i, j + HEIGHT_SECTION3] = pixel[i, j]
        '''
        img = Image.open(filename).resize((1080, 810))
        pixel = img.load()
        for i in range(img.size[0]):
            for j in range(img.size[1]):
                self.pixel[i, j + HEIGHT_SECTION3] = pixel[i, j]

        for i in range(1080):
            for j in range(300):
                r, g, b, a = self.img.getpixel((i,j + HEIGHT_SECTION3+510))
                self.img.putpixel((i, j + HEIGHT_SECTION3+510),
                                  (int(r+255/2), int(g+255/2), int(b+255/2), int(a/2)))
                #self.pixel[i, j + 510] = self.img.getpixel((i,j))

        self.draw_font(FONT_JUA, 20, HEIGHT_SECTION3+530, 35, BG_COLOR_BLACK, summary)

        size = self.get_font_size1(FONT_JUA, text, 1000, 220)
        for i, line in enumerate(text.split('\n'), 0):
            self.draw_font(FONT_JUA, 20, HEIGHT_SECTION3+580+(size+10)*i, size, BG_COLOR_BLACK, line)
        return

    def draw_saying_contents(self, num, text, author):
        self.draw_icon(ICON_SAYING, 30, HEIGHT_SECTION2 + 20)
        self.draw_font(FONT_DOHYEON, 124, HEIGHT_SECTION2 + 30, 40, BG_COLOR_WHITE, '오늘의 명언')

        filename = 'picture/saying/' + num + '.jpg'
        img = Image.open(filename).resize((1080, SECTION3_WIDTH))
        pixel = img.load()

        for i in range(img.size[0]):
            for j in range(img.size[1]):
                self.pixel[i, j + HEIGHT_SECTION3] = pixel[i, j]

        #lines= self.get_multiline(FONT_MONO_REGU, 40, text, 1000)
        self.draw_font(FONT_DOHYEON, 50, HEIGHT_SECTION3 + 200, 40, BG_COLOR_WHITE, text)
        self.draw_font(FONT_DOHYEON, 50, HEIGHT_SECTION3 + 300, 40, BG_COLOR_WHITE, author)
        return

    def draw_news_list(self, news_list):

        self.draw_icon(ICON_NEWS, 30, HEIGHT_SECTION4 + 20)
        self.draw_font(FONT_DOHYEON, 124, HEIGHT_SECTION4 + 30, 40, BG_COLOR_WHITE, '오늘의 헤드라인 뉴스')

        for i, title in enumerate(news_list, 0):
            self.draw_font(FONT_BOLD, 15, HEIGHT_SECTION5 + 10 + (i*60), 35,
                           BG_COLOR_BLACK, str(i+1) + '. ' + title)
        return

    def draw_cumtom(self, num, name, number):
        self.draw_icon(ICON_PHONE, 35, HEIGHT_SECTION6 + 40)
        self.draw_font(FONT_DOHYEON, 124, HEIGHT_SECTION6 + 20, 50, BG_COLOR_WHITE, number)

        self.draw_font(FONT_DOHYEON, 124, HEIGHT_SECTION6 + 20 + 60, 50, BG_COLOR_WHITE, name)

        filename = 'picture/custom/' + num + '.png'
        self.draw_photo(filename, 920, HEIGHT_SECTION6 + 10)
        return

    def save_img(self, filename):
        self.img.save(filename)
        return