import MeCab

rpath = 'ai.txt'

with open(rpath, 'r') as f:
    text = f.read()

# -r /etc/mecabrc
# mecabrc ... OOrcは設定ファイル
# dicdirのpathを通す

tagger = MeCab.Tagger('-Owakati -r /etc/mecabrc')
parsed_text = tagger.parse(text)

wpath = 'ai.txt.parsed'

with open(wpath, 'w') as f:
    f.write(parsed_text)
