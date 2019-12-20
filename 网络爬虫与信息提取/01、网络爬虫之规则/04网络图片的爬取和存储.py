import requests
import os

def get_picture():
    url = 'https://gss0.bdstatic.com/94o3dSag_xI4khGkpoWK1HF6hhy/baike/c0%3Dbaike80%2C5%2C5%2C80%2C26/' \
          'sign=e9d42879c5cec3fd9f33af27b7e1bf5a/58ee3d6d55fbb2fb13d08da7494a20a44723dc88.jpg'
    root = 'E:\Python\Python基础编程\\01Python基础编程\Python网络爬虫与信息提取\\01第一讲：网络爬虫之规则\\'
    path = root + url.split('/')[-1]
    try:
        if not os.path.exists(root):
            os.mkdir(root)
        if not os.path.exists(path):
            r = requests.get(url)
            with open(path, 'wb') as f:
                f.write(r.content)  # r.content返回HTTP响应内容的二进制形式
                f.close()
                print('文件保存成功')
        else:
            print('文件已存在')
    except:
        print('爬取失败')

if __name__ == '__main__':
    get_picture()
