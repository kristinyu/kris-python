import requests
from bs4 import BeautifulSoup
#  beautifulSoup test 

def dragData():
    result=requests.get("https://www.baidu.com")
    result.encoding='utf-8'
    # soup = BeautifulSoup(result.text,'lxml')
    html = """
    <html><head><title>The Dormouse's story</title></head>
    <body>
    <p class="title" name="dromouse"><b>The Dormouse's story</b></p>
    <p class="story">Once upon a time there were three little sisters; and their names were
    <a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
    <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
    <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
    and they lived at the bottom of a well.</p>
    <p class="story">...</p>
    """
    soutObject = BeautifulSoup(html,'lxml')
    # print(soutObject.prettify())
    # print(soutObject.title)
    # print(soutObject.a)
    # print(soutObject.name)
    # print(soutObject.head.name)
    # print(soutObject.title.name)
    # print(soutObject.p.attrs)
    # print(soutObject.p['class'])
    # print(soutObject.p.string)
    # print(soutObject.a.contents[0])
    # for i in soutObject.a.next_siblings:
        # print(i)
     # print(soutObject.find_all(id='link2'))
    # print(soutObject.find_all(id='link2').string)
    #
    print(soutObject.select_one('#link2').get_text())
    print(soutObject.select_one('#link3').get_text())
    for s in soutObject.select('#link2'):
        print(s.get_text())
    for a in soutObject.select('a #link1'):
        print(a.get_text())
dragData()