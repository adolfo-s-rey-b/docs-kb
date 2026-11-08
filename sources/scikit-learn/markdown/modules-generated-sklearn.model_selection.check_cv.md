[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.check_cv.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.model_selection.check_cv.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.check_cv.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.model_selection.check_cv.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.model_selection.check_cv.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.model_selection.check_cv.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.model_selection.check_cv.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.model_selection.check_cv.html)

Collapse Sidebar Expand Sidebar

check\_cv[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.check_cv.html#check-cv "Link to this heading")

======================================================================================================================================

sklearn.model\_selection.check\_cv(_cv\=5_, _y\=None_, _\*_, _classifier\=False_, _shuffle\=False_, _random\_state\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/model_selection/_split.py#L2697)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.check_cv.html#sklearn.model_selection.check_cv "Link to this definition")

Input checker utility for building a cross-validator.

Parameters:

**cv**int, cross-validation generator, iterable or None, default=5

Determines the cross-validation splitting strategy. Possible inputs for cv are: - None, to use the default 5-fold cross validation, - integer, to specify the number of folds, - [CV splitter](https://scikit-learn.org/stable/glossary.html#term-CV-splitter)
, - an iterable that generates (train, test) splits as arrays of indices.

For integer/None inputs, if classifier is True and `y` is either binary or multiclass, [`StratifiedKFold`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.StratifiedKFold.html#sklearn.model_selection.StratifiedKFold "sklearn.model_selection.StratifiedKFold")
 is used. In all other cases, [`KFold`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.KFold.html#sklearn.model_selection.KFold "sklearn.model_selection.KFold")
 is used.

Refer [User Guide](https://scikit-learn.org/stable/modules/cross_validation.html#cross-validation)
 for the various cross-validation strategies that can be used here.

Changed in version 0.22: `cv` default value changed from 3-fold to 5-fold.

**y**array-like, default=None

The target variable for supervised learning problems.

**classifier**bool, default=False

Whether the task is a classification task. When `True` and `cv` is an integer or `None`, [`StratifiedKFold`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.StratifiedKFold.html#sklearn.model_selection.StratifiedKFold "sklearn.model_selection.StratifiedKFold")
 is used if `y` is binary or multiclass; otherwise [`KFold`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.KFold.html#sklearn.model_selection.KFold "sklearn.model_selection.KFold")
 is used. Ignored if `cv` is a cross-validator instance or iterable.

**shuffle**bool, default=False

Whether to shuffle the data before splitting into batches. Note that the samples within each split will not be shuffled. Only applies if `cv` is an int or `None`. If `cv` is a cross-validation generator or an iterable, `shuffle` is ignored.

**random\_state**int, RandomState instance or None, default=None

When `shuffle` is True and `cv` is an integer or `None`, `random_state` affects the ordering of the indices, which controls the randomness of each fold. Otherwise, this parameter has no effect. Pass an int for reproducible output across multiple function calls. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-random_state)
.

Returns:

**checked\_cv**a cross-validator instance.

The return value is a cross-validator which generates the train/test splits via the `split` method.

Examples

\>>> from sklearn.model\_selection import check\_cv
\>>> check\_cv(cv\=5, y\=None, classifier\=False)
KFold(...)
\>>> check\_cv(cv\=5, y\=\[1, 1, 0, 0, 0, 0\], classifier\=True)
StratifiedKFold(...)

Copy to clipboard

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.check_cv.html#gallery-examples "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_callback_support_thumb.png)

[Supporting callbacks in third party estimators](https://scikit-learn.org/stable/auto_examples/callbacks/plot_callback_support.html)

Supporting callbacks in third party estimators

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)