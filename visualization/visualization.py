import bhtsne
import numpy as np
from gensim.models import Word2Vec
from matplotlib import pyplot as plt

# 分散表現の読み込み
model = Word2Vec.load('../w2v/output/neko_w2v.model')

# 最大単語数の指定
# 単語のリスト作成
max_vocab = 200
vocab = list(model.wv.key_to_index.keys())[:max_vocab]

# 取得した単語に対応する単語ベクトルのリスト作成
vectors = [model.wv[word] for word in vocab]

embedded = bhtsne.tsne(np.array(vectors).astype(np.float64), dimensions=2, rand_seed=123)
plt.figure(figsize=(10, 10))
plt.scatter(np.array(embedded).T[0], np.array(embedded).T[1])
for (x, y), name in zip(embedded, vocab):
    plt.annotate(name, (x, y))
plt.savefig("output/neko_mygraph.png")
