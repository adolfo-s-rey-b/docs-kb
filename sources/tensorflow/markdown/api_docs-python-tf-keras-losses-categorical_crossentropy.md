[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/losses/categorical_crossentropy#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/losses/categorical_crossentropy)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/losses/categorical_crossentropy?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fkeras%2Flosses%2Fcategorical_crossentropy&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/losses/categorical_crossentropy#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/losses/categorical_crossentropy#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.losses.categorical\_crossentropy Stay organized with collections Save and categorize content based on your preferences.
================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/losses/categorical_crossentropy#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/losses/categorical_crossentropy#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/losses/losses.py#L2148-L2208)

Computes the categorical crossentropy loss.

#### View aliases

**Main aliases**

[`tf.keras.metrics.categorical_crossentropy`](https://www.tensorflow.org/api_docs/python/tf/keras/losses/categorical_crossentropy)

tf.keras.losses.categorical_crossentropy(
        y_true, y_pred, from_logits=False, label_smoothing=0.0, axis=-1
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `y_true` | Tensor of one-hot true targets. |
| `y_pred` | Tensor of predicted targets. |
| `from_logits` | Whether `y_pred` is expected to be a logits tensor. By default, we assume that `y_pred` encodes a probability distribution. |
| `label_smoothing` | Float in \[0, 1\]. If > `0` then smooth the labels. For example, if `0.1`, use `0.1 / num_classes` for non-target labels and `0.9 + 0.1 / num_classes` for target labels. |
| `axis` | Defaults to `-1`. The dimension along which the entropy is computed. |

|     |
| --- |
| Returns<br>------- |     |
| Categorical crossentropy loss value. |     |

#### Example:

    y_true = [[0, 1, 0], [0, 0, 1]]

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.