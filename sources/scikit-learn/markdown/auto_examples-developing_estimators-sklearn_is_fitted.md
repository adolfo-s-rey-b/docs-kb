[Skip to main content](https://scikit-learn.org/stable/auto_examples/developing_estimators/sklearn_is_fitted.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/developing_estimators/sklearn_is_fitted.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/developing_estimators/sklearn_is_fitted.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/developing_estimators/sklearn_is_fitted.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/developing_estimators/sklearn_is_fitted.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/developing_estimators/sklearn_is_fitted.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/developing_estimators/sklearn_is_fitted.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/developing_estimators/sklearn_is_fitted.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/developing_estimators/sklearn_is_fitted.html#sphx-glr-download-auto-examples-developing-estimators-sklearn-is-fitted-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

`__sklearn_is_fitted__` as Developer API[#](https://scikit-learn.org/stable/auto_examples/developing_estimators/sklearn_is_fitted.html#sklearn-is-fitted-as-developer-api "Link to this heading")

==================================================================================================================================================================================================

The `__sklearn_is_fitted__` method is a convention used in scikit-learn for checking whether an estimator object has been fitted or not. This method is typically implemented in custom estimator classes that are built on top of scikit-learn’s base classes like `BaseEstimator` or its subclasses.

Developers should use [`check_is_fitted`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.validation.check_is_fitted.html#sklearn.utils.validation.check_is_fitted "sklearn.utils.validation.check_is_fitted")
 at the beginning of all methods except `fit`. If they need to customize or speed-up the check, they can implement the `__sklearn_is_fitted__` method as shown below.

In this example the custom estimator showcases the usage of the `__sklearn_is_fitted__` method and the `check_is_fitted` utility function as developer APIs. The `__sklearn_is_fitted__` method checks fitted status by verifying the presence of the `_is_fitted` attribute.

An example custom estimator implementing a simple classifier[#](https://scikit-learn.org/stable/auto_examples/developing_estimators/sklearn_is_fitted.html#an-example-custom-estimator-implementing-a-simple-classifier "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

This code snippet defines a custom estimator class called `CustomEstimator` that extends both the `BaseEstimator` and `ClassifierMixin` classes from scikit-learn and showcases the usage of the `__sklearn_is_fitted__` method and the `check_is_fitted` utility function.

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

from sklearn.base import [BaseEstimator](https://scikit-learn.org/stable/modules/generated/sklearn.base.BaseEstimator.html#sklearn.base.BaseEstimator "sklearn.base.BaseEstimator")
, [ClassifierMixin](https://scikit-learn.org/stable/modules/generated/sklearn.base.ClassifierMixin.html#sklearn.base.ClassifierMixin "sklearn.base.ClassifierMixin")
from sklearn.utils.validation import [check\_is\_fitted](https://scikit-learn.org/stable/modules/generated/sklearn.utils.validation.check_is_fitted.html#sklearn.utils.validation.check_is_fitted "sklearn.utils.validation.check_is_fitted")

class CustomEstimator([BaseEstimator](https://scikit-learn.org/stable/modules/generated/sklearn.base.BaseEstimator.html#sklearn.base.BaseEstimator "sklearn.base.BaseEstimator")
, [ClassifierMixin](https://scikit-learn.org/stable/modules/generated/sklearn.base.ClassifierMixin.html#sklearn.base.ClassifierMixin "sklearn.base.ClassifierMixin")
):
    def \_\_init\_\_(self, parameter\=1):
        self.parameter \= parameter

    def fit(self, X, y):
        """
        Fit the estimator to the training data.
        """
        self.classes\_ \= sorted(set(y))
        \# Custom attribute to track if the estimator is fitted
        self.\_is\_fitted \= True
        return self

    def predict(self, X):
        """
        Perform Predictions

        If the estimator is not fitted, then raise NotFittedError
        """
        [check\_is\_fitted](https://scikit-learn.org/stable/modules/generated/sklearn.utils.validation.check_is_fitted.html#sklearn.utils.validation.check_is_fitted "sklearn.utils.validation.check_is_fitted")
(self)
        \# Perform prediction logic
        predictions \= \[self.classes\_\[0\]\] \* len(X)
        return predictions

    def score(self, X, y):
        """
        Calculate Score

        If the estimator is not fitted, then raise NotFittedError
        """
        [check\_is\_fitted](https://scikit-learn.org/stable/modules/generated/sklearn.utils.validation.check_is_fitted.html#sklearn.utils.validation.check_is_fitted "sklearn.utils.validation.check_is_fitted")
(self)
        \# Perform scoring logic
        return 0.5

    def \_\_sklearn\_is\_fitted\_\_(self):
        """
        Check fitted status and return a Boolean value.
        """
        return hasattr(self, "\_is\_fitted") and self.\_is\_fitted

Copy to clipboard

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo11.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/developing_estimators/sklearn_is_fitted.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo11.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/developing_estimators/sklearn_is_fitted.ipynb)

[`Download Jupyter notebook: sklearn_is_fitted.ipynb`](https://scikit-learn.org/stable/_downloads/1ba22806e611e4b95c469e74c4b23796/sklearn_is_fitted.ipynb)

[`Download Python source code: sklearn_is_fitted.py`](https://scikit-learn.org/stable/_downloads/e2bc37e26274190758a46ac161b8859a/sklearn_is_fitted.py)

[`Download zipped: sklearn_is_fitted.zip`](https://scikit-learn.org/stable/_downloads/c52226c1b0f858148e3768010bf9b091/sklearn_is_fitted.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_inductive_clustering_thumb.png)

[Inductive Clustering](https://scikit-learn.org/stable/auto_examples/cluster/plot_inductive_clustering.html)

Inductive Clustering

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_custom_kernel_thumb.png)

[SVM with custom kernel](https://scikit-learn.org/stable/auto_examples/svm/plot_custom_kernel.html)

SVM with custom kernel

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_callback_support_thumb.png)

[Supporting callbacks in third party estimators](https://scikit-learn.org/stable/auto_examples/callbacks/plot_callback_support.html)

Supporting callbacks in third party estimators

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_1_6_0_thumb.png)

[Release Highlights for scikit-learn 1.6](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_6_0.html)

Release Highlights for scikit-learn 1.6

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page

[Download source code](https://scikit-learn.org/stable/_downloads/e2bc37e26274190758a46ac161b8859a/sklearn_is_fitted.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/1ba22806e611e4b95c469e74c4b23796/sklearn_is_fitted.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/c52226c1b0f858148e3768010bf9b091/sklearn_is_fitted.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo11.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/developing_estimators/sklearn_is_fitted.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo11.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/developing_estimators/sklearn_is_fitted.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)