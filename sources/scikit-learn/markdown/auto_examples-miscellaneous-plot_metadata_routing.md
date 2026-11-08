[Skip to main content](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_metadata_routing.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/miscellaneous/plot_metadata_routing.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_metadata_routing.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/miscellaneous/plot_metadata_routing.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/miscellaneous/plot_metadata_routing.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/miscellaneous/plot_metadata_routing.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/miscellaneous/plot_metadata_routing.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/miscellaneous/plot_metadata_routing.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_metadata_routing.html#sphx-glr-download-auto-examples-miscellaneous-plot-metadata-routing-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Developing Estimators Compliant with Metadata Routing[#](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_metadata_routing.html#developing-estimators-compliant-with-metadata-routing "Link to this heading")

==============================================================================================================================================================================================================================

This document shows how you can use the [metadata routing mechanism](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 in scikit-learn to build estimators that route metadata to other estimators, scorers, and CV splitters, that can consume [metadata](https://scikit-learn.org/stable/glossary.html#term-metadata)
.

To better understand the following document, we need to introduce two concepts: [routers](https://scikit-learn.org/stable/glossary.html#term-router)
 and [consumers](https://scikit-learn.org/stable/glossary.html#term-consumer)
. A [router](https://scikit-learn.org/stable/glossary.html#term-router)
 is an object which forwards some given data and metadata to other objects. In most cases, a router is a [meta-estimator](https://scikit-learn.org/stable/glossary.html#term-meta-estimator)
, i.e. an estimator which takes another estimator as a parameter. A function such as [`sklearn.model_selection.cross_validate`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_validate.html#sklearn.model_selection.cross_validate "sklearn.model_selection.cross_validate")
 which takes an estimator as a parameter and forwards data and metadata, is also a router.

A [consumer](https://scikit-learn.org/stable/glossary.html#term-consumer)
, on the other hand, is an object which accepts and uses some given metadata. For instance, an estimator taking into account `sample_weight` in its [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
 method is a consumer of `sample_weight`.

It is possible for an object to be both a router and a consumer. For instance, a meta-estimator may take into account `sample_weight` in certain calculations, but it may also route it to the underlying estimator.

First a few imports and some random data for the rest of the script.

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

Copy to clipboard

import warnings
from pprint import [pprint](https://docs.python.org/3/library/pprint.html#pprint.pprint "pprint.pprint")

import numpy as np

from sklearn import [set\_config](https://scikit-learn.org/stable/modules/generated/sklearn.set_config.html#sklearn.set_config "sklearn.set_config")
from sklearn.base import (
    [BaseEstimator](https://scikit-learn.org/stable/modules/generated/sklearn.base.BaseEstimator.html#sklearn.base.BaseEstimator "sklearn.base.BaseEstimator")
,
    [ClassifierMixin](https://scikit-learn.org/stable/modules/generated/sklearn.base.ClassifierMixin.html#sklearn.base.ClassifierMixin "sklearn.base.ClassifierMixin")
,
    [MetaEstimatorMixin](https://scikit-learn.org/stable/modules/generated/sklearn.base.MetaEstimatorMixin.html#sklearn.base.MetaEstimatorMixin "sklearn.base.MetaEstimatorMixin")
,
    [RegressorMixin](https://scikit-learn.org/stable/modules/generated/sklearn.base.RegressorMixin.html#sklearn.base.RegressorMixin "sklearn.base.RegressorMixin")
,
    [TransformerMixin](https://scikit-learn.org/stable/modules/generated/sklearn.base.TransformerMixin.html#sklearn.base.TransformerMixin "sklearn.base.TransformerMixin")
,
    clone,
)
from sklearn.linear\_model import [LinearRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html#sklearn.linear_model.LinearRegression "sklearn.linear_model.LinearRegression")
from sklearn.utils import metadata\_routing
from sklearn.utils.metadata\_routing import (
    [MetadataRouter](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRouter.html#sklearn.utils.metadata_routing.MetadataRouter "sklearn.utils.metadata_routing.MetadataRouter")
,
    [MethodMapping](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MethodMapping.html#sklearn.utils.metadata_routing.MethodMapping "sklearn.utils.metadata_routing.MethodMapping")
,
    [process\_routing](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.process_routing.html#sklearn.utils.metadata_routing.process_routing "sklearn.utils.metadata_routing.process_routing")
,
)
from sklearn.utils.validation import [check\_is\_fitted](https://scikit-learn.org/stable/modules/generated/sklearn.utils.validation.check_is_fitted.html#sklearn.utils.validation.check_is_fitted "sklearn.utils.validation.check_is_fitted")

n\_samples, n\_features \= 100, 4
rng \= [np.random.RandomState](https://numpy.org/doc/stable/reference/random/legacy.html#numpy.random.RandomState "numpy.random.RandomState")
(42)
X \= rng.rand(n\_samples, n\_features)
y \= rng.randint(0, 2, size\=n\_samples)
my\_groups \= rng.randint(0, 10, size\=n\_samples)
my\_weights \= rng.rand(n\_samples)
my\_other\_weights \= rng.rand(n\_samples)

Copy to clipboard

Metadata routing is only available if explicitly enabled:

[set\_config](https://scikit-learn.org/stable/modules/generated/sklearn.set_config.html#sklearn.set_config "sklearn.set_config")
(enable\_metadata\_routing\=True)

Copy to clipboard

This utility function is a dummy to check if a metadata is passed:

def check\_metadata(obj, \*\*kwargs):
    for key, value in kwargs.items():
        if value is not None:
            print(
                f"Received {key} of length = {len(value)} in {obj.\_\_class\_\_.\_\_name\_\_}."
            )
        else:
            print(f"{key} is None in {obj.\_\_class\_\_.\_\_name\_\_}.")

Copy to clipboard

A utility function to nicely print the routing information of an object:

def print\_routing(obj):
    [pprint](https://docs.python.org/3/library/pprint.html#pprint.pprint "pprint.pprint")
(obj.get\_metadata\_routing().\_serialize())

Copy to clipboard

Consuming Estimator[#](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_metadata_routing.html#consuming-estimator "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------

Here we demonstrate how an estimator can expose the required API to support metadata routing as a consumer. Imagine a simple classifier accepting `sample_weight` as a metadata in its `fit` and `groups` in its `predict` method:

class ExampleClassifier([ClassifierMixin](https://scikit-learn.org/stable/modules/generated/sklearn.base.ClassifierMixin.html#sklearn.base.ClassifierMixin "sklearn.base.ClassifierMixin")
, [BaseEstimator](https://scikit-learn.org/stable/modules/generated/sklearn.base.BaseEstimator.html#sklearn.base.BaseEstimator "sklearn.base.BaseEstimator")
):
    def fit(self, X, y, sample\_weight\=None):
        check\_metadata(self, sample\_weight\=sample\_weight)
        \# all classifiers need to expose a classes\_ attribute once they're fit.
        self.classes\_ \= [np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
(\[0, 1\])
        return self

    def predict(self, X, groups\=None):
        check\_metadata(self, groups\=groups)
        \# return a constant value of 1, not a very smart classifier!
        return [np.ones](https://numpy.org/doc/stable/reference/generated/numpy.ones.html#numpy.ones "numpy.ones")
(len(X))

Copy to clipboard

The above estimator now has all it needs to consume metadata. This is accomplished by some magic done in [`BaseEstimator`](https://scikit-learn.org/stable/modules/generated/sklearn.base.BaseEstimator.html#sklearn.base.BaseEstimator "sklearn.base.BaseEstimator")
. There are now three methods exposed by the above class: `set_fit_request`, `set_predict_request`, and `get_metadata_routing`. There is also a `set_score_request` for `sample_weight` which is present since [`ClassifierMixin`](https://scikit-learn.org/stable/modules/generated/sklearn.base.ClassifierMixin.html#sklearn.base.ClassifierMixin "sklearn.base.ClassifierMixin")
 implements a `score` method accepting `sample_weight`. The same applies to regressors which inherit from [`RegressorMixin`](https://scikit-learn.org/stable/modules/generated/sklearn.base.RegressorMixin.html#sklearn.base.RegressorMixin "sklearn.base.RegressorMixin")
.

By default, no metadata is requested, which we can see as:

print\_routing(ExampleClassifier())

Copy to clipboard

{'fit': {'sample\_weight': None},
 'predict': {'groups': None},
 'score': {'sample\_weight': None}}

Copy to clipboard

The above output means that `sample_weight` and `groups` are not requested by `ExampleClassifier`, and if a router is given those metadata, it should raise an error, since the user has not explicitly set whether they are required or not. The same is true for `sample_weight` in the `score` method, which is inherited from [`ClassifierMixin`](https://scikit-learn.org/stable/modules/generated/sklearn.base.ClassifierMixin.html#sklearn.base.ClassifierMixin "sklearn.base.ClassifierMixin")
. In order to explicitly set request values for those metadata, we can use these methods:

est \= (
    ExampleClassifier()
    .set\_fit\_request(sample\_weight\=False)
    .set\_predict\_request(groups\=True)
    .set\_score\_request(sample\_weight\=False)
)
print\_routing(est)

Copy to clipboard

{'fit': {'sample\_weight': False},
 'predict': {'groups': True},
 'score': {'sample\_weight': False}}

Copy to clipboard

Note

Please note that as long as the above estimator is not used in a meta-estimator, the user does not need to set any requests for the metadata and the set values are ignored, since a consumer does not validate or route given metadata. A simple usage of the above estimator would work as expected.

est \= ExampleClassifier()
est.fit(X, y, sample\_weight\=my\_weights)
est.predict(X\[:3, :\], groups\=my\_groups)

Copy to clipboard

Out:

Received sample\_weight of length = 100 in ExampleClassifier.
Received groups of length = 100 in ExampleClassifier.

array(\[1., 1., 1.\])

Copy to clipboard

Routing Meta-Estimator[#](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_metadata_routing.html#routing-meta-estimator "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------

Now, we show how to design a meta-estimator to be a router. As a simplified example, here is a meta-estimator, which doesn’t do much other than routing the metadata.

To make the meta-estimator a router, you only need to:

*   define its `get_metadata_routing` method, which returns a `MetadataRouter` instance in charge of configuring the metadata routing.
    
*   use `process_routing` inside its methods (`fit`, `predict`, …) to properly route the metadata from the meta-estimator to its sub-estimator.
    

class MetaClassifier([MetaEstimatorMixin](https://scikit-learn.org/stable/modules/generated/sklearn.base.MetaEstimatorMixin.html#sklearn.base.MetaEstimatorMixin "sklearn.base.MetaEstimatorMixin")
, [ClassifierMixin](https://scikit-learn.org/stable/modules/generated/sklearn.base.ClassifierMixin.html#sklearn.base.ClassifierMixin "sklearn.base.ClassifierMixin")
, [BaseEstimator](https://scikit-learn.org/stable/modules/generated/sklearn.base.BaseEstimator.html#sklearn.base.BaseEstimator "sklearn.base.BaseEstimator")
):
    def \_\_init\_\_(self, estimator):
        self.estimator \= estimator

    def get\_metadata\_routing(self):
        \# This method defines the routing for this meta-estimator.
        \# In order to do so, a \`MetadataRouter\` instance is created, and the
        \# routing is added to it.
        router \= [MetadataRouter](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRouter.html#sklearn.utils.metadata_routing.MetadataRouter "sklearn.utils.metadata_routing.MetadataRouter")
(owner\=self).add(
            estimator\=self.estimator,
            method\_mapping\=[MethodMapping](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MethodMapping.html#sklearn.utils.metadata_routing.MethodMapping "sklearn.utils.metadata_routing.MethodMapping")
()
            .add(caller\="fit", callee\="fit")
            .add(caller\="predict", callee\="predict")
            .add(caller\="score", callee\="score"),
        )
        return router

    def fit(self, X, y, \*\*fit\_params):
        \# Get information on all the metadata that should be routed from here to
        \# consuming methods.
        routed\_params \= [process\_routing](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.process_routing.html#sklearn.utils.metadata_routing.process_routing "sklearn.utils.metadata_routing.process_routing")
(self, "fit", \*\*fit\_params)
        \# A sub-estimator is fitted and its classes are attributed to the
        \# meta-estimator. Since we call the sub-estimator's fit method, we pass the
        \# the metadata stored in \`routed\_params\["estimator"\]\["fit"\]\`.
        self.estimator\_ \= clone(self.estimator).fit(
            X, y, \*\*routed\_params\["estimator"\]\["fit"\]
        )
        self.classes\_ \= self.estimator\_.classes\_
        return self

    def predict(self, X, \*\*predict\_params):
        [check\_is\_fitted](https://scikit-learn.org/stable/modules/generated/sklearn.utils.validation.check_is_fitted.html#sklearn.utils.validation.check_is_fitted "sklearn.utils.validation.check_is_fitted")
(self)
        \# As in \`fit\`, we get information on all the metadata that should be routed
        \# and pass the metadata that is stored in
        \# \`routed\_params\["estimator"\]\["predict"\]\` to the sub-estimator's predict method.
        routed\_params \= [process\_routing](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.process_routing.html#sklearn.utils.metadata_routing.process_routing "sklearn.utils.metadata_routing.process_routing")
(self, "predict", \*\*predict\_params)
        return self.estimator\_.predict(X, \*\*routed\_params\["estimator"\]\["predict"\])

Copy to clipboard

Let’s break down different parts of the above code.

In each method, we use the `process_routing` function to construct a [`Bunch`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.Bunch.html#sklearn.utils.Bunch "sklearn.utils.Bunch")
 of the form `{"object_name": {"method_name": {"metadata": value}}}` to pass to the underlying estimator’s method. The `object_name` (`estimator` in `routed_params["estimator"]["fit"]`) is the same as the `estimator` added in the `get_metadata_routing`. `process_routing` also validates the input metadata: it makes sure all given metadata are requested to avoid silent bugs.

Next, we illustrate the different behaviors and notably the type of errors raised.

meta\_est \= MetaClassifier(
    estimator\=ExampleClassifier().set\_fit\_request(sample\_weight\=True)
)
meta\_est.fit(X, y, sample\_weight\=my\_weights)

Copy to clipboard

Received sample\_weight of length = 100 in ExampleClassifier.

Copy to clipboard

MetaClassifier(estimator=ExampleClassifier())

**In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook.  
On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.**

MetaClassifier

iFitted

Parameters

|     |     |     |
| --- | --- | --- |
|     | estimator | ExampleClassifier() |

Fitted attributes

| Name | Type | Value |
| --- | --- | --- |
| classes\_ | ndarray\[int64\](2,) | \[0,1\] |
| estimator\_ | ExampleClassifier | ExampleClassifier() |

estimator: ExampleClassifier

ExampleClassifier()

ExampleClassifier

Parameters

  
  

Note that the above example is calling our utility function `check_metadata()` via the `ExampleClassifier`. It checks that `sample_weight` is correctly passed to it. If it is not, like in the following example, it would print that `sample_weight` is `None`:

meta\_est.fit(X, y)

Copy to clipboard

sample\_weight is None in ExampleClassifier.

Copy to clipboard

MetaClassifier(estimator=ExampleClassifier())

**In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook.  
On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.**

MetaClassifier

iFitted

Parameters

|     |     |     |
| --- | --- | --- |
|     | estimator | ExampleClassifier() |

Fitted attributes

| Name | Type | Value |
| --- | --- | --- |
| classes\_ | ndarray\[int64\](2,) | \[0,1\] |
| estimator\_ | ExampleClassifier | ExampleClassifier() |

estimator: ExampleClassifier

ExampleClassifier()

ExampleClassifier

Parameters

  
  

If we pass an unknown metadata, an error is raised:

try:
    meta\_est.fit(X, y, test\=my\_weights)
except TypeError as e:
    print(e)

Copy to clipboard

MetaClassifier.fit got unexpected argument(s) {'test'}, which are not routed to any object.

Copy to clipboard

And if we pass a metadata which is not explicitly requested:

try:
    meta\_est.fit(X, y, sample\_weight\=my\_weights).predict(X, groups\=my\_groups)
except ValueError as e:
    print(e)

Copy to clipboard

Received sample\_weight of length = 100 in ExampleClassifier.
\[groups\] are passed but are not explicitly set as requested or not requested for ExampleClassifier.predict, which is used within MetaClassifier.predict. Call \`ExampleClassifier.set\_predict\_request({metadata}=True/False)\` for each metadata you want to request/ignore. See the Metadata Routing User guide <https://scikit-learn.org/stable/metadata\_routing.html> for more information.

Copy to clipboard

Also, if we explicitly set it as not requested, but it is provided:

meta\_est \= MetaClassifier(
    estimator\=ExampleClassifier()
    .set\_fit\_request(sample\_weight\=True)
    .set\_predict\_request(groups\=False)
)
try:
    meta\_est.fit(X, y, sample\_weight\=my\_weights).predict(X\[:3, :\], groups\=my\_groups)
except TypeError as e:
    print(e)

Copy to clipboard

Received sample\_weight of length = 100 in ExampleClassifier.
MetaClassifier.predict got unexpected argument(s) {'groups'}, which are not routed to any object.

Copy to clipboard

Another concept to introduce is **aliased metadata**. This is when an estimator requests a metadata with a different variable name than the default variable name. For instance, in a setting where there are two estimators in a pipeline, one could request `sample_weight1` and the other `sample_weight2`. Note that this doesn’t change what the estimator expects, it only tells the meta-estimator how to map the provided metadata to what is required. Here’s an example, where we pass `aliased_sample_weight` to the meta-estimator, but the meta-estimator understands that `aliased_sample_weight` is an alias for `sample_weight`, and passes it as `sample_weight` to the underlying estimator:

meta\_est \= MetaClassifier(
    estimator\=ExampleClassifier().set\_fit\_request(sample\_weight\="aliased\_sample\_weight")
)
meta\_est.fit(X, y, aliased\_sample\_weight\=my\_weights)

Copy to clipboard

Received sample\_weight of length = 100 in ExampleClassifier.

Copy to clipboard

MetaClassifier(estimator=ExampleClassifier())

**In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook.  
On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.**

MetaClassifier

iFitted

Parameters

|     |     |     |
| --- | --- | --- |
|     | estimator | ExampleClassifier() |

Fitted attributes

| Name | Type | Value |
| --- | --- | --- |
| classes\_ | ndarray\[int64\](2,) | \[0,1\] |
| estimator\_ | ExampleClassifier | ExampleClassifier() |

estimator: ExampleClassifier

ExampleClassifier()

ExampleClassifier

Parameters

  
  

Passing `sample_weight` here will fail since it is requested with an alias and `sample_weight` with that name is not requested:

try:
    meta\_est.fit(X, y, sample\_weight\=my\_weights)
except TypeError as e:
    print(e)

Copy to clipboard

MetaClassifier.fit got unexpected argument(s) {'sample\_weight'}, which are not routed to any object.

Copy to clipboard

This leads us to the `get_metadata_routing`. The way routing works in scikit-learn is that consumers request what they need, and routers pass that along. Additionally, a router exposes what it requires itself so that it can be used inside another router, e.g. a pipeline inside a grid search object. The output of the `get_metadata_routing` which is a dictionary representation of a [`MetadataRouter`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRouter.html#sklearn.utils.metadata_routing.MetadataRouter "sklearn.utils.metadata_routing.MetadataRouter")
, includes the complete tree of requested metadata by all nested objects and their corresponding method routings, i.e. which method of a sub-estimator is used in which method of a meta-estimator:

print\_routing(meta\_est)

Copy to clipboard

{'estimator': {'mapping': \[{'callee': 'fit', 'caller': 'fit'},\
                           {'callee': 'predict', 'caller': 'predict'},\
                           {'callee': 'score', 'caller': 'score'}\],
               'router': {'fit': {'sample\_weight': 'aliased\_sample\_weight'},
                          'predict': {'groups': None},
                          'score': {'sample\_weight': None}}}}

Copy to clipboard

As you can see, the only metadata requested for method `fit` is `"sample_weight"` with `"aliased_sample_weight"` as the alias. The `~utils.metadata_routing.MetadataRouter` class enables us to easily create the routing object which would create the output we need for our `get_metadata_routing`.

In order to understand how aliases work in meta-estimators, imagine our meta-estimator inside another one:

meta\_meta\_est \= MetaClassifier(estimator\=meta\_est).fit(
    X, y, aliased\_sample\_weight\=my\_weights
)

Copy to clipboard

Received sample\_weight of length = 100 in ExampleClassifier.

Copy to clipboard

In the above example, this is how the `fit` method of `meta_meta_est` will call their sub-estimator’s `fit` methods:

\# user feeds \`my\_weights\` as \`aliased\_sample\_weight\` into \`meta\_meta\_est\`:
meta\_meta\_est.fit(X, y, aliased\_sample\_weight\=my\_weights):
    ...

    \# the first sub-estimator (\`meta\_est\`) expects \`aliased\_sample\_weight\`
    self.estimator\_.fit(X, y, aliased\_sample\_weight\=aliased\_sample\_weight):
        ...

        \# the second sub-estimator (\`est\`) expects \`sample\_weight\`
        self.estimator\_.fit(X, y, sample\_weight\=aliased\_sample\_weight):
            ...

Copy to clipboard

Consuming and routing Meta-Estimator[#](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_metadata_routing.html#consuming-and-routing-meta-estimator "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

For a slightly more complex example, consider a meta-estimator that routes metadata to an underlying estimator as before, but it also uses some metadata in its own methods. This meta-estimator is a consumer and a router at the same time. Implementing one is very similar to what we had before, but with a few tweaks.

class RouterConsumerClassifier([MetaEstimatorMixin](https://scikit-learn.org/stable/modules/generated/sklearn.base.MetaEstimatorMixin.html#sklearn.base.MetaEstimatorMixin "sklearn.base.MetaEstimatorMixin")
, [ClassifierMixin](https://scikit-learn.org/stable/modules/generated/sklearn.base.ClassifierMixin.html#sklearn.base.ClassifierMixin "sklearn.base.ClassifierMixin")
, [BaseEstimator](https://scikit-learn.org/stable/modules/generated/sklearn.base.BaseEstimator.html#sklearn.base.BaseEstimator "sklearn.base.BaseEstimator")
):
    def \_\_init\_\_(self, estimator):
        self.estimator \= estimator

    def get\_metadata\_routing(self):
        router \= (
            [MetadataRouter](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRouter.html#sklearn.utils.metadata_routing.MetadataRouter "sklearn.utils.metadata_routing.MetadataRouter")
(owner\=self)
            \# defining metadata routing request values for usage in the meta-estimator
            .add\_self\_request(self)
            \# defining metadata routing request values for usage in the sub-estimator
            .add(
                estimator\=self.estimator,
                method\_mapping\=[MethodMapping](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MethodMapping.html#sklearn.utils.metadata_routing.MethodMapping "sklearn.utils.metadata_routing.MethodMapping")
()
                .add(caller\="fit", callee\="fit")
                .add(caller\="predict", callee\="predict")
                .add(caller\="score", callee\="score"),
            )
        )
        return router

    \# Since \`sample\_weight\` is used and consumed here, it should be defined as
    \# an explicit argument in the method's signature. All other metadata which
    \# are only routed, will be passed as \`\*\*fit\_params\`:
    def fit(self, X, y, sample\_weight, \*\*fit\_params):
        if self.estimator is None:
            raise ValueError("estimator cannot be None!")

        check\_metadata(self, sample\_weight\=sample\_weight)

        \# We add \`sample\_weight\` to the \`fit\_params\` dictionary.
        if sample\_weight is not None:
            fit\_params\["sample\_weight"\] \= sample\_weight
        routed\_params \= [process\_routing](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.process_routing.html#sklearn.utils.metadata_routing.process_routing "sklearn.utils.metadata_routing.process_routing")
(self, "fit", \*\*fit\_params)
        self.estimator\_ \= clone(self.estimator).fit(
            X, y, \*\*routed\_params\["estimator"\]\["fit"\]
        )
        self.classes\_ \= self.estimator\_.classes\_
        return self

    def predict(self, X, \*\*predict\_params):
        [check\_is\_fitted](https://scikit-learn.org/stable/modules/generated/sklearn.utils.validation.check_is_fitted.html#sklearn.utils.validation.check_is_fitted "sklearn.utils.validation.check_is_fitted")
(self)
        routed\_params \= [process\_routing](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.process_routing.html#sklearn.utils.metadata_routing.process_routing "sklearn.utils.metadata_routing.process_routing")
(self, "predict", \*\*predict\_params)
        return self.estimator\_.predict(X, \*\*routed\_params\["estimator"\]\["predict"\])

Copy to clipboard

The key parts where the above meta-estimator differs from our previous meta-estimator is accepting `sample_weight` explicitly in `fit` and including it in `fit_params`. Since `sample_weight` is an explicit argument, we can be sure that `set_fit_request(sample_weight=...)` is present for this method. The meta-estimator is both a consumer, as well as a router of `sample_weight`.

In `get_metadata_routing`, we add `self` to the routing using `add_self_request` to indicate this estimator is consuming `sample_weight` as well as being a router; which also adds a `$self_request` key to the routing info as illustrated below. Now let’s look at some examples:

*   No metadata requested
    

meta\_est \= RouterConsumerClassifier(estimator\=ExampleClassifier())
print\_routing(meta\_est)

Copy to clipboard

{'$self\_request': {'fit': {'sample\_weight': None},
                   'score': {'sample\_weight': None}},
 'estimator': {'mapping': \[{'callee': 'fit', 'caller': 'fit'},\
                           {'callee': 'predict', 'caller': 'predict'},\
                           {'callee': 'score', 'caller': 'score'}\],
               'router': {'fit': {'sample\_weight': None},
                          'predict': {'groups': None},
                          'score': {'sample\_weight': None}}}}

Copy to clipboard

*   `sample_weight` requested by sub-estimator
    

meta\_est \= RouterConsumerClassifier(
    estimator\=ExampleClassifier().set\_fit\_request(sample\_weight\=True)
)
print\_routing(meta\_est)

Copy to clipboard

{'$self\_request': {'fit': {'sample\_weight': None},
                   'score': {'sample\_weight': None}},
 'estimator': {'mapping': \[{'callee': 'fit', 'caller': 'fit'},\
                           {'callee': 'predict', 'caller': 'predict'},\
                           {'callee': 'score', 'caller': 'score'}\],
               'router': {'fit': {'sample\_weight': True},
                          'predict': {'groups': None},
                          'score': {'sample\_weight': None}}}}

Copy to clipboard

*   `sample_weight` requested by meta-estimator
    

meta\_est \= RouterConsumerClassifier(estimator\=ExampleClassifier()).set\_fit\_request(
    sample\_weight\=True
)
print\_routing(meta\_est)

Copy to clipboard

{'$self\_request': {'fit': {'sample\_weight': True},
                   'score': {'sample\_weight': None}},
 'estimator': {'mapping': \[{'callee': 'fit', 'caller': 'fit'},\
                           {'callee': 'predict', 'caller': 'predict'},\
                           {'callee': 'score', 'caller': 'score'}\],
               'router': {'fit': {'sample\_weight': None},
                          'predict': {'groups': None},
                          'score': {'sample\_weight': None}}}}

Copy to clipboard

Note the difference in the requested metadata representations above.

*   We can also alias the metadata to pass different values to the fit methods of the meta- and the sub-estimator:
    

meta\_est \= RouterConsumerClassifier(
    estimator\=ExampleClassifier().set\_fit\_request(sample\_weight\="clf\_sample\_weight"),
).set\_fit\_request(sample\_weight\="meta\_clf\_sample\_weight")
print\_routing(meta\_est)

Copy to clipboard

{'$self\_request': {'fit': {'sample\_weight': 'meta\_clf\_sample\_weight'},
                   'score': {'sample\_weight': None}},
 'estimator': {'mapping': \[{'callee': 'fit', 'caller': 'fit'},\
                           {'callee': 'predict', 'caller': 'predict'},\
                           {'callee': 'score', 'caller': 'score'}\],
               'router': {'fit': {'sample\_weight': 'clf\_sample\_weight'},
                          'predict': {'groups': None},
                          'score': {'sample\_weight': None}}}}

Copy to clipboard

However, `fit` of the meta-estimator only needs the alias for the sub-estimator and addresses their own sample weight as `sample_weight`, since it doesn’t validate and route its own required metadata:

meta\_est.fit(X, y, sample\_weight\=my\_weights, clf\_sample\_weight\=my\_other\_weights)

Copy to clipboard

Received sample\_weight of length = 100 in RouterConsumerClassifier.
Received sample\_weight of length = 100 in ExampleClassifier.

Copy to clipboard

RouterConsumerClassifier(estimator=ExampleClassifier())

**In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook.  
On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.**

RouterConsumerClassifier

iFitted

Parameters

|     |     |     |
| --- | --- | --- |
|     | estimator | ExampleClassifier() |

Fitted attributes

| Name | Type | Value |
| --- | --- | --- |
| classes\_ | ndarray\[int64\](2,) | \[0,1\] |
| estimator\_ | ExampleClassifier | ExampleClassifier() |

estimator: ExampleClassifier

ExampleClassifier()

ExampleClassifier

Parameters

  
  

*   Alias only on the sub-estimator:
    

This is useful when we don’t want the meta-estimator to use the metadata, but the sub-estimator should.

meta\_est \= RouterConsumerClassifier(
    estimator\=ExampleClassifier().set\_fit\_request(sample\_weight\="aliased\_sample\_weight")
)
print\_routing(meta\_est)

Copy to clipboard

{'$self\_request': {'fit': {'sample\_weight': None},
                   'score': {'sample\_weight': None}},
 'estimator': {'mapping': \[{'callee': 'fit', 'caller': 'fit'},\
                           {'callee': 'predict', 'caller': 'predict'},\
                           {'callee': 'score', 'caller': 'score'}\],
               'router': {'fit': {'sample\_weight': 'aliased\_sample\_weight'},
                          'predict': {'groups': None},
                          'score': {'sample\_weight': None}}}}

Copy to clipboard

The meta-estimator cannot use `aliased_sample_weight`, because it expects it passed as `sample_weight`. This would apply even if `set_fit_request(sample_weight=True)` was set on it.

Simple Pipeline[#](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_metadata_routing.html#simple-pipeline "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------

A slightly more complicated use-case is a meta-estimator resembling a [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
. Here is a meta-estimator, which accepts a transformer and a classifier. When calling its `fit` method, it applies the transformer’s `fit` and `transform` before running the classifier on the transformed data. Upon `predict`, it applies the transformer’s `transform` before predicting with the classifier’s `predict` method on the transformed new data.

class SimplePipeline([ClassifierMixin](https://scikit-learn.org/stable/modules/generated/sklearn.base.ClassifierMixin.html#sklearn.base.ClassifierMixin "sklearn.base.ClassifierMixin")
, [BaseEstimator](https://scikit-learn.org/stable/modules/generated/sklearn.base.BaseEstimator.html#sklearn.base.BaseEstimator "sklearn.base.BaseEstimator")
):
    def \_\_init\_\_(self, transformer, classifier):
        self.transformer \= transformer
        self.classifier \= classifier

    def get\_metadata\_routing(self):
        router \= (
            [MetadataRouter](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRouter.html#sklearn.utils.metadata_routing.MetadataRouter "sklearn.utils.metadata_routing.MetadataRouter")
(owner\=self)
            \# We add the routing for the transformer.
            .add(
                transformer\=self.transformer,
                method\_mapping\=[MethodMapping](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MethodMapping.html#sklearn.utils.metadata_routing.MethodMapping "sklearn.utils.metadata_routing.MethodMapping")
()
                \# The metadata is routed such that it retraces how
                \# \`SimplePipeline\` internally calls the transformer's \`fit\` and
                \# \`transform\` methods in its own methods (\`fit\` and \`predict\`).
                .add(caller\="fit", callee\="fit")
                .add(caller\="fit", callee\="transform")
                .add(caller\="predict", callee\="transform"),
            )
            \# We add the routing for the classifier.
            .add(
                classifier\=self.classifier,
                method\_mapping\=[MethodMapping](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MethodMapping.html#sklearn.utils.metadata_routing.MethodMapping "sklearn.utils.metadata_routing.MethodMapping")
()
                .add(caller\="fit", callee\="fit")
                .add(caller\="predict", callee\="predict"),
            )
        )
        return router

    def fit(self, X, y, \*\*fit\_params):
        routed\_params \= [process\_routing](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.process_routing.html#sklearn.utils.metadata_routing.process_routing "sklearn.utils.metadata_routing.process_routing")
(self, "fit", \*\*fit\_params)

        self.transformer\_ \= clone(self.transformer).fit(
            X, y, \*\*routed\_params\["transformer"\]\["fit"\]
        )
        X\_transformed \= self.transformer\_.transform(
            X, \*\*routed\_params\["transformer"\]\["transform"\]
        )

        self.classifier\_ \= clone(self.classifier).fit(
            X\_transformed, y, \*\*routed\_params\["classifier"\]\["fit"\]
        )
        return self

    def predict(self, X, \*\*predict\_params):
        routed\_params \= [process\_routing](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.process_routing.html#sklearn.utils.metadata_routing.process_routing "sklearn.utils.metadata_routing.process_routing")
(self, "predict", \*\*predict\_params)

        X\_transformed \= self.transformer\_.transform(
            X, \*\*routed\_params\["transformer"\]\["transform"\]
        )
        return self.classifier\_.predict(
            X\_transformed, \*\*routed\_params\["classifier"\]\["predict"\]
        )

Copy to clipboard

Note the usage of [`MethodMapping`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MethodMapping.html#sklearn.utils.metadata_routing.MethodMapping "sklearn.utils.metadata_routing.MethodMapping")
 to declare which methods of the child estimator (callee) are used in which methods of the meta estimator (caller). As you can see, `SimplePipeline` uses the transformer’s `transform` and `fit` methods in `fit`, and its `transform` method in `predict`, and that’s what you see implemented in the routing structure of the pipeline class.

Another difference in the above example with the previous ones is the usage of [`process_routing`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.process_routing.html#sklearn.utils.metadata_routing.process_routing "sklearn.utils.metadata_routing.process_routing")
, which processes the input parameters, does the required validation, and returns the `routed_params` which we had created in previous examples. This reduces the boilerplate code a developer needs to write in each meta-estimator’s method. Developers are strongly recommended to use this function unless there is a good reason against it.

In order to test the above pipeline, let’s add an example transformer.

class ExampleTransformer([TransformerMixin](https://scikit-learn.org/stable/modules/generated/sklearn.base.TransformerMixin.html#sklearn.base.TransformerMixin "sklearn.base.TransformerMixin")
, [BaseEstimator](https://scikit-learn.org/stable/modules/generated/sklearn.base.BaseEstimator.html#sklearn.base.BaseEstimator "sklearn.base.BaseEstimator")
):
    def fit(self, X, y, sample\_weight\=None):
        check\_metadata(self, sample\_weight\=sample\_weight)
        return self

    def transform(self, X, groups\=None):
        check\_metadata(self, groups\=groups)
        return X

    def fit\_transform(self, X, y, sample\_weight\=None, groups\=None):
        return self.fit(X, y, sample\_weight).transform(X, groups)

Copy to clipboard

Note that in the above example, we have implemented `fit_transform` which calls `fit` and `transform` with the appropriate metadata. This is only required if `transform` accepts metadata, since the default `fit_transform` implementation in [`TransformerMixin`](https://scikit-learn.org/stable/modules/generated/sklearn.base.TransformerMixin.html#sklearn.base.TransformerMixin "sklearn.base.TransformerMixin")
 doesn’t pass metadata to `transform`.

Now we can test our pipeline, and see if metadata is correctly passed around. This example uses our `SimplePipeline`, our `ExampleTransformer`, and our `RouterConsumerClassifier` which uses our `ExampleClassifier`.

pipe \= SimplePipeline(
    transformer\=ExampleTransformer()
    \# we set transformer's fit to receive sample\_weight
    .set\_fit\_request(sample\_weight\=True)
    \# we set transformer's transform to receive groups
    .set\_transform\_request(groups\=True),
    classifier\=RouterConsumerClassifier(
        estimator\=ExampleClassifier()
        \# we want this sub-estimator to receive sample\_weight in fit
        .set\_fit\_request(sample\_weight\=True)
        \# but not groups in predict
        .set\_predict\_request(groups\=False),
    )
    \# and we want the meta-estimator to receive sample\_weight as well
    .set\_fit\_request(sample\_weight\=True),
)
pipe.fit(X, y, sample\_weight\=my\_weights, groups\=my\_groups).predict(
    X\[:3\], groups\=my\_groups
)

Copy to clipboard

Received sample\_weight of length = 100 in ExampleTransformer.
Received groups of length = 100 in ExampleTransformer.
Received sample\_weight of length = 100 in RouterConsumerClassifier.
Received sample\_weight of length = 100 in ExampleClassifier.
Received groups of length = 100 in ExampleTransformer.
groups is None in ExampleClassifier.

array(\[1., 1., 1.\])

Copy to clipboard

Deprecation / Default Value Change[#](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_metadata_routing.html#deprecation-default-value-change "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

In this section we show how one should handle the case where a router becomes also a consumer, especially when it consumes the same metadata as its sub-estimator, or a consumer starts consuming a metadata which it wasn’t in an older release. In this case, a warning should be raised for a while, to let users know the behavior is changed from previous versions.

class MetaRegressor([MetaEstimatorMixin](https://scikit-learn.org/stable/modules/generated/sklearn.base.MetaEstimatorMixin.html#sklearn.base.MetaEstimatorMixin "sklearn.base.MetaEstimatorMixin")
, [RegressorMixin](https://scikit-learn.org/stable/modules/generated/sklearn.base.RegressorMixin.html#sklearn.base.RegressorMixin "sklearn.base.RegressorMixin")
, [BaseEstimator](https://scikit-learn.org/stable/modules/generated/sklearn.base.BaseEstimator.html#sklearn.base.BaseEstimator "sklearn.base.BaseEstimator")
):
    def \_\_init\_\_(self, estimator):
        self.estimator \= estimator

    def fit(self, X, y, \*\*fit\_params):
        routed\_params \= [process\_routing](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.process_routing.html#sklearn.utils.metadata_routing.process_routing "sklearn.utils.metadata_routing.process_routing")
(self, "fit", \*\*fit\_params)
        self.estimator\_ \= clone(self.estimator).fit(
            X, y, \*\*routed\_params\["estimator"\]\["fit"\]
        )

    def get\_metadata\_routing(self):
        router \= [MetadataRouter](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRouter.html#sklearn.utils.metadata_routing.MetadataRouter "sklearn.utils.metadata_routing.MetadataRouter")
(owner\=self).add(
            estimator\=self.estimator,
            method\_mapping\=[MethodMapping](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MethodMapping.html#sklearn.utils.metadata_routing.MethodMapping "sklearn.utils.metadata_routing.MethodMapping")
().add(caller\="fit", callee\="fit"),
        )
        return router

Copy to clipboard

As explained above, this is a valid usage if `my_weights` aren’t supposed to be passed as `sample_weight` to `MetaRegressor`:

reg \= MetaRegressor(estimator\=[LinearRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html#sklearn.linear_model.LinearRegression "sklearn.linear_model.LinearRegression")
().set\_fit\_request(sample\_weight\=True))
reg.fit(X, y, sample\_weight\=my\_weights)

Copy to clipboard

Now imagine we further develop `MetaRegressor` and it now also _consumes_ `sample_weight`:

class WeightedMetaRegressor([MetaEstimatorMixin](https://scikit-learn.org/stable/modules/generated/sklearn.base.MetaEstimatorMixin.html#sklearn.base.MetaEstimatorMixin "sklearn.base.MetaEstimatorMixin")
, [RegressorMixin](https://scikit-learn.org/stable/modules/generated/sklearn.base.RegressorMixin.html#sklearn.base.RegressorMixin "sklearn.base.RegressorMixin")
, [BaseEstimator](https://scikit-learn.org/stable/modules/generated/sklearn.base.BaseEstimator.html#sklearn.base.BaseEstimator "sklearn.base.BaseEstimator")
):
    \# show warning to remind user to explicitly set the value with
    \# \`.set\_{method}\_request(sample\_weight={boolean})\`
    \_\_metadata\_request\_\_fit \= {"sample\_weight": metadata\_routing.WARN}

    def \_\_init\_\_(self, estimator):
        self.estimator \= estimator

    def fit(self, X, y, sample\_weight\=None, \*\*fit\_params):
        routed\_params \= [process\_routing](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.process_routing.html#sklearn.utils.metadata_routing.process_routing "sklearn.utils.metadata_routing.process_routing")
(
            self, "fit", sample\_weight\=sample\_weight, \*\*fit\_params
        )
        check\_metadata(self, sample\_weight\=sample\_weight)
        self.estimator\_ \= clone(self.estimator).fit(
            X, y, \*\*routed\_params\["estimator"\]\["fit"\]
        )

    def get\_metadata\_routing(self):
        router \= (
            [MetadataRouter](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRouter.html#sklearn.utils.metadata_routing.MetadataRouter "sklearn.utils.metadata_routing.MetadataRouter")
(owner\=self)
            .add\_self\_request(self)
            .add(
                estimator\=self.estimator,
                method\_mapping\=[MethodMapping](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MethodMapping.html#sklearn.utils.metadata_routing.MethodMapping "sklearn.utils.metadata_routing.MethodMapping")
().add(caller\="fit", callee\="fit"),
            )
        )
        return router

Copy to clipboard

The above implementation is almost the same as `MetaRegressor`, and because of the default request value defined in `__metadata_request__fit` there is a warning raised when fitted.

with [warnings.catch\_warnings](https://docs.python.org/3/library/warnings.html#warnings.catch_warnings "warnings.catch_warnings")
(record\=True) as record:
    WeightedMetaRegressor(
        estimator\=[LinearRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html#sklearn.linear_model.LinearRegression "sklearn.linear_model.LinearRegression")
().set\_fit\_request(sample\_weight\=False)
    ).fit(X, y, sample\_weight\=my\_weights)
for w in record:
    print(w.message)

Copy to clipboard

Received sample\_weight of length = 100 in WeightedMetaRegressor.
Support for sample\_weight has recently been added to WeightedMetaRegressor(estimator=LinearRegression()) class. To maintain backward compatibility, it is ignored now. Using \`set\_fit\_request(sample\_weight={True, False})\` on this method of the class, you can set the request value to False to silence this warning, or to True to consume and use the metadata.

Copy to clipboard

When an estimator consumes a metadata which it didn’t consume before, the following pattern can be used to warn the users about it.

class ExampleRegressor([RegressorMixin](https://scikit-learn.org/stable/modules/generated/sklearn.base.RegressorMixin.html#sklearn.base.RegressorMixin "sklearn.base.RegressorMixin")
, [BaseEstimator](https://scikit-learn.org/stable/modules/generated/sklearn.base.BaseEstimator.html#sklearn.base.BaseEstimator "sklearn.base.BaseEstimator")
):
    \_\_metadata\_request\_\_fit \= {"sample\_weight": metadata\_routing.WARN}

    def fit(self, X, y, sample\_weight\=None):
        check\_metadata(self, sample\_weight\=sample\_weight)
        return self

    def predict(self, X):
        return [np.zeros](https://numpy.org/doc/stable/reference/generated/numpy.zeros.html#numpy.zeros "numpy.zeros")
(shape\=(len(X)))

with [warnings.catch\_warnings](https://docs.python.org/3/library/warnings.html#warnings.catch_warnings "warnings.catch_warnings")
(record\=True) as record:
    MetaRegressor(estimator\=ExampleRegressor()).fit(X, y, sample\_weight\=my\_weights)
for w in record:
    print(w.message)

Copy to clipboard

sample\_weight is None in ExampleRegressor.
Support for sample\_weight has recently been added to ExampleRegressor() class. To maintain backward compatibility, it is ignored now. Using \`set\_fit\_request(sample\_weight={True, False})\` on this method of the class, you can set the request value to False to silence this warning, or to True to consume and use the metadata.

Copy to clipboard

At the end we disable the configuration flag for metadata routing:

[set\_config](https://scikit-learn.org/stable/modules/generated/sklearn.set_config.html#sklearn.set_config "sklearn.set_config")
(enable\_metadata\_routing\=False)

Copy to clipboard

Third Party Development and scikit-learn Dependency[#](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_metadata_routing.html#third-party-development-and-scikit-learn-dependency "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

As seen above, information is communicated between classes using [`MetadataRequest`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRequest.html#sklearn.utils.metadata_routing.MetadataRequest "sklearn.utils.metadata_routing.MetadataRequest")
 and [`MetadataRouter`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRouter.html#sklearn.utils.metadata_routing.MetadataRouter "sklearn.utils.metadata_routing.MetadataRouter")
. It is strongly not advised, but possible to vendor the tools related to metadata-routing if you strictly want to have a scikit-learn compatible estimator, without depending on the scikit-learn package. If all of the following conditions are met, you do NOT need to modify your code at all:

*   your estimator inherits from [`BaseEstimator`](https://scikit-learn.org/stable/modules/generated/sklearn.base.BaseEstimator.html#sklearn.base.BaseEstimator "sklearn.base.BaseEstimator")
    
*   the parameters consumed by your estimator’s methods, e.g. `fit`, are explicitly defined in the method’s signature, as opposed to being `*args` or `*kwargs`.
    
*   your estimator does not route any metadata to the underlying objects, i.e. it’s not a _router_.
    

**Total running time of the script:** (0 minutes 0.040 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo21.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/miscellaneous/plot_metadata_routing.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo21.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/miscellaneous/plot_metadata_routing.ipynb)

[`Download Jupyter notebook: plot_metadata_routing.ipynb`](https://scikit-learn.org/stable/_downloads/64a4ce2171987c74f955483a03ac45b5/plot_metadata_routing.ipynb)

[`Download Python source code: plot_metadata_routing.py`](https://scikit-learn.org/stable/_downloads/35686e86ab04c9899b73acd07be52bc7/plot_metadata_routing.py)

[`Download zipped: plot_metadata_routing.zip`](https://scikit-learn.org/stable/_downloads/dfc0bb239d89efaffb5847c5579be995/plot_metadata_routing.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_elastic_net_precomputed_gram_matrix_with_weighted_samples_thumb.png)

[Fitting an Elastic Net with a precomputed Gram Matrix and Weighted Samples](https://scikit-learn.org/stable/auto_examples/linear_model/plot_elastic_net_precomputed_gram_matrix_with_weighted_samples.html)

Fitting an Elastic Net with a precomputed Gram Matrix and Weighted Samples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_1_4_0_thumb.png)

[Release Highlights for scikit-learn 1.4](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_4_0.html)

Release Highlights for scikit-learn 1.4

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_sgd_weighted_samples_thumb.png)

[SGD: Weighted samples](https://scikit-learn.org/stable/auto_examples/linear_model/plot_sgd_weighted_samples.html)

SGD: Weighted samples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_weighted_samples_thumb.png)

[SVM: Weighted samples](https://scikit-learn.org/stable/auto_examples/svm/plot_weighted_samples.html)

SVM: Weighted samples

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page

[Download source code](https://scikit-learn.org/stable/_downloads/35686e86ab04c9899b73acd07be52bc7/plot_metadata_routing.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/64a4ce2171987c74f955483a03ac45b5/plot_metadata_routing.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/dfc0bb239d89efaffb5847c5579be995/plot_metadata_routing.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo21.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/miscellaneous/plot_metadata_routing.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo21.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/miscellaneous/plot_metadata_routing.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)