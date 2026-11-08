[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/math/l2_normalize#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/math/l2_normalize)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/math/l2_normalize?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/math/l2_normalize#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/math/l2_normalize#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/math/l2_normalize#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.math.l2\_normalize Stay organized with collections Save and categorize content based on your preferences.
============================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/math/l2_normalize#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/math/l2_normalize#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/math/l2_normalize#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/nn_impl.py#L541-L597)

Normalizes along dimension `axis` using an L2 norm. (deprecated arguments)

#### View aliases

**Main aliases**

[`tf.linalg.l2_normalize`](https://www.tensorflow.org/api_docs/python/tf/math/l2_normalize)
, [`tf.nn.l2_normalize`](https://www.tensorflow.org/api_docs/python/tf/math/l2_normalize)

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.linalg.l2_normalize`](https://www.tensorflow.org/api_docs/python/tf/math/l2_normalize)
, [`tf.compat.v1.math.l2_normalize`](https://www.tensorflow.org/api_docs/python/tf/math/l2_normalize)
, [`tf.compat.v1.nn.l2_normalize`](https://www.tensorflow.org/api_docs/python/tf/math/l2_normalize)

tf.math.l2_normalize(
        x, axis=None, epsilon=1e-12, name=None, dim=None
    )

### Used in the notebooks

| Used in the tutorials |
| --- |
| *   [Universal Sentence Encoder](https://www.tensorflow.org/hub/tutorials/semantic_similarity_with_tf_hub_universal_encoder)<br>    <br>*   [Universal Sentence Encoder-Lite demo](https://www.tensorflow.org/hub/tutorials/semantic_similarity_with_tf_hub_universal_encoder_lite)<br>    <br>*   [TFP Release Notes notebook (0.11.0)](https://www.tensorflow.org/probability/examples/TFP_Release_Notebook_0_11_0)<br>    <br>*   [TFP Release Notes notebook (0.12.1)](https://www.tensorflow.org/probability/examples/TFP_Release_Notebook_0_12_1) |

For a 1-D tensor with `axis = 0`, computes

output = x / sqrt(max(sum(x**2), epsilon))

For `x` with more dimensions, independently normalizes each 1-D slice along dimension `axis`.

1-D tensor example:

>>> x = tf.constant([3.0, 4.0])
    >>> tf.math.l2_normalize(x).numpy()
    array([0.6, 0.8], dtype=float32)

2-D tensor example:

>>> x = tf.constant([[3.0], [4.0]])
    >>> tf.math.l2_normalize(x, 0).numpy()
    array([[0.6],\
         [0.8]], dtype=float32)

    x = tf.constant([[3.0], [4.0]])

|     |     |
| --- | --- |
| Args<br>---- |     |
| `x` | A `Tensor`. |
| `axis` | Dimension along which to normalize. A scalar or a vector of integers. |
| `epsilon` | A lower bound value for the norm. Will use `sqrt(epsilon)` as the divisor if `norm < sqrt(epsilon)`. |
| `name` | A name for this operation (optional). |
| `dim` | Deprecated, do not use. |

|     |
| --- |
| Returns<br>------- |     |
| A `Tensor` with the same shape as `x`. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.