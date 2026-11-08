[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.utils.InputTags.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.utils.InputTags.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.utils.InputTags.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.utils.InputTags.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.utils.InputTags.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.utils.InputTags.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.utils.InputTags.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.utils.InputTags.html)

Collapse Sidebar Expand Sidebar

InputTags[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.InputTags.html#inputtags "Link to this heading")

==============================================================================================================================

class sklearn.utils.InputTags(_one\_d\_array: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")
 \= False_, _two\_d\_array: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")
 \= True_, _three\_d\_array: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")
 \= False_, _sparse: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")
 \= False_, _categorical: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")
 \= False_, _string: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")
 \= False_, _dict: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")
 \= False_, _positive\_only: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")
 \= False_, _allow\_nan: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")
 \= False_, _pairwise: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")
 \= False_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_tags.py#L9)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.InputTags.html#sklearn.utils.InputTags "Link to this definition")

Tags for the input data.

Parameters:

**one\_d\_array**bool, default=False

Whether the input can be a 1D array.

**two\_d\_array**bool, default=True

Whether the input can be a 2D array. Note that most common tests currently run only if this flag is set to `True`.

**three\_d\_array**bool, default=False

Whether the input can be a 3D array.

**sparse**bool, default=False

Whether the input can be a sparse matrix.

**categorical**bool, default=False

Whether the input can be categorical.

**string**bool, default=False

Whether the input can be an array-like of strings.

**dict**bool, default=False

Whether the input can be a dictionary.

**positive\_only**bool, default=False

Whether the estimator requires positive X.

**allow\_nan**bool, default=False

Whether the estimator supports data with missing values encoded as `np.nan`.

**pairwise**bool, default=False

This boolean attribute indicates whether the data (`X`), [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
 and similar methods consists of pairwise measures over samples rather than a feature representation for each sample. It is usually `True` where an estimator has a `metric` or `affinity` or `kernel` parameter with value ‘precomputed’. Its primary purpose is to support a [meta-estimator](https://scikit-learn.org/stable/glossary.html#term-meta-estimator)
 or a cross validation procedure that extracts a sub-sample of data intended for a pairwise estimator, where the data needs to be indexed on both axes. Specifically, this tag is used by `sklearn.utils.metaestimators._safe_split` to slice rows and columns.

Note that if setting this tag to `True` means the estimator can take only positive values, the `positive_only` tag must reflect it and also be set to `True`.

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)