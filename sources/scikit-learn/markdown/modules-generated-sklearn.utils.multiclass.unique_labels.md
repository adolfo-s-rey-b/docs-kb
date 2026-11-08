[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.utils.multiclass.unique_labels.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.utils.multiclass.unique_labels.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.utils.multiclass.unique_labels.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.utils.multiclass.unique_labels.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.utils.multiclass.unique_labels.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.utils.multiclass.unique_labels.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.utils.multiclass.unique_labels.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.utils.multiclass.unique_labels.html)

Collapse Sidebar Expand Sidebar

unique\_labels[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.multiclass.unique_labels.html#unique-labels "Link to this heading")

======================================================================================================================================================

sklearn.utils.multiclass.unique\_labels(_\*ys_, _ys\_types\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/multiclass.py#L41)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.multiclass.unique_labels.html#sklearn.utils.multiclass.unique_labels "Link to this definition")

Extract an ordered array of unique labels.

We don’t allow:

*   mix of multilabel and multiclass (single label) targets
    
*   mix of label indicator matrix and anything else (because there are no explicit labels)
    
*   mix of label indicator matrices of different sizes
    
*   mix of string and integer labels
    

At the moment, we also don’t allow “multiclass-multioutput” input type.

Parameters:

**\*ys**array-likes

Label values.

**ys\_types**set, default=None

Set of target types of `ys` (as determined by `type_of_target`), with `{"binary", "multiclass"}` being amended to `{"multiclass"}`.

Returns:

**out**ndarray of shape (n\_unique\_labels,)

An ordered array of unique labels.

Examples

\>>> from sklearn.utils.multiclass import unique\_labels
\>>> unique\_labels(\[3, 5, 5, 5, 7, 7\])
array(\[3, 5, 7\])
\>>> unique\_labels(\[1, 2, 3, 4\], \[2, 2, 3, 4\])
array(\[1, 2, 3, 4\])
\>>> unique\_labels(\[1, 2, 10\], \[5, 11\])
array(\[ 1,  2,  5, 10, 11\])

Copy to clipboard

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)