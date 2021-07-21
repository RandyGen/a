import spacy
from spacy import displacy

# 日本語
nlp = spacy.load('ja_ginza')
doc = nlp('銀座でランチをご一緒しましょう。')

# 単語間の係り受け解析
for sent in doc.sents:
    for token in sent:
        print(token.text+' ← '+token.head.text+', '+token.dep_)

# グラフ表示
displacy.render(doc, style='dep', jupyter=True, options={'compact':True, 'distance': 90})
