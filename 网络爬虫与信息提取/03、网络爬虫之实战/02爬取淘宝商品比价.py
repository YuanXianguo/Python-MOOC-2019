import requests
import re

def get_html(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ''

def parse_page(g_list, html):
    try:
        plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"', html)
        tlt = re.findall(r'\"raw_title\"\:\".*?\"', html)
        for i in range(len(plt)):
            price = eval(plt[i].split(':')[1])
            title = eval(tlt[i].split(':')[1])
            g_list.append([price, title])
    except:
        print('')

def print_list(g_list):
    tem = '{:^4}\t{:^8}\t{:^16}'
    print(tem.format('序号', '价格', '商品名称'))
    for i in g_list:
        print(tem.format(i+1, i[0], i[1]))

def main():
    goods = '书包'
    depth = 2
    start_url = 'https://s.taobao.com/search?q={}'.format(goods)
    g_list = []
    for i in range(depth):
        try:
            url = "{}&imgfile=&js=1&stats_click=search_radio_all%3A1&" \
                  "initiative_id=staobaoz_20181115&ie=utf8&style=list&" \
                  "sort=sale-desc&bcoffset=0&p4ppushleft=%2C44&s={}"\
                .format(start_url, str(44*i))
            html = get_html(url)
            parse_page(g_list, html)
        except:
            continue
    print_list(g_list)

if __name__ == '__main__':
    main()

