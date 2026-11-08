[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.utils.parallel.delayed.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.utils.parallel.delayed.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.utils.parallel.delayed.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.utils.parallel.delayed.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.utils.parallel.delayed.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.utils.parallel.delayed.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.utils.parallel.delayed.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.utils.parallel.delayed.html)

Collapse Sidebar Expand Sidebar

delayed[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.parallel.delayed.html#delayed "Link to this heading")

=================================================================================================================================

sklearn.utils.parallel.delayed(_function_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/parallel.py#L95)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.parallel.delayed.html#sklearn.utils.parallel.delayed "Link to this definition")

Decorator used to capture the arguments of a function.

This alternative to `joblib.delayed` is meant to be used in conjunction with `sklearn.utils.parallel.Parallel`. The latter captures the scikit- learn configuration by calling `sklearn.get_config()` in the current thread, prior to dispatching the first task. The captured configuration is then propagated and enabled for the duration of the execution of the delayed function in the joblib workers.

Changed in version 1.3: `delayed` was moved from `sklearn.utils.fixes` to `sklearn.utils.parallel` in scikit-learn 1.3.

Parameters:

**function**callable

The function to be delayed.

Returns:

output: tuple

Tuple containing the delayed function, the positional arguments, and the keyword arguments.

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.parallel.delayed.html#gallery-examples "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------

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