[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_covtype.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.datasets.fetch_covtype.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_covtype.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.datasets.fetch_covtype.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.datasets.fetch_covtype.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.datasets.fetch_covtype.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.datasets.fetch_covtype.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.datasets.fetch_covtype.html)

Collapse Sidebar Expand Sidebar

fetch\_covtype[#](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_covtype.html#fetch-covtype "Link to this heading")

==============================================================================================================================================

sklearn.datasets.fetch\_covtype(_\*_, _data\_home\=None_, _download\_if\_missing\=True_, _random\_state\=None_, _shuffle\=False_, _return\_X\_y\=False_, _as\_frame\=False_, _n\_retries\=3_, _delay\=1.0_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/datasets/_covtype.py#L66)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_covtype.html#sklearn.datasets.fetch_covtype "Link to this definition")

Load the covertype dataset (classification).

Download it if necessary.

|     |     |
| --- | --- |
| Classes | 7   |
| Samples total | 581012 |
| Dimensionality | 54  |
| Features | int |

Read more in the [User Guide](https://scikit-learn.org/stable/datasets/real_world.html#covtype-dataset)
.

Parameters:

**data\_home**str or path-like, default=None

Specify another download and cache folder for the datasets. By default all scikit-learn data is stored in ‘~/scikit\_learn\_data’ subfolders.

**download\_if\_missing**bool, default=True

If False, raise an OSError if the data is not locally available instead of trying to download the data from the source site.

**random\_state**int, RandomState instance or None, default=None

Determines random number generation for dataset shuffling. Pass an int for reproducible output across multiple function calls. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-random_state)
.

**shuffle**bool, default=False

Whether to shuffle dataset.

**return\_X\_y**bool, default=False

If True, returns `(data.data, data.target)` instead of a Bunch object.

Added in version 0.20.

**as\_frame**bool, default=False

If True, the data is a pandas DataFrame including columns with appropriate dtypes (numeric). The target is a pandas DataFrame or Series depending on the number of target columns. If `return_X_y` is True, then (`data`, `target`) will be pandas DataFrames or Series as described below.

Added in version 0.24.

**n\_retries**int, default=3

Number of retries when HTTP errors are encountered.

Added in version 1.5.

**delay**float, default=1.0

Number of seconds between retries.

Added in version 1.5.

Returns:

**dataset**[`Bunch`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.Bunch.html#sklearn.utils.Bunch "sklearn.utils.Bunch")

Dictionary-like object, with the following attributes.

datandarray of shape (581012, 54)

Each row corresponds to the 54 features in the dataset.

targetndarray of shape (581012,)

Each value corresponds to one of the 7 forest covertypes with values ranging between 1 to 7.

framedataframe of shape (581012, 55)

Only present when `as_frame=True`. Contains `data` and `target`.

DESCRstr

Description of the forest covertype dataset.

feature\_nameslist

The names of the dataset columns.

target\_names: list

The names of the target columns.

**(data, target)**tuple if `return_X_y` is True

A tuple of two ndarray. The first containing a 2D array of shape (n\_samples, n\_features) with each row representing one sample and each column representing the features. The second ndarray of shape (n\_samples,) containing the target samples.

Added in version 0.20.

Examples

\>>> from sklearn.datasets import fetch\_covtype
\>>> cov\_type \= fetch\_covtype()
\>>> cov\_type.data.shape
(581012, 54)
\>>> cov\_type.target.shape
(581012,)
\>>> \# Let's check the 4 first feature names
\>>> cov\_type.feature\_names\[:4\]
\['Elevation', 'Aspect', 'Slope', 'Horizontal\_Distance\_To\_Hydrology'\]

Copy to clipboard

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_covtype.html#gallery-examples "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_scalable_poly_kernels_thumb.png)

[Scalable learning with polynomial kernel approximation](https://scikit-learn.org/stable/auto_examples/kernel_approximation/plot_scalable_poly_kernels.html)

Scalable learning with polynomial kernel approximation

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_outlier_detection_bench_thumb.png)

[Evaluation of outlier detection estimators](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_outlier_detection_bench.html)

Evaluation of outlier detection estimators

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_0_24_0_thumb.png)

[Release Highlights for scikit-learn 0.24](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_0_24_0.html)

Release Highlights for scikit-learn 0.24

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)