[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/SessionRunHook#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/SessionRunHook)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/SessionRunHook?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/SessionRunHook#used-in-the-notebooks)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/SessionRunHook#methods)
    *   [after\_create\_session](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/SessionRunHook#after_create_session)
        
    *   [after\_run](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/SessionRunHook#after_run)
        
    *   [before\_run](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/SessionRunHook#before_run)
        
    *   [begin](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/SessionRunHook#begin)
        
    *   [end](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/SessionRunHook#end)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.train.SessionRunHook Stay organized with collections Save and categorize content based on your preferences.
========================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/SessionRunHook#used-in-the-notebooks)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/SessionRunHook#methods)
    *   [after\_create\_session](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/SessionRunHook#after_create_session)
        
    *   [after\_run](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/SessionRunHook#after_run)
        
    *   [before\_run](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/SessionRunHook#before_run)
        
    *   [begin](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/SessionRunHook#begin)
        
    *   [end](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/SessionRunHook#end)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/training/session_run_hook.py#L93-L182)

Hook to extend calls to MonitoredSession.run().

### Used in the notebooks

| Used in the guide |
| --- |
| *   [Migrate the fault tolerance mechanism](https://www.tensorflow.org/guide/migrate/fault_tolerance)<br>    <br>*   [Migrate SessionRunHook to Keras callbacks](https://www.tensorflow.org/guide/migrate/sessionrunhook_callback) |

Methods
-------

### `after_create_session`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/training/session_run_hook.py#L108-L123)

after_create_session(
        session, coord
    )

Called when new TensorFlow session is created.

This is called to signal the hooks that a new session has been created. This has two essential differences with the situation in which `begin` is called:

*   When this is called, the graph is finalized and ops can no longer be added to the graph.
*   This method will also be called as a result of recovering a wrapped session, not only at the beginning of the overall session.

|     |     |
| --- | --- |
| Args |     |
| `session` | A TensorFlow Session that has been created. |
| `coord` | A Coordinator object which keeps track of all threads. |

### `after_run`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/training/session_run_hook.py#L148-L165)

after_run(
        run_context, run_values
    )

Called after each call to run().

The `run_values` argument contains results of requested ops/tensors by `before_run()`.

The `run_context` argument is the same one send to `before_run` call. `run_context.request_stop()` can be called to stop the iteration.

If `session.run()` raises any exceptions then `after_run()` is not called.

|     |     |
| --- | --- |
| Args |     |
| `run_context` | A `SessionRunContext` object. |
| `run_values` | A SessionRunValues object. |

### `before_run`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/training/session_run_hook.py#L125-L146)

before_run(
        run_context
    )

Called before each call to run().

You can return from this call a `SessionRunArgs` object indicating ops or tensors to add to the upcoming `run()` call. These ops/tensors will be run together with the ops/tensors originally passed to the original run() call. The run args you return can also contain feeds to be added to the run() call.

The `run_context` argument is a `SessionRunContext` that provides information about the upcoming `run()` call: the originally requested op/tensors, the TensorFlow Session.

At this point graph is finalized and you can not add ops.

|     |     |
| --- | --- |
| Args |     |
| `run_context` | A `SessionRunContext` object. |

|     |
| --- |
| Returns |     |
| None or a `SessionRunArgs` object. |     |

### `begin`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/training/session_run_hook.py#L97-L106)

begin()

Called once before using the session.

When called, the default graph is the one that will be launched in the session. The hook can modify the graph by adding new operations to it. After the `begin()` call the graph will be finalized and the other callbacks can not modify the graph anymore. Second call of `begin()` on the same graph, should not change the graph.

### `end`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/training/session_run_hook.py#L167-L182)

end(
        session
    )

Called at the end of session.

The `session` argument can be used in case the hook wants to run final ops, such as saving a last checkpoint.

If `session.run()` raises exception other than OutOfRangeError or StopIteration then `end()` is not called. Note the difference between `end()` and `after_run()` behavior when `session.run()` raises OutOfRangeError or StopIteration. In that case `end()` is called but `after_run()` is not called.

|     |     |
| --- | --- |
| Args |     |
| `session` | A TensorFlow Session that will be soon closed. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.