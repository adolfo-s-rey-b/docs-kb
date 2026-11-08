[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/losses/sparse_categorical_focal_crossentropy#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/losses/sparse_categorical_focal_crossentropy)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/losses/sparse_categorical_focal_crossentropy?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/losses/sparse_categorical_focal_crossentropy#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/losses/sparse_categorical_focal_crossentropy#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.losses.sparse\_categorical\_focal\_crossentropy Stay organized with collections Save and categorize content based on your preferences.
===============================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/losses/sparse_categorical_focal_crossentropy#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/losses/sparse_categorical_focal_crossentropy#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/master/keras/src/losses/losses.py#L2507-L2683)

Computes the sparse categorical focal crossentropy loss.

tf.keras.losses.sparse_categorical_focal_crossentropy(
        y_true,
        y_pred,
        alpha=0.25,
        gamma=2.0,
        from_logits=False,
        ignore_class=None,
        axis=-1
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `y_true` | Tensor of integer true targets. |
| `y_pred` | Tensor of predicted targets. |
| `alpha` | A weight balancing factor for all classes. Defaults to `0.25`. It can be a list of floats or a scalar. If a list is provided, it must have the same length as the number of classes. |
| `gamma` | A focusing parameter. Defaults to `2.0`. It gradually reduces the importance given to easy examples. When `gamma=0`, there is no focal effect on the crossentropy loss. |
| `from_logits` | Whether `y_pred` is expected to be a logits tensor. By default, `y_pred` is expected to encode a probability distribution. |
| `ignore_class` | Optional integer. The ID of a class to be ignored during loss computation. This is useful, for example, in segmentation problems featuring a "void" class (commonly -1 or 255). By default (`ignore_class=None`), all classes are considered. |
| `axis` | The axis along which to compute crossentropy (the features axis). Defaults to `-1`. |

|     |
| --- |
| Returns<br>------- |     |
| Sparse categorical focal crossentropy loss value.<br><br>An out-of-range, non-ignored label produces a `NaN` loss value. An `alpha` vector with a statically known wrong length raises `ValueError`; if its length or the class dimension is only known at runtime, a mismatch produces `NaN` loss values. This prevents backend-dependent index selection in compiled and symbolic execution, where Keras does not have a portable runtime assertion primitive. |     |

#### Example:

    y_true = [1, 2]

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.