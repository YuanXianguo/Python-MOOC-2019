import requests

def get_text():
    url = 'https://item.jd.com/100000972490.html'
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        print(r.text[:500])
    except:
        print('爬取失败')

if __name__ == '__main__':
    get_text()
