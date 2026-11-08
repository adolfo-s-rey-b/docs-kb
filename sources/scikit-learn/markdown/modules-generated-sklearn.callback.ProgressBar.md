[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.callback.ProgressBar.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.callback.ProgressBar.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.callback.ProgressBar.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.callback.ProgressBar.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.callback.ProgressBar.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.callback.ProgressBar.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.callback.ProgressBar.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.callback.ProgressBar.html)

Collapse Sidebar Expand Sidebar

ProgressBar[#](https://scikit-learn.org/stable/modules/generated/sklearn.callback.ProgressBar.html#progressbar "Link to this heading")

=======================================================================================================================================

class sklearn.callback.ProgressBar(_max\_propagation\_depth\=1_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/callback/_progressbar.py#L20)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.callback.ProgressBar.html#sklearn.callback.ProgressBar "Link to this definition")

Callback that displays progress bars for each iterative step of an estimator.

Parameters:

**max\_propagation\_depth**int, default=1

The maximum depth of nested levels of estimators to display progress bars for. 0 means that the progress of only the outermost estimator is displayed. If set to None, all levels are displayed.

Notes

This callback requires rich to be installed.

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.callback.ProgressBar.html#gallery-examples "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_callback_support_thumb.png)

[Supporting callbacks in third party estimators](https://scikit-learn.org/stable/auto_examples/callbacks/plot_callback_support.html)

Supporting callbacks in third party estimators

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_scoring_monitor_thumb.png)

[Analysis of the convergence of penalized logistic regression models](https://scikit-learn.org/stable/auto_examples/callbacks/plot_scoring_monitor.html)

Analysis of the convergence of penalized logistic regression models

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_1_9_0_thumb.png)

[Release Highlights for scikit-learn 1.9](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_9_0.html)

Release Highlights for scikit-learn 1.9

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)