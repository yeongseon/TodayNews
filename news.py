from view import CardView
import time

class CardNews(object):
    def __init__(self):
        self.day = 0

        self.kospi_price = ''
        self.kospi_ud = ''
        self.kosdaq_price = ''
        self.kosdaq_ud = ''

        self.news1_title = ''
        self.news1_text = ''
        self.news2_title = ''
        self.news2_text = ''

        self.saying_text = ''
        self.saying_autor = ''
        return

    def set_kospi_price(self, str):
        self.kospi_price = str

    def set_kospi_ud(self, str):
        self.kospi_ud = str

    def set_kosdaq_price(self, str):
        self.kosdaq_price = str

    def set_kosdaq_ud(self, str):
        self.kosdaq_ud = str

    def set_news1_title(self, str):
        self.news1_title = str

    def set_news1_text(self, str):
        self.news1_text = str

    def set_news2_title(self, str):
        self.news2_title = str

    def set_news2_text(self, str):
        self.news2_text = str

    def set_saying_text(self, str):
        self.saying_text = str

    def set_saying_autor(self, str):
        self.saying_autor = str

    def draw(self):
        view = CardView(self.day)
        view.draw_stock(self.kospi_price, self.kospi_ud, self.kosdaq_price, self.kosdaq_ud)

        view.draw_date(str(time.strftime('%Y.%m.%d')))

        view.draw_saying()
        view.draw_saying_contents(self.saying_text, self.saying_autor)

        view.draw_news()
        view.draw_news_contents(self.news1_title, self.news1_text, self.news2_title, self.news2_text)

        view.draw_phone('010-8845-6548')
        view.draw_name('티맥스소프트 최영선')

        view.save_img(str(time.strftime('%Y%m%d')))
        return










