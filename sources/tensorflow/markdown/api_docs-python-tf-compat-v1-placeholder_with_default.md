[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/placeholder_with_default#main-content)

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
    

tf.compat.v1.placeholder\_with\_default Stay organized with collections Save and categorize content based on your preferences.
==============================================================================================================================

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/array_ops.py#L3031-L3080)

A placeholder op that passes through `input` when its output is not fed.

tf.compat.v1.placeholder_with_default(
        input, shape, name=None
    )

Migrate to TF2
--------------

This API is strongly discouraged for use with eager execution and [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)
. The primary use of this API is for testing computation wrapped within a [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)
 where the input tensors might not have statically known fully-defined shapes. The same can be achieved by creating a [concrete function](https://www.tensorflow.org/guide/function#obtaining_concrete_functions)
 from the [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)
 with a [`tf.TensorSpec`](https://www.tensorflow.org/api_docs/python/tf/TensorSpec)
 input which has partially defined shapes. For example, the code

    @tf.function

    f()

can easily be replaced by

    @tf.function

    g = f.get_concrete_function(tf.TensorSpec([None, 3]))

You can learn more about [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)
 at [Better performance with tf.function](https://www.tensorflow.org/guide/function)
.

Description
-----------

|     |     |
| --- | --- |
| Args<br>---- |     |
| `input` | A `Tensor`. The default value to produce when output is not fed. |
| `shape` | A [`tf.TensorShape`](https://www.tensorflow.org/api_docs/python/tf/TensorShape)<br> or list of `int`s. The (possibly partial) shape of the tensor. |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| A `Tensor`. Has the same type as `input`. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.