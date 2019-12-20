import jieba
import wordcloud
from scipy.misc import imread

f = open('F:\电子书\三国演义.txt', 'r', encoding='utf-8')
t = f.read()
f.close()
ls = jieba.lcut(t)
txt = ' '.join(ls)
c = wordcloud.WordCloud(font_path = 'msyh.ttc',\
                        width = 1000, height = 700,\
                        background_color = 'white',\
                        max_words= 15)
c.generate(txt)
c.to_file('F:\电子书\pycloud.png')
