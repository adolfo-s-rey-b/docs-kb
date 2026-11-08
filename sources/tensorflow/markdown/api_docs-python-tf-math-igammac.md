[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/math/igammac#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/math/igammac)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/math/igammac?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/math/igammac#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/math/igammac#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/math/igammac#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.math.igammac Stay organized with collections Save and categorize content based on your preferences.
======================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/math/igammac#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/math/igammac#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/math/igammac#returns)
    

Compute the upper regularized incomplete Gamma function `Q(a, x)`.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.igammac`](https://www.tensorflow.org/api_docs/python/tf/math/igammac)
, [`tf.compat.v1.math.igammac`](https://www.tensorflow.org/api_docs/python/tf/math/igammac)

tf.math.igammac(
        a: Annotated[Any, tf.raw_ops.Any],
        x: Annotated[Any, tf.raw_ops.Any],
        name=None
    ) -> Annotated[Any, tf.raw_ops.Any]

### Used in the notebooks

| Used in the tutorials |
| --- |
| *   [TFP Release Notes notebook (0.13.0)](https://www.tensorflow.org/probability/examples/TFP_Release_Notebook_0_13_0) |

The upper regularized incomplete Gamma function is defined as:

Q(a,x)\=Gamma(a,x)/Gamma(a)\=1−P(a,x)

where

Gamma(a,x)\=∫∞xta−1exp(−t)dt

is the upper incomplete Gamma function.

Note, above `P(a, x)` (`Igamma`) is the lower regularized complete Gamma function.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `a` | A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`. |
| `x` | A `Tensor`. Must have the same type as `a`. |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| A `Tensor`. Has the same type as `a`. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2024-04-26 UTC.