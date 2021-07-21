import spacy
from spacy import displacy
nlp = spacy.load('ja_ginza')
doc = nlp('山田さんと銀座でランチをご一緒しましょう。')

# 固有表現抽出
for ent in doc.ents:
   print(
       ent.text+','+ # テキスト
       ent.label_+','+ # ラベル
       str(ent.start_char)+','+ # 開始位置
       str(ent.end_char)) # 終了位置

# 強調表示
displacy.render(doc, style='ent', jupyter=True, options={'distance': 90})