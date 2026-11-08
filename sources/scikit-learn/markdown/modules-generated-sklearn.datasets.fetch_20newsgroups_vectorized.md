[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_20newsgroups_vectorized.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.datasets.fetch_20newsgroups_vectorized.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_20newsgroups_vectorized.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.datasets.fetch_20newsgroups_vectorized.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.datasets.fetch_20newsgroups_vectorized.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.datasets.fetch_20newsgroups_vectorized.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.datasets.fetch_20newsgroups_vectorized.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.datasets.fetch_20newsgroups_vectorized.html)

Collapse Sidebar Expand Sidebar

fetch\_20newsgroups\_vectorized[#](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_20newsgroups_vectorized.html#fetch-20newsgroups-vectorized "Link to this heading")

===============================================================================================================================================================================================

sklearn.datasets.fetch\_20newsgroups\_vectorized(_\*_, _subset\='train'_, _remove\=()_, _data\_home\=None_, _download\_if\_missing\=True_, _return\_X\_y\=False_, _normalize\=True_, _as\_frame\=False_, _n\_retries\=3_, _delay\=1.0_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/datasets/_twenty_newsgroups.py#L389)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_20newsgroups_vectorized.html#sklearn.datasets.fetch_20newsgroups_vectorized "Link to this definition")

Load and vectorize the 20 newsgroups dataset (classification).

Download it if necessary.

This is a convenience function; the transformation is done using the default settings for [`CountVectorizer`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html#sklearn.feature_extraction.text.CountVectorizer "sklearn.feature_extraction.text.CountVectorizer")
. For more advanced usage (stopword filtering, n-gram extraction, etc.), combine fetch\_20newsgroups with a custom [`CountVectorizer`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html#sklearn.feature_extraction.text.CountVectorizer "sklearn.feature_extraction.text.CountVectorizer")
, [`HashingVectorizer`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.HashingVectorizer.html#sklearn.feature_extraction.text.HashingVectorizer "sklearn.feature_extraction.text.HashingVectorizer")
, [`TfidfTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfTransformer.html#sklearn.feature_extraction.text.TfidfTransformer "sklearn.feature_extraction.text.TfidfTransformer")
 or [`TfidfVectorizer`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html#sklearn.feature_extraction.text.TfidfVectorizer "sklearn.feature_extraction.text.TfidfVectorizer")
.

The resulting counts are normalized using [`sklearn.preprocessing.normalize`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.normalize.html#sklearn.preprocessing.normalize "sklearn.preprocessing.normalize")
 unless normalize is set to False.

|     |     |
| --- | --- |
| Classes | 20  |
| Samples total | 18846 |
| Dimensionality | 130107 |
| Features | real |

Read more in the [User Guide](https://scikit-learn.org/stable/datasets/real_world.html#newsgroups-dataset)
.

Parameters:

**subset**{‘train’, ‘test’, ‘all’}, default=’train’

Select the dataset to load: ‘train’ for the training set, ‘test’ for the test set, ‘all’ for both, with shuffled ordering.

**remove**tuple, default=()

May contain any subset of (‘headers’, ‘footers’, ‘quotes’). Each of these are kinds of text that will be detected and removed from the newsgroup posts, preventing classifiers from overfitting on metadata.

‘headers’ removes newsgroup headers, ‘footers’ removes blocks at the ends of posts that look like signatures, and ‘quotes’ removes lines that appear to be quoting another post.

**data\_home**str or path-like, default=None

Specify a download and cache folder for the datasets. If None, all scikit-learn data is stored in ‘~/scikit\_learn\_data’ subfolders.

**download\_if\_missing**bool, default=True

If False, raise an OSError if the data is not locally available instead of trying to download the data from the source site.

**return\_X\_y**bool, default=False

If True, returns `(data.data, data.target)` instead of a Bunch object.

Added in version 0.20.

**normalize**bool, default=True

If True, normalizes each document’s feature vector to unit norm using [`sklearn.preprocessing.normalize`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.normalize.html#sklearn.preprocessing.normalize "sklearn.preprocessing.normalize")
.

Added in version 0.22.

**as\_frame**bool, default=False

If True, the data is a pandas DataFrame including columns with appropriate dtypes (numeric, string, or categorical). The target is a pandas DataFrame or Series depending on the number of `target_columns`.

Added in version 0.24.

**n\_retries**int, default=3

Number of retries when HTTP errors are encountered.

Added in version 1.5.

**delay**float, default=1.0

Number of seconds between retries.

Added in version 1.5.

Returns:

**bunch**[`Bunch`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.Bunch.html#sklearn.utils.Bunch "sklearn.utils.Bunch")

Dictionary-like object, with the following attributes.

data: {sparse matrix, dataframe} of shape (n\_samples, n\_features)

The input data matrix. If `as_frame` is `True`, `data` is a pandas DataFrame with sparse columns.

target: {ndarray, series} of shape (n\_samples,)

The target labels. If `as_frame` is `True`, `target` is a pandas Series.

target\_names: list of shape (n\_classes,)

The names of target classes.

DESCR: str

The full description of the dataset.

frame: dataframe of shape (n\_samples, n\_features + 1)

Only present when `as_frame=True`. Pandas DataFrame with `data` and `target`.

Added in version 0.24.

**(data, target)**tuple if `return_X_y` is True

`data` and `target` would be of the format defined in the `Bunch` description above.

Added in version 0.20.

Examples

\>>> from sklearn.datasets import fetch\_20newsgroups\_vectorized
\>>> newsgroups\_vectorized \= fetch\_20newsgroups\_vectorized(subset\='test')
\>>> newsgroups\_vectorized.data.shape
(7532, 130107)
\>>> newsgroups\_vectorized.target.shape
(7532,)

Copy to clipboard

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_20newsgroups_vectorized.html#gallery-examples "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_model_complexity_influence_thumb.png)

[Model Complexity Influence](https://scikit-learn.org/stable/auto_examples/applications/plot_model_complexity_influence.html)

Model Complexity Influence

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_sparse_logistic_regression_20newsgroups_thumb.png)

[Multiclass sparse logistic regression on 20newgroups](https://scikit-learn.org/stable/auto_examples/linear_model/plot_sparse_logistic_regression_20newsgroups.html)

Multiclass sparse logistic regression on 20newgroups

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_johnson_lindenstrauss_bound_thumb.png)

[The Johnson-Lindenstrauss bound for embedding with random projections](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_johnson_lindenstrauss_bound.html)

The Johnson-Lindenstrauss bound for embedding with random projections

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)