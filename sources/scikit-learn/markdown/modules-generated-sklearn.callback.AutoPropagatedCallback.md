[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.callback.AutoPropagatedCallback.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.callback.AutoPropagatedCallback.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.callback.AutoPropagatedCallback.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.callback.AutoPropagatedCallback.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.callback.AutoPropagatedCallback.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.callback.AutoPropagatedCallback.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.callback.AutoPropagatedCallback.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.callback.AutoPropagatedCallback.html)

Collapse Sidebar Expand Sidebar

AutoPropagatedCallback[#](https://scikit-learn.org/stable/modules/generated/sklearn.callback.AutoPropagatedCallback.html#autopropagatedcallback "Link to this heading")

========================================================================================================================================================================

class sklearn.callback.AutoPropagatedCallback(_\*args_, _\*\*kwargs_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/callback/_base.py#L124)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.callback.AutoPropagatedCallback.html#sklearn.callback.AutoPropagatedCallback "Link to this definition")

Protocol for the auto-propagated callbacks

An auto-propagated callback is a callback that is meant to be set on a top-level estimator and that is automatically propagated to its sub-estimators (if any).

property max\_propagation\_depth[#](https://scikit-learn.org/stable/modules/generated/sklearn.callback.AutoPropagatedCallback.html#sklearn.callback.AutoPropagatedCallback.max_propagation_depth "Link to this definition")

The maximum number of nested estimators at which the callback should be propagated.

If set to None, the callback is propagated to sub-estimators at all nesting levels.

setup(_estimator_, _context_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/callback/_base.py#L11)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.callback.AutoPropagatedCallback.html#sklearn.callback.AutoPropagatedCallback.setup "Link to this definition")

Method called at the beginning of the fit method of the estimator.

For auto-propagated callbacks, this method is called only once, before running the fit method of the outermost estimator.

Parameters:

**estimator**estimator instance

The estimator calling this callback hook.

**context**`sklearn.callback.CallbackContext` instance

Context of the corresponding task. This is usually the root context of the estimator but it can be an intermediate context if the estimator is a sub-estimator of a meta-estimator.

teardown(_estimator_, _context_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/callback/_base.py#L28)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.callback.AutoPropagatedCallback.html#sklearn.callback.AutoPropagatedCallback.teardown "Link to this definition")

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