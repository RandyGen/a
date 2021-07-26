from gensim.models import word2vec, Word2Vec


# 分かち書きファイルの読み込み
sens = word2vec.LineSentence('../text_data/ai.txt.wakati')
model = Word2Vec(sens)

# 分散表現の保存
model.save('intput/w2v.model')

