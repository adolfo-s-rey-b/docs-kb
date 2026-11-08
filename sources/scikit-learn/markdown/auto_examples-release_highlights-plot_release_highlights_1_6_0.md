[Skip to main content](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_6_0.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/release_highlights/plot_release_highlights_1_6_0.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_6_0.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/release_highlights/plot_release_highlights_1_6_0.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/release_highlights/plot_release_highlights_1_6_0.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/release_highlights/plot_release_highlights_1_6_0.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/release_highlights/plot_release_highlights_1_6_0.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/release_highlights/plot_release_highlights_1_6_0.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_6_0.html#sphx-glr-download-auto-examples-release-highlights-plot-release-highlights-1-6-0-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Release Highlights for scikit-learn 1.6[#](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_6_0.html#release-highlights-for-scikit-learn-1-6 "Link to this heading")

===============================================================================================================================================================================================================

We are pleased to announce the release of scikit-learn 1.6! Many bug fixes and improvements were added, as well as some key new features. Below we detail the highlights of this release. **For an exhaustive list of all the changes**, please refer to the [release notes](https://scikit-learn.org/stable/whats_new/v1.6.html#release-notes-1-6)
.

To install the latest version (with pip):

pip install \--upgrade scikit\-learn

Copy to clipboard

or with conda:

conda install \-c conda\-forge scikit\-learn

Copy to clipboard

FrozenEstimator: Freezing an estimator[#](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_6_0.html#frozenestimator-freezing-an-estimator "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

This meta-estimator allows you to take an estimator and freeze its fit method, meaning that calling `fit` does not perform any operations; also, `fit_predict` and `fit_transform` call `predict` and `transform` respectively without calling `fit`. The original estimator’s other methods and properties are left unchanged. An interesting use case for this is to use a pre-fitted model as a transformer step in a pipeline or to pass a pre-fitted model to some of the meta-estimators. Here’s a short example:

import time

from sklearn.datasets import [make\_classification](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_classification.html#sklearn.datasets.make_classification "sklearn.datasets.make_classification")
from sklearn.frozen import [FrozenEstimator](https://scikit-learn.org/stable/modules/generated/sklearn.frozen.FrozenEstimator.html#sklearn.frozen.FrozenEstimator "sklearn.frozen.FrozenEstimator")
from sklearn.linear\_model import [SGDClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDClassifier.html#sklearn.linear_model.SGDClassifier "sklearn.linear_model.SGDClassifier")
from sklearn.model\_selection import [FixedThresholdClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.FixedThresholdClassifier.html#sklearn.model_selection.FixedThresholdClassifier "sklearn.model_selection.FixedThresholdClassifier")

X, y \= [make\_classification](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_classification.html#sklearn.datasets.make_classification "sklearn.datasets.make_classification")
(n\_samples\=1000, random\_state\=0)

start \= [time.time](https://docs.python.org/3/library/time.html#time.time "time.time")
()
classifier \= [SGDClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDClassifier.html#sklearn.linear_model.SGDClassifier "sklearn.linear_model.SGDClassifier")
().fit(X, y)
print(f"Fitting the classifier took {([time.time](https://docs.python.org/3/library/time.html#time.time "time.time")
() \- start) \* 1\_000:.2f} milliseconds")

start \= [time.time](https://docs.python.org/3/library/time.html#time.time "time.time")
()
threshold\_classifier \= [FixedThresholdClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.FixedThresholdClassifier.html#sklearn.model_selection.FixedThresholdClassifier "sklearn.model_selection.FixedThresholdClassifier")
(
    estimator\=[FrozenEstimator](https://scikit-learn.org/stable/modules/generated/sklearn.frozen.FrozenEstimator.html#sklearn.frozen.FrozenEstimator "sklearn.frozen.FrozenEstimator")
(classifier), threshold\=0.9
).fit(X, y)
print(
    f"Fitting the threshold classifier took {([time.time](https://docs.python.org/3/library/time.html#time.time "time.time")
() \- start) \* 1\_000:.2f} "
    "milliseconds"
)

Copy to clipboard

Fitting the classifier took 4.16 milliseconds
Fitting the threshold classifier took 0.66 milliseconds

Copy to clipboard

Fitting the threshold classifier skipped fitting the inner `SGDClassifier`. For more details refer to the example [Examples of Using FrozenEstimator](https://scikit-learn.org/stable/auto_examples/frozen/plot_frozen_examples.html#sphx-glr-auto-examples-frozen-plot-frozen-examples-py)
.

Transforming data other than X in a Pipeline[#](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_6_0.html#transforming-data-other-than-x-in-a-pipeline "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
 now supports transforming passed data other than `X` if necessary. This can be done by setting the new `transform_input` parameter. This is particularly useful when passing a validation set through the pipeline.

As an example, imagine `EstimatorWithValidationSet` is an estimator which accepts a validation set. We can now have a pipeline which will transform the validation set and pass it to the estimator:

with sklearn.config\_context(enable\_metadata\_routing\=True):
    est\_gs \= GridSearchCV(
        Pipeline(
            (
                StandardScaler(),
                EstimatorWithValidationSet(...).set\_fit\_request(X\_val\=True, y\_val\=True),
            ),
            \# telling pipeline to transform these inputs up to the step which is
            \# requesting them.
            transform\_input\=\["X\_val"\],
        ),
        param\_grid\={"estimatorwithvalidationset\_\_param\_to\_optimize": list(range(5))},
        cv\=5,
    ).fit(X, y, X\_val\=X\_val, y\_val\=y\_val)

Copy to clipboard

In the above code, the key parts are the call to `set_fit_request` to specify that `X_val` and `y_val` are required by the `EstimatorWithValidationSet.fit` method, and the `transform_input` parameter to tell the pipeline to transform `X_val` before passing it to `EstimatorWithValidationSet.fit`.

Note that at this time scikit-learn estimators have not yet been extended to accept user specified validation sets. This feature is released early to collect feedback from third-party libraries who might benefit from it.

Multiclass support for `LogisticRegression(solver="newton-cholesky")`[#](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_6_0.html#multiclass-support-for-logisticregression-solver-newton-cholesky "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The `"newton-cholesky"` solver (originally introduced in scikit-learn version 1.2) was previously limited to binary [`LogisticRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
 and some other generalized linear regression estimators (namely [`PoissonRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.PoissonRegressor.html#sklearn.linear_model.PoissonRegressor "sklearn.linear_model.PoissonRegressor")
, [`GammaRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.GammaRegressor.html#sklearn.linear_model.GammaRegressor "sklearn.linear_model.GammaRegressor")
 and [`TweedieRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.TweedieRegressor.html#sklearn.linear_model.TweedieRegressor "sklearn.linear_model.TweedieRegressor")
).

This new release includes support for multiclass (multinomial) [`LogisticRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
.

This solver is particularly useful when the number of features is small to medium. It has been empirically shown to converge more reliably and faster than other solvers on some medium sized datasets with one-hot encoded categorical features as can be seen in the [benchmark results of the pull-request](https://github.com/scikit-learn/scikit-learn/pull/28840#issuecomment-2065368727)
.

Missing value support for Extra Trees[#](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_6_0.html#missing-value-support-for-extra-trees "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The classes [`ensemble.ExtraTreesClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.ExtraTreesClassifier.html#sklearn.ensemble.ExtraTreesClassifier "sklearn.ensemble.ExtraTreesClassifier")
 and [`ensemble.ExtraTreesRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.ExtraTreesRegressor.html#sklearn.ensemble.ExtraTreesRegressor "sklearn.ensemble.ExtraTreesRegressor")
 now support missing values. More details in the [User Guide](https://scikit-learn.org/stable/modules/tree.html#tree-missing-value-support)
.

import numpy as np

from sklearn.ensemble import [ExtraTreesClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.ExtraTreesClassifier.html#sklearn.ensemble.ExtraTreesClassifier "sklearn.ensemble.ExtraTreesClassifier")

X \= [np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
(\[0, 1, 6, [np.nan](https://numpy.org/doc/stable/reference/constants.html#numpy.nan "numpy.nan")\
\]).reshape(\-1, 1)
y \= \[0, 0, 1, 1\]

forest \= [ExtraTreesClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.ExtraTreesClassifier.html#sklearn.ensemble.ExtraTreesClassifier "sklearn.ensemble.ExtraTreesClassifier")
(random\_state\=0).fit(X, y)
forest.predict(X)

Copy to clipboard

array(\[0, 0, 1, 1\])

Copy to clipboard

Download any dataset from the web[#](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_6_0.html#download-any-dataset-from-the-web "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The function [`datasets.fetch_file`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_file.html#sklearn.datasets.fetch_file "sklearn.datasets.fetch_file")
 allows downloading a file from any given URL. This convenience function provides built-in local disk caching, sha256 digest integrity check and an automated retry mechanism on network error.

The goal is to provide the same convenience and reliability as dataset fetchers while giving the flexibility to work with data from arbitrary online sources and file formats.

The downloaded file can then be loaded with generic or domain specific functions such as `pandas.read_csv`, `pandas.read_parquet`, etc.

Array API support[#](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_6_0.html#array-api-support "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------

Many more estimators and functions have been updated to support array API compatible inputs since version 1.5, in particular the meta-estimators for hyperparameter tuning from the [`sklearn.model_selection`](https://scikit-learn.org/stable/api/sklearn.model_selection.html#module-sklearn.model_selection "sklearn.model_selection")
 module and the metrics from the [`sklearn.metrics`](https://scikit-learn.org/stable/api/sklearn.metrics.html#module-sklearn.metrics "sklearn.metrics")
 module.

Please refer to the [array API support](https://scikit-learn.org/stable/modules/array_api.html#array-api)
 page for instructions to use scikit-learn with array API compatible libraries such as PyTorch or CuPy.

Almost complete Metadata Routing support[#](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_6_0.html#almost-complete-metadata-routing-support "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Support for routing metadata has been added to all remaining estimators and functions except AdaBoost. See [Metadata Routing User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 for more details.

Free-threaded CPython 3.13 support[#](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_6_0.html#free-threaded-cpython-3-13-support "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

scikit-learn has preliminary support for free-threaded CPython, in particular free-threaded wheels are available for all of our supported platforms.

Free-threaded (also known as nogil) CPython 3.13 is an experimental version of CPython 3.13 which aims at enabling efficient multi-threaded use cases by removing the Global Interpreter Lock (GIL).

For more details about free-threaded CPython see [py-free-threading doc](https://py-free-threading.github.io/)
, in particular [how to install a free-threaded CPython](https://py-free-threading.github.io/installing_cpython/)
 and [Ecosystem compatibility tracking](https://py-free-threading.github.io/tracking/)
.

Feel free to try free-threaded CPython on your use case and report any issues!

Improvements to the developer API for third party libraries[#](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_6_0.html#improvements-to-the-developer-api-for-third-party-libraries "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

We have been working on improving the developer API for third party libraries. This is still a work in progress, but a fair amount of work has been done in this release. This release includes:

*   [`sklearn.utils.validation.validate_data`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.validation.validate_data.html#sklearn.utils.validation.validate_data "sklearn.utils.validation.validate_data")
     is introduced and replaces the previously private `BaseEstimator._validate_data` method. This function extends `check_array` and adds support for remembering input feature counts and names.
    
*   Estimator tags are now revamped and a part of the public API via [`sklearn.utils.Tags`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.Tags.html#sklearn.utils.Tags "sklearn.utils.Tags")
    . Estimators should now override the `BaseEstimator.__sklearn_tags__` method instead of implementing a `_more_tags` method. If you’d like to support multiple scikit-learn versions, you can implement both methods in your class.
    
*   As a consequence of developing a public tag API, we’ve removed the `_xfail_checks` tag and tests which are expected to fail are directly passed to [`check_estimator`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.estimator_checks.check_estimator.html#sklearn.utils.estimator_checks.check_estimator "sklearn.utils.estimator_checks.check_estimator")
     and [`parametrize_with_checks`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.estimator_checks.parametrize_with_checks.html#sklearn.utils.estimator_checks.parametrize_with_checks "sklearn.utils.estimator_checks.parametrize_with_checks")
    . See their corresponding API docs for more details.
    
*   Many tests in the common test suite are updated and raise more helpful error messages. We’ve also added some new tests, which should help you more easily fix potential issues with your estimators.
    

An updated version of our [Developing scikit-learn estimators](https://scikit-learn.org/stable/developers/develop.html#develop)
 is also available, which we recommend you check out.

**Total running time of the script:** (0 minutes 0.107 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo29.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/release_highlights/plot_release_highlights_1_6_0.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo29.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/release_highlights/plot_release_highlights_1_6_0.ipynb)

[`Download Jupyter notebook: plot_release_highlights_1_6_0.ipynb`](https://scikit-learn.org/stable/_downloads/862c762bdafef83db4c2c9e803ed6295/plot_release_highlights_1_6_0.ipynb)

[`Download Python source code: plot_release_highlights_1_6_0.py`](https://scikit-learn.org/stable/_downloads/a471e25495d24d0086e798aa9ca44a89/plot_release_highlights_1_6_0.py)

[`Download zipped: plot_release_highlights_1_6_0.zip`](https://scikit-learn.org/stable/_downloads/151e78f803ff9f3154dd7dbbaf45e0b0/plot_release_highlights_1_6_0.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_1_8_0_thumb.png)

[Release Highlights for scikit-learn 1.8](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_8_0.html)

Release Highlights for scikit-learn 1.8

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_1_7_0_thumb.png)

[Release Highlights for scikit-learn 1.7](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_7_0.html)

Release Highlights for scikit-learn 1.7

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_1_2_0_thumb.png)

[Release Highlights for scikit-learn 1.2](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_2_0.html)

Release Highlights for scikit-learn 1.2

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_1_4_0_thumb.png)

[Release Highlights for scikit-learn 1.4](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_4_0.html)

Release Highlights for scikit-learn 1.4

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page

[Download source code](https://scikit-learn.org/stable/_downloads/a471e25495d24d0086e798aa9ca44a89/plot_release_highlights_1_6_0.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/862c762bdafef83db4c2c9e803ed6295/plot_release_highlights_1_6_0.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/151e78f803ff9f3154dd7dbbaf45e0b0/plot_release_highlights_1_6_0.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo29.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/release_highlights/plot_release_highlights_1_6_0.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo29.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/release_highlights/plot_release_highlights_1_6_0.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)