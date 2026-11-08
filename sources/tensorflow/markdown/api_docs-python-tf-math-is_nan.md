[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/math/is_nan#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/math/is_nan)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/math/is_nan?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/math/is_nan#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/math/is_nan#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/math/is_nan#returns)
    
*   [numpy compatibility](https://www.tensorflow.org/api_docs/python/tf/math/is_nan#numpy-compatibility)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.math.is\_nan Stay organized with collections Save and categorize content based on your preferences.
======================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/math/is_nan#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/math/is_nan#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/math/is_nan#returns)
    
*   [numpy compatibility](https://www.tensorflow.org/api_docs/python/tf/math/is_nan#numpy-compatibility)
    

Returns which elements of x are NaN.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.debugging.is_nan`](https://www.tensorflow.org/api_docs/python/tf/math/is_nan)
, [`tf.compat.v1.is_nan`](https://www.tensorflow.org/api_docs/python/tf/math/is_nan)
, [`tf.compat.v1.math.is_nan`](https://www.tensorflow.org/api_docs/python/tf/math/is_nan)

tf.math.is_nan(
        x: Annotated[Any, tf.raw_ops.Any],
        name=None
    ) -> Annotated[Any, tf.raw_ops.Any]

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Optimizers with Core APIs](https://www.tensorflow.org/guide/core/optimizers_core) | *   [TFX Estimator Component Tutorial](https://www.tensorflow.org/tfx/tutorials/tfx/components)<br>    <br>*   [TFX Keras Component Tutorial](https://www.tensorflow.org/tfx/tutorials/tfx/components_keras) |

#### Example:

x = tf.constant([5.0, np.nan, 6.8, np.nan, np.inf])
    tf.math.is_nan(x) ==> [False, True, False, True, False]

|     |     |
| --- | --- |
| Args<br>---- |     |
| `x` | A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`. |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| A `Tensor` of type `bool`. |     |

numpy compatibility
-------------------

Equivalent to np.isnan

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2024-04-26 UTC.