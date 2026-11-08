[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/bincount#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/bincount)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/bincount?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fcompat%2Fv1%2Fbincount&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/bincount#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/bincount#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.bincount Stay organized with collections Save and categorize content based on your preferences.
============================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/bincount#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/bincount#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/bincount_ops.py#L190-L220)

Counts the number of occurrences of each value in an integer array.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.math.bincount`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/bincount)

tf.compat.v1.bincount(
        arr,
        weights=None,
        minlength=None,
        maxlength=None,
        dtype=tf.dtypes.int32
    )

If `minlength` and `maxlength` are not given, returns a vector with length `tf.reduce_max(arr) + 1` if `arr` is non-empty, and length 0 otherwise. If `weights` are non-None, then index `i` of the output stores the sum of the value in `weights` at each index where the corresponding value in `arr` is `i`.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `arr` | An int32 tensor of non-negative values. |
| `weights` | If non-None, must be the same shape as arr. For each value in `arr`, the bin will be incremented by the corresponding weight instead of 1. |
| `minlength` | If given, ensures the output has length at least `minlength`, padding with zeros at the end if necessary. |
| `maxlength` | If given, skips values in `arr` that are equal or greater than `maxlength`, ensuring that the output has length at most `maxlength`. |
| `dtype` | If `weights` is None, determines the type of the output bins. |

|     |
| --- |
| Returns<br>------- |     |
| A vector with the same dtype as `weights` or the given `dtype`. The bin values. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.