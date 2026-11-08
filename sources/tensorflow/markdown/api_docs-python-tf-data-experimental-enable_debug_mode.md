[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/data/experimental/enable_debug_mode#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/data/experimental/enable_debug_mode)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/data/experimental/enable_debug_mode?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/data/experimental/enable_debug_mode#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.data.experimental.enable\_debug\_mode Stay organized with collections Save and categorize content based on your preferences.
===============================================================================================================================

*   On this page
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/data/experimental/enable_debug_mode#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/data/ops/debug_mode.py#L24-L72)

Enables debug mode for tf.data.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.data.experimental.enable_debug_mode`](https://www.tensorflow.org/api_docs/python/tf/data/experimental/enable_debug_mode)

tf.data.experimental.enable_debug_mode()

Example usage with pdb module:

import tensorflow as tf
    import pdb
    
    tf.data.experimental.enable_debug_mode()
    
    def func(x):
      # Python 3.7 and older requires `pdb.Pdb(nosigint=True).set_trace()`
      pdb.set_trace()
      x = x + 1
      return x
    
    dataset = tf.data.Dataset.from_tensor_slices([1, 2, 3])
    dataset = dataset.map(func)
    
    for item in dataset:
      print(item)

The effect of debug mode is two-fold:

1) Any transformations that would introduce asynchrony, parallelism, or non-determinism to the input pipeline execution will be forced to execute synchronously, sequentially, and deterministically.

2) Any user-defined functions passed into tf.data transformations such as `map` will be wrapped in [`tf.py_function`](https://www.tensorflow.org/api_docs/python/tf/py_function)
 so that their body is executed "eagerly" as a Python function as opposed to a traced TensorFlow graph, which is the default behavior. Note that even when debug mode is enabled, the user-defined function is still traced to infer the shape and type of its outputs; as a consequence, any `print` statements or breakpoints will be triggered once during the tracing before the actual execution of the input pipeline.

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | When invoked from graph mode. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.