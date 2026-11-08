[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_svmlight_files.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.datasets.load_svmlight_files.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_svmlight_files.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.datasets.load_svmlight_files.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.datasets.load_svmlight_files.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.datasets.load_svmlight_files.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.datasets.load_svmlight_files.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.datasets.load_svmlight_files.html)

Collapse Sidebar Expand Sidebar

load\_svmlight\_files[#](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_svmlight_files.html#load-svmlight-files "Link to this heading")

=================================================================================================================================================================

sklearn.datasets.load\_svmlight\_files(_files_, _\*_, _n\_features\=None_, _dtype\=<class 'numpy.float64'>_, _multilabel\=False_, _zero\_based\='auto'_, _query\_id\=False_, _offset\=0_, _length\=\-1_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/datasets/_svmlight_format_io.py#L239)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_svmlight_files.html#sklearn.datasets.load_svmlight_files "Link to this definition")

Load dataset from multiple files in SVMlight format.

This function is equivalent to mapping load\_svmlight\_file over a list of files, except that the results are concatenated into a single, flat list and the samples vectors are constrained to all have the same number of features.

In case the file contains a pairwise preference constraint (known as “qid” in the svmlight format) these are ignored unless the query\_id parameter is set to True. These pairwise preference constraints can be used to constraint the combination of samples when using pairwise loss functions (as is the case in some learning to rank problems) so that only pairs with the same query\_id value are considered.

Parameters:

**files**array-like, dtype=str, path-like, file-like or int

(Paths of) files to load. If a path ends in “.gz” or “.bz2”, it will be uncompressed on the fly. If an integer is passed, it is assumed to be a file descriptor. File-likes and file descriptors will not be closed by this function. File-like objects must be opened in binary mode.

Changed in version 1.2: Path-like objects are now accepted.

**n\_features**int, default=None

The number of features to use. If None, it will be inferred from the maximum column index occurring in any of the files.

This can be set to a higher value than the actual number of features in any of the input files, but setting it to a lower value will cause an exception to be raised.

**dtype**numpy data type, default=np.float64

Data type of dataset to be loaded. This will be the data type of the output numpy arrays `X` and `y`.

**multilabel**bool, default=False

Samples may have several labels each (see [https://www.csie.ntu.edu.tw/~cjlin/libsvmtools/datasets/multilabel.html](https://www.csie.ntu.edu.tw/~cjlin/libsvmtools/datasets/multilabel.html)
).

**zero\_based**bool or “auto”, default=”auto”

Whether column indices in f are zero-based (True) or one-based (False). If column indices are one-based, they are transformed to zero-based to match Python/NumPy conventions. If set to “auto”, a heuristic check is applied to determine this from the file contents. Both kinds of files occur “in the wild”, but they are unfortunately not self-identifying. Using “auto” or True should always be safe when no offset or length is passed. If offset or length are passed, the “auto” mode falls back to zero\_based=True to avoid having the heuristic check yield inconsistent results on different segments of the file.

**query\_id**bool, default=False

If True, will return the query\_id array for each file.

**offset**int, default=0

Ignore the offset first bytes by seeking forward, then discarding the following bytes up until the next new line character.

**length**int, default=-1

If strictly positive, stop reading any new line of data once the position in the file has reached the (offset + length) bytes threshold.

Returns:

\[X1, y1, …, Xn, yn\] or \[X1, y1, q1, …, Xn, yn, qn\]: list of arrays

Each (Xi, yi) pair is the result from load\_svmlight\_file(files\[i\]). If query\_id is set to True, this will return instead (Xi, yi, qi) triplets.

See also

[`load_svmlight_file`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_svmlight_file.html#sklearn.datasets.load_svmlight_file "sklearn.datasets.load_svmlight_file")

Similar function for loading a single file in this format.

Notes

When fitting a model to a matrix X\_train and evaluating it against a matrix X\_test, it is essential that X\_train and X\_test have the same number of features (X\_train.shape\[1\] == X\_test.shape\[1\]). This may not be the case if you load the files individually with load\_svmlight\_file.

Examples

To use joblib.Memory to cache the svmlight file:

from joblib import Memory
from sklearn.datasets import load\_svmlight\_file
mem \= Memory("./mycache")

@mem.cache
def get\_data():
    data\_train, target\_train, data\_test, target\_test \= load\_svmlight\_files(
        \["svmlight\_file\_train", "svmlight\_file\_test"\]
    )
    return data\_train, target\_train, data\_test, target\_test

X\_train, y\_train, X\_test, y\_test \= get\_data()

Copy to clipboard

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)