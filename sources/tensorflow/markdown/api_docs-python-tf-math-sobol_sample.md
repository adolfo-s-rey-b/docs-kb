[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/math/sobol_sample#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/math/sobol_sample)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/math/sobol_sample?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/math/sobol_sample#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/math/sobol_sample#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.math.sobol\_sample Stay organized with collections Save and categorize content based on your preferences.
============================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/math/sobol_sample#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/math/sobol_sample#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/math_ops.py#L5824-L5846)

Generates points from the Sobol sequence.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.math.sobol_sample`](https://www.tensorflow.org/api_docs/python/tf/math/sobol_sample)

tf.math.sobol_sample(
        dim,
        num_results,
        skip=0,
        dtype=tf.dtypes.float32,
        name=None
    )

Creates a Sobol sequence with `num_results` samples. Each sample has dimension `dim`. Skips the first `skip` samples.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `dim` | Positive scalar `Tensor` representing each sample's dimension. |
| `num_results` | Positive scalar `Tensor` of dtype int32. The number of Sobol points to return in the output. |
| `skip` | (Optional) Positive scalar `Tensor` of dtype int32. The number of initial points of the Sobol sequence to skip. Default value is 0. |
| `dtype` | (Optional) The `tf.Dtype` of the sample. One of: [`tf.float32`](https://www.tensorflow.org/api_docs/python/tf#float32)<br> or [`tf.float64`](https://www.tensorflow.org/api_docs/python/tf#float64)<br>. Defaults to [`tf.float32`](https://www.tensorflow.org/api_docs/python/tf#float32)<br>. |
| `name` | (Optional) Python `str` name prefixed to ops created by this function. |

|     |
| --- |
| Returns<br>------- |     |
| `Tensor` of samples from Sobol sequence with `shape` \[num\_results, dim\]. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.