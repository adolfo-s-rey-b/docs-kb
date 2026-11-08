[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.callback.with_callbacks.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

Choose version

Collapse Sidebar Expand Sidebar

with\_callbacks[#](https://scikit-learn.org/stable/modules/generated/sklearn.callback.with_callbacks.html#with-callbacks "Link to this heading")

=================================================================================================================================================

sklearn.callback.with\_callbacks(_method_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/callback/_callback_support.py#L145)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.callback.with_callbacks.html#sklearn.callback.with_callbacks "Link to this definition")

Decorator to run the method within a callback context manager.

This decorator is responsible for calling the callbacks `teardown` hooks of callbacks in a `try finally` block, which guarantees that callbacks teardown will always be called, whether the estimator’s method exits successfully or not.

It will only teardown callbacks that are not propagated from a meta-estimator.

Parameters:

**method**method

The method to decorate.

Returns:

**decorated\_method**method

The decorated method.

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.callback.with_callbacks.html#gallery-examples "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------

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