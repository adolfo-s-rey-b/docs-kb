[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/MonitoredSession/StepContext#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   English
*   中文 – 简体

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.train.MonitoredSession.StepContext Stay organized with collections Save and categorize content based on your preferences.
======================================================================================================================================

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/training/monitored_session.py#L840-L875)

Control flow instrument for the `step_fn` from `run_step_fn()`.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.train.SingularMonitoredSession.StepContext`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/MonitoredSession/StepContext)

tf.compat.v1.train.MonitoredSession.StepContext(
        session, run_with_hooks_fn
    )

Users of `step_fn` may perform `run()` calls without running hooks by accessing the `session`. A `run()` call with hooks may be performed using `run_with_hooks()`. Computation flow can be interrupted using `request_stop()`.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `session` | An instance of [`tf.compat.v1.Session`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/Session)<br>. |
| `run_with_hooks_fn` | A function for running fetches and hooks. |

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `session` |     |

Methods
-------

### `request_stop`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/training/monitored_session.py#L867-L875)

request_stop()

Exit the training loop by causing `should_stop()` to return `True`.

Causes `step_fn` to exit by raising an exception.

|     |
| --- |
| Raises |     |
| StopIteration |     |

### `run_with_hooks`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/training/monitored_session.py#L863-L865)

run_with_hooks(
        *args, **kwargs
    )

Same as `MonitoredSession.run`. Accepts the same arguments.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.