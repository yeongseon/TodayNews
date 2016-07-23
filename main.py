from TodayNews import CardNews
import argparse

if __name__ == "__main__":
    # args = parser.parse_args()
    cardnews = CardNews()
    cardnews.draw_section1()
    cardnews.draw_section2()
    cardnews.draw_section3()
    cardnews.draw_section4()
    cardnews.save()
