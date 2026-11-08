[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/MixingMechanism#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/MixingMechanism)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/MixingMechanism?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Possible options](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/MixingMechanism#possible-options)
    
*   [Class Variables](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/MixingMechanism#class-variables)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.nlp.layers.MixingMechanism Stay organized with collections Save and categorize content based on your preferences.
=====================================================================================================================

*   On this page
*   [Possible options](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/MixingMechanism#possible-options)
    
*   [Class Variables](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/MixingMechanism#class-variables)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/modeling/layers/mixing.py#L45-L56)

Determines the type of mixing layer.

|     |     |
| --- | --- |
| Possible options<br>---------------- |     |
| `FOURIER` | Fourier Transform mixing. |
| `LINEAR` | Mixing using dense matrix multiplications with learnable weights. |
| `HARTLEY` | Hartley Transform mixing. |

|     |     |
| --- | --- |
| Class Variables<br>--------------- |     |
| FOURIER | `<MixingMechanism.FOURIER: 'fourier'>` |
| HARTLEY | `<MixingMechanism.HARTLEY: 'hartley'>` |
| LINEAR | `<MixingMechanism.LINEAR: 'linear'>` |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.