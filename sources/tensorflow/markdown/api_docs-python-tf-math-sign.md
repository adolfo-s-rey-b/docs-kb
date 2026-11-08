[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/math/sign#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/math/sign)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/math/sign?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/math/sign#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/math/sign#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/math/sign#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.math.sign Stay organized with collections Save and categorize content based on your preferences.
===================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/math/sign#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/math/sign#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/math/sign#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/math_ops.py#L775-L819)

Returns an element-wise indication of the sign of a number.

#### View aliases

**Main aliases**

[`tf.sign`](https://www.tensorflow.org/api_docs/python/tf/math/sign)

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.sign`](https://www.tensorflow.org/api_docs/python/tf/math/sign)

tf.math.sign(
        x, name=None
    )

### Used in the notebooks

| Used in the tutorials |
| --- |
| *   [Adversarial example using FGSM](https://www.tensorflow.org/tutorials/generative/adversarial_fgsm)<br>    <br>*   [Tutorial on Multi Armed Bandits in TF-Agents](https://www.tensorflow.org/agents/tutorials/bandits_tutorial) |

`y = sign(x) = -1 if x < 0; 0 if x == 0; 1 if x > 0`.

For complex numbers, `y = sign(x) = x / |x| if x != 0, otherwise y = 0`.

#### Example usage:

    # real number

    # complex number

|     |     |
| --- | --- |
| Args<br>---- |     |
| `x` | A Tensor. Must be one of the following types: bfloat16, half, float32, float64, int32, int64, complex64, complex128. |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| A Tensor. Has the same type as x.<br><br>If x is a SparseTensor, returns SparseTensor(x.indices, tf.math.sign(x.values, ...), x.dense\_shape).<br><br>If `x` is a `SparseTensor`, returns `SparseTensor(x.indices, tf.math.sign(x.values, ...), x.dense_shape)` |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.