import MeCab
from matplotlib import pyplot as plt
from wordcloud import WordCloud

fpath = '../text_data/neko.txt'

with open(fpath, 'r',encoding='utf-8') as f:
    s = f.read()

wakati = MeCab.Tagger('-Owakati -r /etc/mecabrc')
parsed_text = wakati.parse(s)

wc = WordCloud(width=1920, height=1080,
                # 日本語が含まれている場合フォントの指定が必要
                font_path="/usr/share/fonts/opentype/ipaexfont-gothic/ipaexg.ttf",
                stopwords={"の","は","か","と","で","を","に","も","が","もの","これ","ため","それ","ところ","よう","こと","そう","ます","ので","から","など","です","する","いる","ない","あり","なく","また","だ","この"},
                max_words=300,
                background_color="white")
wc.generate(parsed_text)
wc.to_file('output/neko_wordcloud.png')

