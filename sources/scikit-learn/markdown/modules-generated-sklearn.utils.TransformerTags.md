[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.utils.TransformerTags.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.utils.TransformerTags.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.utils.TransformerTags.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.utils.TransformerTags.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.utils.TransformerTags.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.utils.TransformerTags.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.utils.TransformerTags.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.utils.TransformerTags.html)

Collapse Sidebar Expand Sidebar

TransformerTags[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.TransformerTags.html#transformertags "Link to this heading")

================================================================================================================================================

class sklearn.utils.TransformerTags(_preserves\_dtype: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")
\[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")\
\] \= <factory>_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_tags.py#L115)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.TransformerTags.html#sklearn.utils.TransformerTags "Link to this definition")

Tags for the transformer.

Parameters:

**preserves\_dtype**list\[str\], default=\[“float64”\]

Applies only on transformers. It corresponds to the data types which will be preserved such that `X_trans.dtype` is the same as `X.dtype` after calling `transformer.transform(X)`. If this list is empty, then the transformer is not expected to preserve the data type. The first value in the list is considered as the default data type, corresponding to the data type of the output when the input data type is not going to be preserved.

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)