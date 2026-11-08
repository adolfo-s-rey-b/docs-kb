[Skip to main content](https://scikit-learn.org/stable/callbacks.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/callbacks.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/callbacks.html)
[1.8.0](https://scikit-learn.org/1.8/callbacks.html)
[1.7.2](https://scikit-learn.org/1.7/callbacks.html)
[1.6.1](https://scikit-learn.org/1.6/callbacks.html)
[1.5.2](https://scikit-learn.org/1.5/callbacks.html)
[1.4.2](https://scikit-learn.org/1.4/callbacks.html)

Collapse Sidebar Expand Sidebar

7\. Callbacks[#](https://scikit-learn.org/stable/callbacks.html#callbacks "Link to this heading")

==================================================================================================

Note

The callback API is experimental, and is not yet implemented for all estimators. Please refer to the [list of callback-compatible estimators](https://scikit-learn.org/stable/callbacks.html#callback-compatible-estimators)
 for more information. It may change without the usual deprecation cycle.

This guide demonstrates how to use scikit-learn’s [callbacks](https://scikit-learn.org/stable/glossary.html#term-callbacks)
 on compatible [estimators](https://scikit-learn.org/stable/glossary.html#term-estimators)
. For information about how to implement the callback API, you can refer to the following sections of the developer’s guide:

*   the [Implementing callback support in estimators](https://scikit-learn.org/stable/developers/callback_support.html#callbacks-support)
     section for making estimators compatible with callbacks.
    
*   the [Developing callbacks](https://scikit-learn.org/stable/developers/developing_callbacks.html#developing-callbacks)
     section for how to implement a new callback.
    

In scikit-learn, callbacks are objects from the [`callback`](https://scikit-learn.org/stable/api/sklearn.callback.html#module-sklearn.callback "sklearn.callback")
 module that can be registered on an estimator to insert custom logic like monitoring progress or metrics, without modifying the underlying learning algorithm. The registered callbacks are invoked at specific steps of the [fitting](https://scikit-learn.org/stable/glossary.html#term-fitting)
 process.

7.1. Registering callbacks[#](https://scikit-learn.org/stable/callbacks.html#registering-callbacks "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------

Estimators that support callbacks expose a [`set_callbacks`](https://scikit-learn.org/stable/modules/generated/sklearn.callback.CallbackSupportMixin.html#sklearn.callback.CallbackSupportMixin.set_callbacks "sklearn.callback.CallbackSupportMixin.set_callbacks")
 method to register callbacks on them. The following example shows how to register a [`ProgressBar`](https://scikit-learn.org/stable/modules/generated/sklearn.callback.ProgressBar.html#sklearn.callback.ProgressBar "sklearn.callback.ProgressBar")
 callback on a [`LogisticRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
:

\>>> from sklearn.callback import ProgressBar
\>>> from sklearn.linear\_model import LogisticRegression
\>>> progress\_bar \= ProgressBar()
\>>> logreg \= LogisticRegression(max\_iter\=200)
\>>> logreg.set\_callbacks(progress\_bar)
LogisticRegression(max\_iter=200)

Copy to clipboard

Now that the progress bar is registered on the estimator, calling its `fit` method will display a progress bar:

\>>> from sklearn.datasets import load\_iris
\>>> X, y \= load\_iris(return\_X\_y\=True)
\>>> logreg.fit(X, y)
LogisticRegression - fit ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
LogisticRegression(max\_iter=200)

Copy to clipboard

Multiple callbacks can be registered on the same estimator, for example a [`ScoringMonitor`](https://scikit-learn.org/stable/modules/generated/sklearn.callback.ScoringMonitor.html#sklearn.callback.ScoringMonitor "sklearn.callback.ScoringMonitor")
 callback can be registered in addition to the [`ProgressBar`](https://scikit-learn.org/stable/modules/generated/sklearn.callback.ProgressBar.html#sklearn.callback.ProgressBar "sklearn.callback.ProgressBar")
:

\>>> from sklearn.callback import ScoringMonitor
\>>> scoring\_monitor \= ScoringMonitor(scoring\="accuracy")
\>>> logreg.set\_callbacks(progress\_bar, scoring\_monitor)
LogisticRegression(max\_iter=200)

Copy to clipboard

7.2. Callback invocation[#](https://scikit-learn.org/stable/callbacks.html#callback-invocation "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------

During `fit`, the callbacks are invoked at the start and end of each [task](https://scikit-learn.org/stable/glossary.html#term-fit-task)
, where tasks are arbitrary units of work defined by the estimator. Usually, tasks correspond to iterations of the estimator’s learning algorithm, but they can also correspond to more abstract operations like fitting an estimator, steps of a pipeline, cross-validation folds, etc. Within `fit`, tasks are divided into subtasks, which can themselves be divided and so on, giving them a natural [tree structure](https://scikit-learn.org/stable/developers/callback_support.html#example-task-tree)
 where fitting the estimator is the root task.

This tree structure will usually be reflected in a callback’s generated objects and tasks will be identified by their name, id, and a reference to their parent task. For tasks that have a natural ordering, like the iterations of a learning algorithm, the ids are consecutive integers starting from 0. Some callbacks may provide additional contextual information about the tasks. Here’s an example of the logs of the [`ScoringMonitor`](https://scikit-learn.org/stable/modules/generated/sklearn.callback.ScoringMonitor.html#sklearn.callback.ScoringMonitor "sklearn.callback.ScoringMonitor")
:

\>>> logreg.fit(X, y)
LogisticRegression - fit ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
LogisticRegression(max\_iter=200)
\>>> scoring\_monitor.get\_logs().data\_as\_pandas\[\["task\_name", "task\_id", "accuracy"\]\]
      task\_name  task\_id  accuracy
0           fit        0  0.973...
1    lbfgs-iter        0  0.333...
2    lbfgs-iter        1  0.333...
3    lbfgs-iter        2  0.666...
4    lbfgs-iter        3  0.926...
...

Copy to clipboard

7.3. Usage with meta-estimators[#](https://scikit-learn.org/stable/callbacks.html#usage-with-meta-estimators "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------

When using callbacks in estimator compositions, involving estimators and [meta-estimators](https://scikit-learn.org/stable/glossary.html#term-meta-estimators)
, we distinguish two types of callbacks: regular and auto-propagated. They serve different purposes and are meant to be registered on different estimators or meta-estimators in the composition.

### 7.3.1. Regular callbacks[#](https://scikit-learn.org/stable/callbacks.html#regular-callbacks "Link to this heading")

Regular callbacks are meant to be invoked within the `fit` of a given estimator. Their goal is usually to track the learning process of that estimator. [`ScoringMonitor`](https://scikit-learn.org/stable/modules/generated/sklearn.callback.ScoringMonitor.html#sklearn.callback.ScoringMonitor "sklearn.callback.ScoringMonitor")
, for example, records the scores at each iteration of a model. A regular callback can be registered on an estimator at any level of a composition. If a regular callback is registered on an estimator that is [cloned](https://scikit-learn.org/stable/glossary.html#term-cloned)
 by a meta-estimator, possibly multiple times, that callback will be invoked in each one of the `fit` executions of the clones.

For example, when tuning the hyperparameters of a [`LogisticRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
 using a [`GridSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV")
, a [`ScoringMonitor`](https://scikit-learn.org/stable/modules/generated/sklearn.callback.ScoringMonitor.html#sklearn.callback.ScoringMonitor "sklearn.callback.ScoringMonitor")
 can be registered on the [`LogisticRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
 to monitor the scores of the logistic regression model for each parameter combination and each fold of the grid search:

\>>> from sklearn.model\_selection import GridSearchCV
\>>> scoring\_monitor \= ScoringMonitor(scoring\="accuracy")
\>>> logreg \= LogisticRegression(max\_iter\=200).set\_callbacks(scoring\_monitor)
\>>> grid\_search \= GridSearchCV(logreg, {"C": \[10, 1, 0.1\]})
\>>> grid\_search.fit(X, y)
GridSearchCV(estimator=LogisticRegression(max\_iter=200),
             param\_grid={'C': \[10, 1, 0.1\]})
\>>> log \= scoring\_monitor.get\_logs().data\_as\_pandas
\>>> \# show the scores at the end of each fit of the search
\>>> log\[log\["parent\_task\_id\_path"\] \== (0,0)\]\[\["task\_name", "task\_id", "accuracy"\]\]
   task\_name  task\_id  accuracy
1        fit        0  0.975...
2        fit        1  0.975...
3        fit        2  0.991...
4        fit        3  0.991...
5        fit        4  0.975...
6        fit        5  0.966...
7        fit        6  0.966...
8        fit        7  0.983...
9        fit        8  0.983...
10       fit        9  0.975...
11       fit       10  0.958...
12       fit       11  0.958...
13       fit       12  0.958...
14       fit       13  0.958...
15       fit       14  0.941...

Copy to clipboard

See [Analysis of the convergence of penalized logistic regression models](https://scikit-learn.org/stable/auto_examples/callbacks/plot_scoring_monitor.html#sphx-glr-auto-examples-callbacks-plot-scoring-monitor-py)
 for an example of how to use and plot the scores from the logs.

### 7.3.2. Auto-propagated callbacks[#](https://scikit-learn.org/stable/callbacks.html#auto-propagated-callbacks "Link to this heading")

[Auto-propagated](https://scikit-learn.org/stable/glossary.html#term-auto-propagated)
 callbacks are meant to be invoked within the `fit` of all (meta-)estimators in an estimator composition. Their goal is usually to report more general information about the status at each step of the composition. [`ProgressBar`](https://scikit-learn.org/stable/modules/generated/sklearn.callback.ProgressBar.html#sklearn.callback.ProgressBar "sklearn.callback.ProgressBar")
 for instance displays nested progress bars for the meta-estimators, their sub-estimators and so on. When registered on a meta-estimator, an auto-propagated callback will automatically be registered on all its sub-estimators that support callbacks.

registration restrictions[#](https://scikit-learn.org/stable/callbacks.html#registration-restrictions "Link to this dropdown")

Auto-propagated callbacks are designed to be registered on the top-level meta-estimator of an estimator composition. If some of its sub-estimators already have auto-propagated callbacks registered on them, an error will be raised.

If the top-level meta-estimator doesn’t itself support callbacks, then its sub-estimators are allowed to have auto-propagated callbacks registered on them. However, be aware that this is not optimal and that callbacks might not be able to deliver their full capabilities.

Let’s add progress bars to the example of the previous section, tuning the hyperparameters of a [`LogisticRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
. The [`ProgressBar`](https://scikit-learn.org/stable/modules/generated/sklearn.callback.ProgressBar.html#sklearn.callback.ProgressBar "sklearn.callback.ProgressBar")
 callback needs to be registered on the grid search:

\>>> grid\_search.set\_callbacks(ProgressBar())
GridSearchCV(estimator=LogisticRegression(max\_iter=200),
             param\_grid={'C': \[10, 1, 0.1\]})
\>>> grid\_search.fit(X, y)
GridSearchCV - fit                                                           ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  GridSearchCV - search #0                                                   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
    GridSearchCV - candidate-split-evaluation | LogisticRegression - fit #0  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
    GridSearchCV - candidate-split-evaluation | LogisticRegression - fit #3  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
    GridSearchCV - candidate-split-evaluation | LogisticRegression - fit #6  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
    GridSearchCV - candidate-split-evaluation | LogisticRegression - fit #9  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
    GridSearchCV - candidate-split-evaluation | LogisticRegression - fit #12 ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
    GridSearchCV - candidate-split-evaluation | LogisticRegression - fit #1  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
    GridSearchCV - candidate-split-evaluation | LogisticRegression - fit #4  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
    GridSearchCV - candidate-split-evaluation | LogisticRegression - fit #7  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
    GridSearchCV - candidate-split-evaluation | LogisticRegression - fit #10 ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
    GridSearchCV - candidate-split-evaluation | LogisticRegression - fit #13 ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
    GridSearchCV - candidate-split-evaluation | LogisticRegression - fit #2  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
    GridSearchCV - candidate-split-evaluation | LogisticRegression - fit #5  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
    GridSearchCV - candidate-split-evaluation | LogisticRegression - fit #8  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
    GridSearchCV - candidate-split-evaluation | LogisticRegression - fit #11 ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
    GridSearchCV - candidate-split-evaluation | LogisticRegression - fit #14 ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  GridSearchCV - refit-with-best-params | LogisticRegression - fit #1        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
GridSearchCV(estimator=LogisticRegression(max\_iter=200),
             param\_grid={'C': \[10, 1, 0.1\]})

Copy to clipboard

Control the propagation depth[#](https://scikit-learn.org/stable/callbacks.html#control-the-propagation-depth "Link to this dropdown")

Auto-propagated callbacks can be distinguished from regular callbacks by the fact that they have a `max_propagation_depth` attribute. This attribute indicates the maximum depth of nested estimators at which the callback will be propagated. In the previous example, the grid search is at depth 0 and the logistic regression is at depth 1 for instance.

If `max_propagation_depth` is set to 0, the callback will not be propagated to any sub-estimators and will only be invoked for the (meta-)estimator it is registered on. If it is set to `None`, it will be propagated to all nested levels of the estimator composition.

7.4. Scikit-learn’s built-in callbacks[#](https://scikit-learn.org/stable/callbacks.html#scikit-learn-s-built-in-callbacks "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------

The built-in callbacks currently available in scikit-learn are the following:

| Callback | Description |
| --- | --- |
| [`ProgressBar`](https://scikit-learn.org/stable/modules/generated/sklearn.callback.ProgressBar.html#sklearn.callback.ProgressBar "sklearn.callback.ProgressBar") | Display progress bars. |
| [`ScoringMonitor`](https://scikit-learn.org/stable/modules/generated/sklearn.callback.ScoringMonitor.html#sklearn.callback.ScoringMonitor "sklearn.callback.ScoringMonitor") | Log a scoring metric at the end of each task during fit. |

7.5. Callback Support Status[#](https://scikit-learn.org/stable/callbacks.html#callback-support-status "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------

The development of support for callbacks in estimators is in progress. Here is a list of the estimators that support callbacks:

*   [`sklearn.linear_model.LogisticRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
    
*   [`sklearn.model_selection.GridSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV")
    
*   [`sklearn.model_selection.HalvingGridSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.HalvingGridSearchCV.html#sklearn.model_selection.HalvingGridSearchCV "sklearn.model_selection.HalvingGridSearchCV")
    
*   [`sklearn.model_selection.HalvingRandomSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.HalvingRandomSearchCV.html#sklearn.model_selection.HalvingRandomSearchCV "sklearn.model_selection.HalvingRandomSearchCV")
    
*   [`sklearn.model_selection.RandomizedSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RandomizedSearchCV.html#sklearn.model_selection.RandomizedSearchCV "sklearn.model_selection.RandomizedSearchCV")
    
*   [`sklearn.pipeline.Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
    
*   [`sklearn.preprocessing.StandardScaler`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler")
    

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)