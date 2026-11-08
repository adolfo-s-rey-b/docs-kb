[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/uplift/layers/heads/two_tower_logits_head/LinearLayeringConfig#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/uplift/layers/heads/two_tower_logits_head/LinearLayeringConfig)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/uplift/layers/heads/two_tower_logits_head/LinearLayeringConfig?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Attributes](https://www.tensorflow.org/api_docs/python/tfm/uplift/layers/heads/two_tower_logits_head/LinearLayeringConfig#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/uplift/layers/heads/two_tower_logits_head/LinearLayeringConfig#methods)
    *   [\_\_eq\_\_](https://www.tensorflow.org/api_docs/python/tfm/uplift/layers/heads/two_tower_logits_head/LinearLayeringConfig#__eq__)
        
*   [Class Variables](https://www.tensorflow.org/api_docs/python/tfm/uplift/layers/heads/two_tower_logits_head/LinearLayeringConfig#class-variables)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.uplift.layers.heads.two\_tower\_logits\_head.LinearLayeringConfig Stay organized with collections Save and categorize content based on your preferences.
============================================================================================================================================================

*   On this page
*   [Attributes](https://www.tensorflow.org/api_docs/python/tfm/uplift/layers/heads/two_tower_logits_head/LinearLayeringConfig#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/uplift/layers/heads/two_tower_logits_head/LinearLayeringConfig#methods)
    *   [\_\_eq\_\_](https://www.tensorflow.org/api_docs/python/tfm/uplift/layers/heads/two_tower_logits_head/LinearLayeringConfig#__eq__)
        
*   [Class Variables](https://www.tensorflow.org/api_docs/python/tfm/uplift/layers/heads/two_tower_logits_head/LinearLayeringConfig#class-variables)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/recommendation/uplift/layers/heads/two_tower_logits_head.py#L44-L54)

Configuration for the linear layering method.

tfm.uplift.layers.heads.two_tower_logits_head.LinearLayeringConfig(
        kernel_initializer: str = 'glorot_uniform',
        kernel_regularizer: (str | None) = None
    )

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `kernel_initializer` | kernel initializer for the learnable weight matrix. |
| `kernel_regularizer` | kernel regularizer for the learnable weight matrix. |

Methods
-------

### `__eq__`

__eq__(
        other
    )

Return self==value.

|     |     |
| --- | --- |
| Class Variables<br>--------------- |     |
| kernel\_initializer | `'glorot_uniform'` |
| kernel\_regularizer | `None` |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.