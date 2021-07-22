from collections import defaultdict
from gensim.models.keyedvectors import KeyedVectors
from sklearn.cluster import KMeans

model = KeyedVectors.load('input/word2vec.gensim.model')
max_vocab = 30000
vocab = list(model.wv.vocab.keys())[:max_vocab]
vectors = [model.wv[word] for word in vocab]

n_clusters = 1000
kmeans_model = KMeans(
    n_clusters=n_clusters, 
    verbose=1, 
    random_state=42, 
    n_jobs=-1
)
kmeans_model.fit(vectors)

cluster_labels = kmeans_model.labels_
cluster_to_words = defaultdict(list)

for cluster_id, word in zip(cluster_labels, vocab):
    cluster_to_words[cluster_id].append(word)

for words in cluster_to_words.values():
    print(words[:10])
