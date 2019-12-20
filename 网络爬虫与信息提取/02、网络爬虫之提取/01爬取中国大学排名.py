import requests
from bs4 import BeautifulSoup
import bs4


def get_html(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ''


def fill_list(u_list, html):
    soup = BeautifulSoup(html, 'html.parser')
    for tr in soup.find('tbody').children:
        if isinstance(tr, bs4.element.Tag):
            tds = tr('td')
            u_list.append([tds[0].string, tds[1].string, tds[3].string])


def print_list(u_lsit, num):
    tplt = '{0:^10}\t{1:{3}^10}\t{2:^10}'
    print(tplt.format('排名', '学习名称', '总分', chr(12288)))
    for i in range(num):
        print(tplt.format(u_lsit[i][0], u_lsit[i][1], u_lsit[i][2], chr(12288)))


def main():
    u_list = []
    url = 'http://zuihaodaxue.cn/zuihaodaxuepaiming2018.html'
    html = get_html(url)
    fill_list(u_list, html)
    print_list(u_list, 20)


if __name__ == '__main__':
    main()
