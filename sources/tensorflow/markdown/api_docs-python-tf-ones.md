[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/ones#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/ones)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/ones?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/ones#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/ones#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/ones#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.ones Stay organized with collections Save and categorize content based on your preferences.
==============================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/ones#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/ones#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/ones#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/array_ops.py#L2917-L2973)

Creates a tensor with all elements set to one (1).

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.ones`](https://www.tensorflow.org/api_docs/python/tf/ones)

tf.ones(
        shape,
        dtype=tf.dtypes.float32,
        name=None,
        layout=None
    )

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Validating correctness & numerical equivalence](https://www.tensorflow.org/guide/migrate/validate_correctness)<br>    <br>*   [Use TF1.x models in TF2 workflows](https://www.tensorflow.org/guide/migrate/model_mapping)<br>    <br>*   [Better performance with tf.function](https://www.tensorflow.org/guide/function)<br>    <br>*   [Extension types](https://www.tensorflow.org/guide/extension_type)<br>    <br>*   [Ragged tensors](https://www.tensorflow.org/guide/ragged_tensor) | *   [Multilevel Modeling Primer in TensorFlow Probability](https://www.tensorflow.org/probability/examples/Multilevel_Modeling_Primer)<br>    <br>*   [Learnable Distributions Zoo](https://www.tensorflow.org/probability/examples/Learnable_Distributions_Zoo)<br>    <br>*   [Probabilistic PCA](https://www.tensorflow.org/probability/examples/Probabilistic_PCA)<br>    <br>*   [Policies](https://www.tensorflow.org/agents/tutorials/3_policies_tutorial)<br>    <br>*   [Bayesian Switchpoint Analysis](https://www.tensorflow.org/probability/examples/Bayesian_Switchpoint_Analysis) |

See also [`tf.ones_like`](https://www.tensorflow.org/api_docs/python/tf/ones_like)
, [`tf.zeros`](https://www.tensorflow.org/api_docs/python/tf/zeros)
, [`tf.fill`](https://www.tensorflow.org/api_docs/python/tf/fill)
, [`tf.eye`](https://www.tensorflow.org/api_docs/python/tf/eye)
.

This operation returns a tensor of type `dtype` with shape `shape` and all elements set to one.

    tf.ones([3, 4], tf.int32)

|     |     |
| --- | --- |
| Args<br>---- |     |
| `shape` | A `list` of integers, a `tuple` of integers, or a 1-D `Tensor` of type `int32`. |
| `dtype` | Optional DType of an element in the resulting `Tensor`. Default is [`tf.float32`](https://www.tensorflow.org/api_docs/python/tf#float32)<br>. |
| `name` | Optional string. A name for the operation. |
| `layout` | Optional, [`tf.experimental.dtensor.Layout`](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/Layout)<br>. If provided, the result is a [DTensor](https://www.tensorflow.org/guide/dtensor_overview)<br> with the provided layout. |

|     |
| --- |
| Returns<br>------- |     |
| A `Tensor` with all elements set to one (1). |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.