[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/test/experimental/sync_devices#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/test/experimental/sync_devices)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/test/experimental/sync_devices?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/test/experimental/sync_devices#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.test.experimental.sync\_devices Stay organized with collections Save and categorize content based on your preferences.
=========================================================================================================================

*   On this page
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/test/experimental/sync_devices#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/test_util.py#L4257-L4310)

Synchronizes all devices.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.test.experimental.sync_devices`](https://www.tensorflow.org/api_docs/python/tf/test/experimental/sync_devices)

tf.test.experimental.sync_devices() -> None

By default, GPUs run asynchronously. This means that when you run an op on the GPU, like [`tf.linalg.matmul`](https://www.tensorflow.org/api_docs/python/tf/linalg/matmul)
, the op may still be running on the GPU when the function returns. Non-GPU devices can also be made to run asynchronously by calling [`tf.config.experimental.set_synchronous_execution(False)`](https://www.tensorflow.org/api_docs/python/tf/config/experimental/set_synchronous_execution)
. Calling `sync_devices()` blocks until pending ops have finished executing. This is primarily useful for measuring performance during a benchmark.

For example, here is how you can measure how long [`tf.linalg.matmul`](https://www.tensorflow.org/api_docs/python/tf/linalg/matmul)
 runs:

    import time

If the call to `sync_devices()` was omitted, the time printed could be too small. This is because the op could still be running asynchronously when the line `end = time.time()` is executed.

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `RuntimeError` | If run outside Eager mode. This must be called in Eager mode, outside any [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)<br>s. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.