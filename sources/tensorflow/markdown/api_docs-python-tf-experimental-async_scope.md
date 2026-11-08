[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/experimental/async_scope#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/experimental/async_scope)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/experimental/async_scope?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Yields](https://www.tensorflow.org/api_docs/python/tf/experimental/async_scope#yields)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.experimental.async\_scope Stay organized with collections Save and categorize content based on your preferences.
===================================================================================================================

*   On this page
*   [Yields](https://www.tensorflow.org/api_docs/python/tf/experimental/async_scope#yields)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/eager/context.py#L3054-L3099)

Context manager for grouping async operations.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.experimental.async_scope`](https://www.tensorflow.org/api_docs/python/tf/experimental/async_scope)

@tf_contextlib.contextmanager

Ops/function calls inside the scope can return before finishing the actual execution. When exiting the async scope, a synchronization barrier will be automatically added to ensure the completion of all async op and function execution, potentially raising exceptions if async execution results in an error state.

Users may write the following code to asynchronously invoke `train_step_fn` and log the `loss` metric for every `num_steps` steps in a training loop. `train_step_fn` internally consumes data using `iterator.get_next()`, and may throw OutOfRangeError when running out of data. In the case:

try:
      with tf.experimental.async_scope():
        for _ in range(num_steps):
          # Step function updates the metric `loss` internally
          train_step_fn()
    except tf.errors.OutOfRangeError:
      tf.experimental.async_clear_error()
    logging.info('loss = %s', loss.numpy())

|     |
| --- |
| Yields<br>------ |     |
| Context manager for grouping async operations. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.