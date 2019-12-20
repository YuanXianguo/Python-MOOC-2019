import requests

def get_text():
    url = 'https://www.amazon.cn/dp/B06VXL4CZN'
    try:
        headers = {'user-agent': 'Mozilla/5.0'}
        r = requests.get(url, headers=headers)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        print(r.text[:500])
    except:
        print('爬取失败')

if __name__ == '__main__':
    get_text()
