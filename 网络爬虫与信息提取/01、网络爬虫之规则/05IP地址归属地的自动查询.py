import requests

def get_ip_address():
    url = 'http://m.ip138.com/ip.asp?ip='
    try:
        r = requests.get(url + '202.204.80.112')
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        print(r.text[-500:])
    except:
        print('爬取失败')

if __name__ == '__main__':
    get_ip_address()
