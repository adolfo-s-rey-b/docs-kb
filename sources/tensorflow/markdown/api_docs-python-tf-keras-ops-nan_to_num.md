[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/ops/nan_to_num#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/ops/nan_to_num)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/ops/nan_to_num?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fkeras%2Fops%2Fnan_to_num&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/nan_to_num#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/nan_to_num#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.ops.nan\_to\_num Stay organized with collections Save and categorize content based on your preferences.
================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/nan_to_num#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/nan_to_num#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L6504-L6526)

Replace NaN with zero and infinity with large finite numbers.

#### View aliases

**Main aliases**

[`tf.keras.ops.numpy.nan_to_num`](https://www.tensorflow.org/api_docs/python/tf/keras/ops/nan_to_num)

tf.keras.ops.nan_to_num(
        x, nan=0.0, posinf=None, neginf=None
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `x` | Input data. |
| `nan` | Optional float or int. Value to replace `NaN` entries with. |
| `posinf` | Optional float or int. Value to replace positive infinity with. |
| `neginf` | Optional float or int. Value to replace negative infinity with. |

|     |
| --- |
| Returns<br>------- |     |
| `x`, with non-finite values replaced. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.