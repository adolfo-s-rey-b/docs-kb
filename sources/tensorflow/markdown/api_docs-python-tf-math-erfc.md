[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/math/erfc#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/math/erfc)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/math/erfc?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/math/erfc#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/math/erfc#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/math/erfc#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.math.erfc Stay organized with collections Save and categorize content based on your preferences.
===================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/math/erfc#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/math/erfc#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/math/erfc#returns)
    

Computes the complementary error function of `x` element-wise.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.erfc`](https://www.tensorflow.org/api_docs/python/tf/math/erfc)

tf.math.erfc(
        x: Annotated[Any, tf.raw_ops.Any],
        name=None
    ) -> Annotated[Any, tf.raw_ops.Any]

### Used in the notebooks

| Used in the tutorials |
| --- |
| *   [TFP Release Notes notebook (0.12.1)](https://www.tensorflow.org/probability/examples/TFP_Release_Notebook_0_12_1) |

|     |     |
| --- | --- |
| Args<br>---- |     |
| `x` | A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`. |
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