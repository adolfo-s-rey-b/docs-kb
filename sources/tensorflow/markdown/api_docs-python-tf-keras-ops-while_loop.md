[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/ops/while_loop#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/ops/while_loop)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/ops/while_loop?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/while_loop#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/while_loop#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.ops.while\_loop Stay organized with collections Save and categorize content based on your preferences.
===============================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/while_loop#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/while_loop#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/core.py#L614-L665)

While loop implementation.

tf.keras.ops.while_loop(
        cond, body, loop_vars, maximum_iterations=None
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `cond` | A callable that represents the termination condition of the loop. Must accept a `loop_vars` like structure as an argument. If `loop_vars` is a tuple or list, each element of `loop_vars` will be passed positionally to the callable. |
| `body` | A callable that represents the loop body. Must accept a `loop_vars` like structure as an argument, and return update value with the same structure. If `loop_vars` is a tuple or list, each element of `loop_vars` will be passed positionally to the callable. |
| `loop_vars` | An arbitrary nested structure of tensor state to persist across loop iterations. |
| `maximum_iterations` | Optional maximum number of iterations of the while loop to run. If provided, the `cond` output is AND-ed with an additional condition ensuring the number of iterations executed is no greater than `maximum_iterations`. |

|     |
| --- |
| Returns<br>------- |     |
| A list/tuple of tensors, has the same shape and dtype as `inputs`. |     |

#### Examples:

    i = 0

    x, y = 0, 1

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.