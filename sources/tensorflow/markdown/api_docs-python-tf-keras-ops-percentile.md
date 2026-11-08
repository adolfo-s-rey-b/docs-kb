[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/ops/percentile#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/ops/percentile)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/ops/percentile?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fkeras%2Fops%2Fpercentile&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/percentile#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/percentile#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.ops.percentile Stay organized with collections Save and categorize content based on your preferences.
==============================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/percentile#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/percentile#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L6855-L6904)

Compute the q-th percentile(s) of the data along the specified axis.

#### View aliases

**Main aliases**

[`tf.keras.ops.numpy.percentile`](https://www.tensorflow.org/api_docs/python/tf/keras/ops/percentile)

tf.keras.ops.percentile(
        x, q, axis=None, method='linear', keepdims=False
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `x` | Input tensor. |
| `q` | Percentile or sequence of percentiles to compute. Values must be between 0 and 100 inclusive. |
| `axis` | Axis or axes along which the percentiles are computed. |
| `method` | A string specifies the method to use for estimating the percentile. Available methods are `"linear"`, `"lower"`, `"higher"`, `"midpoint"`, and `"nearest"`. Defaults to `"linear"`. If the desired percentile lies between two data points `i < j`:<br><br>*   `"linear"`: `i + (j - i) * fraction`, where fraction is the fractional part of the index surrounded by `i` and `j`.<br>*   `"lower"`: `i`.<br>*   `"higher"`: `j`.<br>*   `"midpoint"`: `(i + j) / 2`<br>*   `"nearest"`: `i` or `j`, whichever is nearest. |
| `keepdims` | If True, reduced axes are kept with size 1. |

|     |
| --- |
| Returns<br>------- |     |
| The percentile(s). If `q` is a single percentile and `axis=None`, then the result is a scalar. If multiple percentile levels are given, the first axis of the result corresponds to the percentiles. The other axes are the axes that remain after the reduction of `x`. |     |

#### Examples:

    import keras

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.