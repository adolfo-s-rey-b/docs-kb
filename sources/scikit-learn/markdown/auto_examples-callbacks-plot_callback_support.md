[Skip to main content](https://scikit-learn.org/stable/auto_examples/callbacks/plot_callback_support.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/callbacks/plot_callback_support.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/callbacks/plot_callback_support.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/callbacks/plot_callback_support.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/callbacks/plot_callback_support.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/callbacks/plot_callback_support.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/callbacks/plot_callback_support.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/callbacks/plot_callback_support.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/callbacks/plot_callback_support.html#sphx-glr-download-auto-examples-callbacks-plot-callback-support-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Supporting callbacks in third party estimators[#](https://scikit-learn.org/stable/auto_examples/callbacks/plot_callback_support.html#supporting-callbacks-in-third-party-estimators "Link to this heading")

============================================================================================================================================================================================================

This document shows how to make third party [estimators](https://scikit-learn.org/stable/glossary.html#term-estimators)
 and [meta-estimators](https://scikit-learn.org/stable/glossary.html#term-meta-estimators)
 compatible with the callback infrastructure supported by scikit-learn.

Generally speaking, a callback is a function that is provided by the user to be called at specific steps of a process, or to be triggered by specific events. Callbacks provide a clean mechanism for inserting custom logic like monitoring progress or metrics, without modifying the core algorithm of the process.

In scikit-learn, callbacks take the form of classes following a [protocol](https://typing.python.org/en/latest/spec/protocol.html)
. This protocol requires the callback classes to implement specific methods (referred to as callback hooks) which are called at specific steps of the fitting of an estimator or a meta-estimator. These hooks are [`setup`](https://scikit-learn.org/stable/modules/generated/sklearn.callback.FitCallback.html#sklearn.callback.FitCallback.setup "sklearn.callback.FitCallback.setup")
, [`on_fit_task_begin`](https://scikit-learn.org/stable/modules/generated/sklearn.callback.FitCallback.html#sklearn.callback.FitCallback.on_fit_task_begin "sklearn.callback.FitCallback.on_fit_task_begin")
, [`on_fit_task_end`](https://scikit-learn.org/stable/modules/generated/sklearn.callback.FitCallback.html#sklearn.callback.FitCallback.on_fit_task_end "sklearn.callback.FitCallback.on_fit_task_end")
 and [`teardown`](https://scikit-learn.org/stable/modules/generated/sklearn.callback.FitCallback.html#sklearn.callback.FitCallback.teardown "sklearn.callback.FitCallback.teardown")
. The [`setup`](https://scikit-learn.org/stable/modules/generated/sklearn.callback.FitCallback.html#sklearn.callback.FitCallback.setup "sklearn.callback.FitCallback.setup")
 and [`teardown`](https://scikit-learn.org/stable/modules/generated/sklearn.callback.FitCallback.html#sklearn.callback.FitCallback.teardown "sklearn.callback.FitCallback.teardown")
 hooks are called only once, respectively at the start and end of the estimator’s [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
 method, and are responsible for setting up and shutting down the callback. The [`on_fit_task_begin`](https://scikit-learn.org/stable/modules/generated/sklearn.callback.FitCallback.html#sklearn.callback.FitCallback.on_fit_task_begin "sklearn.callback.FitCallback.on_fit_task_begin")
 and [`on_fit_task_end`](https://scikit-learn.org/stable/modules/generated/sklearn.callback.FitCallback.html#sklearn.callback.FitCallback.on_fit_task_end "sklearn.callback.FitCallback.on_fit_task_end")
 hooks are respectively called at the beginning and end of each task in `fit` and are responsible for the actual callback work. In scikit-learn estimators, a task in `fit` is usually one step of a loop, with nested loops corresponding to nested tasks. In general, a task can be whatever unit of work the estimator’s developer wants it to be.

In order to support the callbacks, estimators need to initialize and manage [`CallbackContext`](https://scikit-learn.org/stable/modules/generated/sklearn.callback.CallbackContext.html#sklearn.callback.CallbackContext "sklearn.callback.CallbackContext")
 objects. As the name implies, these objects hold the contextual information necessary to run the callback hooks. They are also responsible for calling the callback hooks at the right time.

In the following, we show how to convert an example estimator class and an example meta-estimator class to make them compliant with the scikit-learn callback infrastructure.

First a few imports and some random data for the rest of the script.

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

Copy to clipboard

import numpy as np

from sklearn.base import [BaseEstimator](https://scikit-learn.org/stable/modules/generated/sklearn.base.BaseEstimator.html#sklearn.base.BaseEstimator "sklearn.base.BaseEstimator")
, clone
from sklearn.callback import [CallbackSupportMixin](https://scikit-learn.org/stable/modules/generated/sklearn.callback.CallbackSupportMixin.html#sklearn.callback.CallbackSupportMixin "sklearn.callback.CallbackSupportMixin")
, [ProgressBar](https://scikit-learn.org/stable/modules/generated/sklearn.callback.ProgressBar.html#sklearn.callback.ProgressBar "sklearn.callback.ProgressBar")
, [with\_callbacks](https://scikit-learn.org/stable/modules/generated/sklearn.callback.with_callbacks.html#sklearn.callback.with_callbacks "sklearn.callback.with_callbacks")
from sklearn.metrics.pairwise import euclidean\_distances
from sklearn.model\_selection import [check\_cv](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.check_cv.html#sklearn.model_selection.check_cv "sklearn.model_selection.check_cv")
from sklearn.utils import [check\_random\_state](https://scikit-learn.org/stable/modules/generated/sklearn.utils.check_random_state.html#sklearn.utils.check_random_state "sklearn.utils.check_random_state")
from sklearn.utils.parallel import [Parallel](https://scikit-learn.org/stable/modules/generated/sklearn.utils.parallel.Parallel.html#sklearn.utils.parallel.Parallel "sklearn.utils.parallel.Parallel")
, [delayed](https://scikit-learn.org/stable/modules/generated/sklearn.utils.parallel.delayed.html#sklearn.utils.parallel.delayed "sklearn.utils.parallel.delayed")
from sklearn.utils.validation import [check\_is\_fitted](https://scikit-learn.org/stable/modules/generated/sklearn.utils.validation.check_is_fitted.html#sklearn.utils.validation.check_is_fitted "sklearn.utils.validation.check_is_fitted")
, [validate\_data](https://scikit-learn.org/stable/modules/generated/sklearn.utils.validation.validate_data.html#sklearn.utils.validation.validate_data "sklearn.utils.validation.validate_data")

n\_samples, n\_features \= 100, 4
rng \= [np.random.RandomState](https://numpy.org/doc/stable/reference/random/legacy.html#numpy.random.RandomState "numpy.random.RandomState")
(42)
X \= rng.rand(n\_samples, n\_features)

Copy to clipboard

Custom Estimator[#](https://scikit-learn.org/stable/auto_examples/callbacks/plot_callback_support.html#custom-estimator "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------

Here we demonstrate how to implement a custom estimator that supports callbacks. For the example, a simplified version of KMeans is presented. First, let’s implement our `SimpleKMeans` estimator without the callback support.

class SimpleKMeans([BaseEstimator](https://scikit-learn.org/stable/modules/generated/sklearn.base.BaseEstimator.html#sklearn.base.BaseEstimator "sklearn.base.BaseEstimator")
):
    def \_\_init\_\_(self, n\_clusters\=6, n\_iter\=100, random\_state\=None):
        self.n\_clusters \= n\_clusters
        self.n\_iter \= n\_iter
        self.random\_state \= random\_state  \# controls the centroids' initialization

    def \_compute\_labels(self, X):
        \# Get the index of the closest centroid for each point in X.
        return [np.argmin](https://numpy.org/doc/stable/reference/generated/numpy.argmin.html#numpy.argmin "numpy.argmin")
(euclidean\_distances(X, self.cluster\_centers\_), axis\=1)

    def fit(self, X, y\=None):
        \# \`y\` is not used but we need to declare it to adhere to scikit-learn's
        \# estimators fit convention.

        \# Input validation is a good practice in estimators, for more information about
        \# it you can refer to
        \# https://scikit-learn.org/stable/developers/develop.html#input-validation.
        X \= [validate\_data](https://scikit-learn.org/stable/modules/generated/sklearn.utils.validation.validate_data.html#sklearn.utils.validation.validate_data "sklearn.utils.validation.validate_data")
(self, X)
        random\_state \= [check\_random\_state](https://scikit-learn.org/stable/modules/generated/sklearn.utils.check_random_state.html#sklearn.utils.check_random_state "sklearn.utils.check_random_state")
(self.random\_state)
        \# Randomly initialize the centroids.
        self.cluster\_centers\_ \= random\_state.rand(self.n\_clusters, X.shape\[1\])

        for i in range(self.n\_iter):
            \# The fit iterations consist in getting the cluster label of each data point
            \# according to their closest centroid, and then updating the centroids as
            \# the center of each cluster.
            labels \= self.\_compute\_labels(X)

            for k in range(self.n\_clusters):
                \# For each centroid, if its cluster is not empty, its coordinates are
                \# updated with the coordinates of the cluster's center.
                if (labels \== k).any():
                    self.cluster\_centers\_\[k\] \= X\[labels \== k\].mean(axis\=0)

        return self

    def predict(self, X):
        [check\_is\_fitted](https://scikit-learn.org/stable/modules/generated/sklearn.utils.validation.check_is_fitted.html#sklearn.utils.validation.check_is_fitted "sklearn.utils.validation.check_is_fitted")
(self)
        return self.\_compute\_labels(X)

    def transform(self, X):
        [check\_is\_fitted](https://scikit-learn.org/stable/modules/generated/sklearn.utils.validation.check_is_fitted.html#sklearn.utils.validation.check_is_fitted "sklearn.utils.validation.check_is_fitted")
(self)
        return euclidean\_distances(X, self.cluster\_centers\_)

Copy to clipboard

Now let’s add all the elements necessary to support callbacks.

\# First things first, the estimator must inherit from the \`CallbackSupportMixin\` class.
class SimpleKMeans([CallbackSupportMixin](https://scikit-learn.org/stable/modules/generated/sklearn.callback.CallbackSupportMixin.html#sklearn.callback.CallbackSupportMixin "sklearn.callback.CallbackSupportMixin")
, [BaseEstimator](https://scikit-learn.org/stable/modules/generated/sklearn.base.BaseEstimator.html#sklearn.base.BaseEstimator "sklearn.base.BaseEstimator")
):  \# noqa: F811
    def \_\_init\_\_(self, n\_clusters\=6, n\_iter\=100, random\_state\=None):
        self.n\_clusters \= n\_clusters
        self.n\_iter \= n\_iter
        self.random\_state \= random\_state

    def \_compute\_labels(self, X):
        return [np.argmin](https://numpy.org/doc/stable/reference/generated/numpy.argmin.html#numpy.argmin "numpy.argmin")
(euclidean\_distances(X, self.cluster\_centers\_), axis\=1)

    \# Then the \`fit\` function must be decorated with the \`with\_callbacks\`
    \# decorator, which takes care of the proper teardown of callbacks.
    @with\_callbacks
    def fit(self, X, y\=None):
        X \= [validate\_data](https://scikit-learn.org/stable/modules/generated/sklearn.utils.validation.validate_data.html#sklearn.utils.validation.validate_data "sklearn.utils.validation.validate_data")
(self, X)
        random\_state \= [check\_random\_state](https://scikit-learn.org/stable/modules/generated/sklearn.utils.check_random_state.html#sklearn.utils.check_random_state "sklearn.utils.check_random_state")
(self.random\_state)
        \# The \`CallbackContext\` object must be instantiated with the
        \# \`\_init\_callback\_context\` method provided by the mixin, which calls the
        \# \`setup\` hooks of the callbacks. This context corresponds to the root task of
        \# the fit function.
        callback\_ctx \= self.\_init\_callback\_context(
            task\_name\="fit", max\_subtasks\=self.n\_iter
        )
        \# Then the callback context's \`call\_on\_fit\_task\_begin\` method must be called. It
        \# will call all the callbacks' \`on\_fit\_task\_begin\` hooks. The \`estimator\`
        \# argument is mandatory and optional \`kwargs\` can be passed to provide extra
        \# contextual information for the callbacks, for example here \`X\` and \`y\` are
        \# passed. See the following note for more details on these extra \`kwargs\`.
        callback\_ctx.call\_on\_fit\_task\_begin(estimator\=self, X\=X, y\=y)

        self.cluster\_centers\_ \= random\_state.rand(self.n\_clusters, X.shape\[1\])

        for i in range(self.n\_iter):
            \# For each sub-task of fit (here each iteration of the loop), a sub-context
            \# must be created with the callback context's \`subcontext\` method.
            subcontext \= callback\_ctx.subcontext(task\_name\="fit iteration")
            \# The sub-context corresponds to a new sub-task, so its
            \# \`call\_on\_fit\_task\_begin\` method must also be called.
            subcontext.call\_on\_fit\_task\_begin(estimator\=self, X\=X, y\=y)

            labels \= self.\_compute\_labels(X)

            for k in range(self.n\_clusters):
                if (labels \== k).any():
                    self.cluster\_centers\_\[k\] \= X\[labels \== k\].mean(axis\=0)

            \# After each sub-task, the \`call\_on\_fit\_task\_end\` method of its sub-context
            \# must be called, also with \`estimator\` as a mandatory argument and optional
            \# \`kwargs\`. It will call all the callbacks' \`on\_fit\_task\_end\` hooks. Here
            \# the extra \`kwargs\` contain a \`reconstruction\_attributes\` callable,
            \# which returns the necessary attributes to generate an estimator instance
            \# ready to predict, as if the fit process just stopped at this step.
            if subcontext.call\_on\_fit\_task\_end(
                estimator\=self,
                X\=X,
                y\=y,
                reconstruction\_attributes\=lambda: {
                    "cluster\_centers\_": self.cluster\_centers\_,
                },
            ):
                \# The \`call\_on\_fit\_task\_end\` method returns a boolean, which is set
                \# to True if any of the callbacks' \`on\_fit\_task\_end\` methods return
                \# True. This enables the interruption of the \`fit\` process by the
                \# callbacks, for example to implement early stopping. Thus the
                \# \`call\_on\_fit\_task\_end\` method can be used in an \`if\` / \`break\` block
                \# to enable such interruptions.
                break

        \# After the root task of the fit function is done, the \`call\_on\_fit\_task\_end\`
        \# method of its callback context must be called.
        callback\_ctx.call\_on\_fit\_task\_end(
            estimator\=self,
            X\=X,
            y\=y,
            reconstruction\_attributes\=lambda: {
                "cluster\_centers\_": self.cluster\_centers\_,
            },
        )

        \# The callbacks' \`teardown\` hooks are called automatically in the decorator,
        \# after fit finishes, even if it crashed.
        return self

    def predict(self, X):
        [check\_is\_fitted](https://scikit-learn.org/stable/modules/generated/sklearn.utils.validation.check_is_fitted.html#sklearn.utils.validation.check_is_fitted "sklearn.utils.validation.check_is_fitted")
(self)
        return self.\_compute\_labels(X)

    def transform(self, X):
        [check\_is\_fitted](https://scikit-learn.org/stable/modules/generated/sklearn.utils.validation.check_is_fitted.html#sklearn.utils.validation.check_is_fitted "sklearn.utils.validation.check_is_fitted")
(self)
        return euclidean\_distances(X, self.cluster\_centers\_)

Copy to clipboard

Note

See the documentation of the methods [`call_on_fit_task_begin`](https://scikit-learn.org/stable/modules/generated/sklearn.callback.CallbackContext.html#sklearn.callback.CallbackContext.call_on_fit_task_begin "sklearn.callback.CallbackContext.call_on_fit_task_begin")
 and [`call_on_fit_task_end`](https://scikit-learn.org/stable/modules/generated/sklearn.callback.CallbackContext.html#sklearn.callback.CallbackContext.call_on_fit_task_end "sklearn.callback.CallbackContext.call_on_fit_task_end")
 for the description of the `kwargs` they can accept. These `kwargs` are optional, but an estimator should provide all the ones it is capable of producing in each task to be compatible with a maximum number of callbacks.

Registering callbacks to the custom estimator[#](https://scikit-learn.org/stable/auto_examples/callbacks/plot_callback_support.html#registering-callbacks-to-the-custom-estimator "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Now the `SimpleKMeans` estimator can be used with callbacks, for example with the [`ProgressBar`](https://scikit-learn.org/stable/modules/generated/sklearn.callback.ProgressBar.html#sklearn.callback.ProgressBar "sklearn.callback.ProgressBar")
 callback to monitor progress.

estimator \= SimpleKMeans(random\_state\=rng)
callback \= [ProgressBar](https://scikit-learn.org/stable/modules/generated/sklearn.callback.ProgressBar.html#sklearn.callback.ProgressBar "sklearn.callback.ProgressBar")
()
estimator.set\_callbacks(callback)
estimator.fit(X)

Copy to clipboard

SimpleKMeans - fit ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00

Copy to clipboard

SimpleKMeans(random\_state=RandomState(MT19937) at 0x7E1DF5B93340)

**In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook.  
On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.**

SimpleKMeans

iFitted

Parameters

|     |     |     |
| --- | --- | --- |
|     | random\_state | RandomState(M...0x7E1DF5B93340 |
|     | n\_clusters | 6   |
|     | n\_iter | 100 |

Fitted attributes

| Name | Type | Value |
| --- | --- | --- |
| cluster\_centers\_ | ndarray\[float64\](6, 4) | \[\[0.2 ,0.71,0.57,0.71\], \[0.21,0.42,0.25,0.16\], \[0.64,0.26,0.2 ,0.62\], \[0.86,0.71,0.77,0.68\], \[0.41,0.21,0.79,0.4 \], \[0.78,0.69,0.37,0.29\]\] |
| n\_features\_in\_ | int | 4   |

  
  

Custom meta-estimator[#](https://scikit-learn.org/stable/auto_examples/callbacks/plot_callback_support.html#custom-meta-estimator "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------

Now we demonstrate how to implement a custom meta-estimator that supports callbacks. For the example, we implement a simplified version of a grid search, where only a list of parameter combinations is searched through instead of a grid, parallelizing the evaluation of the parameters. Let’s start with the implementation without the callback support.

\# Function to run in parallel, it fits and scores an estimator on the folds of a CV.
def \_fit\_and\_score\_cv(estimator, X, y, cv, score\_func):
    scores\_per\_fold \= \[\]
    \# We iterate over the folds of the CV split.
    for train\_idx, test\_idx in cv.split(X):
        \# A clone of the estimator is used for the current fold.
        cloned\_estimator \= clone(estimator)
        \# The split of the current fold is applied to the data.
        X\_train, X\_test \= X\[train\_idx\], X\[test\_idx\]
        y\_train, y\_test \= (y\[train\_idx\], y\[test\_idx\]) if y is not None else (None, None)
        \# The clone of the estimator is fitted.
        cloned\_estimator.fit(X\_train, y\_train)
        \# Its score is computed.
        scores\_per\_fold.append(score\_func(cloned\_estimator, X\_test, y\_test))
    return scores\_per\_fold

class SimpleGridSearch([BaseEstimator](https://scikit-learn.org/stable/modules/generated/sklearn.base.BaseEstimator.html#sklearn.base.BaseEstimator "sklearn.base.BaseEstimator")
):
    def \_\_init\_\_(self, estimator, param\_list, cv, score\_func, n\_jobs\=1):
        \# the estimator to evaluate
        self.estimator \= estimator
        \# the list of parameter combinations to iterate over
        self.param\_list \= param\_list
        \# the number of splits for the CV, or a CV splitter instance
        self.cv \= cv
        \# the scoring function
        self.score\_func \= score\_func
        \# number of jobs for parallelization
        self.n\_jobs \= n\_jobs

    def fit(self, X, y\=None):
        \# We use a cross-validator instance to evaluate each parameter combination on
        \# multiple folds.
        cv \= [check\_cv](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.check_cv.html#sklearn.model_selection.check_cv "sklearn.model_selection.check_cv")
(self.cv)

        \# We iterate over the parameter combinations in parallel, fitting an estimator
        \# and computing a score value for each fold.
        scores\_per\_fold \= [Parallel](https://scikit-learn.org/stable/modules/generated/sklearn.utils.parallel.Parallel.html#sklearn.utils.parallel.Parallel "sklearn.utils.parallel.Parallel")
(n\_jobs\=self.n\_jobs)(
            [delayed](https://scikit-learn.org/stable/modules/generated/sklearn.utils.parallel.delayed.html#sklearn.utils.parallel.delayed "sklearn.utils.parallel.delayed")
(\_fit\_and\_score\_cv)(
                estimator\=clone(self.estimator).set\_params(\*\*params),
                X\=X,
                y\=y,
                cv\=cv,
                score\_func\=self.score\_func,
            )
            for params in self.param\_list
        )

        \# The \`cv\_results\_\` attribute holds the score values for each parameter
        \# combination and fold, as a list of tuples, each one of the form
        \# (parameter combination, list of scores per fold).
        self.cv\_results\_ \= list(zip(self.param\_list, scores\_per\_fold))

        return self

Copy to clipboard

Now let’s update the class to support callbacks.

\# The parallelized function needs to receive the callback context corresponding to its
\# task and the instance calling it.
def \_fit\_and\_score\_cv(estimator, X, y, cv, score\_func, outer\_subcontext, caller):
    \# The outer sub-context's \`call\_on\_fit\_task\_begin\` must be called.
    outer\_subcontext.call\_on\_fit\_task\_begin(estimator\=caller, X\=X, y\=y)
    scores\_per\_fold \= \[\]
    for i, (train\_idx, test\_idx) in enumerate(cv.split(X)):
        cloned\_estimator \= clone(estimator)
        X\_train, X\_test \= X\[train\_idx\], X\[test\_idx\]
        y\_train, y\_test \= (y\[train\_idx\], y\[test\_idx\]) if y is not None else (None, None)
        \# For each inner iteration a sub-context must be created.
        inner\_subcontext \= outer\_subcontext.subcontext(task\_name\=f"fold {i}")
        \# Since a sub-estimator is fitted in this task, the callbacks must be propagated
        \# to that estimator with the \`propagate\_callback\_context\` context manager. Note
        \# that only the callbacks following the \`AutoPropagatedCallback\` protocol can be
        \# propagated.
        with inner\_subcontext.propagate\_callback\_context(cloned\_estimator):
            \# After the propagation, the inner sub-context's \`call\_on\_fit\_task\_begin\`
            \# method must be called.
            inner\_subcontext.call\_on\_fit\_task\_begin(
                estimator\=caller, X\=X\_train, y\=y\_train
            )
            cloned\_estimator.fit(X\_train, y\_train)
            scores\_per\_fold.append(score\_func(cloned\_estimator, X\_test, y\_test))
            \# The inner sub-context's \`call\_on\_fit\_task\_end\` method must be called.
            inner\_subcontext.call\_on\_fit\_task\_end(
                estimator\=caller, X\=X\_train, y\=y\_train
            )
    \# The outer sub-context's \`call\_on\_fit\_task\_end\` method must be called.
    outer\_subcontext.call\_on\_fit\_task\_end(estimator\=caller, X\=X, y\=y)
    return scores\_per\_fold

\# The class must inherit from \`CallbackSupportMixin\`.
class SimpleGridSearch([CallbackSupportMixin](https://scikit-learn.org/stable/modules/generated/sklearn.callback.CallbackSupportMixin.html#sklearn.callback.CallbackSupportMixin "sklearn.callback.CallbackSupportMixin")
, [BaseEstimator](https://scikit-learn.org/stable/modules/generated/sklearn.base.BaseEstimator.html#sklearn.base.BaseEstimator "sklearn.base.BaseEstimator")
):  \# noqa: F811
    def \_\_init\_\_(self, estimator, param\_list, cv, score\_func, n\_jobs\=1):
        self.estimator \= estimator
        self.param\_list \= param\_list
        self.cv \= cv
        self.score\_func \= score\_func
        self.n\_jobs \= n\_jobs

    \# The \`fit\` method must be decorated.
    @with\_callbacks
    def fit(self, X, y\=None):
        cv \= [check\_cv](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.check_cv.html#sklearn.model_selection.check_cv "sklearn.model_selection.check_cv")
(self.cv)
        \# The callback context must be instantiated, which also calls the \`setup\` hooks
        \# of the callbacks.
        callback\_ctx \= self.\_init\_callback\_context(
            task\_name\="fit", max\_subtasks\=len(self.param\_list)
        )
        \# The \`call\_on\_fit\_task\_begin\` method of this context must be called.
        callback\_ctx.call\_on\_fit\_task\_begin(estimator\=self, X\=X, y\=y)

        \# The sub-tasks of the \`fit\` function are nested on two levels : the outer
        \# iterations over parameter combinations and the inner iterations over CV folds.
        \# Sub-contexts must be created for each of these levels. For the outer level,
        \# the sub-contexts are instantiated outside of the parallelized function. In
        \# order to prevent any racing condition during their creation, these
        \# sub-contexts must be all created before the parallelization.
        outer\_subcontexts \= \[\
            callback\_ctx.subcontext(\
                task\_name\="param iteration", max\_subtasks\=cv.get\_n\_splits()\
            )\
            for \_ in range(len(self.param\_list))\
        \]

        scores\_per\_fold \= [Parallel](https://scikit-learn.org/stable/modules/generated/sklearn.utils.parallel.Parallel.html#sklearn.utils.parallel.Parallel "sklearn.utils.parallel.Parallel")
(n\_jobs\=self.n\_jobs)(
            [delayed](https://scikit-learn.org/stable/modules/generated/sklearn.utils.parallel.delayed.html#sklearn.utils.parallel.delayed "sklearn.utils.parallel.delayed")
(\_fit\_and\_score\_cv)(
                estimator\=clone(self.estimator).set\_params(\*\*params),
                X\=X,
                y\=y,
                cv\=cv,
                score\_func\=self.score\_func,
                outer\_subcontext\=outer\_subcontexts\[i\],
                caller\=self,
            )
            for i, params in enumerate(self.param\_list)
        )

        self.cv\_results\_ \= list(zip(self.param\_list, scores\_per\_fold))

        \# The root context's \`call\_on\_fit\_task\_end\` must be called.
        callback\_ctx.call\_on\_fit\_task\_end(estimator\=self, X\=X, y\=y)

        \# The callbacks' \`teardown\` hooks are called automatically in the decorator.
        return self

Copy to clipboard

The main difference with a simple estimator is that the callbacks must be propagated to the sub-estimators through the corresponding callback sub-context’s [`propagate_callback_context`](https://scikit-learn.org/stable/modules/generated/sklearn.callback.CallbackContext.html#sklearn.callback.CallbackContext.propagate_callback_context "sklearn.callback.CallbackContext.propagate_callback_context")
 context manager.

Note

A meta-estimator that supports callback can be used with sub-estimators that do not. In that case a warning is raised when trying to propagate the callbacks and the callbacks are ignored in the sub-estimator.

Registering callbacks to the meta-estimator[#](https://scikit-learn.org/stable/auto_examples/callbacks/plot_callback_support.html#registering-callbacks-to-the-meta-estimator "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Callbacks are registered to a meta-estimator the same way as to regular estimators. The callbacks which respect the [`AutoPropagatedCallback`](https://scikit-learn.org/stable/modules/generated/sklearn.callback.AutoPropagatedCallback.html#sklearn.callback.AutoPropagatedCallback "sklearn.callback.AutoPropagatedCallback")
 protocol (such as [`ProgressBar`](https://scikit-learn.org/stable/modules/generated/sklearn.callback.ProgressBar.html#sklearn.callback.ProgressBar "sklearn.callback.ProgressBar")
) are propagated to the sub-estimators.

param\_list \= \[{"n\_clusters": 5, "n\_iter": 20}, {"n\_clusters": 4, "n\_iter": 50}\]

def score\_func(estimator, X, y\=None):
    return [np.sum](https://numpy.org/doc/stable/reference/generated/numpy.sum.html#numpy.sum "numpy.sum")
(estimator.transform(X).min(axis\=1))

sub\_estimator \= SimpleKMeans(random\_state\=rng)
meta\_estimator \= SimpleGridSearch(
    estimator\=sub\_estimator, param\_list\=param\_list, cv\=4, score\_func\=score\_func
)
callback \= [ProgressBar](https://scikit-learn.org/stable/modules/generated/sklearn.callback.ProgressBar.html#sklearn.callback.ProgressBar "sklearn.callback.ProgressBar")
()
meta\_estimator.set\_callbacks(callback)
meta\_estimator.fit(X)

Copy to clipboard

SimpleGridSearch - fit                                ━━━━━━━━━━━━━ 100% 0:00:00
  SimpleGridSearch - param iteration #0               ━━━━━━━━━━━━━ 100% 0:00:00
    SimpleGridSearch - fold 0 | SimpleKMeans - fit #0 ━━━━━━━━━━━━━ 100% 0:00:00
    SimpleGridSearch - fold 1 | SimpleKMeans - fit #1 ━━━━━━━━━━━━━ 100% 0:00:00
    SimpleGridSearch - fold 2 | SimpleKMeans - fit #2 ━━━━━━━━━━━━━ 100% 0:00:00
    SimpleGridSearch - fold 3 | SimpleKMeans - fit #3 ━━━━━━━━━━━━━ 100% 0:00:00
  SimpleGridSearch - param iteration #1               ━━━━━━━━━━━━━ 100% 0:00:00
    SimpleGridSearch - fold 0 | SimpleKMeans - fit #0 ━━━━━━━━━━━━━ 100% 0:00:00
    SimpleGridSearch - fold 1 | SimpleKMeans - fit #1 ━━━━━━━━━━━━━ 100% 0:00:00
    SimpleGridSearch - fold 2 | SimpleKMeans - fit #2 ━━━━━━━━━━━━━ 100% 0:00:00
    SimpleGridSearch - fold 3 | SimpleKMeans - fit #3 ━━━━━━━━━━━━━ 100% 0:00:00

Copy to clipboard

SimpleGridSearch(cv=4,
                 estimator=SimpleKMeans(random\_state=RandomState(MT19937) at 0x7E1DF5B93340),
                 param\_list=\[{'n\_clusters': 5, 'n\_iter': 20},\
                             {'n\_clusters': 4, 'n\_iter': 50}\],
                 score\_func=<function score\_func at 0x7e1dbd4f99b0>)

**In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook.  
On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.**

SimpleGridSearch

iFitted

Parameters

|     |     |     |
| --- | --- | --- |
|     | estimator | SimpleKMeans(...x7E1DF5B93340) |
|     | param\_list | \[{'n\_clusters': 5, 'n\_iter': 20}, {'n\_clusters': 4, 'n\_iter': 50}\] |
|     | cv  | 4   |
|     | score\_func | <function sco...x7e1dbd4f99b0> |
|     | n\_jobs | 1   |

Fitted attributes

| Name | Type | Value |
| --- | --- | --- |
| cv\_results\_ | list | \[({'n\_...rs': 5, 'n\_iter': 20}, \[np.float64(10.91424581701756), np.float64(11.359114841755346), np.float64(10.797904247904043), np.float64(10.874941524888662)\]), ({'n\_...rs': 4, 'n\_iter': 50}, \[np.float64(11.691406409750513), np.float64(11.73823101129824), np.float64(11.3696726284519), np.float64(11.974176461029863)\])\] |

estimator: SimpleKMeans

SimpleKMeans(random\_state=RandomState(MT19937) at 0x7E1DF5B93340)

SimpleKMeans

Parameters

|     |     |     |
| --- | --- | --- |
|     | random\_state | RandomState(M...0x7E1DF5B93340 |
|     | n\_clusters | 6   |
|     | n\_iter | 100 |

  
  

**Total running time of the script:** (0 minutes 0.238 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo3.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/callbacks/plot_callback_support.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo3.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/callbacks/plot_callback_support.ipynb)

[`Download Jupyter notebook: plot_callback_support.ipynb`](https://scikit-learn.org/stable/_downloads/e79f7ef202cb51e147d56261691eae8d/plot_callback_support.ipynb)

[`Download Python source code: plot_callback_support.py`](https://scikit-learn.org/stable/_downloads/f7bd2e6f55b4932ff2335edacd28f5f5/plot_callback_support.py)

[`Download zipped: plot_callback_support.zip`](https://scikit-learn.org/stable/_downloads/1db5be5d11e097d856e8393d23c4bd11/plot_callback_support.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_scoring_monitor_thumb.png)

[Analysis of the convergence of penalized logistic regression models](https://scikit-learn.org/stable/auto_examples/callbacks/plot_scoring_monitor.html)

Analysis of the convergence of penalized logistic regression models

![](https://scikit-learn.org/stable/_images/sphx_glr_sklearn_is_fitted_thumb.png)

[\_\_sklearn\_is\_fitted\_\_ as Developer API](https://scikit-learn.org/stable/auto_examples/developing_estimators/sklearn_is_fitted.html)

\_\_sklearn\_is\_fitted\_\_ as Developer API

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_1_9_0_thumb.png)

[Release Highlights for scikit-learn 1.9](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_9_0.html)

Release Highlights for scikit-learn 1.9

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_nested_cross_validation_iris_thumb.png)

[Nested versus non-nested cross-validation](https://scikit-learn.org/stable/auto_examples/model_selection/plot_nested_cross_validation_iris.html)

Nested versus non-nested cross-validation

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page

[Download source code](https://scikit-learn.org/stable/_downloads/f7bd2e6f55b4932ff2335edacd28f5f5/plot_callback_support.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/e79f7ef202cb51e147d56261691eae8d/plot_callback_support.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/1db5be5d11e097d856e8393d23c4bd11/plot_callback_support.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo3.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/callbacks/plot_callback_support.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo3.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/callbacks/plot_callback_support.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)