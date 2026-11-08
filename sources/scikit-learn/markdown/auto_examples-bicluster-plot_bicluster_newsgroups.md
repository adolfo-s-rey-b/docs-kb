[Skip to main content](https://scikit-learn.org/stable/auto_examples/bicluster/plot_bicluster_newsgroups.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/bicluster/plot_bicluster_newsgroups.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/bicluster/plot_bicluster_newsgroups.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/bicluster/plot_bicluster_newsgroups.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/bicluster/plot_bicluster_newsgroups.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/bicluster/plot_bicluster_newsgroups.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/bicluster/plot_bicluster_newsgroups.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/bicluster/plot_bicluster_newsgroups.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/bicluster/plot_bicluster_newsgroups.html#sphx-glr-download-auto-examples-bicluster-plot-bicluster-newsgroups-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Biclustering documents with the Spectral Co-clustering algorithm[#](https://scikit-learn.org/stable/auto_examples/bicluster/plot_bicluster_newsgroups.html#biclustering-documents-with-the-spectral-co-clustering-algorithm "Link to this heading")

====================================================================================================================================================================================================================================================

This example demonstrates the Spectral Co-clustering algorithm on the twenty newsgroups dataset. The ‘comp.os.ms-windows.misc’ category is excluded because it contains many posts containing nothing but data.

The TF-IDF vectorized posts form a word frequency matrix, which is then biclustered using Dhillon’s Spectral Co-Clustering algorithm. The resulting document-word biclusters indicate subsets words used more often in those subsets documents.

For a few of the best biclusters, its most common document categories and its ten most important words get printed. The best biclusters are determined by their normalized cut. The best words are determined by comparing their sums inside and outside the bicluster.

For comparison, the documents are also clustered using MiniBatchKMeans. The document clusters derived from the biclusters achieve a better V-measure than clusters found by MiniBatchKMeans.

Vectorizing...
Coclustering...
Done in 1.08s. V-measure: 0.4415
MiniBatchKMeans...
Done in 3.35s. V-measure: 0.3043

Best biclusters:
----------------
bicluster 0 : 8 documents, 6 words
categories   : 100% talk.politics.mideast
words        : cosmo, angmar, alfalfa, alphalpha, proline, benson

bicluster 1 : 1948 documents, 4325 words
categories   : 23% talk.politics.guns, 18% talk.politics.misc, 17% sci.med
words        : gun, guns, geb, banks, gordon, clinton, pitt, cdt, surrender, veal

bicluster 2 : 1259 documents, 3534 words
categories   : 27% soc.religion.christian, 25% talk.politics.mideast, 25% alt.atheism
words        : god, jesus, christians, kent, sin, objective, belief, christ, faith, moral

bicluster 3 : 775 documents, 1623 words
categories   : 30% comp.windows.x, 25% comp.sys.ibm.pc.hardware, 20% comp.graphics
words        : scsi, nada, ide, vga, esdi, isa, kth, s3, vlb, bmug

bicluster 4 : 2180 documents, 2802 words
categories   : 18% comp.sys.mac.hardware, 16% sci.electronics, 16% comp.sys.ibm.pc.hardware
words        : voltage, shipping, circuit, receiver, processing, scope, mpce, analog, kolstad, umass

Copy to clipboard

  

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause
from collections import [Counter](https://docs.python.org/3/library/collections.html#collections.Counter "collections.Counter")
from time import [time](https://docs.python.org/3/library/time.html#time.time "time.time")

import numpy as np

from sklearn.cluster import [MiniBatchKMeans](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.MiniBatchKMeans.html#sklearn.cluster.MiniBatchKMeans "sklearn.cluster.MiniBatchKMeans")
, [SpectralCoclustering](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.SpectralCoclustering.html#sklearn.cluster.SpectralCoclustering "sklearn.cluster.SpectralCoclustering")
from sklearn.datasets import [fetch\_20newsgroups](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_20newsgroups.html#sklearn.datasets.fetch_20newsgroups "sklearn.datasets.fetch_20newsgroups")
from sklearn.feature\_extraction.text import [TfidfVectorizer](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html#sklearn.feature_extraction.text.TfidfVectorizer "sklearn.feature_extraction.text.TfidfVectorizer")
from sklearn.metrics.cluster import [v\_measure\_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.v_measure_score.html#sklearn.metrics.v_measure_score "sklearn.metrics.v_measure_score")

def number\_normalizer(tokens):
    """Map all numeric tokens to a placeholder.

    For many applications, tokens that begin with a number are not directly
    useful, but the fact that such a token exists can be relevant.  By applying
    this form of dimensionality reduction, some methods may perform better.
    """
    return ("#NUMBER" if token\[0\].isdigit() else token for token in tokens)

class NumberNormalizingVectorizer([TfidfVectorizer](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html#sklearn.feature_extraction.text.TfidfVectorizer "sklearn.feature_extraction.text.TfidfVectorizer")
):
    def build\_tokenizer(self):
        tokenize \= super().build\_tokenizer()
        return lambda doc: list(number\_normalizer(tokenize(doc)))

\# exclude 'comp.os.ms-windows.misc'
categories \= \[\
    "alt.atheism",\
    "comp.graphics",\
    "comp.sys.ibm.pc.hardware",\
    "comp.sys.mac.hardware",\
    "comp.windows.x",\
    "misc.forsale",\
    "rec.autos",\
    "rec.motorcycles",\
    "rec.sport.baseball",\
    "rec.sport.hockey",\
    "sci.crypt",\
    "sci.electronics",\
    "sci.med",\
    "sci.space",\
    "soc.religion.christian",\
    "talk.politics.guns",\
    "talk.politics.mideast",\
    "talk.politics.misc",\
    "talk.religion.misc",\
\]
newsgroups \= [fetch\_20newsgroups](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_20newsgroups.html#sklearn.datasets.fetch_20newsgroups "sklearn.datasets.fetch_20newsgroups")
(categories\=categories)
y\_true \= newsgroups.target

vectorizer \= NumberNormalizingVectorizer(stop\_words\="english", min\_df\=5)
cocluster \= [SpectralCoclustering](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.SpectralCoclustering.html#sklearn.cluster.SpectralCoclustering "sklearn.cluster.SpectralCoclustering")
(
    n\_clusters\=len(categories), svd\_method\="arpack", random\_state\=0
)
kmeans \= [MiniBatchKMeans](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.MiniBatchKMeans.html#sklearn.cluster.MiniBatchKMeans "sklearn.cluster.MiniBatchKMeans")
(
    n\_clusters\=len(categories), batch\_size\=20000, random\_state\=0, n\_init\=3
)

print("Vectorizing...")
X \= vectorizer.fit\_transform(newsgroups.data)

print("Coclustering...")
start\_time \= [time](https://docs.python.org/3/library/time.html#time.time "time.time")
()
cocluster.fit(X)
y\_cocluster \= cocluster.row\_labels\_
print(
    f"Done in {[time](https://docs.python.org/3/library/time.html#time.time "time.time")
() \- start\_time:.2f}s. V-measure: \\
{[v\_measure\_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.v_measure_score.html#sklearn.metrics.v_measure_score "sklearn.metrics.v_measure_score")
(y\_cocluster, y\_true):.4f}"
)

print("MiniBatchKMeans...")
start\_time \= [time](https://docs.python.org/3/library/time.html#time.time "time.time")
()
y\_kmeans \= kmeans.fit\_predict(X)
print(
    f"Done in {[time](https://docs.python.org/3/library/time.html#time.time "time.time")
() \- start\_time:.2f}s. V-measure: \\
{[v\_measure\_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.v_measure_score.html#sklearn.metrics.v_measure_score "sklearn.metrics.v_measure_score")
(y\_kmeans, y\_true):.4f}"
)

feature\_names \= vectorizer.get\_feature\_names\_out()
document\_names \= list(newsgroups.target\_names\[i\] for i in newsgroups.target)

def bicluster\_ncut(i):
    rows, cols \= cocluster.get\_indices(i)
    if not ([np.any](https://numpy.org/doc/stable/reference/generated/numpy.any.html#numpy.any "numpy.any")
(rows) and [np.any](https://numpy.org/doc/stable/reference/generated/numpy.any.html#numpy.any "numpy.any")
(cols)):
        import sys

        return [sys.float\_info.max](https://docs.python.org/3/library/sys.html#sys.float_info.max "sys.float_info.max")
    row\_complement \= [np.nonzero](https://numpy.org/doc/stable/reference/generated/numpy.nonzero.html#numpy.nonzero "numpy.nonzero")
([np.logical\_not](https://numpy.org/doc/stable/reference/generated/numpy.logical_not.html#numpy.logical_not "numpy.logical_not")
(cocluster.rows\_\[i\]))\[0\]
    col\_complement \= [np.nonzero](https://numpy.org/doc/stable/reference/generated/numpy.nonzero.html#numpy.nonzero "numpy.nonzero")
([np.logical\_not](https://numpy.org/doc/stable/reference/generated/numpy.logical_not.html#numpy.logical_not "numpy.logical_not")
(cocluster.columns\_\[i\]))\[0\]
    \# Note: the following is identical to X\[rows\[:, np.newaxis\],\
    \# cols\].sum() but much faster in scipy <= 0.16
    weight \= X\[rows\]\[:, cols\].sum()
    cut \= X\[row\_complement\]\[:, cols\].sum() + X\[rows\]\[:, col\_complement\].sum()
    return cut / weight

bicluster\_ncuts \= list(bicluster\_ncut(i) for i in range(len(newsgroups.target\_names)))
best\_idx \= [np.argsort](https://numpy.org/doc/stable/reference/generated/numpy.argsort.html#numpy.argsort "numpy.argsort")
(bicluster\_ncuts)\[:5\]

print()
print("Best biclusters:")
print("----------------")
for idx, cluster in enumerate(best\_idx):
    n\_rows, n\_cols \= cocluster.get\_shape(cluster)
    cluster\_docs, cluster\_words \= cocluster.get\_indices(cluster)
    if not len(cluster\_docs) or not len(cluster\_words):
        continue

    \# categories
    counter \= [Counter](https://docs.python.org/3/library/collections.html#collections.Counter "collections.Counter")
(document\_names\[doc\] for doc in cluster\_docs)

    cat\_string \= ", ".join(
        f"{(c / n\_rows \* 100):.0f}% {name}" for name, c in counter.most\_common(3)
    )

    \# words
    out\_of\_cluster\_docs \= cocluster.row\_labels\_ != cluster
    out\_of\_cluster\_docs \= out\_of\_cluster\_docs.nonzero()\[0\]
    word\_col \= X\[:, cluster\_words\]
    word\_scores \= [np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
(
        word\_col\[cluster\_docs, :\].sum(axis\=0)
        \- word\_col\[out\_of\_cluster\_docs, :\].sum(axis\=0)
    )
    word\_scores \= word\_scores.ravel()
    important\_words \= list(
        feature\_names\[cluster\_words\[i\]\] for i in word\_scores.argsort()\[:\-11:\-1\]
    )

    print(f"bicluster {idx} : {n\_rows} documents, {n\_cols} words")
    print(f"categories   : {cat\_string}")
    print(f"words        : {', '.join(important\_words)}\\n")

Copy to clipboard

**Total running time of the script:** (0 minutes 6.869 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo1.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/bicluster/plot_bicluster_newsgroups.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo1.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/bicluster/plot_bicluster_newsgroups.ipynb)

[`Download Jupyter notebook: plot_bicluster_newsgroups.ipynb`](https://scikit-learn.org/stable/_downloads/3f7191b01d0103d1886c959ed7687c4d/plot_bicluster_newsgroups.ipynb)

[`Download Python source code: plot_bicluster_newsgroups.py`](https://scikit-learn.org/stable/_downloads/e68419b513284db108081422c73a5667/plot_bicluster_newsgroups.py)

[`Download zipped: plot_bicluster_newsgroups.zip`](https://scikit-learn.org/stable/_downloads/ccd24a43e08ccb154430edf7f927cfc7/plot_bicluster_newsgroups.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_document_classification_20newsgroups_thumb.png)

[Classification of text documents using sparse features](https://scikit-learn.org/stable/auto_examples/text/plot_document_classification_20newsgroups.html)

Classification of text documents using sparse features

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_document_clustering_thumb.png)

[Clustering text documents using k-means](https://scikit-learn.org/stable/auto_examples/text/plot_document_clustering.html)

Clustering text documents using k-means

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_hashing_vs_dict_vectorizer_thumb.png)

[FeatureHasher and DictVectorizer Comparison](https://scikit-learn.org/stable/auto_examples/text/plot_hashing_vs_dict_vectorizer.html)

FeatureHasher and DictVectorizer Comparison

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_spectral_coclustering_thumb.png)

[A demo of the Spectral Co-Clustering algorithm](https://scikit-learn.org/stable/auto_examples/bicluster/plot_spectral_coclustering.html)

A demo of the Spectral Co-Clustering algorithm

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

[Download source code](https://scikit-learn.org/stable/_downloads/e68419b513284db108081422c73a5667/plot_bicluster_newsgroups.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/3f7191b01d0103d1886c959ed7687c4d/plot_bicluster_newsgroups.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/ccd24a43e08ccb154430edf7f927cfc7/plot_bicluster_newsgroups.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo1.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/bicluster/plot_bicluster_newsgroups.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo1.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/bicluster/plot_bicluster_newsgroups.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)