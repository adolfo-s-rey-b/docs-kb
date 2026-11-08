[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.callback.FitCallback.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.callback.FitCallback.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.callback.FitCallback.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.callback.FitCallback.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.callback.FitCallback.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.callback.FitCallback.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.callback.FitCallback.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.callback.FitCallback.html)

Collapse Sidebar Expand Sidebar

FitCallback[#](https://scikit-learn.org/stable/modules/generated/sklearn.callback.FitCallback.html#fitcallback "Link to this heading")

=======================================================================================================================================

class sklearn.callback.FitCallback(_\*args_, _\*\*kwargs_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/callback/_base.py#L46)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.callback.FitCallback.html#sklearn.callback.FitCallback "Link to this definition")

Protocol for the callbacks evaluated on tasks during the fit of an estimator.

on\_fit\_task\_begin(_estimator_, _context_, _\*_, _X\=None_, _y\=None_, _metadata\=None_, _fitted\_estimator\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/callback/_base.py#L50)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.callback.FitCallback.html#sklearn.callback.FitCallback.on_fit_task_begin "Link to this definition")

Method called at the beginning of each fit task of the estimator.

Parameters:

**estimator**estimator instance

The estimator calling this callback hook.

**context**`sklearn.callback.CallbackContext` instance

Context of the corresponding task.

**X**array-like

The training data at this task.

**y**array-like

The training target values at this task.

**metadata**dict

Training metadata at this task, e.g. sample weights.

**fitted\_estimator**estimator instance

A new instance of the estimator that is ready to predict, transform, etc … as if fit had stopped at the beginning of this task.

on\_fit\_task\_end(_estimator_, _context_, _\*_, _X\=None_, _y\=None_, _metadata\=None_, _fitted\_estimator\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/callback/_base.py#L84)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.callback.FitCallback.html#sklearn.callback.FitCallback.on_fit_task_end "Link to this definition")

Method called at the end of each fit task of the estimator.

Parameters:

**estimator**estimator instance

The estimator calling this callback hook.

**context**`sklearn.callback.CallbackContext` instance

Context of the corresponding task.

**X**array-like

The training data at this task.

**y**array-like

The training target values at this task.

**metadata**dict

Training metadata at this task, e.g. sample weights.

**fitted\_estimator**estimator instance

A new instance of the estimator that is ready to predict, transform, etc … as if fit had stopped at the end of this task.

Returns:

**stop**bool

Whether or not to stop the current level of iterations at this task.

setup(_estimator_, _context_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/callback/_base.py#L11)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.callback.FitCallback.html#sklearn.callback.FitCallback.setup "Link to this definition")

Method called at the beginning of the fit method of the estimator.

For auto-propagated callbacks, this method is called only once, before running the fit method of the outermost estimator.

Parameters:

**estimator**estimator instance

The estimator calling this callback hook.

**context**`sklearn.callback.CallbackContext` instance

Context of the corresponding task. This is usually the root context of the estimator but it can be an intermediate context if the estimator is a sub-estimator of a meta-estimator.

teardown(_estimator_, _context_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/callback/_base.py#L28)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.callback.FitCallback.html#sklearn.callback.FitCallback.teardown "Link to this definition")

Method called after finishing the fit method of the estimator.

For auto-propagated callbacks, this method is called only once, after finishing the fit method of the outermost estimator.

Parameters:

**estimator**estimator instance

The estimator calling this callback hook.

**context**`sklearn.callback.CallbackContext` instance

Context of the corresponding task. This is usually the root context of the estimator but it can be an intermediate context if the estimator is a sub-estimator of a meta-estimator.

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)