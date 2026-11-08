[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.callback.CallbackSupportMixin.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.callback.CallbackSupportMixin.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.callback.CallbackSupportMixin.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.callback.CallbackSupportMixin.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.callback.CallbackSupportMixin.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.callback.CallbackSupportMixin.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.callback.CallbackSupportMixin.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.callback.CallbackSupportMixin.html)

Collapse Sidebar Expand Sidebar

CallbackSupportMixin[#](https://scikit-learn.org/stable/modules/generated/sklearn.callback.CallbackSupportMixin.html#callbacksupportmixin "Link to this heading")

==================================================================================================================================================================

class sklearn.callback.CallbackSupportMixin[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/callback/_callback_support.py#L11)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.callback.CallbackSupportMixin.html#sklearn.callback.CallbackSupportMixin "Link to this definition")

Mixin class to add callback support to an estimator.

\_init\_callback\_context(_task\_name\='fit'_, _task\_id\=0_, _max\_subtasks\=0_, _sequential\_subtasks\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/callback/_callback_support.py#L48)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.callback.CallbackSupportMixin.html#sklearn.callback.CallbackSupportMixin._init_callback_context "Link to this definition")

Initialize the callback context for the estimator and setup its callbacks.

This method should be called once, at the beginning of the fit method.

It will only setup callbacks that are not propagated from a meta-estimator.

Parameters:

**task\_name**str, default=”fit”

The name of the root task.

**task\_id**int, default=0

Identifier for the root task.

**max\_subtasks**int or None, default=0

The maximum number of subtasks that can be children of the root task. None means the maximum number of subtasks is not known in advance. 0 means it’s a leaf.

**sequential\_subtasks**bool, default=True

Whether the root context has sequential subtasks. If True, children contexts of the root context, created via `subcontext`, will have automatically assigned consecutive integer task\_ids starting from 0.

Returns:

**callback\_fit\_ctx**CallbackContext

The root callback context for the estimator.

set\_callbacks(_\*callbacks_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/callback/_callback_support.py#L18)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.callback.CallbackSupportMixin.html#sklearn.callback.CallbackSupportMixin.set_callbacks "Link to this definition")

Set callbacks for the estimator.

Parameters:

**\*callbacks**callback instances

The callbacks to set.

Returns:

**self**estimator instance

The estimator instance itself.

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.callback.CallbackSupportMixin.html#gallery-examples "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_callback_support_thumb.png)

[Supporting callbacks in third party estimators](https://scikit-learn.org/stable/auto_examples/callbacks/plot_callback_support.html)

Supporting callbacks in third party estimators

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)