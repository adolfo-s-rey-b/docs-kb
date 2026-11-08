[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.dump_svmlight_file.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.datasets.dump_svmlight_file.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.dump_svmlight_file.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.datasets.dump_svmlight_file.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.datasets.dump_svmlight_file.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.datasets.dump_svmlight_file.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.datasets.dump_svmlight_file.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.datasets.dump_svmlight_file.html)

Collapse Sidebar Expand Sidebar

dump\_svmlight\_file[#](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.dump_svmlight_file.html#dump-svmlight-file "Link to this heading")

==============================================================================================================================================================

sklearn.datasets.dump\_svmlight\_file(_X_, _y_, _f_, _\*_, _zero\_based\=True_, _comment\=None_, _query\_id\=None_, _multilabel\=False_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/datasets/_svmlight_format_io.py#L451)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.dump_svmlight_file.html#sklearn.datasets.dump_svmlight_file "Link to this definition")

Dump the dataset in svmlight / libsvm file format.

This format is a text-based format, with one sample per line. It does not store zero valued features hence is suitable for sparse dataset.

The first element of each line can be used to store a target variable to predict.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)

Training vectors, where `n_samples` is the number of samples and `n_features` is the number of features.

**y**{array-like, sparse matrix}, shape = (n\_samples,) or (n\_samples, n\_labels)

Target values. Class labels must be an integer or float, or array-like objects of integer or float for multilabel classifications.

**f**str or file-like in binary mode

If string, specifies the path that will contain the data. If file-like, data will be written to f. f should be opened in binary mode.

**zero\_based**bool, default=True

Whether column indices should be written zero-based (True) or one-based (False).

**comment**str or bytes, default=None

Comment to insert at the top of the file. This should be either a Unicode string, which will be encoded as UTF-8, or an ASCII byte string. If a comment is given, then it will be preceded by one that identifies the file as having been dumped by scikit-learn. Note that not all tools grok comments in SVMlight files.

**query\_id**array-like of shape (n\_samples,), default=None

Array containing pairwise preference constraints (qid in svmlight format).

**multilabel**bool, default=False

Samples may have several labels each (see [https://www.csie.ntu.edu.tw/~cjlin/libsvmtools/datasets/multilabel.html](https://www.csie.ntu.edu.tw/~cjlin/libsvmtools/datasets/multilabel.html)
).

Added in version 0.17: parameter `multilabel` to support multilabel datasets.

Examples

\>>> from sklearn.datasets import dump\_svmlight\_file, make\_classification
\>>> X, y \= make\_classification(random\_state\=0)
\>>> output\_file \= "my\_dataset.svmlight"
\>>> dump\_svmlight\_file(X, y, output\_file)

Copy to clipboard

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)