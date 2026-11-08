[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.callback.ScoringMonitor.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.callback.ScoringMonitor.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.callback.ScoringMonitor.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.callback.ScoringMonitor.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.callback.ScoringMonitor.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.callback.ScoringMonitor.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.callback.ScoringMonitor.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.callback.ScoringMonitor.html)

Collapse Sidebar Expand Sidebar

ScoringMonitor[#](https://scikit-learn.org/stable/modules/generated/sklearn.callback.ScoringMonitor.html#scoringmonitor "Link to this heading")

================================================================================================================================================

class sklearn.callback.ScoringMonitor(_\*_, _scoring_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/callback/_scoring_monitor.py#L76)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.callback.ScoringMonitor.html#sklearn.callback.ScoringMonitor "Link to this definition")

Callback that monitors a score for each iterative step of an estimator.

The specified scorer is called on the training data at each iterative step of the estimator, and the score is logged by the callback. The logs can be retrieved through the `get_logs` method.

Parameters:

**scoring**str, callable, list, tuple, dict or None

The scoring method to use to monitor the model.

If `scoring` represents a single score, one can use:

*   a single string (see [String name scorers](https://scikit-learn.org/stable/modules/model_evaluation.html#scoring-string-names)
    );
    
*   a callable (see [Callable scorers](https://scikit-learn.org/stable/modules/model_evaluation.html#scoring-callable)
    ) that returns a single value;
    
*   `None`, the `estimator`’s [default evaluation criterion](https://scikit-learn.org/stable/modules/model_evaluation.html#scoring-api-overview)
     is used.
    

If `scoring` represents multiple scores, one can use:

*   a list or tuple of unique strings;
    
*   a callable returning a dictionary where the keys are the metric names and the values are the metric scores;
    
*   a dictionary with metric names as keys and callables as values.
    

get\_logs(_select\='most\_recent'_, _include\_lineage\=False_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/callback/_scoring_monitor.py#L192)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.callback.ScoringMonitor.html#sklearn.callback.ScoringMonitor.get_logs "Link to this definition")

Retrieve the logged scores.

Log entries are grouped by runs, which are the outermost enclosing fit calls. If the estimator this callback is registered on is wrapped in meta-estimators, a run corresponds to one fit of the outermost meta-estimator. If it is not wrapped in a meta-estimator, a run simply corresponds to a single fit of the estimator.

For a given run, the scores are logged in a [`ScoringMonitorLog`](https://scikit-learn.org/stable/modules/generated/sklearn.callback.ScoringMonitorLog.html#sklearn.callback.ScoringMonitorLog "sklearn.callback.ScoringMonitorLog")
 object containing:

*   `run_id`: a unique identifier for the run;
    
*   `estimator_name`: the name of the (meta-)estimator of the run;
    
*   `timestamp`: the timestamp of the start of the run;
    
*   `data`: the recorded scores for the run. Each score value is associated with the context of the task for which the score was computed;
    
*   `data_as_pandas`: the recorded scores as a Pandas DataFrame.
    

See [`ScoringMonitorLog`](https://scikit-learn.org/stable/modules/generated/sklearn.callback.ScoringMonitorLog.html#sklearn.callback.ScoringMonitorLog "sklearn.callback.ScoringMonitorLog")
 for more details about the structure of the recorded scores.

Parameters:

**select**{“all”, “most\_recent”}, default=”most\_recent”

Which log run to return:

*   `"all"`: return the logged scores for all runs;
    
*   `"most_recent"`: return the logged scores for the most recent run.
    

**include\_lineage**bool, default=False

Whether to include lineage information of the tasks in the log.

If set to True, the log contains extra rows for each task that is an ancestor of a task for which the score was computed. These extra rows can be used to retrieve the context of all ancestor tasks of a given task for which the score was computed. For these extra rows, there are no score entries if `as_frame` is False, or NaN values if `as_frame` is True.

Returns:

**logs**[`ScoringMonitorLog`](https://scikit-learn.org/stable/modules/generated/sklearn.callback.ScoringMonitorLog.html#sklearn.callback.ScoringMonitorLog "sklearn.callback.ScoringMonitorLog")
 or list of [`ScoringMonitorLog`](https://scikit-learn.org/stable/modules/generated/sklearn.callback.ScoringMonitorLog.html#sklearn.callback.ScoringMonitorLog "sklearn.callback.ScoringMonitorLog")

The logged scores. If `select=="most_recent"`, returns a single [`ScoringMonitorLog`](https://scikit-learn.org/stable/modules/generated/sklearn.callback.ScoringMonitorLog.html#sklearn.callback.ScoringMonitorLog "sklearn.callback.ScoringMonitorLog")
 object. Otherwise, returns the list of all run logs.

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.callback.ScoringMonitor.html#gallery-examples "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------

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