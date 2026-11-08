[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/zeros#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/zeros)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/zeros?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fzeros&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/zeros#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/zeros#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/zeros#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.zeros Stay organized with collections Save and categorize content based on your preferences.
===============================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/zeros#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/zeros#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/zeros#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/array_ops.py#L2599-L2658)

Creates a tensor with all elements set to zero.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.zeros`](https://www.tensorflow.org/api_docs/python/tf/zeros)

tf.zeros(
        shape,
        dtype=tf.dtypes.float32,
        name=None,
        layout=None
    )

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Training checkpoints](https://www.tensorflow.org/guide/checkpoint)<br>    <br>*   [Multilayer perceptrons for digit recognition with Core APIs](https://www.tensorflow.org/guide/core/mlp_core)<br>    <br>*   [Better performance with the tf.data API](https://www.tensorflow.org/guide/data_performance)<br>    <br>*   [Optimizers with Core APIs](https://www.tensorflow.org/guide/core/optimizers_core)<br>    <br>*   [Better performance with tf.function](https://www.tensorflow.org/guide/function) | *   [Custom layers](https://www.tensorflow.org/tutorials/customization/custom_layers)<br>    <br>*   [Learned data compression](https://www.tensorflow.org/tutorials/generative/data_compression)<br>    <br>*   [Using DTensors with Keras](https://www.tensorflow.org/tutorials/distribute/dtensor_keras_tutorial)<br>    <br>*   [Integrated gradients](https://www.tensorflow.org/tutorials/interpretability/integrated_gradients)<br>    <br>*   [Multilevel Modeling Primer in TensorFlow Probability](https://www.tensorflow.org/probability/examples/Multilevel_Modeling_Primer) |

See also [`tf.zeros_like`](https://www.tensorflow.org/api_docs/python/tf/zeros_like)
, [`tf.ones`](https://www.tensorflow.org/api_docs/python/tf/ones)
, [`tf.fill`](https://www.tensorflow.org/api_docs/python/tf/fill)
, [`tf.eye`](https://www.tensorflow.org/api_docs/python/tf/eye)
.

This operation returns a tensor of type `dtype` with shape `shape` and all elements set to zero.

    tf.zeros([3, 4], tf.int32)

|     |     |
| --- | --- |
| Args<br>---- |     |
| `shape` | A `list` of integers, a `tuple` of integers, or a 1-D `Tensor` of type `int32`. |
| `dtype` | The DType of an element in the resulting `Tensor`. |
| `name` | Optional string. A name for the operation. |
| `layout` | Optional, [`tf.experimental.dtensor.Layout`](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/Layout)<br>. If provided, the result is a [DTensor](https://www.tensorflow.org/guide/dtensor_overview)<br> with the provided layout. |

|     |
| --- |
| Returns<br>------- |     |
| A `Tensor` with all elements set to zero. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-05 UTC.