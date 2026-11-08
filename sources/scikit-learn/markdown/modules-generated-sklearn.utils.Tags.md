[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.utils.Tags.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.utils.Tags.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.utils.Tags.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.utils.Tags.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.utils.Tags.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.utils.Tags.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.utils.Tags.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.utils.Tags.html)

Collapse Sidebar Expand Sidebar

Tags[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.Tags.html#tags "Link to this heading")

===============================================================================================================

class sklearn.utils.Tags(_estimator\_type: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")
 | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
_, _target\_tags: [TargetTags](https://scikit-learn.org/stable/modules/generated/sklearn.utils.TargetTags.html#sklearn.utils.TargetTags "sklearn.utils._tags.TargetTags")
_, _transformer\_tags: [TransformerTags](https://scikit-learn.org/stable/modules/generated/sklearn.utils.TransformerTags.html#sklearn.utils.TransformerTags "sklearn.utils._tags.TransformerTags")
 | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
 \= None_, _classifier\_tags: [ClassifierTags](https://scikit-learn.org/stable/modules/generated/sklearn.utils.ClassifierTags.html#sklearn.utils.ClassifierTags "sklearn.utils._tags.ClassifierTags")
 | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
 \= None_, _regressor\_tags: [RegressorTags](https://scikit-learn.org/stable/modules/generated/sklearn.utils.RegressorTags.html#sklearn.utils.RegressorTags "sklearn.utils._tags.RegressorTags")
 | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
 \= None_, _array\_api\_support: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")
 \= False_, _no\_validation: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")
 \= False_, _non\_deterministic: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")
 \= False_, _requires\_fit: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")
 \= True_, _\_skip\_test: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")
 \= False_, _input\_tags: [InputTags](https://scikit-learn.org/stable/modules/generated/sklearn.utils.InputTags.html#sklearn.utils.InputTags "sklearn.utils._tags.InputTags")
 \= <factory>_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_tags.py#L186)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.Tags.html#sklearn.utils.Tags "Link to this definition")

Tags for the estimator.

See [Estimator Tags](https://scikit-learn.org/stable/developers/develop.html#estimator-tags)
 for more information.

Parameters:

**estimator\_type**str or None

The type of the estimator. Can be one of: - “classifier” - “regressor” - “transformer” - “clusterer” - “outlier\_detector” - “density\_estimator”

**target\_tags**[`TargetTags`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.TargetTags.html#sklearn.utils.TargetTags "sklearn.utils.TargetTags")

The target(y) tags.

**transformer\_tags**[`TransformerTags`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.TransformerTags.html#sklearn.utils.TransformerTags "sklearn.utils.TransformerTags")
 or None

The transformer tags.

**classifier\_tags**[`ClassifierTags`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.ClassifierTags.html#sklearn.utils.ClassifierTags "sklearn.utils.ClassifierTags")
 or None

The classifier tags.

**regressor\_tags**[`RegressorTags`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.RegressorTags.html#sklearn.utils.RegressorTags "sklearn.utils.RegressorTags")
 or None

The regressor tags.

**array\_api\_support**bool, default=False

Whether the estimator supports Array API compatible inputs.

**no\_validation**bool, default=False

Whether the estimator skips input-validation. This is only meant for stateless and dummy transformers!

**non\_deterministic**bool, default=False

Whether the estimator is not deterministic given a fixed `random_state`.

**requires\_fit**bool, default=True

Whether the estimator requires to be fitted before calling one of `transform`, `predict`, `predict_proba`, or `decision_function`.

**\_skip\_test**bool, default=False

Whether to skip common tests entirely. Don’t use this unless you have a _very good_ reason.

**input\_tags**[`InputTags`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.InputTags.html#sklearn.utils.InputTags "sklearn.utils.InputTags")

The input data(X) tags.

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.Tags.html#gallery-examples "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_1_6_0_thumb.png)

[Release Highlights for scikit-learn 1.6](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_6_0.html)

Release Highlights for scikit-learn 1.6

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)