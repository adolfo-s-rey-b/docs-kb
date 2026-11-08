[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/activations/relu#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/activations/relu)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/activations/relu?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fkeras%2Factivations%2Frelu&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/activations/relu#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/activations/relu#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.activations.relu Stay organized with collections Save and categorize content based on your preferences.
================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/activations/relu#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/activations/relu#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/activations/activations.py#L6-L52)

Applies the rectified linear unit activation function.

tf.keras.activations.relu(
        x, negative_slope=0.0, max_value=None, threshold=0.0
    )

With default values, this returns the standard ReLU activation: `max(x, 0)`, the element-wise maximum of 0 and the input tensor.

Modifying default parameters allows you to use non-zero thresholds, change the max value of the activation, and to use a non-zero multiple of the input for values below the threshold.

#### Examples:

    x = [-10, -5, 0.0, 5, 10]

|     |     |
| --- | --- |
| Args<br>---- |     |
| `x` | Input tensor. |
| `negative_slope` | A `float` that controls the slope for values lower than the threshold. |
| `max_value` | A `float` that sets the saturation threshold (the largest value the function will return). |
| `threshold` | A `float` giving the threshold value of the activation function below which values will be damped or set to zero. |

|     |
| --- |
| Returns<br>------- |     |
| A tensor with the same shape and dtype as input `x`. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.