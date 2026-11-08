[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_kddcup99.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.datasets.fetch_kddcup99.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_kddcup99.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.datasets.fetch_kddcup99.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.datasets.fetch_kddcup99.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.datasets.fetch_kddcup99.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.datasets.fetch_kddcup99.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.datasets.fetch_kddcup99.html)

Collapse Sidebar Expand Sidebar

fetch\_kddcup99[#](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_kddcup99.html#fetch-kddcup99 "Link to this heading")

=================================================================================================================================================

sklearn.datasets.fetch\_kddcup99(_\*_, _subset\=None_, _data\_home\=None_, _shuffle\=False_, _random\_state\=None_, _percent10\=True_, _download\_if\_missing\=True_, _return\_X\_y\=False_, _as\_frame\=False_, _n\_retries\=3_, _delay\=1.0_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/datasets/_kddcup99.py#L54)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_kddcup99.html#sklearn.datasets.fetch_kddcup99 "Link to this definition")

Load the kddcup99 dataset (classification).

Download it if necessary.

|     |     |
| --- | --- |
| Classes | 23  |
| Samples total | 4898431 |
| Dimensionality | 41  |
| Features | discrete (int) or continuous (float) |

Read more in the [User Guide](https://scikit-learn.org/stable/datasets/real_world.html#kddcup99-dataset)
.

Added in version 0.18.

Parameters:

**subset**{‘SA’, ‘SF’, ‘http’, ‘smtp’}, default=None

To return the corresponding classical subsets of kddcup 99. If None, return the entire kddcup 99 dataset.

**data\_home**str or path-like, default=None

Specify another download and cache folder for the datasets. By default all scikit-learn data is stored in ‘~/scikit\_learn\_data’ subfolders.

Added in version 0.19.

**shuffle**bool, default=False

Whether to shuffle dataset.

**random\_state**int, RandomState instance or None, default=None

Determines random number generation for dataset shuffling and for selection of abnormal samples if `subset='SA'`. Pass an int for reproducible output across multiple function calls. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-random_state)
.

**percent10**bool, default=True

Whether to load only 10 percent of the data.

**download\_if\_missing**bool, default=True

If False, raise an OSError if the data is not locally available instead of trying to download the data from the source site.

**return\_X\_y**bool, default=False

If True, returns `(data, target)` instead of a Bunch object. See below for more information about the `data` and `target` objects.

Added in version 0.20.

**as\_frame**bool, default=False

If `True`, returns a pandas Dataframe for the `data` and `target` objects in the `Bunch` returned object; `Bunch` return object will also have a `frame` member.

Added in version 0.24.

**n\_retries**int, default=3

Number of retries when HTTP errors are encountered.

Added in version 1.5.

**delay**float, default=1.0

Number of seconds between retries.

Added in version 1.5.

Returns:

**data**[`Bunch`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.Bunch.html#sklearn.utils.Bunch "sklearn.utils.Bunch")

Dictionary-like object, with the following attributes.

data{ndarray, dataframe} of shape (494021, 41)

The data matrix to learn. If `as_frame=True`, `data` will be a pandas DataFrame.

target{ndarray, series} of shape (494021,)

The regression target for each sample. If `as_frame=True`, `target` will be a pandas Series.

framedataframe of shape (494021, 42)

Only present when `as_frame=True`. Contains `data` and `target`.

DESCRstr

The full description of the dataset.

feature\_nameslist

The names of the dataset columns

target\_names: list

The names of the target columns

**(data, target)**tuple if `return_X_y` is True

A tuple of two ndarray. The first containing a 2D array of shape (n\_samples, n\_features) with each row representing one sample and each column representing the features. The second ndarray of shape (n\_samples,) containing the target samples.

Added in version 0.20.

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_kddcup99.html#gallery-examples "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_outlier_detection_bench_thumb.png)

[Evaluation of outlier detection estimators](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_outlier_detection_bench.html)

Evaluation of outlier detection estimators

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)