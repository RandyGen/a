from gensim.models import Word2Vec
import gensim

fpath = '../clustering/input/w2v.model'

# 分散表現の読み込み
model = gensim.models.Word2Vec.load(fpath)

a = model.wv['人工']
print(type(a))
print(a.shape)
print(a)

print(model.wv.most_similar('知能'))

print(model.wv.similarity('人工', '知能'))

