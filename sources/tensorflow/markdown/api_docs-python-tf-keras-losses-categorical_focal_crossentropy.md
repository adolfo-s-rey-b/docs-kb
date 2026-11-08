[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/losses/categorical_focal_crossentropy#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/losses/categorical_focal_crossentropy)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/losses/categorical_focal_crossentropy?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/oauth2authorize?return_url=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fkeras%2Flosses%2Fcategorical_focal_crossentropy&scopes=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles.award+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdevprofiles.full_control.firstparty)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/losses/categorical_focal_crossentropy#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/losses/categorical_focal_crossentropy#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.losses.categorical\_focal\_crossentropy Stay organized with collections Save and categorize content based on your preferences.
=======================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/losses/categorical_focal_crossentropy#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/losses/categorical_focal_crossentropy#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/losses/losses.py#L2211-L2304)

Computes the categorical focal crossentropy loss.

#### View aliases

**Main aliases**

[`tf.keras.metrics.categorical_focal_crossentropy`](https://www.tensorflow.org/api_docs/python/tf/keras/losses/categorical_focal_crossentropy)

tf.keras.losses.categorical_focal_crossentropy(
        y_true,
        y_pred,
        alpha=0.25,
        gamma=2.0,
        from_logits=False,
        label_smoothing=0.0,
        axis=-1
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `y_true` | Tensor of one-hot true targets. |
| `y_pred` | Tensor of predicted targets. |
| `alpha` | A weight balancing factor for all classes, default is `0.25` as mentioned in the reference. It can be a list of floats or a scalar. In the multi-class case, alpha may be set by inverse class frequency by using `compute_class_weight` from `sklearn.utils`. |
| `gamma` | A focusing parameter, default is `2.0` as mentioned in the reference. It helps to gradually reduce the importance given to simple examples in a smooth manner. When `gamma` = 0, there is no focal effect on the categorical crossentropy. |
| `from_logits` | Whether `y_pred` is expected to be a logits tensor. By default, we assume that `y_pred` encodes a probability distribution. |
| `label_smoothing` | Float in \[0, 1\]. If > `0` then smooth the labels. For example, if `0.1`, use `0.1 / num_classes` for non-target labels and `0.9 + 0.1 / num_classes` for target labels. |
| `axis` | Defaults to `-1`. The dimension along which the entropy is computed. |

|     |
| --- |
| Returns<br>------- |     |
| Categorical focal crossentropy loss value. |     |

#### Example:

    y_true = [[0, 1, 0], [0, 0, 1]]

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.