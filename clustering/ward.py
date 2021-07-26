from gensim.models import Word2Vec
from matplotlib import pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage


# 分散表現の読み込み
model = Word2Vec.load('../w2v/output/neko_w2v.model')

# 最大単語数の指定
# 単語のリスト作成
max_vocab = 100
vocab = list(model.wv.key_to_index.keys())[:max_vocab]

# 取得した単語に対応する単語ベクトルのリスト作成
vectors = [model.wv[word] for word in vocab]

# Ward法による階層型クラスタリングモデルの作成
# クラスタリングの実行
plt.figure(figsize=(15, 5))
Z = linkage(vectors, method='ward')
dendrogram(Z, labels=vocab)
plt.savefig("output/neko_mygraph.png")
