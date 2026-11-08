[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.utils.multiclass.type_of_target.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.utils.multiclass.type_of_target.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.utils.multiclass.type_of_target.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.utils.multiclass.type_of_target.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.utils.multiclass.type_of_target.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.utils.multiclass.type_of_target.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.utils.multiclass.type_of_target.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.utils.multiclass.type_of_target.html)

Collapse Sidebar Expand Sidebar

type\_of\_target[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.multiclass.type_of_target.html#type-of-target "Link to this heading")

==========================================================================================================================================================

sklearn.utils.multiclass.type\_of\_target(_y_, _input\_name\=''_, _raise\_unknown\=False_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/multiclass.py#L249)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.multiclass.type_of_target.html#sklearn.utils.multiclass.type_of_target "Link to this definition")

Determine the type of data indicated by the target.

Note that this type is the most specific type that can be inferred. For example:

*   `binary` is more specific but compatible with `multiclass`.
    
*   `multiclass` of integers is more specific but compatible with `continuous`.
    
*   `multilabel-indicator` is more specific but compatible with `multiclass-multioutput`.
    

Parameters:

**y**{array-like, sparse matrix}

Target values. If a sparse matrix, `y` is expected to be a CSR/CSC matrix.

**input\_name**str, default=””

The data name used to construct the error message.

Added in version 1.1.0.

**raise\_unknown**bool, default=False

If `True`, raise an error when the type of target returned by [`type_of_target`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.multiclass.type_of_target.html#sklearn.utils.multiclass.type_of_target "sklearn.utils.multiclass.type_of_target")
 is `"unknown"`.

Added in version 1.6.

Returns:

**target\_type**str

One of:

*   ‘continuous’: `y` is an array-like of floats that are not all integers, and is 1d or a column vector.
    
*   ‘continuous-multioutput’: `y` is a 2d array of floats that are not all integers, and both dimensions are of size > 1.
    
*   ‘binary’: `y` contains <= 2 discrete values and is 1d or a column vector.
    
*   ‘multiclass’: `y` contains more than two discrete values, is not a sequence of sequences, and is 1d or a column vector.
    
*   ‘multiclass-multioutput’: `y` is a 2d array that contains more than two discrete values, is not a sequence of sequences, and both dimensions are of size > 1.
    
*   ‘multilabel-indicator’: `y` is a label indicator matrix, an array of two dimensions with at least two columns, and at most 2 unique values.
    
*   ‘unknown’: `y` is array-like but none of the above, such as a 3d array, sequence of sequences, or an array of non-sequence objects.
    

Examples

\>>> from sklearn.utils.multiclass import type\_of\_target
\>>> import numpy as np
\>>> type\_of\_target(\[0.1, 0.6\])
'continuous'
\>>> type\_of\_target(\[1, \-1, \-1, 1\])
'binary'
\>>> type\_of\_target(\['a', 'b', 'a'\])
'binary'
\>>> type\_of\_target(\[1.0, 2.0\])
'binary'
\>>> type\_of\_target(\[1, 0, 2\])
'multiclass'
\>>> type\_of\_target(\[1.0, 0.0, 3.0\])
'multiclass'
\>>> type\_of\_target(\['a', 'b', 'c'\])
'multiclass'
\>>> type\_of\_target(np.array(\[\[1, 2\], \[3, 1\]\]))
'multiclass-multioutput'
\>>> type\_of\_target(\[\[1, 2\]\])
'multilabel-indicator'
\>>> type\_of\_target(np.array(\[\[1.5, 2.0\], \[3.0, 1.6\]\]))
'continuous-multioutput'
\>>> type\_of\_target(np.array(\[\[0, 1\], \[1, 1\]\]))
'multilabel-indicator'

Copy to clipboard

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)