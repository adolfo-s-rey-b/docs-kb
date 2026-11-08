[Skip to main content](https://scikit-learn.org/stable/auto_examples/text/plot_document_clustering.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/text/plot_document_clustering.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/text/plot_document_clustering.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/text/plot_document_clustering.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/text/plot_document_clustering.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/text/plot_document_clustering.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/text/plot_document_clustering.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/text/plot_document_clustering.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/text/plot_document_clustering.html#sphx-glr-download-auto-examples-text-plot-document-clustering-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Clustering text documents using k-means[#](https://scikit-learn.org/stable/auto_examples/text/plot_document_clustering.html#clustering-text-documents-using-k-means "Link to this heading")

============================================================================================================================================================================================

This is an example showing how the scikit-learn API can be used to cluster documents by topics using a [Bag of Words approach](https://en.wikipedia.org/wiki/Bag-of-words_model)
.

Two algorithms are demonstrated, namely [`KMeans`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html#sklearn.cluster.KMeans "sklearn.cluster.KMeans")
 and its more scalable variant, [`MiniBatchKMeans`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.MiniBatchKMeans.html#sklearn.cluster.MiniBatchKMeans "sklearn.cluster.MiniBatchKMeans")
. Additionally, latent semantic analysis is used to reduce dimensionality and discover latent patterns in the data.

This example uses two different text vectorizers: a [`TfidfVectorizer`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html#sklearn.feature_extraction.text.TfidfVectorizer "sklearn.feature_extraction.text.TfidfVectorizer")
 and a [`HashingVectorizer`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.HashingVectorizer.html#sklearn.feature_extraction.text.HashingVectorizer "sklearn.feature_extraction.text.HashingVectorizer")
. See the example notebook [FeatureHasher and DictVectorizer Comparison](https://scikit-learn.org/stable/auto_examples/text/plot_hashing_vs_dict_vectorizer.html#sphx-glr-auto-examples-text-plot-hashing-vs-dict-vectorizer-py)
 for more information on vectorizers and a comparison of their processing times.

For document analysis via a supervised learning approach, see the example script [Classification of text documents using sparse features](https://scikit-learn.org/stable/auto_examples/text/plot_document_classification_20newsgroups.html#sphx-glr-auto-examples-text-plot-document-classification-20newsgroups-py)
.

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

Copy to clipboard

Loading text data[#](https://scikit-learn.org/stable/auto_examples/text/plot_document_clustering.html#loading-text-data "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------

We load data from [The 20 newsgroups text dataset](https://scikit-learn.org/stable/datasets/real_world.html#newsgroups-dataset)
, which comprises around 18,000 newsgroups posts on 20 topics. For illustrative purposes and to reduce the computational cost, we select a subset of 4 topics only accounting for around 3,400 documents. See the example [Classification of text documents using sparse features](https://scikit-learn.org/stable/auto_examples/text/plot_document_classification_20newsgroups.html#sphx-glr-auto-examples-text-plot-document-classification-20newsgroups-py)
 to gain intuition on the overlap of such topics.

Notice that, by default, the text samples contain some message metadata such as `"headers"`, `"footers"` (signatures) and `"quotes"` to other posts. We use the `remove` parameter from [`fetch_20newsgroups`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_20newsgroups.html#sklearn.datasets.fetch_20newsgroups "sklearn.datasets.fetch_20newsgroups")
 to strip those features and have a more sensible clustering problem.

import numpy as np

from sklearn.datasets import [fetch\_20newsgroups](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_20newsgroups.html#sklearn.datasets.fetch_20newsgroups "sklearn.datasets.fetch_20newsgroups")

categories \= \[\
    "alt.atheism",\
    "talk.religion.misc",\
    "comp.graphics",\
    "sci.space",\
\]

dataset \= [fetch\_20newsgroups](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_20newsgroups.html#sklearn.datasets.fetch_20newsgroups "sklearn.datasets.fetch_20newsgroups")
(
    remove\=("headers", "footers", "quotes"),
    subset\="all",
    categories\=categories,
    shuffle\=True,
    random\_state\=42,
)

labels \= dataset.target
unique\_labels, category\_sizes \= [np.unique](https://numpy.org/doc/stable/reference/generated/numpy.unique.html#numpy.unique "numpy.unique")
(labels, return\_counts\=True)
true\_k \= unique\_labels.shape\[0\]

print(f"{len(dataset.data)} documents - {true\_k} categories")

Copy to clipboard

3387 documents - 4 categories

Copy to clipboard

Quantifying the quality of clustering results[#](https://scikit-learn.org/stable/auto_examples/text/plot_document_clustering.html#quantifying-the-quality-of-clustering-results "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

In this section we define a function to score different clustering pipelines using several metrics.

Clustering algorithms are fundamentally unsupervised learning methods. However, since we happen to have class labels for this specific dataset, it is possible to use evaluation metrics that leverage this “supervised” ground truth information to quantify the quality of the resulting clusters. Examples of such metrics are the following:

*   homogeneity, which quantifies how much clusters contain only members of a single class;
    
*   completeness, which quantifies how much members of a given class are assigned to the same clusters;
    
*   V-measure, the harmonic mean of completeness and homogeneity;
    
*   Rand-Index, which measures how frequently pairs of data points are grouped consistently according to the result of the clustering algorithm and the ground truth class assignment;
    
*   Adjusted Rand-Index, a chance-adjusted Rand-Index such that random cluster assignment have an ARI of 0.0 in expectation.
    

If the ground truth labels are not known, evaluation can only be performed using the model results itself. In that case, the Silhouette Coefficient comes in handy. See [Selecting the number of clusters with silhouette analysis on KMeans clustering](https://scikit-learn.org/stable/auto_examples/cluster/plot_kmeans_silhouette_analysis.html#sphx-glr-auto-examples-cluster-plot-kmeans-silhouette-analysis-py)
 for an example on how to do it.

For more reference, see [Clustering performance evaluation](https://scikit-learn.org/stable/modules/clustering.html#clustering-evaluation)
.

from collections import [defaultdict](https://docs.python.org/3/library/collections.html#collections.defaultdict "collections.defaultdict")
from time import [time](https://docs.python.org/3/library/time.html#time.time "time.time")

from sklearn import metrics

evaluations \= \[\]
evaluations\_std \= \[\]

def fit\_and\_evaluate(km, X, name\=None, n\_runs\=5):
    name \= km.\_\_class\_\_.\_\_name\_\_ if name is None else name

    train\_times \= \[\]
    scores \= [defaultdict](https://docs.python.org/3/library/collections.html#collections.defaultdict "collections.defaultdict")
(list)
    for seed in range(n\_runs):
        km.set\_params(random\_state\=seed)
        t0 \= [time](https://docs.python.org/3/library/time.html#time.time "time.time")
()
        km.fit(X)
        train\_times.append([time](https://docs.python.org/3/library/time.html#time.time "time.time")
() \- t0)
        scores\["Homogeneity"\].append([metrics.homogeneity\_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.homogeneity_score.html#sklearn.metrics.homogeneity_score "sklearn.metrics.homogeneity_score")
(labels, km.labels\_))
        scores\["Completeness"\].append([metrics.completeness\_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.completeness_score.html#sklearn.metrics.completeness_score "sklearn.metrics.completeness_score")
(labels, km.labels\_))
        scores\["V-measure"\].append([metrics.v\_measure\_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.v_measure_score.html#sklearn.metrics.v_measure_score "sklearn.metrics.v_measure_score")
(labels, km.labels\_))
        scores\["Adjusted Rand-Index"\].append(
            [metrics.adjusted\_rand\_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.adjusted_rand_score.html#sklearn.metrics.adjusted_rand_score "sklearn.metrics.adjusted_rand_score")
(labels, km.labels\_)
        )
        scores\["Silhouette Coefficient"\].append(
            [metrics.silhouette\_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.silhouette_score.html#sklearn.metrics.silhouette_score "sklearn.metrics.silhouette_score")
(X, km.labels\_, sample\_size\=2000)
        )
    train\_times \= [np.asarray](https://numpy.org/doc/stable/reference/generated/numpy.asarray.html#numpy.asarray "numpy.asarray")
(train\_times)

    print(f"clustering done in {train\_times.mean():.2f} ± {train\_times.std():.2f} s ")
    evaluation \= {
        "estimator": name,
        "train\_time": train\_times.mean(),
    }
    evaluation\_std \= {
        "estimator": name,
        "train\_time": train\_times.std(),
    }
    for score\_name, score\_values in scores.items():
        mean\_score, std\_score \= [np.mean](https://numpy.org/doc/stable/reference/generated/numpy.mean.html#numpy.mean "numpy.mean")
(score\_values), [np.std](https://numpy.org/doc/stable/reference/generated/numpy.std.html#numpy.std "numpy.std")
(score\_values)
        print(f"{score\_name}: {mean\_score:.3f} ± {std\_score:.3f}")
        evaluation\[score\_name\] \= mean\_score
        evaluation\_std\[score\_name\] \= std\_score
    evaluations.append(evaluation)
    evaluations\_std.append(evaluation\_std)

Copy to clipboard

K-means clustering on text features[#](https://scikit-learn.org/stable/auto_examples/text/plot_document_clustering.html#k-means-clustering-on-text-features "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Two feature extraction methods are used in this example:

*   [`TfidfVectorizer`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html#sklearn.feature_extraction.text.TfidfVectorizer "sklearn.feature_extraction.text.TfidfVectorizer")
     uses an in-memory vocabulary (a Python dict) to map the most frequent words to features indices and hence compute a word occurrence frequency (sparse) matrix. The word frequencies are then reweighted using the Inverse Document Frequency (IDF) vector collected feature-wise over the corpus.
    
*   [`HashingVectorizer`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.HashingVectorizer.html#sklearn.feature_extraction.text.HashingVectorizer "sklearn.feature_extraction.text.HashingVectorizer")
     hashes word occurrences to a fixed dimensional space, possibly with collisions. The word count vectors are then normalized to each have l2-norm equal to one (projected to the euclidean unit-sphere) which seems to be important for k-means to work in high dimensional space.
    

Furthermore it is possible to post-process those extracted features using dimensionality reduction. We will explore the impact of those choices on the clustering quality in the following.

### Feature Extraction using TfidfVectorizer[#](https://scikit-learn.org/stable/auto_examples/text/plot_document_clustering.html#feature-extraction-using-tfidfvectorizer "Link to this heading")

We first benchmark the estimators using a dictionary vectorizer along with an IDF normalization as provided by [`TfidfVectorizer`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html#sklearn.feature_extraction.text.TfidfVectorizer "sklearn.feature_extraction.text.TfidfVectorizer")
.

from sklearn.feature\_extraction.text import [TfidfVectorizer](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html#sklearn.feature_extraction.text.TfidfVectorizer "sklearn.feature_extraction.text.TfidfVectorizer")

vectorizer \= [TfidfVectorizer](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html#sklearn.feature_extraction.text.TfidfVectorizer "sklearn.feature_extraction.text.TfidfVectorizer")
(
    max\_df\=0.5,
    min\_df\=5,
    stop\_words\="english",
)
t0 \= [time](https://docs.python.org/3/library/time.html#time.time "time.time")
()
X\_tfidf \= vectorizer.fit\_transform(dataset.data)

print(f"vectorization done in {[time](https://docs.python.org/3/library/time.html#time.time "time.time")
() \- t0:.3f} s")
print(f"n\_samples: {X\_tfidf.shape\[0\]}, n\_features: {X\_tfidf.shape\[1\]}")

Copy to clipboard

vectorization done in 0.386 s
n\_samples: 3387, n\_features: 7929

Copy to clipboard

After ignoring terms that appear in more than 50% of the documents (as set by `max_df=0.5`) and terms that are not present in at least 5 documents (set by `min_df=5`), the resulting number of unique terms `n_features` is around 8,000. We can additionally quantify the sparsity of the `X_tfidf` matrix as the fraction of non-zero entries divided by the total number of elements.

print(f"{X\_tfidf.nnz / [np.prod](https://numpy.org/doc/stable/reference/generated/numpy.prod.html#numpy.prod "numpy.prod")
(X\_tfidf.shape):.3f}")

Copy to clipboard

0.007

Copy to clipboard

We find that around 0.7% of the entries of the `X_tfidf` matrix are non-zero.

### Clustering sparse data with k-means[#](https://scikit-learn.org/stable/auto_examples/text/plot_document_clustering.html#clustering-sparse-data-with-k-means "Link to this heading")

As both [`KMeans`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html#sklearn.cluster.KMeans "sklearn.cluster.KMeans")
 and [`MiniBatchKMeans`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.MiniBatchKMeans.html#sklearn.cluster.MiniBatchKMeans "sklearn.cluster.MiniBatchKMeans")
 optimize a non-convex objective function, their clustering is not guaranteed to be optimal for a given random init. Even further, on sparse high-dimensional data such as text vectorized using the Bag of Words approach, k-means can initialize centroids on extremely isolated data points. Those data points can stay their own centroids all along.

The following code illustrates how the previous phenomenon can sometimes lead to highly imbalanced clusters, depending on the random initialization:

from sklearn.cluster import [KMeans](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html#sklearn.cluster.KMeans "sklearn.cluster.KMeans")

for seed in range(5):
    kmeans \= [KMeans](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html#sklearn.cluster.KMeans "sklearn.cluster.KMeans")
(
        n\_clusters\=true\_k,
        max\_iter\=100,
        n\_init\=1,
        random\_state\=seed,
    ).fit(X\_tfidf)
    cluster\_ids, cluster\_sizes \= [np.unique](https://numpy.org/doc/stable/reference/generated/numpy.unique.html#numpy.unique "numpy.unique")
(kmeans.labels\_, return\_counts\=True)
    print(f"Number of elements assigned to each cluster: {cluster\_sizes}")
print()
print(
    "True number of documents in each category according to the class labels: "
    f"{category\_sizes}"
)

Copy to clipboard

Number of elements assigned to each cluster: \[ 481  675 1785  446\]
Number of elements assigned to each cluster: \[1689  638  480  580\]
Number of elements assigned to each cluster: \[   1    1    1 3384\]
Number of elements assigned to each cluster: \[1887  311  332  857\]
Number of elements assigned to each cluster: \[ 291  673 1771  652\]

True number of documents in each category according to the class labels: \[799 973 987 628\]

Copy to clipboard

To avoid this problem, one possibility is to increase the number of runs with independent random initiations `n_init`. In such case the clustering with the best inertia (objective function of k-means) is chosen.

kmeans \= [KMeans](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html#sklearn.cluster.KMeans "sklearn.cluster.KMeans")
(
    n\_clusters\=true\_k,
    max\_iter\=100,
    n\_init\=5,
)

fit\_and\_evaluate(kmeans, X\_tfidf, name\="KMeans\\non tf-idf vectors")

Copy to clipboard

clustering done in 0.18 ± 0.04 s
Homogeneity: 0.349 ± 0.010
Completeness: 0.398 ± 0.009
V-measure: 0.372 ± 0.009
Adjusted Rand-Index: 0.203 ± 0.017
Silhouette Coefficient: 0.007 ± 0.000

Copy to clipboard

All those clustering evaluation metrics have a maximum value of 1.0 (for a perfect clustering result). Higher values are better. Values of the Adjusted Rand-Index close to 0.0 correspond to a random labeling. Notice from the scores above that the cluster assignment is indeed well above chance level, but the overall quality can certainly improve.

Keep in mind that the class labels may not reflect accurately the document topics and therefore metrics that use labels are not necessarily the best to evaluate the quality of our clustering pipeline.

### Performing dimensionality reduction using LSA[#](https://scikit-learn.org/stable/auto_examples/text/plot_document_clustering.html#performing-dimensionality-reduction-using-lsa "Link to this heading")

A `n_init=1` can still be used as long as the dimension of the vectorized space is reduced first to make k-means more stable. For such purpose we use [`TruncatedSVD`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.TruncatedSVD.html#sklearn.decomposition.TruncatedSVD "sklearn.decomposition.TruncatedSVD")
, which works on term count/tf-idf matrices. Since SVD results are not normalized, we redo the normalization to improve the [`KMeans`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html#sklearn.cluster.KMeans "sklearn.cluster.KMeans")
 result. Using SVD to reduce the dimensionality of TF-IDF document vectors is often known as [latent semantic analysis](https://en.wikipedia.org/wiki/Latent_semantic_analysis)
 (LSA) in the information retrieval and text mining literature.

from sklearn.decomposition import [TruncatedSVD](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.TruncatedSVD.html#sklearn.decomposition.TruncatedSVD "sklearn.decomposition.TruncatedSVD")
from sklearn.pipeline import [make\_pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html#sklearn.pipeline.make_pipeline "sklearn.pipeline.make_pipeline")
from sklearn.preprocessing import [Normalizer](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.Normalizer.html#sklearn.preprocessing.Normalizer "sklearn.preprocessing.Normalizer")

lsa \= [make\_pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html#sklearn.pipeline.make_pipeline "sklearn.pipeline.make_pipeline")
([TruncatedSVD](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.TruncatedSVD.html#sklearn.decomposition.TruncatedSVD "sklearn.decomposition.TruncatedSVD")
(n\_components\=100), [Normalizer](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.Normalizer.html#sklearn.preprocessing.Normalizer "sklearn.preprocessing.Normalizer")
(copy\=False))
t0 \= [time](https://docs.python.org/3/library/time.html#time.time "time.time")
()
X\_lsa \= lsa.fit\_transform(X\_tfidf)
explained\_variance \= lsa\[0\].explained\_variance\_ratio\_.sum()

print(f"LSA done in {[time](https://docs.python.org/3/library/time.html#time.time "time.time")
() \- t0:.3f} s")
print(f"Explained variance of the SVD step: {explained\_variance \* 100:.1f}%")

Copy to clipboard

LSA done in 0.316 s
Explained variance of the SVD step: 18.4%

Copy to clipboard

Using a single initialization means the processing time will be reduced for both [`KMeans`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html#sklearn.cluster.KMeans "sklearn.cluster.KMeans")
 and [`MiniBatchKMeans`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.MiniBatchKMeans.html#sklearn.cluster.MiniBatchKMeans "sklearn.cluster.MiniBatchKMeans")
.

kmeans \= [KMeans](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html#sklearn.cluster.KMeans "sklearn.cluster.KMeans")
(
    n\_clusters\=true\_k,
    max\_iter\=100,
    n\_init\=1,
)

fit\_and\_evaluate(kmeans, X\_lsa, name\="KMeans\\nwith LSA on tf-idf vectors")

Copy to clipboard

clustering done in 0.02 ± 0.00 s
Homogeneity: 0.400 ± 0.014
Completeness: 0.431 ± 0.013
V-measure: 0.415 ± 0.011
Adjusted Rand-Index: 0.317 ± 0.016
Silhouette Coefficient: 0.030 ± 0.000

Copy to clipboard

We can observe that clustering on the LSA representation of the document is significantly faster (both because of `n_init=1` and because the dimensionality of the LSA feature space is much smaller). Furthermore, all the clustering evaluation metrics have improved. We repeat the experiment with [`MiniBatchKMeans`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.MiniBatchKMeans.html#sklearn.cluster.MiniBatchKMeans "sklearn.cluster.MiniBatchKMeans")
.

from sklearn.cluster import [MiniBatchKMeans](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.MiniBatchKMeans.html#sklearn.cluster.MiniBatchKMeans "sklearn.cluster.MiniBatchKMeans")

minibatch\_kmeans \= [MiniBatchKMeans](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.MiniBatchKMeans.html#sklearn.cluster.MiniBatchKMeans "sklearn.cluster.MiniBatchKMeans")
(
    n\_clusters\=true\_k,
    n\_init\=1,
    init\_size\=1000,
    batch\_size\=1000,
)

fit\_and\_evaluate(
    minibatch\_kmeans,
    X\_lsa,
    name\="MiniBatchKMeans\\nwith LSA on tf-idf vectors",
)

Copy to clipboard

clustering done in 0.02 ± 0.01 s
Homogeneity: 0.303 ± 0.117
Completeness: 0.342 ± 0.067
V-measure: 0.315 ± 0.103
Adjusted Rand-Index: 0.268 ± 0.125
Silhouette Coefficient: 0.024 ± 0.004

Copy to clipboard

### Top terms per cluster[#](https://scikit-learn.org/stable/auto_examples/text/plot_document_clustering.html#top-terms-per-cluster "Link to this heading")

Since [`TfidfVectorizer`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html#sklearn.feature_extraction.text.TfidfVectorizer "sklearn.feature_extraction.text.TfidfVectorizer")
 can be inverted we can identify the cluster centers, which provide an intuition of the most influential words **for each cluster**. See the example script [Classification of text documents using sparse features](https://scikit-learn.org/stable/auto_examples/text/plot_document_classification_20newsgroups.html#sphx-glr-auto-examples-text-plot-document-classification-20newsgroups-py)
 for a comparison with the most predictive words **for each target class**.

original\_space\_centroids \= lsa\[0\].inverse\_transform(kmeans.cluster\_centers\_)
order\_centroids \= original\_space\_centroids.argsort()\[:, ::\-1\]
terms \= vectorizer.get\_feature\_names\_out()

for i in range(true\_k):
    print(f"Cluster {i}: ", end\="")
    for ind in order\_centroids\[i, :10\]:
        print(f"{terms\[ind\]} ", end\="")
    print()

Copy to clipboard

Cluster 0: thanks graphics image know files file program looking software does
Cluster 1: space launch orbit nasa shuttle earth moon like mission just
Cluster 2: god jesus bible believe christian faith people say does christians
Cluster 3: think don people just say know like time did does

Copy to clipboard

### HashingVectorizer[#](https://scikit-learn.org/stable/auto_examples/text/plot_document_clustering.html#hashingvectorizer "Link to this heading")

An alternative vectorization can be done using a [`HashingVectorizer`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.HashingVectorizer.html#sklearn.feature_extraction.text.HashingVectorizer "sklearn.feature_extraction.text.HashingVectorizer")
 instance, which does not provide IDF weighting as this is a stateless model (the fit method does nothing). When IDF weighting is needed it can be added by pipelining the [`HashingVectorizer`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.HashingVectorizer.html#sklearn.feature_extraction.text.HashingVectorizer "sklearn.feature_extraction.text.HashingVectorizer")
 output to a [`TfidfTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfTransformer.html#sklearn.feature_extraction.text.TfidfTransformer "sklearn.feature_extraction.text.TfidfTransformer")
 instance. In this case we also add LSA to the pipeline to reduce the dimension and sparcity of the hashed vector space.

from sklearn.feature\_extraction.text import [HashingVectorizer](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.HashingVectorizer.html#sklearn.feature_extraction.text.HashingVectorizer "sklearn.feature_extraction.text.HashingVectorizer")
, [TfidfTransformer](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfTransformer.html#sklearn.feature_extraction.text.TfidfTransformer "sklearn.feature_extraction.text.TfidfTransformer")

lsa\_vectorizer \= [make\_pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html#sklearn.pipeline.make_pipeline "sklearn.pipeline.make_pipeline")
(
    [HashingVectorizer](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.HashingVectorizer.html#sklearn.feature_extraction.text.HashingVectorizer "sklearn.feature_extraction.text.HashingVectorizer")
(stop\_words\="english", n\_features\=50\_000),
    [TfidfTransformer](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfTransformer.html#sklearn.feature_extraction.text.TfidfTransformer "sklearn.feature_extraction.text.TfidfTransformer")
(),
    [TruncatedSVD](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.TruncatedSVD.html#sklearn.decomposition.TruncatedSVD "sklearn.decomposition.TruncatedSVD")
(n\_components\=100, random\_state\=0),
    [Normalizer](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.Normalizer.html#sklearn.preprocessing.Normalizer "sklearn.preprocessing.Normalizer")
(copy\=False),
)

t0 \= [time](https://docs.python.org/3/library/time.html#time.time "time.time")
()
X\_hashed\_lsa \= lsa\_vectorizer.fit\_transform(dataset.data)
print(f"vectorization done in {[time](https://docs.python.org/3/library/time.html#time.time "time.time")
() \- t0:.3f} s")

Copy to clipboard

vectorization done in 1.515 s

Copy to clipboard

One can observe that the LSA step takes a relatively long time to fit, especially with hashed vectors. The reason is that a hashed space is typically large (set to `n_features=50_000` in this example). One can try lowering the number of features at the expense of having a larger fraction of features with hash collisions as shown in the example notebook [FeatureHasher and DictVectorizer Comparison](https://scikit-learn.org/stable/auto_examples/text/plot_hashing_vs_dict_vectorizer.html#sphx-glr-auto-examples-text-plot-hashing-vs-dict-vectorizer-py)
.

We now fit and evaluate the `kmeans` and `minibatch_kmeans` instances on this hashed-lsa-reduced data:

fit\_and\_evaluate(kmeans, X\_hashed\_lsa, name\="KMeans\\nwith LSA on hashed vectors")

Copy to clipboard

clustering done in 0.02 ± 0.00 s
Homogeneity: 0.396 ± 0.006
Completeness: 0.442 ± 0.009
V-measure: 0.418 ± 0.007
Adjusted Rand-Index: 0.341 ± 0.030
Silhouette Coefficient: 0.030 ± 0.001

Copy to clipboard

fit\_and\_evaluate(
    minibatch\_kmeans,
    X\_hashed\_lsa,
    name\="MiniBatchKMeans\\nwith LSA on hashed vectors",
)

Copy to clipboard

clustering done in 0.02 ± 0.01 s
Homogeneity: 0.317 ± 0.088
Completeness: 0.336 ± 0.092
V-measure: 0.326 ± 0.089
Adjusted Rand-Index: 0.272 ± 0.104
Silhouette Coefficient: 0.027 ± 0.003

Copy to clipboard

Both methods lead to good results that are similar to running the same models on the traditional LSA vectors (without hashing).

Clustering evaluation summary[#](https://scikit-learn.org/stable/auto_examples/text/plot_document_clustering.html#clustering-evaluation-summary "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------------

import matplotlib.pyplot as plt
import pandas as pd

fig, (ax0, ax1) \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(ncols\=2, figsize\=(16, 6), sharey\=True)

df \= [pd.DataFrame](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
(evaluations\[::\-1\]).set\_index("estimator")
df\_std \= [pd.DataFrame](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
(evaluations\_std\[::\-1\]).set\_index("estimator")

df.drop(
    \["train\_time"\],
    axis\="columns",
).plot.barh(ax\=ax0, xerr\=df\_std)
ax0.set\_xlabel("Clustering scores")
ax0.set\_ylabel("")

df\["train\_time"\].plot.barh(ax\=ax1, xerr\=df\_std\["train\_time"\])
ax1.set\_xlabel("Clustering time (s)")
[plt.tight\_layout](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tight_layout.html#matplotlib.pyplot.tight_layout "matplotlib.pyplot.tight_layout")
()

Copy to clipboard

![plot document clustering](https://scikit-learn.org/stable/_images/sphx_glr_plot_document_clustering_001.png)

[`KMeans`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html#sklearn.cluster.KMeans "sklearn.cluster.KMeans")
 and [`MiniBatchKMeans`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.MiniBatchKMeans.html#sklearn.cluster.MiniBatchKMeans "sklearn.cluster.MiniBatchKMeans")
 suffer from the phenomenon called the [Curse of Dimensionality](https://en.wikipedia.org/wiki/Curse_of_dimensionality)
 for high dimensional datasets such as text data. That is the reason why the overall scores improve when using LSA. Using LSA reduced data also improves the stability and requires lower clustering time, though keep in mind that the LSA step itself takes a long time, especially with hashed vectors.

The Silhouette Coefficient is defined between 0 and 1. In all cases we obtain values close to 0 (even if they improve a bit after using LSA) because its definition requires measuring distances, in contrast with other evaluation metrics such as the V-measure and the Adjusted Rand Index which are only based on cluster assignments rather than distances. Notice that strictly speaking, one should not compare the Silhouette Coefficient between spaces of different dimension, due to the different notions of distance they imply.

The homogeneity, completeness and hence v-measure metrics do not yield a baseline with regards to random labeling: this means that depending on the number of samples, clusters and ground truth classes, a completely random labeling will not always yield the same values. In particular random labeling won’t yield zero scores, especially when the number of clusters is large. This problem can safely be ignored when the number of samples is more than a thousand and the number of clusters is less than 10, which is the case of the present example. For smaller sample sizes or larger number of clusters it is safer to use an adjusted index such as the Adjusted Rand Index (ARI). See the example [Adjustment for chance in clustering performance evaluation](https://scikit-learn.org/stable/auto_examples/cluster/plot_adjusted_for_chance_measures.html#sphx-glr-auto-examples-cluster-plot-adjusted-for-chance-measures-py)
 for a demo on the effect of random labeling.

The size of the error bars show that [`MiniBatchKMeans`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.MiniBatchKMeans.html#sklearn.cluster.MiniBatchKMeans "sklearn.cluster.MiniBatchKMeans")
 is less stable than [`KMeans`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html#sklearn.cluster.KMeans "sklearn.cluster.KMeans")
 for this relatively small dataset. It is more interesting to use when the number of samples is much bigger, but it can come at the expense of a small degradation in clustering quality compared to the traditional k-means algorithm.

**Total running time of the script:** (0 minutes 6.793 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo32.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/text/plot_document_clustering.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo32.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/text/plot_document_clustering.ipynb)

[`Download Jupyter notebook: plot_document_clustering.ipynb`](https://scikit-learn.org/stable/_downloads/751db3d5e6b909ff00972495eaae53df/plot_document_clustering.ipynb)

[`Download Python source code: plot_document_clustering.py`](https://scikit-learn.org/stable/_downloads/ba68199eea858ec04949b2c6c65147e0/plot_document_clustering.py)

[`Download zipped: plot_document_clustering.zip`](https://scikit-learn.org/stable/_downloads/038d1885eb5f5ea53aca42da3031fe38/plot_document_clustering.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_kmeans_digits_thumb.png)

[A demo of K-Means clustering on the handwritten digits data](https://scikit-learn.org/stable/auto_examples/cluster/plot_kmeans_digits.html)

A demo of K-Means clustering on the handwritten digits data

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_mini_batch_kmeans_thumb.png)

[Comparison of the K-Means and MiniBatchKMeans clustering algorithms](https://scikit-learn.org/stable/auto_examples/cluster/plot_mini_batch_kmeans.html)

Comparison of the K-Means and MiniBatchKMeans clustering algorithms

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_bicluster_newsgroups_thumb.png)

[Biclustering documents with the Spectral Co-clustering algorithm](https://scikit-learn.org/stable/auto_examples/bicluster/plot_bicluster_newsgroups.html)

Biclustering documents with the Spectral Co-clustering algorithm

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_document_classification_20newsgroups_thumb.png)

[Classification of text documents using sparse features](https://scikit-learn.org/stable/auto_examples/text/plot_document_classification_20newsgroups.html)

Classification of text documents using sparse features

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page

[Download source code](https://scikit-learn.org/stable/_downloads/ba68199eea858ec04949b2c6c65147e0/plot_document_clustering.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/751db3d5e6b909ff00972495eaae53df/plot_document_clustering.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/038d1885eb5f5ea53aca42da3031fe38/plot_document_clustering.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo32.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/text/plot_document_clustering.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo32.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/text/plot_document_clustering.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)