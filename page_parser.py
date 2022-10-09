import argparse
import pickle
import time
from selenium import webdriver
from bs4 import BeautifulSoup as BS
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import Keys, ActionChains
import hashlib


class VideoPageParser():
    def __init__(self, url: str, scroll_count: int = 30):
        self._url = url
        self._scroll_count = scroll_count 
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get(self._url)
        self._load_page()
        self._parse_page()
        self._pickle_videos_metadata()
        self.driver.close()


    def _load_page(self):
        for _ in range(self._scroll_count):
            time.sleep(0.5)
            ActionChains(self.driver).key_down(Keys.PAGE_DOWN).perform()

        self._html = self.driver.page_source

    def _parse_page(self):
        soup = BS(self._html, "html.parser")
        videos = soup.find_all(
            "ytd-grid-video-renderer",
            {"class":"style-scope ytd-grid-renderer"}
        )

        self.video_dict = {}
        for video in videos:
            a = video.find("a",{"id":"video-title"})
            self.video_dict[a.get("href")] = {
                "href": "https://www.youtube.com" + a.get("href"),
                "title": a.get("title"),
                "description": a.get("aria-label")
            }
    
    def _pickle_videos_metadata(self):
        encoded_url = self._url.encode("utf-8")
        url_hash = hashlib.sha1(encoded_url).hexdigest()[15:]
        cache_path = url_hash + ".pkl"
        with open(cache_path, 'wb+') as cf:
            pickle.dump(self.video_dict, cf)


def main():
    parser = argparse.ArgumentParser(
        description='%(prog)s used for YouTube videos metadata parsing')
    parser.add_argument(
        'url', 
        type=str,
        help="channel url", 
        )
    parser.add_argument(
        '--scrolls', 
        type=int,
        required=False, 
        default=30, 
        help="number of page scroll down", 
        )
    args = parser.parse_args()
    VideoPageParser(args.url, args.scrolls)

if __name__ == '__main__':
    main()
