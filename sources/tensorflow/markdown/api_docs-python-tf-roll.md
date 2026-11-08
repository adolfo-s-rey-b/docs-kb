[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/roll#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/roll)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/roll?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Froll&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/roll#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/roll#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/roll#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.roll Stay organized with collections Save and categorize content based on your preferences.
==============================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/roll#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/roll#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/roll#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/manip_ops.py#L27-L31)

Rolls the elements of a tensor along an axis.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.manip.roll`](https://www.tensorflow.org/api_docs/python/tf/roll)
, [`tf.compat.v1.roll`](https://www.tensorflow.org/api_docs/python/tf/roll)

tf.roll(
        input, shift, axis, name=None
    )

### Used in the notebooks

| Used in the tutorials |
| --- |
| *   [DeepDream](https://www.tensorflow.org/tutorials/generative/deepdream) |

The elements are shifted positively (towards larger indices) by the offset of `shift` along the dimension of `axis`. Negative `shift` values will shift elements in the opposite direction. Elements that roll passed the last position will wrap around to the first and vice versa. Multiple shifts along multiple axes may be specified.

#### For example:

# 't' is [0, 1, 2, 3, 4]
    roll(t, shift=2, axis=0) ==> [3, 4, 0, 1, 2]
    
    # shifting along multiple dimensions
    # 't' is [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]]
    roll(t, shift=[1, -2], axis=[0, 1]) ==> [[7, 8, 9, 5, 6], [2, 3, 4, 0, 1]]
    
    # shifting along the same axis multiple times
    # 't' is [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]]
    roll(t, shift=[2, -3], axis=[1, 1]) ==> [[1, 2, 3, 4, 0], [6, 7, 8, 9, 5]]

|     |     |
| --- | --- |
| Args<br>---- |     |
| `input` | A `Tensor`. |
| `shift` | A `Tensor`. Must be one of the following types: `int32`, `int64`. Dimension must be 0-D or 1-D. `shift[i]` specifies the number of places by which elements are shifted positively (towards larger indices) along the dimension specified by `axis[i]`. Negative shifts will roll the elements in the opposite direction. |
| `axis` | A `Tensor`. Must be one of the following types: `int32`, `int64`. Dimension must be 0-D or 1-D. `axis[i]` specifies the dimension that the shift `shift[i]` should occur. If the same axis is referenced more than once, the total shift for that axis will be the sum of all the shifts that belong to that axis. |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| A `Tensor`. Has the same type as `input`. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.