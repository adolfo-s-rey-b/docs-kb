[Skip to main content](https://scikit-learn.org/stable/api/sklearn.callback.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/api/sklearn.callback.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/api/sklearn.callback.html)
[1.8.0](https://scikit-learn.org/1.8/api/sklearn.callback.html)
[1.7.2](https://scikit-learn.org/1.7/api/sklearn.callback.html)
[1.6.1](https://scikit-learn.org/1.6/api/sklearn.callback.html)
[1.5.2](https://scikit-learn.org/1.5/api/sklearn.callback.html)
[1.4.2](https://scikit-learn.org/1.4/api/sklearn.callback.html)

Collapse Sidebar Expand Sidebar

sklearn.callback[#](https://scikit-learn.org/stable/api/sklearn.callback.html#module-sklearn.callback "Link to this heading")

==============================================================================================================================

The [`sklearn.callback`](https://scikit-learn.org/stable/api/sklearn.callback.html#module-sklearn.callback "sklearn.callback")
 module implements the framework and off the shelf callbacks for scikit-learn estimators.

|     |     |
| --- | --- |
| [`AutoPropagatedCallback`](https://scikit-learn.org/stable/modules/generated/sklearn.callback.AutoPropagatedCallback.html#sklearn.callback.AutoPropagatedCallback "sklearn.callback.AutoPropagatedCallback") | Protocol for the auto-propagated callbacks |
| [`CallbackContext`](https://scikit-learn.org/stable/modules/generated/sklearn.callback.CallbackContext.html#sklearn.callback.CallbackContext "sklearn.callback.CallbackContext") | Task level context for the callbacks. |
| [`CallbackSupportMixin`](https://scikit-learn.org/stable/modules/generated/sklearn.callback.CallbackSupportMixin.html#sklearn.callback.CallbackSupportMixin "sklearn.callback.CallbackSupportMixin") | Mixin class to add callback support to an estimator. |
| [`FitCallback`](https://scikit-learn.org/stable/modules/generated/sklearn.callback.FitCallback.html#sklearn.callback.FitCallback "sklearn.callback.FitCallback") | Protocol for the callbacks evaluated on tasks during the fit of an estimator. |
| [`ProgressBar`](https://scikit-learn.org/stable/modules/generated/sklearn.callback.ProgressBar.html#sklearn.callback.ProgressBar "sklearn.callback.ProgressBar") | Callback that displays progress bars for each iterative step of an estimator. |
| [`ScoringMonitor`](https://scikit-learn.org/stable/modules/generated/sklearn.callback.ScoringMonitor.html#sklearn.callback.ScoringMonitor "sklearn.callback.ScoringMonitor") | Callback that monitors a score for each iterative step of an estimator. |
| [`ScoringMonitorLog`](https://scikit-learn.org/stable/modules/generated/sklearn.callback.ScoringMonitorLog.html#sklearn.callback.ScoringMonitorLog "sklearn.callback.ScoringMonitorLog") | Log for one run of a scoring monitor. |
| [`with_callbacks`](https://scikit-learn.org/stable/modules/generated/sklearn.callback.with_callbacks.html#sklearn.callback.with_callbacks "sklearn.callback.with_callbacks") | Decorator to run the method within a callback context manager. |