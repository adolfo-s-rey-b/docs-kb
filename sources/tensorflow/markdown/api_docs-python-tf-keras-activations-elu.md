[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/activations/elu#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/activations/elu)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/activations/elu?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/activations/elu#args)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.activations.elu Stay organized with collections Save and categorize content based on your preferences.
===============================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/activations/elu#args)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/activations/activations.py#L168-L194)

Exponential Linear Unit.

tf.keras.activations.elu(
        x, alpha=1.0
    )

The exponential linear unit (ELU) with `alpha > 0` is defined as:

*   `x` if `x > 0`
*   alpha \* `exp(x) - 1` if `x < 0`

ELUs have negative values which pushes the mean of the activations closer to zero.

Mean activations that are closer to zero enable faster learning as they bring the gradient closer to the natural gradient. ELUs saturate to a negative value when the argument gets smaller. Saturation means a small derivative which decreases the variation and the information that is propagated to the next layer.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `x` | Input tensor. |
| `alpha` | A scalar, slope of positive section. Defaults to `1.0`. |

#### Reference:

*   [Clevert et al., 2016](https://arxiv.org/abs/1511.07289)
    

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.