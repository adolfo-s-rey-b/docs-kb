[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.utils.RegressorTags.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.utils.RegressorTags.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.utils.RegressorTags.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.utils.RegressorTags.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.utils.RegressorTags.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.utils.RegressorTags.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.utils.RegressorTags.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.utils.RegressorTags.html)

Collapse Sidebar Expand Sidebar

RegressorTags[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.RegressorTags.html#regressortags "Link to this heading")

==========================================================================================================================================

class sklearn.utils.RegressorTags(_poor\_score: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")
 \= False_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_tags.py#L168)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.RegressorTags.html#sklearn.utils.RegressorTags "Link to this definition")

Tags for the regressor.

Parameters:

**poor\_score**bool, default=False

Whether the estimator fails to provide a “reasonable” test-set score, which currently for regression is an R2 of 0.5 on `make_regression(n_samples=200, n_features=10, n_informative=1, bias=5.0, noise=20, random_state=42)`. The dataset and values are based on current estimators in scikit-learn and might be replaced by something more systematic.

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)