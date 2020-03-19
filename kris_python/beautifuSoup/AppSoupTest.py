#beautiful soup test for
import requests
from bs4 import BeautifulSoup

def soupTest():
    url = "https://www.apple.com"
    req = requests.get(url)
    req.encoding='utf-8'
    soup = BeautifulSoup(req.text,'lxml')
    # print(soup.prettify())
    print(soup.select('.ac-gn-link-text'))


soupTest()


if __name__ == '__main__':
    print("main method")