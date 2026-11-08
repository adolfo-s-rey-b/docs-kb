[Skip to main content](https://scikit-learn.org/stable/auto_examples/applications/plot_topics_extraction_with_nmf_lda.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/applications/plot_topics_extraction_with_nmf_lda.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/applications/plot_topics_extraction_with_nmf_lda.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/applications/plot_topics_extraction_with_nmf_lda.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/applications/plot_topics_extraction_with_nmf_lda.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/applications/plot_topics_extraction_with_nmf_lda.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/applications/plot_topics_extraction_with_nmf_lda.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/applications/plot_topics_extraction_with_nmf_lda.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/applications/plot_topics_extraction_with_nmf_lda.html#sphx-glr-download-auto-examples-applications-plot-topics-extraction-with-nmf-lda-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Topic extraction with Non-negative Matrix Factorization and Latent Dirichlet Allocation[#](https://scikit-learn.org/stable/auto_examples/applications/plot_topics_extraction_with_nmf_lda.html#topic-extraction-with-non-negative-matrix-factorization-and-latent-dirichlet-allocation "Link to this heading")

===============================================================================================================================================================================================================================================================================================================

This is an example of applying [`NMF`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.NMF.html#sklearn.decomposition.NMF "sklearn.decomposition.NMF")
 and [`LatentDirichletAllocation`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.LatentDirichletAllocation.html#sklearn.decomposition.LatentDirichletAllocation "sklearn.decomposition.LatentDirichletAllocation")
 on a corpus of documents and extract additive models of the topic structure of the corpus. The output is a plot of topics, each represented as bar plot using top few words based on weights.

Non-negative Matrix Factorization is applied with two different objective functions: the Frobenius norm, and the generalized Kullback-Leibler divergence. The latter is equivalent to Probabilistic Latent Semantic Indexing.

The default parameters (n\_samples / n\_features / n\_components) should make the example runnable in a couple of tens of seconds. You can try to increase the dimensions of the problem, but be aware that the time complexity is polynomial in NMF. In LDA, the time complexity is proportional to (n\_samples \* iterations).

*   ![Topics in NMF model (Frobenius norm), Topic 1, Topic 2, Topic 3, Topic 4, Topic 5, Topic 6, Topic 7, Topic 8, Topic 9, Topic 10](https://scikit-learn.org/stable/_images/sphx_glr_plot_topics_extraction_with_nmf_lda_001.png)
*   ![Topics in NMF model (generalized Kullback-Leibler divergence), Topic 1, Topic 2, Topic 3, Topic 4, Topic 5, Topic 6, Topic 7, Topic 8, Topic 9, Topic 10](https://scikit-learn.org/stable/_images/sphx_glr_plot_topics_extraction_with_nmf_lda_002.png)
*   ![Topics in MiniBatchNMF model (Frobenius norm), Topic 1, Topic 2, Topic 3, Topic 4, Topic 5, Topic 6, Topic 7, Topic 8, Topic 9, Topic 10](https://scikit-learn.org/stable/_images/sphx_glr_plot_topics_extraction_with_nmf_lda_003.png)
*   ![Topics in MiniBatchNMF model (generalized Kullback-Leibler divergence), Topic 1, Topic 2, Topic 3, Topic 4, Topic 5, Topic 6, Topic 7, Topic 8, Topic 9, Topic 10](https://scikit-learn.org/stable/_images/sphx_glr_plot_topics_extraction_with_nmf_lda_004.png)
*   ![Topics in LDA model, Topic 1, Topic 2, Topic 3, Topic 4, Topic 5, Topic 6, Topic 7, Topic 8, Topic 9, Topic 10](https://scikit-learn.org/stable/_images/sphx_glr_plot_topics_extraction_with_nmf_lda_005.png)

Loading dataset...
done in 1.226s.
Extracting tf-idf features for NMF...
done in 0.267s.
Extracting tf features for LDA...
done in 0.261s.

Fitting the NMF model (Frobenius norm) with tf-idf features, n\_samples=2000 and n\_features=1000...
done in 0.076s.


 Fitting the NMF model (generalized Kullback-Leibler divergence) with tf-idf features, n\_samples=2000 and n\_features=1000...
done in 1.571s.


 Fitting the MiniBatchNMF model (Frobenius norm) with tf-idf features, n\_samples=2000 and n\_features=1000, batch\_size=128...
done in 0.102s.


 Fitting the MiniBatchNMF model (generalized Kullback-Leibler divergence) with tf-idf features, n\_samples=2000 and n\_features=1000, batch\_size=128...
done in 0.228s.


 Fitting LDA models with tf features, n\_samples=2000 and n\_features=1000...
done in 2.761s.

Copy to clipboard

  

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

from time import [time](https://docs.python.org/3/library/time.html#time.time "time.time")

import matplotlib.pyplot as plt

from sklearn.datasets import [fetch\_20newsgroups](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_20newsgroups.html#sklearn.datasets.fetch_20newsgroups "sklearn.datasets.fetch_20newsgroups")
from sklearn.decomposition import [NMF](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.NMF.html#sklearn.decomposition.NMF "sklearn.decomposition.NMF")
, [LatentDirichletAllocation](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.LatentDirichletAllocation.html#sklearn.decomposition.LatentDirichletAllocation "sklearn.decomposition.LatentDirichletAllocation")
, [MiniBatchNMF](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.MiniBatchNMF.html#sklearn.decomposition.MiniBatchNMF "sklearn.decomposition.MiniBatchNMF")
from sklearn.feature\_extraction.text import [CountVectorizer](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html#sklearn.feature_extraction.text.CountVectorizer "sklearn.feature_extraction.text.CountVectorizer")
, [TfidfVectorizer](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html#sklearn.feature_extraction.text.TfidfVectorizer "sklearn.feature_extraction.text.TfidfVectorizer")

n\_samples \= 2000
n\_features \= 1000
n\_components \= 10
n\_top\_words \= 20
batch\_size \= 128
init \= "nndsvda"

def plot\_top\_words(model, feature\_names, n\_top\_words, title):
    fig, axes \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(2, 5, figsize\=(30, 15), sharex\=True)
    axes \= axes.flatten()
    for topic\_idx, topic in enumerate(model.components\_):
        top\_features\_ind \= topic.argsort()\[\-n\_top\_words:\]
        top\_features \= feature\_names\[top\_features\_ind\]
        weights \= topic\[top\_features\_ind\]

        ax \= axes\[topic\_idx\]
        ax.barh(top\_features, weights, height\=0.7)
        ax.set\_title(f"Topic {topic\_idx + 1}", fontdict\={"fontsize": 30})
        ax.tick\_params(axis\="both", which\="major", labelsize\=20)
        for i in "top right left".split():
            ax.spines\[i\].set\_visible(False)
        fig.suptitle(title, fontsize\=40)

    [plt.subplots\_adjust](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots_adjust.html#matplotlib.pyplot.subplots_adjust "matplotlib.pyplot.subplots_adjust")
(top\=0.90, bottom\=0.05, wspace\=0.90, hspace\=0.3)
    [plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

\# Load the 20 newsgroups dataset and vectorize it. We use a few heuristics
\# to filter out useless terms early on: the posts are stripped of headers,
\# footers and quoted replies, and common English words, words occurring in
\# only one document or in at least 95% of the documents are removed.

print("Loading dataset...")
t0 \= [time](https://docs.python.org/3/library/time.html#time.time "time.time")
()
data, \_ \= [fetch\_20newsgroups](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_20newsgroups.html#sklearn.datasets.fetch_20newsgroups "sklearn.datasets.fetch_20newsgroups")
(
    shuffle\=True,
    random\_state\=1,
    remove\=("headers", "footers", "quotes"),
    return\_X\_y\=True,
)
data\_samples \= data\[:n\_samples\]
print("done in %0.3fs." % ([time](https://docs.python.org/3/library/time.html#time.time "time.time")
() \- t0))

\# Use tf-idf features for NMF.
print("Extracting tf-idf features for NMF...")
tfidf\_vectorizer \= [TfidfVectorizer](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html#sklearn.feature_extraction.text.TfidfVectorizer "sklearn.feature_extraction.text.TfidfVectorizer")
(
    max\_df\=0.95, min\_df\=2, max\_features\=n\_features, stop\_words\="english"
)
t0 \= [time](https://docs.python.org/3/library/time.html#time.time "time.time")
()
tfidf \= tfidf\_vectorizer.fit\_transform(data\_samples)
print("done in %0.3fs." % ([time](https://docs.python.org/3/library/time.html#time.time "time.time")
() \- t0))

\# Use tf (raw term count) features for LDA.
print("Extracting tf features for LDA...")
tf\_vectorizer \= [CountVectorizer](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html#sklearn.feature_extraction.text.CountVectorizer "sklearn.feature_extraction.text.CountVectorizer")
(
    max\_df\=0.95, min\_df\=2, max\_features\=n\_features, stop\_words\="english"
)
t0 \= [time](https://docs.python.org/3/library/time.html#time.time "time.time")
()
tf \= tf\_vectorizer.fit\_transform(data\_samples)
print("done in %0.3fs." % ([time](https://docs.python.org/3/library/time.html#time.time "time.time")
() \- t0))
print()

\# Fit the NMF model
print(
    "Fitting the NMF model (Frobenius norm) with tf-idf features, "
    "n\_samples=%d and n\_features=%d..." % (n\_samples, n\_features)
)
t0 \= [time](https://docs.python.org/3/library/time.html#time.time "time.time")
()
nmf \= [NMF](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.NMF.html#sklearn.decomposition.NMF "sklearn.decomposition.NMF")
(
    n\_components\=n\_components,
    random\_state\=1,
    init\=init,
    beta\_loss\="frobenius",
    alpha\_W\=0.00005,
    alpha\_H\=0.00005,
    l1\_ratio\=1,
).fit(tfidf)
print("done in %0.3fs." % ([time](https://docs.python.org/3/library/time.html#time.time "time.time")
() \- t0))

tfidf\_feature\_names \= tfidf\_vectorizer.get\_feature\_names\_out()
plot\_top\_words(
    nmf, tfidf\_feature\_names, n\_top\_words, "Topics in NMF model (Frobenius norm)"
)

\# Fit the NMF model
print(
    "\\n" \* 2,
    "Fitting the NMF model (generalized Kullback-Leibler "
    "divergence) with tf-idf features, n\_samples=%d and n\_features=%d..."
    % (n\_samples, n\_features),
)
t0 \= [time](https://docs.python.org/3/library/time.html#time.time "time.time")
()
nmf \= [NMF](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.NMF.html#sklearn.decomposition.NMF "sklearn.decomposition.NMF")
(
    n\_components\=n\_components,
    random\_state\=1,
    init\=init,
    beta\_loss\="kullback-leibler",
    solver\="mu",
    max\_iter\=1000,
    alpha\_W\=0.00005,
    alpha\_H\=0.00005,
    l1\_ratio\=0.5,
).fit(tfidf)
print("done in %0.3fs." % ([time](https://docs.python.org/3/library/time.html#time.time "time.time")
() \- t0))

tfidf\_feature\_names \= tfidf\_vectorizer.get\_feature\_names\_out()
plot\_top\_words(
    nmf,
    tfidf\_feature\_names,
    n\_top\_words,
    "Topics in NMF model (generalized Kullback-Leibler divergence)",
)

\# Fit the MiniBatchNMF model
print(
    "\\n" \* 2,
    "Fitting the MiniBatchNMF model (Frobenius norm) with tf-idf "
    "features, n\_samples=%d and n\_features=%d, batch\_size=%d..."
    % (n\_samples, n\_features, batch\_size),
)
t0 \= [time](https://docs.python.org/3/library/time.html#time.time "time.time")
()
mbnmf \= [MiniBatchNMF](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.MiniBatchNMF.html#sklearn.decomposition.MiniBatchNMF "sklearn.decomposition.MiniBatchNMF")
(
    n\_components\=n\_components,
    random\_state\=1,
    batch\_size\=batch\_size,
    init\=init,
    beta\_loss\="frobenius",
    alpha\_W\=0.00005,
    alpha\_H\=0.00005,
    l1\_ratio\=0.5,
).fit(tfidf)
print("done in %0.3fs." % ([time](https://docs.python.org/3/library/time.html#time.time "time.time")
() \- t0))

tfidf\_feature\_names \= tfidf\_vectorizer.get\_feature\_names\_out()
plot\_top\_words(
    mbnmf,
    tfidf\_feature\_names,
    n\_top\_words,
    "Topics in MiniBatchNMF model (Frobenius norm)",
)

\# Fit the MiniBatchNMF model
print(
    "\\n" \* 2,
    "Fitting the MiniBatchNMF model (generalized Kullback-Leibler "
    "divergence) with tf-idf features, n\_samples=%d and n\_features=%d, "
    "batch\_size=%d..." % (n\_samples, n\_features, batch\_size),
)
t0 \= [time](https://docs.python.org/3/library/time.html#time.time "time.time")
()
mbnmf \= [MiniBatchNMF](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.MiniBatchNMF.html#sklearn.decomposition.MiniBatchNMF "sklearn.decomposition.MiniBatchNMF")
(
    n\_components\=n\_components,
    random\_state\=1,
    batch\_size\=batch\_size,
    init\=init,
    beta\_loss\="kullback-leibler",
    alpha\_W\=0.00005,
    alpha\_H\=0.00005,
    l1\_ratio\=0.5,
).fit(tfidf)
print("done in %0.3fs." % ([time](https://docs.python.org/3/library/time.html#time.time "time.time")
() \- t0))

tfidf\_feature\_names \= tfidf\_vectorizer.get\_feature\_names\_out()
plot\_top\_words(
    mbnmf,
    tfidf\_feature\_names,
    n\_top\_words,
    "Topics in MiniBatchNMF model (generalized Kullback-Leibler divergence)",
)

print(
    "\\n" \* 2,
    "Fitting LDA models with tf features, n\_samples=%d and n\_features=%d..."
    % (n\_samples, n\_features),
)
lda \= [LatentDirichletAllocation](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.LatentDirichletAllocation.html#sklearn.decomposition.LatentDirichletAllocation "sklearn.decomposition.LatentDirichletAllocation")
(
    n\_components\=n\_components,
    max\_iter\=5,
    learning\_method\="online",
    learning\_offset\=50.0,
    random\_state\=0,
)
t0 \= [time](https://docs.python.org/3/library/time.html#time.time "time.time")
()
lda.fit(tf)
print("done in %0.3fs." % ([time](https://docs.python.org/3/library/time.html#time.time "time.time")
() \- t0))

tf\_feature\_names \= tf\_vectorizer.get\_feature\_names\_out()
plot\_top\_words(lda, tf\_feature\_names, n\_top\_words, "Topics in LDA model")

Copy to clipboard

**Total running time of the script:** (0 minutes 12.329 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/applications/plot_topics_extraction_with_nmf_lda.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/applications/plot_topics_extraction_with_nmf_lda.ipynb)

[`Download Jupyter notebook: plot_topics_extraction_with_nmf_lda.ipynb`](https://scikit-learn.org/stable/_downloads/b26574ccf9c31e12ab2afd8d683f3279/plot_topics_extraction_with_nmf_lda.ipynb)

[`Download Python source code: plot_topics_extraction_with_nmf_lda.py`](https://scikit-learn.org/stable/_downloads/2b2bebba7f9fb4d03b9c12d63c8b44ad/plot_topics_extraction_with_nmf_lda.py)

[`Download zipped: plot_topics_extraction_with_nmf_lda.zip`](https://scikit-learn.org/stable/_downloads/6c079edbd131768ca2f3068e9fdb94eb/plot_topics_extraction_with_nmf_lda.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_1_1_0_thumb.png)

[Release Highlights for scikit-learn 1.1](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_1_0.html)

Release Highlights for scikit-learn 1.1

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_document_clustering_thumb.png)

[Clustering text documents using k-means](https://scikit-learn.org/stable/auto_examples/text/plot_document_clustering.html)

Clustering text documents using k-means

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_lda_thumb.png)

[Normal, Ledoit-Wolf and OAS Linear Discriminant Analysis for classification](https://scikit-learn.org/stable/auto_examples/classification/plot_lda.html)

Normal, Ledoit-Wolf and OAS Linear Discriminant Analysis for classification

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_compare_reduction_thumb.png)

[Selecting dimensionality reduction with Pipeline and GridSearchCV](https://scikit-learn.org/stable/auto_examples/compose/plot_compare_reduction.html)

Selecting dimensionality reduction with Pipeline and GridSearchCV

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

[Download source code](https://scikit-learn.org/stable/_downloads/2b2bebba7f9fb4d03b9c12d63c8b44ad/plot_topics_extraction_with_nmf_lda.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/b26574ccf9c31e12ab2afd8d683f3279/plot_topics_extraction_with_nmf_lda.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/6c079edbd131768ca2f3068e9fdb94eb/plot_topics_extraction_with_nmf_lda.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/applications/plot_topics_extraction_with_nmf_lda.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/applications/plot_topics_extraction_with_nmf_lda.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)