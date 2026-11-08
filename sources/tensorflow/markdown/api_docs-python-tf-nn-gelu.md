[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/nn/gelu#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/nn/gelu)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/nn/gelu?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/oauth2authorize?return_url=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fnn%2Fgelu&scopes=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles.award+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdevprofiles.full_control.firstparty)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/nn/gelu#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/nn/gelu#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/nn/gelu#raises)
    
*   [References](https://www.tensorflow.org/api_docs/python/tf/nn/gelu#references)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.nn.gelu Stay organized with collections Save and categorize content based on your preferences.
=================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/nn/gelu#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/nn/gelu#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/nn/gelu#raises)
    
*   [References](https://www.tensorflow.org/api_docs/python/tf/nn/gelu#references)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/nn_ops.py#L3702-L3758)

Compute the Gaussian Error Linear Unit (GELU) activation function.

tf.nn.gelu(
        features, approximate=False, name=None
    )

Gaussian error linear unit (GELU) computes `x * P(X <= x)`, where `P(X) ~ N(0, 1)`. The (GELU) nonlinearity weights inputs by their value, rather than gates inputs by their sign as in ReLU.

#### For example:

    x = tf.constant([-3.0, -1.0, 0.0, 1.0, 3.0], dtype=tf.float32)

|     |     |
| --- | --- |
| Args<br>---- |     |
| `features` | A `float Tensor` representing preactivation values. |
| `approximate` | An optional `bool`. Defaults to `False`. Whether to enable approximation. |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| A `Tensor` with the same type as `features`. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | if `features` is not a floating point `Tensor`. |

|     |
| --- |
| References<br>---------- |     |
| [Gaussian Error Linear Units (GELUs)](https://arxiv.org/abs/1606.08415)<br>. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.