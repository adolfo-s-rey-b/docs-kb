[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/identity#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/identity)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/identity?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/identity#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/identity#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/identity#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.identity Stay organized with collections Save and categorize content based on your preferences.
==================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/identity#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/identity#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/identity#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/array_ops.py#L253-L314)

Return a Tensor with the same shape and contents as input.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.identity`](https://www.tensorflow.org/api_docs/python/tf/identity)

tf.identity(
        input, name=None
    )

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Migrate LoggingTensorHook and StopAtStepHook to Keras callbacks](https://www.tensorflow.org/guide/migrate/logging_stop_hook) | *   [Substantial Undocumented Infection Facilitates the Rapid Dissemination of Novel Coronavirus (SARS-CoV2)](https://www.tensorflow.org/probability/examples/Undocumented_Infection_and_the_Dissemination_of_SARS-CoV2) |

The return value is not the same Tensor as the original, but contains the same values. This operation is fast when used on the same device.

#### For example:

    a = tf.constant([0.78])

Calling [`tf.identity`](https://www.tensorflow.org/api_docs/python/tf/identity)
 on a variable will make a Tensor that represents the value of that variable at the time it is called. This is equivalent to calling `<variable>.read_value()`.

    a = tf.Variable(5)

This function can also be used to explicitly transfer tensors between devices. For example, to transfer a tensor in GPU memory back to host memory, one can use:

    with tf.device("/gpu:0"):

|     |     |
| --- | --- |
| Args<br>---- |     |
| `input` | A `Tensor`, a `Variable`, a `CompositeTensor` or anything that can be converted to a tensor using [`tf.convert_to_tensor`](https://www.tensorflow.org/api_docs/python/tf/convert_to_tensor)<br>. |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| A `Tensor` or CompositeTensor. Has the same type and contents as `input`. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.