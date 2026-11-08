[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/math/cos#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/math/cos)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/math/cos?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/math/cos#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/math/cos#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/math/cos#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.math.cos Stay organized with collections Save and categorize content based on your preferences.
==================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/math/cos#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/math/cos#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/math/cos#returns)
    

Computes cos of x element-wise.

#### View aliases

**Main aliases**

[`tf.cos`](https://www.tensorflow.org/api_docs/python/tf/math/cos)

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.cos`](https://www.tensorflow.org/api_docs/python/tf/math/cos)

tf.math.cos(
        x: Annotated[Any, tf.raw_ops.Any],
        name=None
    ) -> Annotated[Any, tf.raw_ops.Any]

### Used in the notebooks

| Used in the tutorials |
| --- |
| *   [TFP Release Notes notebook (0.12.1)](https://www.tensorflow.org/probability/examples/TFP_Release_Notebook_0_12_1) |

Given an input tensor, this function computes cosine of every element in the tensor. Input range is `(-inf, inf)` and output range is `[-1,1]`. If input lies outside the boundary, `nan` is returned.

  x = tf.constant([-float("inf"), -9, -0.5, 1, 1.2, 200, 10000, float("inf")])
      tf.math.cos(x) ==> [nan -0.91113025 0.87758255 0.5403023 0.36235774 0.48718765 -0.95215535 nan]

|     |     |
| --- | --- |
| Args<br>---- |     |
| `x` | A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`, `complex64`, `complex128`. |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| A `Tensor`. Has the same type as `x`. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2024-04-26 UTC.