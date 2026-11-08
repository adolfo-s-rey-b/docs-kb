[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/losses/categorical_hinge#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/losses/categorical_hinge)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/losses/categorical_hinge?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/losses/categorical_hinge#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/losses/categorical_hinge#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.losses.categorical\_hinge Stay organized with collections Save and categorize content based on your preferences.
=========================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/losses/categorical_hinge#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/losses/categorical_hinge#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/losses/losses.py#L1711-L1749)

Computes the categorical hinge loss between `y_true` & `y_pred`.

#### View aliases

**Main aliases**

[`tf.keras.metrics.categorical_hinge`](https://www.tensorflow.org/api_docs/python/tf/keras/losses/categorical_hinge)

tf.keras.losses.categorical_hinge(
        y_true, y_pred
    )

#### Formula:

loss = maximum(neg - pos + 1, 0)

where `neg=maximum((1-y_true)*y_pred)` and `pos=sum(y_true*y_pred)`

|     |     |
| --- | --- |
| Args<br>---- |     |
| `y_true` | The ground truth values. `y_true` values are expected to be either `{-1, +1}` or `{0, 1}` (i.e. a one-hot-encoded tensor) with shape = `[batch_size, d0, .. dN]`. |
| `y_pred` | The predicted values with shape = `[batch_size, d0, .. dN]`. |

|     |
| --- |
| Returns<br>------- |     |
| Categorical hinge loss values with shape = `[batch_size, d0, .. dN-1]`. |     |

#### Example:

    y_true = np.random.randint(0, 3, size=(2,))

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.