[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.utils.validation.check_is_fitted.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.utils.validation.check_is_fitted.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.utils.validation.check_is_fitted.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.utils.validation.check_is_fitted.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.utils.validation.check_is_fitted.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.utils.validation.check_is_fitted.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.utils.validation.check_is_fitted.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.utils.validation.check_is_fitted.html)

Collapse Sidebar Expand Sidebar

check\_is\_fitted[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.validation.check_is_fitted.html#check-is-fitted "Link to this heading")

=============================================================================================================================================================

sklearn.utils.validation.check\_is\_fitted(_estimator_, _attributes\=None_, _\*_, _msg\=None_, _all\_or\_any\=<built-in function all>_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/validation.py#L1637)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.validation.check_is_fitted.html#sklearn.utils.validation.check_is_fitted "Link to this definition")

Perform is\_fitted validation for estimator.

Checks if the estimator is fitted by verifying the presence of fitted attributes (ending with a trailing underscore) and otherwise raises a [`NotFittedError`](https://scikit-learn.org/stable/modules/generated/sklearn.exceptions.NotFittedError.html#sklearn.exceptions.NotFittedError "sklearn.exceptions.NotFittedError")
 with the given message.

If an estimator does not set any attributes with a trailing underscore, it can define a `__sklearn_is_fitted__` method returning a boolean to specify if the estimator is fitted or not. See [\_\_sklearn\_is\_fitted\_\_ as Developer API](https://scikit-learn.org/stable/auto_examples/developing_estimators/sklearn_is_fitted.html#sphx-glr-auto-examples-developing-estimators-sklearn-is-fitted-py)
 for an example on how to use the API.

If no `attributes` are passed, this function will pass if an estimator is stateless. An estimator can indicate it’s stateless by setting the `requires_fit` tag. See [Estimator Tags](https://scikit-learn.org/stable/developers/develop.html#estimator-tags)
 for more information. Note that the `requires_fit` tag is ignored if `attributes` are passed.

Parameters:

**estimator**estimator instance

Estimator instance for which the check is performed.

**attributes**str, list or tuple of str, default=None

Attribute name(s) given as string or a list/tuple of strings Eg.: `["coef_", "estimator_", ...], "coef_"`

If `None`, `estimator` is considered fitted if there exist an attribute that ends with a underscore and does not start with double underscore.

**msg**str, default=None

The default error message is, “This %(name)s instance is not fitted yet. Call ‘fit’ with appropriate arguments before using this estimator.”

For custom messages if “%(name)s” is present in the message string, it is substituted for the estimator name.

Eg. : “Estimator, %(name)s, must be fitted before sparsifying”.

**all\_or\_any**callable, {all, any}, default=all

Specify whether all or any of the given attributes must exist.

Raises:

TypeError

If the estimator is a class or not an estimator instance

NotFittedError

If the attributes are not found.

Examples

\>>> from sklearn.linear\_model import LogisticRegression
\>>> from sklearn.utils.validation import check\_is\_fitted
\>>> from sklearn.exceptions import NotFittedError
\>>> lr \= LogisticRegression()
\>>> try:
...     check\_is\_fitted(lr)
... except NotFittedError as exc:
...     print(f"Model is not fitted yet.")
Model is not fitted yet.
\>>> lr.fit(\[\[1, 2\], \[1, 3\]\], \[1, 0\])
LogisticRegression()
\>>> check\_is\_fitted(lr)

Copy to clipboard

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.validation.check_is_fitted.html#gallery-examples "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_callback_support_thumb.png)

[Supporting callbacks in third party estimators](https://scikit-learn.org/stable/auto_examples/callbacks/plot_callback_support.html)

Supporting callbacks in third party estimators

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_inductive_clustering_thumb.png)

[Inductive Clustering](https://scikit-learn.org/stable/auto_examples/cluster/plot_inductive_clustering.html)

Inductive Clustering

![](https://scikit-learn.org/stable/_images/sphx_glr_sklearn_is_fitted_thumb.png)

[\_\_sklearn\_is\_fitted\_\_ as Developer API](https://scikit-learn.org/stable/auto_examples/developing_estimators/sklearn_is_fitted.html)

\_\_sklearn\_is\_fitted\_\_ as Developer API

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_metadata_routing_thumb.png)

[Developing Estimators Compliant with Metadata Routing](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_metadata_routing.html)

Developing Estimators Compliant with Metadata Routing

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)