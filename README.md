# README
本課題の内容は以下の通りであった。

①　データセットを用意する。

②　クラスタ分析（k-近傍法K-平均法たは階層化分類法）

③　独自の分析

データセットに自然言語を設定したことから以下の解析を行った
- 形態素解析（分かち書き）
    - MeCab
- 係り受け解析
    - Spacy(NoteBook)
- 固有表現抽出
    - Spacy（NoteBook）
- WordCloud
- 単語の分散表現化（word2vector）
    - gensim(Word2Vec, word2vec), matplotlib
- クラスタリング
    - K-平均法（k-means）
        - sklearn(KMeans)
    - 階層化分類法（ward法）
        - scipy
- 単語ベクトルの可視化（t-SNE）
    - bhtsne

今回は日本語を使用したためmatploylibにて文字化けが発生した。
[参考サイト](https://self-development.info/ipaexgothic%e3%81%ab%e3%82%88%e3%82%8bmatplotlib%e3%81%ae%e6%97%a5%e6%9c%ac%e8%aa%9e%e5%8c%96%e3%80%90python%e3%80%91/)


これらの解析を行ったコードがこのレポジトリに残されています
(2021/07/27)
