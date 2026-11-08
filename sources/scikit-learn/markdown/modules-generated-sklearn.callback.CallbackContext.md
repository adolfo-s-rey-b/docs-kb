[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.callback.CallbackContext.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.callback.CallbackContext.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.callback.CallbackContext.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.callback.CallbackContext.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.callback.CallbackContext.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.callback.CallbackContext.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.callback.CallbackContext.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.callback.CallbackContext.html)

Collapse Sidebar Expand Sidebar

CallbackContext[#](https://scikit-learn.org/stable/modules/generated/sklearn.callback.CallbackContext.html#callbackcontext "Link to this heading")

===================================================================================================================================================

class sklearn.callback.CallbackContext[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/callback/_callback_context.py#L21)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.callback.CallbackContext.html#sklearn.callback.CallbackContext "Link to this definition")

Task level context for the callbacks.

This class is responsible for managing the callbacks and holding the tree structure of an estimator’s tasks. Each instance corresponds to a task of the estimator.

This class should not be instantiated directly, but through the `_init_callback_context` method of the estimator to create the root context or using the `subcontext` method of this class to create sub-contexts.

These contexts are passed to the callback hooks to be able to keep track of the position of a task in the task tree from within the callbacks.

Attributes:

**task\_name**str

The name of the task this context is responsible for.

**task\_id**int

The identifier of the task this context is responsible for. It uniquely identifies the task among its siblings.

**max\_subtasks**int or None

The maximum number of children tasks for this task. 0 means it’s a leaf. None means the maximum number of subtasks is not known in advance.

**sequential\_subtasks**bool

Whether this context’s subtasks are sequential. When True, children contexts’ have consecutive integer task\_ids starting from 0.

**estimator\_name**str

The name of the estimator that holds this context.

**parent**CallbackContext or None

The parent context of this context. None if this context is the root.

**root\_uuid**uuid.UUID instance

The UUID of the root context. All contexts in the same task tree have the same root UUID that is used to identify the task tree itself.

**init\_time**datetime.datetime

The time when the context was initialised, in the UTC timezone.

**source\_estimator\_name**str or None

The name of the estimator that holds the parent task this task was merged with. None if it was not merged with another context.

**source\_task\_name**str or None

The task name of the parent task this task was merged with. None if it was not merged with another context.

call\_on\_fit\_task\_begin(_\*_, _estimator_, _X\=None_, _y\=None_, _metadata\=None_, _reconstruction\_attributes\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/callback/_callback_context.py#L365)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.callback.CallbackContext.html#sklearn.callback.CallbackContext.call_on_fit_task_begin "Link to this definition")

Call the `on_fit_task_begin` hook of the callbacks.

Parameters:

**estimator**estimator instance

The estimator calling the callback hook.

**X**array-like or None, default=None

The training data of the current task.

**y**array-like or None, default=None

The training targets of the current task.

**metadata**dict or None, default=None

A dictionary containing training metadata for the current task.

**reconstruction\_attributes**dict or None, default=None

A dictionary of the sufficient fitted attributes needed to construct a `fitted_estimator` from the current state of the estimator, i.e. an estimator instance ready to predict, transform, etc … as if the fit had stopped at the beginning of this task. The `fitted_estimator` is the object that will be passed to the callbacks, if required.

call\_on\_fit\_task\_end(_\*_, _estimator_, _X\=None_, _y\=None_, _metadata\=None_, _reconstruction\_attributes\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/callback/_callback_context.py#L407)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.callback.CallbackContext.html#sklearn.callback.CallbackContext.call_on_fit_task_end "Link to this definition")

Call the `on_fit_task_end` hook of the callbacks.

Parameters:

**estimator**estimator instance

The estimator calling the callback hook.

**X**array-like or None, default=None

The training data of the current task.

**y**array-like or None, default=None

The training targets of the current task.

**metadata**dict or None, default=None

A dictionary containing training metadata of the current task.

**reconstruction\_attributes**dict or None, default=None

A dictionary of the sufficient fitted attributes needed to construct a `fitted_estimator` from the current state of the estimator, i.e. an estimator instance ready to predict, transform, etc … as if the fit had stopped at the end of this task. The `fitted_estimator` is the object that will be passed to the callbacks, if required.

Returns:

**stop**bool

Whether or not to stop the current level of iterations at this end of this task.

propagate\_callback\_context(_sub\_estimator_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/callback/_callback_context.py#L454)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.callback.CallbackContext.html#sklearn.callback.CallbackContext.propagate_callback_context "Link to this definition")

Propagate the context and callbacks to a sub-estimator.

Clear the propagated callbacks from the sub-estimator on exit.

Only auto-propagated callbacks are propagated to the sub-estimator. An error is raised if the sub-estimator already holds auto-propagated callbacks.

The sub-estimator receives this context as an attribute named `_parent_callback_ctx` so that the meta-estimator’s task tree can be merged with the sub-estimator’s one.

Parameters:

**sub\_estimator**estimator instance

The estimator to propagate the callbacks and context to.

subcontext(_task\_name\=''_, _task\_id\=None_, _max\_subtasks\=0_, _sequential\_subtasks\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/callback/_callback_context.py#L243)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.callback.CallbackContext.html#sklearn.callback.CallbackContext.subcontext "Link to this definition")

Create a context for a subtask of the current task.

Parameters:

**task\_name**str, default=””

The name of the subtask.

**task\_id**int or None, default=None

An identifier of the subtask. It must be distinct from the task\_ids of its siblings. If None, task\_id is automatically set to the next available integer task\_id.

**max\_subtasks**int or None, default=0

The maximum number of tasks that can be children of the subtask. 0 means it’s a leaf. None means the maximum number of subtasks is not known in advance.

**sequential\_subtasks**bool, default=True

Whether the new context’s subtasks are sequential. If True, children contexts of the new context, created via `subcontext`, will have automatically assigned consecutive integer task\_ids starting from 0.

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)