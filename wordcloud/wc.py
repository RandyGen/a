import MeCab
from matplotlib import pyplot as plt
from wordcloud import WordCloud

fpath = 'ai.txt'

with open(fpath, 'r',encoding='utf-8') as f:
    s = f.read()

wakati = MeCab.Tagger('-Owakati -r /etc/mecabrc')
parsed_text = wakati.parse(s)

wc = WordCloud(width=1920, height=1080,
                # 日本語が含まれている場合フォントの指定が必要
                # font_path="/System/Library/Fonts/ヒラギノ角ゴシック W6.ttc",
                # stopwords={"もの","これ","ため","それ","ところ","よう","こと","そう","ます","ので","から","など","です","する","いる","ない","あり","なく","また"},
                max_words=500,
                background_color="white")
wc.generate(parsed_text)
wc.to_file('wordcloud.png')

