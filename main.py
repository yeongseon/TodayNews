import time
import argparse

from data import Data
from news import CardNews

if __name__ == "__main__":
    # args = parser.parse_args()
    day = time.localtime().tm_wday
    data = Data()

    data.craw_stoK()
    data.select_stock()

    data.craw_news()
    data.select_news_list()

    for i in range(data.get_custom_size()):
        cardnews = CardNews()
        data.select_peple(i)
        cardnews.set_custom_num(i+1)
        cardnews.set_custom_name(data.get_custom_name())
        cardnews.set_custom_phone(data.get_custom_phone())
        cardnews.set_custom_job(data.get_custom_job())

        cardnews.set_kosdaq_price(data.get_kosdaq_price())
        cardnews.set_kosdaq_ud(data.get_kosdaq_ud())
        cardnews.set_kospi_price(data.get_kospi_price())
        cardnews.set_kospi_ud(data.get_kospi_ud())

        if day == 0:
            data.select_saying()
            cardnews.set_saying_num(data.get_saying_num())
            cardnews.set_saying_text(data.get_saying_text())
            cardnews.set_saying_autor(data.get_saying_author())
        elif day == 3:
            data.select_book()
            cardnews.set_book_num(data.get_book_num())
            cardnews.set_book_name(data.get_book_name())
            cardnews.set_book_author(data.get_book_author())
            cardnews.set_book_text(data.get_book_text())
        elif day == 5:
            data.select_movie()
            cardnews.set_movie_num(data.get_movie_num())
            cardnews.set_movie_name(data.get_movie_name())
            cardnews.set_movie_director(data.get_movie_director())
            cardnews.set_movie_summary(data.get_movie_summary())
            cardnews.set_movie_actor(data.get_movie_actor())
            cardnews.set_movie_text(data.get_movie_text())


        cardnews.set_news_list(data.get_news_list())

        cardnews.draw()
