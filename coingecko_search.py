'''This script scrapes coingecko coins and stores coins that are up 20-50% on the day
or over 50% on the week. We need this info to establish which coins are potentially in an uptrend
'''

from pycoingecko import CoinGeckoAPI
from bs4 import BeautifulSoup
class Searcher:

    def __init__(self):
        self.cgk = CoinGeckoAPI()
    def search_coingecko(self):
        for coin in self.cgk.get_search_trending()['coins']:
            print(coin['item'])

    def scraped_search(self):
        self.soup = BeautifulSoup(page.content,"html.parser")


if __name__ == "__main__":
    searcher = Searcher()
    searcher.search_coingecko()