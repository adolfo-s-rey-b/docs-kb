[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/crelu#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/crelu)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/crelu?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/crelu#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/crelu#returns)
    
*   [References](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/crelu#references)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.nn.crelu Stay organized with collections Save and categorize content based on your preferences.
============================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/crelu#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/crelu#returns)
    
*   [References](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/crelu#references)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/nn_ops.py#L3590-L3620)

Computes Concatenated ReLU.

tf.compat.v1.nn.crelu(
        features, name=None, axis=-1
    )

Concatenates a ReLU which selects only the positive part of the activation with a ReLU which selects only the _negative_ part of the activation. Note that as a result this non-linearity doubles the depth of the activations. Source: [Understanding and Improving Convolutional Neural Networks via Concatenated Rectified Linear Units. W. Shang, et al.](https://arxiv.org/abs/1603.05201)

|     |     |
| --- | --- |
| Args<br>---- |     |
| `features` | A `Tensor` with type `float`, `double`, `int32`, `int64`, `uint8`, `int16`, or `int8`. |
| `name` | A name for the operation (optional). |
| `axis` | The axis that the output values are concatenated along. Default is -1. |

|     |
| --- |
| Returns<br>------- |     |
| A `Tensor` with the same type as `features`. |     |

|     |
| --- |
| References<br>---------- |     |
| Understanding and Improving Convolutional Neural Networks via Concatenated Rectified Linear Units: [Shang et al., 2016](http://proceedings.mlr.press/v48/shang16)<br> ([pdf](http://proceedings.mlr.press/v48/shang16.pdf)<br>) |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.