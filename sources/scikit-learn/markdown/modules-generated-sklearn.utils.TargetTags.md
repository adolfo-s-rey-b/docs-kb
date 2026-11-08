[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.utils.TargetTags.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.utils.TargetTags.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.utils.TargetTags.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.utils.TargetTags.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.utils.TargetTags.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.utils.TargetTags.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.utils.TargetTags.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.utils.TargetTags.html)

Collapse Sidebar Expand Sidebar

TargetTags[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.TargetTags.html#targettags "Link to this heading")

=================================================================================================================================

class sklearn.utils.TargetTags(_required: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")
_, _one\_d\_labels: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")
 \= False_, _two\_d\_labels: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")
 \= False_, _positive\_only: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")
 \= False_, _multi\_output: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")
 \= False_, _single\_output: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")
 \= True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_tags.py#L74)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.TargetTags.html#sklearn.utils.TargetTags "Link to this definition")

Tags for the target data.

Parameters:

**required**bool

Whether the estimator requires y to be passed to `fit`, `fit_predict` or `fit_transform` methods. The tag is `True` for estimators inheriting from `~sklearn.base.RegressorMixin` and `~sklearn.base.ClassifierMixin`.

**one\_d\_labels**bool, default=False

Whether the input is a 1D labels (y).

**two\_d\_labels**bool, default=False

Whether the input is a 2D labels (y).

**positive\_only**bool, default=False

Whether the estimator requires a positive y (only applicable for regression).

**multi\_output**bool, default=False

Whether a regressor supports multi-target outputs or a classifier supports multi-class multi-output.

See [multi-output](https://scikit-learn.org/stable/glossary.html#term-multi-output)
 in the glossary.

**single\_output**bool, default=True

Whether the target can be single-output. This can be `False` if the estimator supports only multi-output cases.

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)