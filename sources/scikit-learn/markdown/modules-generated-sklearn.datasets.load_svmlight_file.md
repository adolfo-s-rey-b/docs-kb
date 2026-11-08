[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_svmlight_file.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.datasets.load_svmlight_file.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_svmlight_file.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.datasets.load_svmlight_file.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.datasets.load_svmlight_file.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.datasets.load_svmlight_file.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.datasets.load_svmlight_file.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.datasets.load_svmlight_file.html)

Collapse Sidebar Expand Sidebar

load\_svmlight\_file[#](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_svmlight_file.html#load-svmlight-file "Link to this heading")

==============================================================================================================================================================

sklearn.datasets.load\_svmlight\_file(_f_, _\*_, _n\_features\=None_, _dtype\=<class 'numpy.float64'>_, _multilabel\=False_, _zero\_based\='auto'_, _query\_id\=False_, _offset\=0_, _length\=\-1_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/datasets/_svmlight_format_io.py#L38)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_svmlight_file.html#sklearn.datasets.load_svmlight_file "Link to this definition")

Load datasets in the svmlight / libsvm format into sparse CSR matrix.

This format is a text-based format, with one sample per line. It does not store zero valued features hence is suitable for sparse dataset.

The first element of each line can be used to store a target variable to predict.

This format is used as the default format for both svmlight and the libsvm command line programs.

Parsing a text based source can be expensive. When repeatedly working on the same dataset, it is recommended to wrap this loader with joblib.Memory.cache to store a memmapped backup of the CSR results of the first call and benefit from the near instantaneous loading of memmapped structures for the subsequent calls.

In case the file contains a pairwise preference constraint (known as “qid” in the svmlight format) these are ignored unless the query\_id parameter is set to True. These pairwise preference constraints can be used to constraint the combination of samples when using pairwise loss functions (as is the case in some learning to rank problems) so that only pairs with the same query\_id value are considered.

This implementation is written in Cython and is reasonably fast. However, a faster API-compatible loader is also available at: [mblondel/svmlight-loader](https://github.com/mblondel/svmlight-loader)

Parameters:

**f**str, path-like, file-like or int

(Path to) a file to load. If a path ends in “.gz” or “.bz2”, it will be uncompressed on the fly. If an integer is passed, it is assumed to be a file descriptor. A file-like or file descriptor will not be closed by this function. A file-like object must be opened in binary mode.

Changed in version 1.2: Path-like objects are now accepted.

**n\_features**int, default=None

The number of features to use. If None, it will be inferred. This argument is useful to load several files that are subsets of a bigger sliced dataset: each subset might not have examples of every feature, hence the inferred shape might vary from one slice to another. n\_features is only required if `offset` or `length` are passed a non-default value.

**dtype**numpy data type, default=np.float64

Data type of dataset to be loaded. This will be the data type of the output numpy arrays `X` and `y`.

**multilabel**bool, default=False

Samples may have several labels each (see [https://www.csie.ntu.edu.tw/~cjlin/libsvmtools/datasets/multilabel.html](https://www.csie.ntu.edu.tw/~cjlin/libsvmtools/datasets/multilabel.html)
).

**zero\_based**bool or “auto”, default=”auto”

Whether column indices in f are zero-based (True) or one-based (False). If column indices are one-based, they are transformed to zero-based to match Python/NumPy conventions. If set to “auto”, a heuristic check is applied to determine this from the file contents. Both kinds of files occur “in the wild”, but they are unfortunately not self-identifying. Using “auto” or True should always be safe when no `offset` or `length` is passed. If `offset` or `length` are passed, the “auto” mode falls back to `zero_based=True` to avoid having the heuristic check yield inconsistent results on different segments of the file.

**query\_id**bool, default=False

If True, will return the query\_id array for each file.

**offset**int, default=0

Ignore the offset first bytes by seeking forward, then discarding the following bytes up until the next new line character.

**length**int, default=-1

If strictly positive, stop reading any new line of data once the position in the file has reached the (offset + length) bytes threshold.

Returns:

**X**scipy.sparse matrix of shape (n\_samples, n\_features)

The data matrix.

**y**ndarray of shape (n\_samples,), or a list of tuples of length n\_samples

The target. It is a list of tuples when `multilabel=True`, else a ndarray.

**query\_id**array of shape (n\_samples,)

The query\_id for each sample. Only returned when query\_id is set to True.

See also

[`load_svmlight_files`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_svmlight_files.html#sklearn.datasets.load_svmlight_files "sklearn.datasets.load_svmlight_files")

Similar function for loading multiple files in this format, enforcing the same number of features/columns on all of them.

Examples

To use joblib.Memory to cache the svmlight file:

from joblib import Memory
from sklearn.datasets import load\_svmlight\_file
mem \= Memory("./mycache")

@mem.cache
def get\_data():
    data \= load\_svmlight\_file("mysvmlightfile")
    return data\[0\], data\[1\]

X, y \= get\_data()

Copy to clipboard

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)