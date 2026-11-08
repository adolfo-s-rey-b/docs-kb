[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/losses/cosine_similarity#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/losses/cosine_similarity)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/losses/cosine_similarity?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/losses/cosine_similarity#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/losses/cosine_similarity#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.losses.cosine\_similarity Stay organized with collections Save and categorize content based on your preferences.
=========================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/losses/cosine_similarity#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/losses/cosine_similarity#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/losses/losses.py#L1921-L1958)

Computes the cosine similarity between labels and predictions.

tf.keras.losses.cosine_similarity(
        y_true, y_pred, axis=-1
    )

#### Formula:

loss = -sum(l2_norm(y_true) * l2_norm(y_pred))

Note that it is a number between -1 and 1. When it is a negative number between -1 and 0, 0 indicates orthogonality and values closer to -1 indicate greater similarity. This makes it usable as a loss function in a setting where you try to maximize the proximity between predictions and targets. If either `y_true` or `y_pred` is a zero vector, cosine similarity will be 0 regardless of the proximity between predictions and targets.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `y_true` | Tensor of true targets. |
| `y_pred` | Tensor of predicted targets. |
| `axis` | Axis along which to determine similarity. Defaults to `-1`. |

|     |
| --- |
| Returns<br>------- |     |
| Cosine similarity tensor. |     |

#### Example:

    y_true = [[0., 1.], [1., 1.], [1., 1.]]

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.