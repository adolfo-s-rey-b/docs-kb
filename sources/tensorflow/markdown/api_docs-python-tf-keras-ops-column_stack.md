[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/ops/column_stack#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/ops/column_stack)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/ops/column_stack?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fkeras%2Fops%2Fcolumn_stack&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/column_stack#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/column_stack#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.ops.column\_stack Stay organized with collections Save and categorize content based on your preferences.
=================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/column_stack#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/column_stack#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/master/keras/src/ops/numpy.py#L10767-L10793)

Stack 1-D tensors as columns into a 2-D tensor.

#### View aliases

**Main aliases**

[`tf.keras.ops.numpy.column_stack`](https://www.tensorflow.org/api_docs/python/tf/keras/ops/column_stack)

tf.keras.ops.column_stack(
        xs
    )

Take a sequence of 1-D tensors and stack them as columns to make a single 2-D tensor. 2-D tensors are stacked as-is, like with `hstack`. Tensors with more than 2 dimensions are concatenated along the second axis.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `xs` | Sequence of tensors. |

|     |
| --- |
| Returns<br>------- |     |
| The tensor formed by stacking the given tensors. |     |

#### Example:

    a = keras.ops.array([1, 2, 3])

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-04 UTC.