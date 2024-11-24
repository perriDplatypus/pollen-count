""" Scraper to fetch data from MelbournePollen """

from datetime import datetime
from bs4 import BeautifulSoup as bs
import requests as req


class Scraper:
    """scraper class to get data"""

    def __init__(self) -> None:
        self.url = 'https://www.melbournepollen.com.au/'
        self.data = {
            "date": "no_data", "pollen": "no_data", "asthma": "no_data"
        }

    def get_data(self) -> None:
        """connects and gets data from the site"""
        print("-----Connecting to MelbournePollen----")
        res = req.get(self.url, timeout=5000)
        melb_pollen_level = bs(res.content, "html5lib")
        self.data["pollen"] = melb_pollen_level.find(
            "div", id="plevel").string.strip().lower()
        print(bs(res.content, "html5lib").find(
            "div", {"class": "uk-grid-collapse forecast-value"}))
        self.data["asthma"] = bs(res.content, "html5lib").find_all(
            "div", {"class": "uk-grid-collapse forecast-value"})
        self.data["date"] = datetime.today().strftime('%Y-%m-%d')
        print(self.data)
        print("-----Data fetched-----")


if __name__ == "__main__":
    Scraper().get_data()
