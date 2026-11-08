[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/ops/bincount#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   English
*   中文 – 简体

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.ops.bincount Stay organized with collections Save and categorize content based on your preferences.
============================================================================================================

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L1573-L1617)

Count the number of occurrences of each value in a tensor of integers.

#### View aliases

**Main aliases**

[`tf.keras.ops.numpy.bincount`](https://www.tensorflow.org/api_docs/python/tf/keras/ops/bincount)

tf.keras.ops.bincount(
        x, weights=None, minlength=0, sparse=False
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `x` | Input tensor. It must be of dimension 1, and it must only contain non-negative integer(s). |
| `weights` | Weight tensor. It must have the same length as `x`. The default value is `None`. If specified, `x` is weighted by it, i.e. if `n = x[i]`, `out[n] += weight[i]` instead of the default behavior `out[n] += 1`. |
| `minlength` | An integer. The default value is 0. If specified, there will be at least this number of bins in the output tensor. If greater than `max(x) + 1`, each value of the output at an index higher than `max(x)` is set to 0. |
| `sparse` | Whether to return a sparse tensor; for backends that support sparse tensors. |

|     |
| --- |
| Returns<br>------- |     |
| 1D tensor where each element gives the number of occurrence(s) of its index value in x. Its length is the maximum between `max(x) + 1` and minlength. |     |

#### Examples:

    x = keras.ops.array([1, 2, 2, 3], dtype="uint8")

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.