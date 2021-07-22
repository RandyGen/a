from gensim.models import word2vec, Word2Vec
from collections import defaultdict
from sklearn.cluster import KMeans

# # 分かち書きファイルの読み込み
# sens = word2vec.LineSentence('../sample_data/ai.txt.wakati')
# model = Word2Vec(sens)

## 分散表現の保存
# model.save('w2v.model')

# 分散表現の読み込み
model = Word2Vec.load('w2v.model')

# 最大単語数の指定
# 単語のリスト作成
max_vocab = 1000
vocab = list(model.wv.key_to_index.keys())[:max_vocab]
vectors = [model.wv[word] for word in vocab]

# クラスタの数の指定
# k-meansモデルの作成
# クラスタリングの実行
n_clusters = 50
kmeans_model = KMeans(
    n_clusters=n_clusters, 
    verbose=1, 
    random_state=42, 
    n_jobs=-1
)
kmeans_model.fit(vectors)

# クラスタリング後の結果作成
cluster_labels = kmeans_model.labels_
cluster_to_words = defaultdict(list)
for cluster_id, word in zip(cluster_labels, vocab):
    cluster_to_words[cluster_id].append(word)

# 出力
for words in cluster_to_words.values():
    print(words[:10])
