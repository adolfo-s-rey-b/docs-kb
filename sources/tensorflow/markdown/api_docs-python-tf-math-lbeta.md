Loading \[MathJax\]/jax/output/SVG/jax.js

[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/math/lbeta#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/math/lbeta)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/math/lbeta?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/math/lbeta#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/math/lbeta#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.math.lbeta Stay organized with collections Save and categorize content based on your preferences.
====================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/math/lbeta#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/math/lbeta#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/special_math_ops.py#L45-L98)

Computes ln(|Beta(x)|), reducing along the last dimension.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.lbeta`](https://www.tensorflow.org/api_docs/python/tf/math/lbeta)
, [`tf.compat.v1.math.lbeta`](https://www.tensorflow.org/api_docs/python/tf/math/lbeta)

tf.math.lbeta(
        x, name=None
    )

Given one-dimensional z\=\[z1,...,zK\], we define

Beta(z)\=∏jΓ(zj)Γ(∑jzj),

where Γ is the gamma function.

And for n+1 dimensional x with shape \[N1,...,Nn,K\], we define

lbeta(x)\[i1,...,in\]\=log|Beta(x\[i1,...,in,:\])|.

In other words, the last dimension is treated as the z vector.

Note that if z\=\[u,v\], then

Beta(z)\=Γ(u)Γ(v)Γ(u+v)\=∫10tu−1(1−t)v−1dt,

which defines the traditional bivariate beta function.

If the last dimension is empty, we follow the convention that the sum over the empty set is zero, and the product is one.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `x` | A rank `n + 1` `Tensor`, `n >= 0` with type `float`, or `double`. |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| The logarithm of \|Beta(x)\| reducing along the last dimension. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.