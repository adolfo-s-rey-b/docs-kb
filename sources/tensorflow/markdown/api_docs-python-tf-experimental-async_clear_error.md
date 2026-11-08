[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/experimental/async_clear_error#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/experimental/async_clear_error)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/experimental/async_clear_error?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.experimental.async\_clear\_error Stay organized with collections Save and categorize content based on your preferences.
==========================================================================================================================

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/eager/context.py#L3118-L3139)

Clear pending operations and error statuses in async execution.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.experimental.async_clear_error`](https://www.tensorflow.org/api_docs/python/tf/experimental/async_clear_error)

tf.experimental.async_clear_error()

In async execution mode, an error in op/function execution can lead to errors in subsequent ops/functions that are scheduled but not yet executed. Calling this method clears all pending operations and reset the async execution state.

#### Example:

while True:
      try:
        # Step function updates the metric `loss` internally
        train_step_fn()
      except tf.errors.OutOfRangeError:
        tf.experimental.async_clear_error()
        break
    logging.info('loss = %s', loss.numpy())

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.