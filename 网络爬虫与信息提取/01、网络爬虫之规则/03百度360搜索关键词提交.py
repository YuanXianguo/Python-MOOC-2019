import requests

def get_baidu_text():
    keyword = 'Python'
    try:
        params = {'wd': keyword}
        r = requests.get('http://www.baidu.com/s', params=params)
        print(r.request.url)
        r.raise_for_status()
        print(len(r.text))
    except:
        print('爬取失败')

def get_360_text():
    keyword = 'Python'
    try:
        params = {'q': keyword}
        r = requests.get('http://www.so.com/s', params=params)
        print(r.request.url)
        r.raise_for_status()
        print(len(r.text))
    except:
        print('爬取失败')

if __name__ == '__main__':
    get_baidu_text()
    get_360_text()
