[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.callback.ScoringMonitorLog.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.callback.ScoringMonitorLog.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.callback.ScoringMonitorLog.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.callback.ScoringMonitorLog.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.callback.ScoringMonitorLog.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.callback.ScoringMonitorLog.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.callback.ScoringMonitorLog.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.callback.ScoringMonitorLog.html)

Collapse Sidebar Expand Sidebar

ScoringMonitorLog[#](https://scikit-learn.org/stable/modules/generated/sklearn.callback.ScoringMonitorLog.html#scoringmonitorlog "Link to this heading")

=========================================================================================================================================================

class sklearn.callback.ScoringMonitorLog(_run\_id: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "(in Python v3.14)")
_, _estimator\_name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")
_, _timestamp: [datetime](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.14)")
_, _data: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")
\[[dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")\
\]_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/callback/_scoring_monitor.py#L15)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.callback.ScoringMonitorLog.html#sklearn.callback.ScoringMonitorLog "Link to this definition")

Log for one run of a scoring monitor.

The recorded scores are accessed through the `data` attribute, as a list of dicts, or the `data_as_pandas` attribute, as a Pandas DataFrame. In the former case, each dict corresponds to one row of the corresponding DataFrame and contains column\_name -> value pairs. The columns are structured as follows:

*   `task_id_path`: tuple containing the task ids from the root task to the task for which the score was computed. Each value in this column is unique.
    
*   `parent_task_id_path`: tuple containing the task ids from the root to the parent task. It can be used to group scores from tasks that have the same parent task.
    
*   `estimator_name`: the name of the estimator.
    
*   `task_name`: the name of the task.
    
*   `task_id`: the id of the task.
    
*   `sequential_subtasks`: whether the task has sequential subtasks.
    
*   A column for each score name that was passed as `scoring` parameter.
    

Attributes:

**run\_id**uuid.UUID

The unique identifier for the run.

**estimator\_name**str

The name of the estimator for the run.

**timestamp**datetime.datetime

The timestamp of the start of the run.

**data**list\[dict\]

The recorded scores for the run.

**data\_as\_pandas**pandas.DataFrame

The recorded scores for the run as a Pandas DataFrame.

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)