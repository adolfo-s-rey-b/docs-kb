[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_rcv1.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.datasets.fetch_rcv1.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_rcv1.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.datasets.fetch_rcv1.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.datasets.fetch_rcv1.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.datasets.fetch_rcv1.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.datasets.fetch_rcv1.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.datasets.fetch_rcv1.html)

Collapse Sidebar Expand Sidebar

fetch\_rcv1[#](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_rcv1.html#fetch-rcv1 "Link to this heading")

=====================================================================================================================================

sklearn.datasets.fetch\_rcv1(_\*_, _data\_home\=None_, _subset\='all'_, _download\_if\_missing\=True_, _random\_state\=None_, _shuffle\=False_, _return\_X\_y\=False_, _n\_retries\=3_, _delay\=1.0_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/datasets/_rcv1.py#L82)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_rcv1.html#sklearn.datasets.fetch_rcv1 "Link to this definition")

Load the RCV1 multilabel dataset (classification).

Download it if necessary.

Version: RCV1-v2, vectors, full sets, topics multilabels.

|     |     |
| --- | --- |
| Classes | 103 |
| Samples total | 804414 |
| Dimensionality | 47236 |
| Features | real, between 0 and 1 |

Read more in the [User Guide](https://scikit-learn.org/stable/datasets/real_world.html#rcv1-dataset)
.

Added in version 0.17.

Parameters:

**data\_home**str or path-like, default=None

Specify another download and cache folder for the datasets. By default all scikit-learn data is stored in ‘~/scikit\_learn\_data’ subfolders.

**subset**{‘train’, ‘test’, ‘all’}, default=’all’

Select the dataset to load: ‘train’ for the training set (23149 samples), ‘test’ for the test set (781265 samples), ‘all’ for both, with the training samples first if shuffle is False. This follows the official LYRL2004 chronological split.

**download\_if\_missing**bool, default=True

If False, raise an OSError if the data is not locally available instead of trying to download the data from the source site.

**random\_state**int, RandomState instance or None, default=None

Determines random number generation for dataset shuffling. Pass an int for reproducible output across multiple function calls. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-random_state)
.

**shuffle**bool, default=False

Whether to shuffle dataset.

**return\_X\_y**bool, default=False

If True, returns `(dataset.data, dataset.target)` instead of a Bunch object. See below for more information about the `dataset.data` and `dataset.target` object.

Added in version 0.20.

**n\_retries**int, default=3

Number of retries when HTTP errors are encountered.

Added in version 1.5.

**delay**float, default=1.0

Number of seconds between retries.

Added in version 1.5.

Returns:

**dataset**[`Bunch`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.Bunch.html#sklearn.utils.Bunch "sklearn.utils.Bunch")

Dictionary-like object. Returned only if `return_X_y` is False. `dataset` has the following attributes:

*   datasparse matrix of shape (804414, 47236), dtype=np.float64
    
    The array has 0.16% of non zero values. Will be of CSR format.
    
*   targetsparse matrix of shape (804414, 103), dtype=np.uint8
    
    Each sample has a value of 1 in its categories, and 0 in others. The array has 3.15% of non zero values. Will be of CSR format.
    
*   sample\_idndarray of shape (804414,), dtype=np.uint32,
    
    Identification number of each sample, as ordered in dataset.data.
    
*   target\_namesndarray of shape (103,), dtype=object
    
    Names of each target (RCV1 topics), as ordered in dataset.target.
    
*   DESCRstr
    
    Description of the RCV1 dataset.
    

**(data, target)**tuple

A tuple consisting of `dataset.data` and `dataset.target`, as described above. Returned only if `return_X_y` is True.

Added in version 0.20.

Examples

\>>> from sklearn.datasets import fetch\_rcv1
\>>> rcv1 \= fetch\_rcv1()
\>>> rcv1.data.shape
(804414, 47236)
\>>> rcv1.target.shape
(804414, 103)

Copy to clipboard

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)