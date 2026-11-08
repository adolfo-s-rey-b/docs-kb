[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/ragged/placeholder#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/ragged/placeholder)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/ragged/placeholder?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Migrate to TF2](https://www.tensorflow.org/api_docs/python/tf/compat/v1/ragged/placeholder#migrate-to-tf2)
    
*   [Description](https://www.tensorflow.org/api_docs/python/tf/compat/v1/ragged/placeholder#description)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/ragged/placeholder#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/ragged/placeholder#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/ragged/placeholder#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.ragged.placeholder Stay organized with collections Save and categorize content based on your preferences.
======================================================================================================================

*   On this page
*   [Migrate to TF2](https://www.tensorflow.org/api_docs/python/tf/compat/v1/ragged/placeholder#migrate-to-tf2)
    
*   [Description](https://www.tensorflow.org/api_docs/python/tf/compat/v1/ragged/placeholder#description)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/ragged/placeholder#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/ragged/placeholder#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/ragged/placeholder#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/ragged/ragged_factory_ops.py#L338-L386)

Creates a placeholder for a [`tf.RaggedTensor`](https://www.tensorflow.org/api_docs/python/tf/RaggedTensor)
 that will always be fed.

tf.compat.v1.ragged.placeholder(
        dtype, ragged_rank, value_shape=None, name=None
    )

Migrate to TF2
--------------

This API is not compatible with eager execution and [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)
. To migrate to TF2, rewrite the code to be compatible with eager execution. Check the [migration guide](https://www.tensorflow.org/guide/migrate#1_replace_v1sessionrun_calls)
 on replacing `Session.run` calls. In TF2, you can just pass tensors directly into ops and layers. If you want to explicitly set up your inputs, also see [Keras functional API](https://www.tensorflow.org/guide/keras/functional)
 on how to use [`tf.keras.Input`](https://www.tensorflow.org/api_docs/python/tf/keras/Input)
 to replace [`tf.compat.v1.ragged.placeholder`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/ragged/placeholder)
. [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)
 arguments also do the job of [`tf.compat.v1.ragged.placeholder`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/ragged/placeholder)
. For more details please read [Better performance with tf.function](https://www.tensorflow.org/guide/function)
.

Description
-----------

|     |     |
| --- | --- |
| Args<br>---- |     |
| `dtype` | The data type for the `RaggedTensor`. |
| `ragged_rank` | The ragged rank for the `RaggedTensor` |
| `value_shape` | The shape for individual flat values in the `RaggedTensor`. |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| A `RaggedTensor` that may be used as a handle for feeding a value, but not evaluated directly. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `RuntimeError` | if eager execution is enabled |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.