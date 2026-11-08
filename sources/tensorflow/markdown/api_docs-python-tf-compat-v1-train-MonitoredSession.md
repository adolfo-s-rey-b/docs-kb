[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/MonitoredSession#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/MonitoredSession)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/MonitoredSession?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Migrate to TF2](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/MonitoredSession#migrate-to-tf2)
    
*   [Description](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/MonitoredSession#description)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/MonitoredSession#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/MonitoredSession#returns)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/MonitoredSession#attributes)
    
*   [Child Classes](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/MonitoredSession#child_classes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/MonitoredSession#methods)
    *   [close](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/MonitoredSession#close)
        
    *   [run](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/MonitoredSession#run)
        
    *   [run\_step\_fn](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/MonitoredSession#run_step_fn)
        
    *   [should\_stop](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/MonitoredSession#should_stop)
        
    *   [\_\_enter\_\_](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/MonitoredSession#__enter__)
        
    *   [\_\_exit\_\_](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/MonitoredSession#__exit__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.train.MonitoredSession Stay organized with collections Save and categorize content based on your preferences.
==========================================================================================================================

*   On this page
*   [Migrate to TF2](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/MonitoredSession#migrate-to-tf2)
    
*   [Description](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/MonitoredSession#description)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/MonitoredSession#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/MonitoredSession#returns)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/MonitoredSession#attributes)
    
*   [Child Classes](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/MonitoredSession#child_classes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/MonitoredSession#methods)
    *   [close](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/MonitoredSession#close)
        
    *   [run](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/MonitoredSession#run)
        
    *   [run\_step\_fn](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/MonitoredSession#run_step_fn)
        
    *   [should\_stop](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/MonitoredSession#should_stop)
        
    *   [\_\_enter\_\_](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/MonitoredSession#__enter__)
        
    *   [\_\_exit\_\_](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/MonitoredSession#__exit__)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/training/monitored_session.py#L957-L1054)

Session-like object that handles initialization, recovery and hooks.

tf.compat.v1.train.MonitoredSession(
        session_creator=None, hooks=None, stop_grace_period_secs=120
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

#### Example usage:

saver_hook = CheckpointSaverHook(...)
    summary_hook = SummarySaverHook(...)
    with MonitoredSession(session_creator=ChiefSessionCreator(...),
                          hooks=[saver_hook, summary_hook]) as sess:
      while not sess.should_stop():
        sess.run(train_op)

Initialization: At creation time the monitored session does following things in given order:

*   calls `hook.begin()` for each given hook
*   finalizes the graph via `scaffold.finalize()`
*   create session
*   initializes the model via initialization ops provided by `Scaffold`
*   restores variables if a checkpoint exists
*   launches queue runners
*   calls `hook.after_create_session()`

Run: When `run()` is called, the monitored session does following things:

*   calls `hook.before_run()`
*   calls TensorFlow `session.run()` with merged fetches and feed\_dict
*   calls `hook.after_run()`
*   returns result of `session.run()` asked by user
*   if `AbortedError` or `UnavailableError` occurs, it recovers or reinitializes the session before executing the run() call again

Exit: At the `close()`, the monitored session does following things in order:

*   calls `hook.end()`
*   closes the queue runners and the session
*   suppresses `OutOfRange` error which indicates that all inputs have been processed if the monitored\_session is used as a context

How to set [`tf.compat.v1.Session`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/Session)
 arguments:

*   In most cases you can set session arguments as follows:

MonitoredSession(
      session_creator=ChiefSessionCreator(master=..., config=...))

*   In distributed setting for a non-chief worker, you can use following:

MonitoredSession(
      session_creator=WorkerSessionCreator(master=..., config=...))

See `MonitoredTrainingSession` for an example usage based on chief or worker.

*   it cannot be set as default session.
*   it cannot be sent to saver.save.
*   it cannot be sent to tf.train.start\_queue\_runners.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `session_creator` | A factory object to create session. Typically a `ChiefSessionCreator` which is the default one. |
| `hooks` | An iterable of \`SessionRunHook' objects. |

|     |
| --- |
| Returns<br>------- |     |
| A MonitoredSession object. |     |

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