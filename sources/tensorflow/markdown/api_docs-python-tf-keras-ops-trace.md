[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/ops/trace#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/ops/trace)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/ops/trace?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fkeras%2Fops%2Ftrace&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/trace#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/trace#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.ops.trace Stay organized with collections Save and categorize content based on your preferences.
=========================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/trace#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/trace#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L8181-L8211)

Return the sum along diagonals of the tensor.

#### View aliases

**Main aliases**

[`tf.keras.ops.numpy.trace`](https://www.tensorflow.org/api_docs/python/tf/keras/ops/trace)

tf.keras.ops.trace(
        x, offset=0, axis1=0, axis2=1
    )

If `x` is 2-D, the sum along its diagonal with the given offset is returned, i.e., the sum of elements `x[i, i+offset]` for all `i`.

If a has more than two dimensions, then the axes specified by `axis1` and `axis2` are used to determine the 2-D sub-arrays whose traces are returned.

The shape of the resulting tensor is the same as that of `x` with `axis1` and `axis2` removed.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `x` | Input tensor. |
| `offset` | Offset of the diagonal from the main diagonal. Can be both positive and negative. Defaults to `0`. |
| `axis1` | Axis to be used as the first axis of the 2-D sub-arrays. Defaults to `0`.(first axis). |
| `axis2` | Axis to be used as the second axis of the 2-D sub-arrays. Defaults to `1` (second axis). |

|     |
| --- |
| Returns<br>------- |     |
| If `x` is 2-D, the sum of the diagonal is returned. If `x` has larger dimensions, then a tensor of sums along diagonals is returned. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.