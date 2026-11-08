[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/ops/layer_normalization#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/ops/layer_normalization)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/ops/layer_normalization?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/layer_normalization#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/layer_normalization#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.ops.layer\_normalization Stay organized with collections Save and categorize content based on your preferences.
========================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/layer_normalization#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/layer_normalization#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/nn.py#L3079-L3134)

Layer normalization layer (Ba et al., 2016).

#### View aliases

**Main aliases**

[`tf.keras.ops.nn.layer_normalization`](https://www.tensorflow.org/api_docs/python/tf/keras/ops/layer_normalization)

tf.keras.ops.layer_normalization(
        x, gamma=None, beta=None, axis=-1, epsilon=None, **kwargs
    )

Normalize the activations of the previous layer for each given example in a batch independently, rather than across a batch like Batch Normalization. i.e. applies a transformation that maintains the mean activation within each example close to 0 and the activation standard deviation close to 1.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `x` | Input tensor. |
| `gamma` | Optional scaling factor for the normalization. |
| `beta` | Optional add offset for the normalized tensor. |
| `axis` | The axis or axes along which to perform normalization. Default to `-1`. |
| `epsilon` | A lower bound value for the norm. Defaults to [`backend.epsilon()`](https://www.tensorflow.org/api_docs/python/tf/keras/backend/epsilon)<br>. |

|     |
| --- |
| Returns<br>------- |     |
| The normalized array. |     |

#### Example:

    x = keras.ops.arange(5, dtype="float32")

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.