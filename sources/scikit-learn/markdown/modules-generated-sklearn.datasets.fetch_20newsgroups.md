[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_20newsgroups.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.datasets.fetch_20newsgroups.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_20newsgroups.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.datasets.fetch_20newsgroups.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.datasets.fetch_20newsgroups.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.datasets.fetch_20newsgroups.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.datasets.fetch_20newsgroups.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.datasets.fetch_20newsgroups.html)

Collapse Sidebar Expand Sidebar

fetch\_20newsgroups[#](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_20newsgroups.html#fetch-20newsgroups "Link to this heading")

=============================================================================================================================================================

sklearn.datasets.fetch\_20newsgroups(_\*_, _data\_home\=None_, _subset\='train'_, _categories\=None_, _shuffle\=True_, _random\_state\=42_, _remove\=()_, _download\_if\_missing\=True_, _return\_X\_y\=False_, _n\_retries\=3_, _delay\=1.0_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/datasets/_twenty_newsgroups.py#L162)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_20newsgroups.html#sklearn.datasets.fetch_20newsgroups "Link to this definition")

Load the filenames and data from the 20 newsgroups dataset (classification).

Download it if necessary.

|     |     |
| --- | --- |
| Classes | 20  |
| Samples total | 18846 |
| Dimensionality | 1   |
| Features | text |

Read more in the [User Guide](https://scikit-learn.org/stable/datasets/real_world.html#newsgroups-dataset)
.

Parameters:

**data\_home**str or path-like, default=None

Specify a download and cache folder for the datasets. If None, all scikit-learn data is stored in ‘~/scikit\_learn\_data’ subfolders.

**subset**{‘train’, ‘test’, ‘all’}, default=’train’

Select the dataset to load: ‘train’ for the training set, ‘test’ for the test set, ‘all’ for both, with shuffled ordering.

**categories**array-like, dtype=str, default=None

If None (default), load all the categories. If not None, list of category names to load (other categories ignored).

**shuffle**bool, default=True

Whether or not to shuffle the data: might be important for models that make the assumption that the samples are independent and identically distributed (i.i.d.), such as stochastic gradient descent.

**random\_state**int, RandomState instance or None, default=42

Determines random number generation for dataset shuffling. Pass an int for reproducible output across multiple function calls. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-random_state)
.

**remove**tuple, default=()

May contain any subset of (‘headers’, ‘footers’, ‘quotes’). Each of these are kinds of text that will be detected and removed from the newsgroup posts, preventing classifiers from overfitting on metadata.

‘headers’ removes newsgroup headers, ‘footers’ removes blocks at the ends of posts that look like signatures, and ‘quotes’ removes lines that appear to be quoting another post.

‘headers’ follows an exact standard; the other filters are not always correct.

**download\_if\_missing**bool, default=True

If False, raise an OSError if the data is not locally available instead of trying to download the data from the source site.

**return\_X\_y**bool, default=False

If True, returns `(data.data, data.target)` instead of a Bunch object.

Added in version 0.22.

**n\_retries**int, default=3

Number of retries when HTTP errors are encountered.

Added in version 1.5.

**delay**float, default=1.0

Number of seconds between retries.

Added in version 1.5.

Returns:

**bunch**[`Bunch`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.Bunch.html#sklearn.utils.Bunch "sklearn.utils.Bunch")

Dictionary-like object, with the following attributes.

datalist of shape (n\_samples,)

The data list to learn.

target: ndarray of shape (n\_samples,)

The target labels.

filenames: list of shape (n\_samples,)

The path to the location of the data.

DESCR: str

The full description of the dataset.

target\_names: list of shape (n\_classes,)

The names of target classes.

**(data, target)**tuple if `return_X_y=True`

A tuple of two ndarrays. The first contains a 2D array of shape (n\_samples, n\_classes) with each row representing one sample and each column representing the features. The second array of shape (n\_samples,) contains the target samples.

Added in version 0.22.

Examples

\>>> from sklearn.datasets import fetch\_20newsgroups
\>>> cats \= \['alt.atheism', 'sci.space'\]
\>>> newsgroups\_train \= fetch\_20newsgroups(subset\='train', categories\=cats)
\>>> list(newsgroups\_train.target\_names)
\['alt.atheism', 'sci.space'\]
\>>> newsgroups\_train.filenames.shape
(1073,)
\>>> newsgroups\_train.target.shape
(1073,)
\>>> newsgroups\_train.target\[:10\]
array(\[0, 1, 1, 1, 0, 1, 1, 0, 0, 0\])

Copy to clipboard

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_20newsgroups.html#gallery-examples "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_topics_extraction_with_nmf_lda_thumb.png)

[Topic extraction with Non-negative Matrix Factorization and Latent Dirichlet Allocation](https://scikit-learn.org/stable/auto_examples/applications/plot_topics_extraction_with_nmf_lda.html)

Topic extraction with Non-negative Matrix Factorization and Latent Dirichlet Allocation

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_bicluster_newsgroups_thumb.png)

[Biclustering documents with the Spectral Co-clustering algorithm](https://scikit-learn.org/stable/auto_examples/bicluster/plot_bicluster_newsgroups.html)

Biclustering documents with the Spectral Co-clustering algorithm

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_column_transformer_thumb.png)

[Column Transformer with Heterogeneous Data Sources](https://scikit-learn.org/stable/auto_examples/compose/plot_column_transformer.html)

Column Transformer with Heterogeneous Data Sources

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_grid_search_text_feature_extraction_thumb.png)

[Sample pipeline for text feature extraction and evaluation](https://scikit-learn.org/stable/auto_examples/model_selection/plot_grid_search_text_feature_extraction.html)

Sample pipeline for text feature extraction and evaluation

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_semi_supervised_newsgroups_thumb.png)

[Semi-supervised Classification on a Text Dataset](https://scikit-learn.org/stable/auto_examples/semi_supervised/plot_semi_supervised_newsgroups.html)

Semi-supervised Classification on a Text Dataset

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_document_classification_20newsgroups_thumb.png)

[Classification of text documents using sparse features](https://scikit-learn.org/stable/auto_examples/text/plot_document_classification_20newsgroups.html)

Classification of text documents using sparse features

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_document_clustering_thumb.png)

[Clustering text documents using k-means](https://scikit-learn.org/stable/auto_examples/text/plot_document_clustering.html)

Clustering text documents using k-means

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_hashing_vs_dict_vectorizer_thumb.png)

[FeatureHasher and DictVectorizer Comparison](https://scikit-learn.org/stable/auto_examples/text/plot_hashing_vs_dict_vectorizer.html)

FeatureHasher and DictVectorizer Comparison

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)