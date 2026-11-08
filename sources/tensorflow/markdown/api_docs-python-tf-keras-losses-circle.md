[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/losses/circle#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/losses/circle)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/losses/circle?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/losses/circle#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/losses/circle#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.losses.circle Stay organized with collections Save and categorize content based on your preferences.
=============================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/losses/circle#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/losses/circle#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/losses/losses.py#L2657-L2742)

Computes the Circle loss.

tf.keras.losses.circle(
        y_true,
        y_pred,
        ref_labels=None,
        ref_embeddings=None,
        remove_diagonal=True,
        gamma=80,
        margin=0.4
    )

It is designed to minimize within-class distances and maximize between-class distances in L2 normalized embedding space.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `y_true` | Tensor with ground truth labels in integer format. |
| `y_pred` | Tensor with predicted L2 normalized embeddings. |
| `ref_labels` | Optional integer tensor with labels for reference embeddings. If `None`, defaults to `y_true`. |
| `ref_embeddings` | Optional tensor with L2 normalized reference embeddings. If `None`, defaults to `y_pred`. |
| `remove_diagonal` | Boolean, whether to remove self-similarities from positive mask. Defaults to `True`. |
| `gamma` | Float, scaling factor for the loss. Defaults to `80`. |
| `margin` | Float, relaxation factor for the loss. Defaults to `0.4`. |

|     |
| --- |
| Returns<br>------- |     |
| Circle loss value. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.