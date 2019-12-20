import os
libs = ['beautifulsoup4', 'pyqt5==5.10', 'docopt', 'pyqt5-tools', 'matplotlib',
        'networkx', 'numpy', 'pandas', 'pillow', 'pygame',
        'pyinstaller', 'pyopengl', 'pypdf2', 'pyqt5', 'requests',
        'scrapy', 'sklearn', 'sympy', 'werobot', 'wheel',
        'wordcloud', 'jieba']
unlibs = []

for lib in libs:
    try:
        os.system('pip install ' + lib)
    except:
        continue
