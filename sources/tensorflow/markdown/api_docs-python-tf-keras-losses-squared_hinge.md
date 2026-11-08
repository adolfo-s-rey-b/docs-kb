[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/losses/squared_hinge#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/losses/squared_hinge)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/losses/squared_hinge?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/losses/squared_hinge#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/losses/squared_hinge#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.losses.squared\_hinge Stay organized with collections Save and categorize content based on your preferences.
=====================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/losses/squared_hinge#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/losses/squared_hinge#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/losses/losses.py#L1673-L1708)

Computes the squared hinge loss between `y_true` & `y_pred`.

#### View aliases

**Main aliases**

[`tf.keras.metrics.squared_hinge`](https://www.tensorflow.org/api_docs/python/tf/keras/losses/squared_hinge)

tf.keras.losses.squared_hinge(
        y_true, y_pred
    )

#### Formula:

loss = mean(square(maximum(1 - y_true * y_pred, 0)), axis=-1)

|     |     |
| --- | --- |
| Args<br>---- |     |
| `y_true` | The ground truth values. `y_true` values are expected to be -1 or 1. If binary (0 or 1) labels are provided we will convert them to -1 or 1 with shape = `[batch_size, d0, .. dN]`. |
| `y_pred` | The predicted values with shape = `[batch_size, d0, .. dN]`. |

|     |
| --- |
| Returns<br>------- |     |
| Squared hinge loss values with shape = `[batch_size, d0, .. dN-1]`. |     |

#### Example:

    y_true = np.random.choice([-1, 1], size=(2, 3))

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.