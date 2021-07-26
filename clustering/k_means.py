from gensim.models import word2vec, Word2Vec
from collections import defaultdict
from sklearn.cluster import KMeans


# 分散表現の読み込み
model = Word2Vec.load('../w2v/output/neko_w2v.model')

# 最大単語数の指定
# 単語のリスト作成
max_vocab = 10000
vocab = list(model.wv.key_to_index.keys())[:max_vocab]

# 作成した単語リストの単語ベクトルリスト作成
vectors = [model.wv[word] for word in vocab]

# クラスタの数の指定
# k-meansモデルの作成
# クラスタリングの実行
n_clusters = 20
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

