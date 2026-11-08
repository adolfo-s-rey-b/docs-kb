[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.utils.parallel.Parallel.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.utils.parallel.Parallel.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.utils.parallel.Parallel.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.utils.parallel.Parallel.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.utils.parallel.Parallel.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.utils.parallel.Parallel.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.utils.parallel.Parallel.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.utils.parallel.Parallel.html)

Collapse Sidebar Expand Sidebar

Parallel[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.parallel.Parallel.html#parallel "Link to this heading")

====================================================================================================================================

class sklearn.utils.parallel.Parallel(_n\_jobs\=default(None)_, _backend\=default(None)_, _return\_as\='list'_, _verbose\=default(0)_, _timeout\=None_, _pre\_dispatch\='2 \* n\_jobs'_, _batch\_size\='auto'_, _temp\_folder\=default(None)_, _max\_nbytes\=default('1M')_, _mmap\_mode\=default('r')_, _prefer\=default(None)_, _require\=default(None)_, _\*\*backend\_kwargs_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/parallel.py#L41)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.parallel.Parallel.html#sklearn.utils.parallel.Parallel "Link to this definition")

Tweak of [`joblib.Parallel`](https://joblib.readthedocs.io/en/latest/generated/joblib.Parallel.html#joblib.Parallel "(in joblib v1.7)")
 that propagates the scikit-learn configuration.

This subclass of [`joblib.Parallel`](https://joblib.readthedocs.io/en/latest/generated/joblib.Parallel.html#joblib.Parallel "(in joblib v1.7)")
 ensures that the active configuration (thread-local) of scikit-learn is propagated to the parallel workers for the duration of the execution of the parallel tasks.

The API does not change and you can refer to [`joblib.Parallel`](https://joblib.readthedocs.io/en/latest/generated/joblib.Parallel.html#joblib.Parallel "(in joblib v1.7)")
 documentation for more details.

Added in version 1.3.

\_\_call\_\_(_iterable_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/parallel.py#L54)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.parallel.Parallel.html#sklearn.utils.parallel.Parallel.__call__ "Link to this definition")

Dispatch the tasks and return the results.

Parameters:

**iterable**iterable

Iterable containing tuples of (delayed\_function, args, kwargs) that should be consumed.

Returns:

**results**list

List of results of the tasks.

dispatch\_next()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/miniforge3/envs/testenv/lib/python3.14/site-packages/joblib/parallel.py#L1468)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.parallel.Parallel.html#sklearn.utils.parallel.Parallel.dispatch_next "Link to this definition")

Dispatch more data for parallel processing

This method is meant to be called concurrently by the multiprocessing callback. We rely on the thread-safety of dispatch\_one\_batch to protect against concurrent consumption of the unprotected iterator.

dispatch\_one\_batch(_iterator_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/miniforge3/envs/testenv/lib/python3.14/site-packages/joblib/parallel.py#L1479)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.parallel.Parallel.html#sklearn.utils.parallel.Parallel.dispatch_one_batch "Link to this definition")

Prefetch the tasks for the next batch and dispatch them.

The effective size of the batch is computed here. If there are no more jobs to dispatch, return False, else return True.

The iterator consumption and dispatching is protected by the same lock so calling this function should be thread safe.

format(_obj_, _indent\=0_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/miniforge3/envs/testenv/lib/python3.14/site-packages/joblib/logger.py#L137)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.parallel.Parallel.html#sklearn.utils.parallel.Parallel.format "Link to this definition")

Return the formatted representation of the object.

print\_progress()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/miniforge3/envs/testenv/lib/python3.14/site-packages/joblib/parallel.py#L1591)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.parallel.Parallel.html#sklearn.utils.parallel.Parallel.print_progress "Link to this definition")

Display the process of the parallel execution only a fraction of time, controlled by self.verbose.

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.parallel.Parallel.html#gallery-examples "Link to this heading")

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