[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/nn/sufficient_statistics#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/nn/sufficient_statistics)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/nn/sufficient_statistics?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/nn/sufficient_statistics#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/nn/sufficient_statistics#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.nn.sufficient\_statistics Stay organized with collections Save and categorize content based on your preferences.
===================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/nn/sufficient_statistics#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/nn/sufficient_statistics#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/nn_impl.py#L1161-L1188)

Calculate the sufficient statistics for the mean and variance of `x`.

tf.nn.sufficient_statistics(
        x, axes, shift=None, keepdims=False, name=None
    )

These sufficient statistics are computed using the one pass algorithm on an input that's optionally shifted. See: [https://en.wikipedia.org/wiki/Algorithms\_for\_calculating\_variance#Computing\_shifted\_data](https://en.wikipedia.org/wiki/Algorithms_for_calculating_variance#Computing_shifted_data)

|     |     |
| --- | --- |
| Args<br>---- |     |
| `x` | A `Tensor`. |
| `axes` | Array of ints. Axes along which to compute mean and variance. |
| `shift` | A `Tensor` containing the value by which to shift the data for numerical stability, or `None` if no shift is to be performed. A shift close to the true mean provides the most numerically stable results. |
| `keepdims` | produce statistics with the same dimensionality as the input. |
| `name` | Name used to scope the operations that compute the sufficient stats. |

|     |
| --- |
| Returns<br>------- |     |
| Four `Tensor` objects of the same type as `x`:<br><br>*   the count (number of elements to average over).<br>*   the (possibly shifted) sum of the elements in the array.<br>*   the (possibly shifted) sum of squares of the elements in the array.<br>*   the shift by which the mean must be corrected or None if `shift` is None. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.