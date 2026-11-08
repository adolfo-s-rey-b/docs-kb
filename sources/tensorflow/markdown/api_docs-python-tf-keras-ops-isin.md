[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/ops/isin#main-content)

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
    

tf.keras.ops.isin Stay organized with collections Save and categorize content based on your preferences.
========================================================================================================

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L4266-L4304)

Test whether each element of `x1` is present in `x2`.

#### View aliases

**Main aliases**

[`tf.keras.ops.numpy.isin`](https://www.tensorflow.org/api_docs/python/tf/keras/ops/isin)

tf.keras.ops.isin(
        x1, x2, assume_unique=False, invert=False
    )

This operation performs element-wise checks to determine if each value in `x1` is contained within `x2`. The result is a boolean tensor with the same shape as `x1`, where each entry is `True` if the corresponding element in `x1` is in `x2`, and `False` otherwise.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `x1` | Input tensor or array-like structure to test. |
| `x2` | Values against which each element of `x1` is tested. Can be a tensor, list, or scalar. |
| `assume_unique` | Boolean (default: False). If True, assumes both `x1` and `x2` contain only unique elements. This can speed up the computation. If False, duplicates will be handled correctly but may impact performance. |
| `invert` | A boolean (default: False). If True, inverts the result. Entries will be `True` where `x1` elements are not in `x2`. |

|     |
| --- |
| Returns<br>------- |     |
| A boolean tensor of the same shape as `x1` indicating element-wise membership in `x2`. |     |

#### Example:

    from keras import ops

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.