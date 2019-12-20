import requests
import re
from bs4 import BeautifulSoup
import traceback

def get_html(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ''

def get_stock_list(stock_list, stock_url):
    """获取股票列表"""
    html = get_html(stock_url)
    soup = BeautifulSoup(html, 'html.parser')
    a = soup.find_all('a')
    for i in a:
        try:
            href = i.attrs['href']
            stock_list.append(re.findall(r'[s][zh]\d{6}', href)[0])
        except:
            continue

def get_stock_info(stock_list, stock_url, file):
    """获取股票信息并保存"""
    for stock in stock_list:
        url = stock_url + stock + '.html'
        html = get_html(url)
        try:
            if html == '':
                continue
            info_dict = {}
            soup = BeautifulSoup(html, 'html.parser')
            stock_info = soup.find('div', attrs={'class': 'stock-bets'})

            name = stock_info.find(attrs={'class': 'bets-name'})
            info_dict.update({'股票名称': name.text.split()[0]})

            key_list = stock_info.find_all('dt')
            value_list = stock_info.find_all('dd')
            for i in range(len(key_list)):
                info_dict[key_list[i].text] = value_list[i].text

            with open(file, 'a', encoding='utf-8') as f:
                f.write(str(info_dict) + '\n')
        except:
            traceback.print_exc()
            continue

def main():
    stock_list_url = 'http://quote.eastmoney.com/stocklist.html'
    stock_info_url = 'https://gupiao.baidu.com/stock/'
    output_file = 'E:\Python\Python基础编程\\01Python基础编程\
    Python网络爬虫与信息提取\\03第三讲：网络爬虫之实战\stock_info.txt'
    stock_list = []
    get_stock_list(stock_list, stock_list_url)
    get_stock_info(stock_list, stock_info_url, output_file)

if __name__ == '__main__':
    main()
