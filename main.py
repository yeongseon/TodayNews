import argparse

from data import Data
from news import CardNews



if __name__ == "__main__":
    # args = parser.parse_args()

    data = Data()
    cardnews = CardNews()

    data.craw_news()
    #data.craw_stoK()
    '''
    data.select_stock()
    cardnews.set_kosdaq_price(data.get_kosdaq_price())
    cardnews.set_kosdaq_ud(data.get_kosdaq_ud())
    cardnews.set_kospi_price(data.get_kospi_price())
    cardnews.set_kospi_ud(data.get_kospi_ud())

    data.select_saying()
    cardnews.set_saying_text(data.get_saying_text())
    cardnews.set_saying_autor(data.get_saying_author())

    data.select_news()
    cardnews.set_news1_title(data.get_news1_title())
    cardnews.set_news1_text(data.get_news1_text())
    cardnews.set_news2_title(data.get_news2_title())
    cardnews.set_news2_text(data.get_news2_text())
    '''
    cardnews.draw()
