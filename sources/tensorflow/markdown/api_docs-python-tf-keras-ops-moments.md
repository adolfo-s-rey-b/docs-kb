[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/ops/moments#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/ops/moments)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/ops/moments?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fkeras%2Fops%2Fmoments&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/moments#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/moments#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.ops.moments Stay organized with collections Save and categorize content based on your preferences.
===========================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/moments#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/moments#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/nn.py#L2344-L2383)

Calculates the mean and variance of `x`.

#### View aliases

**Main aliases**

[`tf.keras.ops.nn.moments`](https://www.tensorflow.org/api_docs/python/tf/keras/ops/moments)

tf.keras.ops.moments(
        x, axes, keepdims=False, synchronized=False
    )

The mean and variance are calculated by aggregating the contents of `x` across `axes`. If `x` is 1-D and `axes = [0]` this is just the mean and variance of a vector.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `x` | Input tensor. |
| `axes` | A list of axes which to compute mean and variance. |
| `keepdims` | If this is set to `True`, the axes which are reduced are left in the result as dimensions with size one. |
| `synchronized` | Only applicable with the TensorFlow backend. If `True`, synchronizes the global batch statistics (mean and variance) across all devices at each training step in a distributed training strategy. If `False`, each replica uses its own local batch statistics. |

|     |
| --- |
| Returns<br>------- |     |
| A tuple containing two tensors - mean and variance. |     |

#### Example:

    x = keras.ops.convert_to_tensor([0, 1, 2, 3, 100], dtype="float32")

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.