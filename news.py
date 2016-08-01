from view import CardView
import time

class CardNews(object):
    def __init__(self):
        self.day = time.localtime().tm_wday

        self.custom_num = ''
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

        self.saying_num = 0
        self.saying_text = ''
        self.saying_autor = ''

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

    def set_custom_num(self, str):
        self.custom_num = str

    def set_custom_name(self, str):
        self.custom_name = str

    def set_custom_phone(self, str):
        self.custom_phone = str

    def set_custom_job(self, str):
        self.custom_job = str

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

    def set_news_list(self, list):
        self.news_list = list

    def set_saying_num(self, num):
        self.saying_num = num

    def set_saying_text(self, str):
        self.saying_text = str

    def set_saying_autor(self, str):
        self.saying_autor = str

    def set_book_num(self, num):
        self.book_num = num

    def set_book_name(self, str):
        self.book_name = str

    def set_book_author(self, str):
        self.book_author = str

    def set_book_text(self, str):
        self.book_text = str

    def set_movie_num(self, num):
        self.movie_num = num

    def set_movie_name(self, str):
        self.movie_name = str

    def set_movie_summary(self, str):
        self.movie_summary = str

    def set_movie_director(self, str):
        self.movie_director = str

    def set_movie_actor(self, str):
        self.movie_actor = str

    def set_movie_text(self, str):
        self.movie_text = str


    def draw(self):
        view = CardView(self.day)

        view.draw_stock(self.kospi_price, self.kospi_ud, self.kosdaq_price, self.kosdaq_ud)

        view.draw_date(str(time.strftime('%Y.%m.%d')))

        if self.day == 0:
            view.draw_saying_contents(str(self.saying_num), self.saying_text, self.saying_autor)
        elif self.day == 3:
            view.draw_book_contents(str(self.book_num), self.book_name,
                                    self.book_author, self.book_text)
        elif self.day == 5:
            view.draw_movie_contents(str(self.movie_num), self.movie_name,
                                     self.movie_summary, self.movie_director,
                                     self.movie_actor, self.movie_text)


        view.draw_news_list(self.news_list)

        view.draw_cumtom(str(self.custom_num), self.custom_job + ' ' + self.custom_name, self.custom_phone)

        view.save_img(str(self.custom_num) + '_' + str(time.strftime('%Y%m%d')) + '.jpg')
        return