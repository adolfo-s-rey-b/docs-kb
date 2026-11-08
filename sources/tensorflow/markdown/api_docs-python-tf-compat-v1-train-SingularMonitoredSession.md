[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/SingularMonitoredSession#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/SingularMonitoredSession)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/SingularMonitoredSession?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fcompat%2Fv1%2Ftrain%2FSingularMonitoredSession&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Migrate to TF2](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/SingularMonitoredSession#migrate-to-tf2)
    
*   [Description](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/SingularMonitoredSession#description)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/SingularMonitoredSession#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/SingularMonitoredSession#attributes)
    
*   [Child Classes](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/SingularMonitoredSession#child_classes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/SingularMonitoredSession#methods)
    *   [close](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/SingularMonitoredSession#close)
        
    *   [raw\_session](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/SingularMonitoredSession#raw_session)
        
    *   [run](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/SingularMonitoredSession#run)
        
    *   [run\_step\_fn](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/SingularMonitoredSession#run_step_fn)
        
    *   [should\_stop](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/SingularMonitoredSession#should_stop)
        
    *   [\_\_enter\_\_](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/SingularMonitoredSession#__enter__)
        
    *   [\_\_exit\_\_](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/SingularMonitoredSession#__exit__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.train.SingularMonitoredSession Stay organized with collections Save and categorize content based on your preferences.
==================================================================================================================================

*   On this page
*   [Migrate to TF2](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/SingularMonitoredSession#migrate-to-tf2)
    
*   [Description](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/SingularMonitoredSession#description)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/SingularMonitoredSession#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/SingularMonitoredSession#attributes)
    
*   [Child Classes](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/SingularMonitoredSession#child_classes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/SingularMonitoredSession#methods)
    *   [close](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/SingularMonitoredSession#close)
        
    *   [raw\_session](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/SingularMonitoredSession#raw_session)
        
    *   [run](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/SingularMonitoredSession#run)
        
    *   [run\_step\_fn](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/SingularMonitoredSession#run_step_fn)
        
    *   [should\_stop](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/SingularMonitoredSession#should_stop)
        
    *   [\_\_enter\_\_](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/SingularMonitoredSession#__enter__)
        
    *   [\_\_exit\_\_](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/SingularMonitoredSession#__exit__)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/training/monitored_session.py#L1057-L1160)

Session-like object that handles initialization, restoring, and hooks.

tf.compat.v1.train.SingularMonitoredSession(
        hooks=None,
        scaffold=None,
        master='',
        config=None,
        checkpoint_dir=None,
        stop_grace_period_secs=120,
        checkpoint_filename_with_path=None
    )

Migrate to TF2
--------------

This API is not compatible with eager execution and [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)
. To migrate to TF2, rewrite the code to be compatible with eager execution. Check the [migration guide](https://www.tensorflow.org/guide/migrate#1_replace_v1sessionrun_calls)
 on replacing `Session.run` calls. In Keras, session hooks can be replaced by Callbacks e.g. [logging hook notebook](https://github.com/tensorflow/docs/blob/master/site/en/guide/migrate/logging_stop_hook.ipynb)
 For more details please read [Better performance with tf.function](https://www.tensorflow.org/guide/function)
.

Description
-----------

Please note that this utility is not recommended for distributed settings. For distributed settings, please use [`tf.compat.v1.train.MonitoredSession`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/MonitoredSession)
. The differences between `MonitoredSession` and `SingularMonitoredSession` are:

*   `MonitoredSession` handles `AbortedError` and `UnavailableError` for distributed settings, but `SingularMonitoredSession` does not.
*   `MonitoredSession` can be created in `chief` or `worker` modes. `SingularMonitoredSession` is always created as `chief`.
*   You can access the raw [`tf.compat.v1.Session`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/Session)
     object used by `SingularMonitoredSession`, whereas in MonitoredSession the raw session is private. This can be used:
    *   To `run` without hooks.
    *   To save and restore.
*   All other functionality is identical.

#### Example usage:

saver_hook = CheckpointSaverHook(...)
    summary_hook = SummarySaverHook(...)
    with SingularMonitoredSession(hooks=[saver_hook, summary_hook]) as sess:
      while not sess.should_stop():
        sess.run(train_op)

Initialization: At creation time the hooked session does following things in given order:

*   calls `hook.begin()` for each given hook
*   finalizes the graph via `scaffold.finalize()`
*   create session
*   initializes the model via initialization ops provided by `Scaffold`
*   restores variables if a checkpoint exists
*   launches queue runners

Run: When `run()` is called, the hooked session does following things:

*   calls `hook.before_run()`
*   calls TensorFlow `session.run()` with merged fetches and feed\_dict
*   calls `hook.after_run()`
*   returns result of `session.run()` asked by user

Exit: At the `close()`, the hooked session does following things in order:

*   calls `hook.end()`
*   closes the queue runners and the session
*   suppresses `OutOfRange` error which indicates that all inputs have been processed if the `SingularMonitoredSession` is used as a context.

|     |     |     |
| --- | --- | --- |
| Args<br>---- |     |
| `hooks` | An iterable of `SessionRunHook' objects. </td> </tr><tr> <td>`scaffold`<a id="scaffold"></a> </td> <td> A`Scaffold`used for gathering or building supportive ops. If not specified a default one is created. It's used to finalize the graph. </td> </tr><tr> <td>`master`<a id="master"></a> </td> <td>`String`representation of the TensorFlow master to use. </td> </tr><tr> <td>`config`<a id="config"></a> </td> <td>`ConfigProto`proto used to configure the session. </td> </tr><tr> <td>`checkpoint\_dir`<a id="checkpoint_dir"></a> </td> <td> A string. Optional path to a directory where to restore variables. </td> </tr><tr> <td>`stop\_grace\_period\_secs`<a id="stop_grace_period_secs"></a> </td> <td> Number of seconds given to threads to stop after`close()`has been called. </td> </tr><tr> <td>`checkpoint\_filename\_with\_path\` | A string. Optional path to a checkpoint file from which to restore variables. |

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `graph` | The graph that was launched in this session. |

Child Classes
-------------

[`class StepContext`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/MonitoredSession/StepContext)

Methods
-------

### `close`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/training/monitored_session.py#L880-L881)

close()

### `raw_session`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/training/monitored_session.py#L1158-L1160)

raw_session()

Returns underlying `TensorFlow.Session` object.

### `run`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/training/monitored_session.py#L764-L782)

run(
        fetches, feed_dict=None, options=None, run_metadata=None
    )

Run ops in the monitored session.

This method is completely compatible with the `tf.Session.run()` method.

|     |     |
| --- | --- |
| Args |     |
| `fetches` | Same as `tf.Session.run()`. |
| `feed_dict` | Same as `tf.Session.run()`. |
| `options` | Same as `tf.Session.run()`. |
| `run_metadata` | Same as `tf.Session.run()`. |

|     |
| --- |
| Returns |     |
| Same as `tf.Session.run()`. |     |

### `run_step_fn`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/training/monitored_session.py#L784-L838)

run_step_fn(
        step_fn
    )

Run ops using a step function.

|     |     |
| --- | --- |
| Args |     |
| `step_fn` | A function or a method with a single argument of type `StepContext`. The function may use methods of the argument to perform computations with access to a raw session. The returned value of the `step_fn` will be returned from `run_step_fn`, unless a stop is requested. In that case, the next `should_stop` call will return True. Example usage:<br><br>```python<br>    with tf.Graph().as_default():<br>      c = tf.compat.v1.placeholder(dtypes.float32)<br>      v = tf.add(c, 4.0)<br>      w = tf.add(c, 0.5)<br>      def step_fn(step_context):<br>        a = step_context.session.run(fetches=v, feed_dict={c: 0.5})<br>        if a <= 4.5:<br>          step_context.request_stop()<br>          return step_context.run_with_hooks(fetches=w,<br>                                             feed_dict={c: 0.1})<br>    <br>      with tf.MonitoredSession() as session:<br>        while not session.should_stop():<br>          a = session.run_step_fn(step_fn)<br>    ```<br>    Hooks interact with the `run_with_hooks()` call inside the<br>         `step_fn` as they do with a `MonitoredSession.run` call. |

|     |
| --- |
| Returns |     |
| Returns the returned value of `step_fn`. |     |

|     |     |
| --- | --- |
| Raises |     |
| `StopIteration` | if `step_fn` has called `request_stop()`. It may be caught by `with tf.MonitoredSession()` to close the session. |
| `ValueError` | if `step_fn` doesn't have a single argument called `step_context`. It may also optionally have `self` for cases when it belongs to an object. |

### `should_stop`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/training/monitored_session.py#L877-L878)

should_stop()

### `__enter__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/training/monitored_session.py#L883-L884)

__enter__()

### `__exit__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/training/monitored_session.py#L886-L891)

__exit__(
        exception_type, exception_value, traceback
    )

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.