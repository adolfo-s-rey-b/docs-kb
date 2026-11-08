[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/utils/activations/hard_swish#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/utils/activations/hard_swish)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/utils/activations/hard_swish?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/utils/activations/hard_swish#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfm/utils/activations/hard_swish#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.utils.activations.hard\_swish Stay organized with collections Save and categorize content based on your preferences.
========================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/utils/activations/hard_swish#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfm/utils/activations/hard_swish#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/modeling/activations/swish.py#L41-L56)

Computes a hard version of the swish function.

tfm.utils.activations.hard_swish(
        features
    )

This operation can be used to reduce computational cost and improve quantization for edge devices.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `features` | A `Tensor` representing preactivation values. |

|     |
| --- |
| Returns<br>------- |     |
| The activation value. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.