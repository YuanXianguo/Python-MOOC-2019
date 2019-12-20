def getText():
    txt = open('F:\论文\奥巴马英文演讲.txt', 'r').read()
    txt = txt.lower()
    for ch in '''!@#￥%^`~&*()_+{}[]:"|;'\<>?,./''':
        txt.replace(ch, ' ')
    return txt

aobamaTxt = getText()
words = aobamaTxt.split()
counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1
items = list(counts.items())
items.sort(key=lambda x:x[1], reverse=True) #以第二位（值）从大到小排序
for i in range(10):
    word, count = items[i]
    print("{:<10}{:>5}".format(word,count))
