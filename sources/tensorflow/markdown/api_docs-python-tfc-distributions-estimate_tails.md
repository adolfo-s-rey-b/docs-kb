[Skip to main content](https://www.tensorflow.org/api_docs/python/tfc/distributions/estimate_tails#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfc/distributions/estimate_tails)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfc/distributions/estimate_tails?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfc/distributions/estimate_tails#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfc/distributions/estimate_tails#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfc.distributions.estimate\_tails Stay organized with collections Save and categorize content based on your preferences.
========================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfc/distributions/estimate_tails#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfc/distributions/estimate_tails#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/compression/blob/v2.14.1/tensorflow_compression/python/distributions/helpers.py#L29-L101)

Estimates approximate tail quantiles.

#### View aliases

**Main aliases**

[`tfc.estimate_tails`](https://www.tensorflow.org/api_docs/python/tfc/distributions/estimate_tails)

tfc.distributions.estimate_tails(
        func, target, shape, dtype
    )

This runs a simple Adam iteration to determine tail quantiles. The objective is to find an `x` such that:

func(x) == target

For instance, if `func` is a CDF and the target is a quantile value, this would find the approximate location of that quantile. Note that `func` is assumed to be monotonic. When each tail estimate has passed the optimal value of `x`, the algorithm does 100 additional iterations and then stops.

This operation is vectorized. The tensor shape of `x` is given by `shape`, and `target` must have a shape that is broadcastable to the output of `func(x)`.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `func` | A callable that computes cumulative distribution function, survival function, or similar. |
| `target` | The desired target value. |
| `shape` | The shape of the [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> representing `x`. |
| `dtype` | The `tf.dtypes.Dtype` of the computation (and the return value). |

|     |
| --- |
| Returns<br>------- |     |
| A [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> representing the solution (`x`). |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2024-04-26 UTC.