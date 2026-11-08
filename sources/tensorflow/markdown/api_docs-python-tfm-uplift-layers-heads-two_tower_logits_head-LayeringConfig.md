[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/uplift/layers/heads/two_tower_logits_head/LayeringConfig#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/uplift/layers/heads/two_tower_logits_head/LayeringConfig)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/uplift/layers/heads/two_tower_logits_head/LayeringConfig?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Attributes](https://www.tensorflow.org/api_docs/python/tfm/uplift/layers/heads/two_tower_logits_head/LayeringConfig#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/uplift/layers/heads/two_tower_logits_head/LayeringConfig#methods)
    *   [from\_dict](https://www.tensorflow.org/api_docs/python/tfm/uplift/layers/heads/two_tower_logits_head/LayeringConfig#from_dict)
        
    *   [\_\_eq\_\_](https://www.tensorflow.org/api_docs/python/tfm/uplift/layers/heads/two_tower_logits_head/LayeringConfig#__eq__)
        
*   [Class Variables](https://www.tensorflow.org/api_docs/python/tfm/uplift/layers/heads/two_tower_logits_head/LayeringConfig#class-variables)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.uplift.layers.heads.two\_tower\_logits\_head.LayeringConfig Stay organized with collections Save and categorize content based on your preferences.
======================================================================================================================================================

*   On this page
*   [Attributes](https://www.tensorflow.org/api_docs/python/tfm/uplift/layers/heads/two_tower_logits_head/LayeringConfig#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/uplift/layers/heads/two_tower_logits_head/LayeringConfig#methods)
    *   [from\_dict](https://www.tensorflow.org/api_docs/python/tfm/uplift/layers/heads/two_tower_logits_head/LayeringConfig#from_dict)
        
    *   [\_\_eq\_\_](https://www.tensorflow.org/api_docs/python/tfm/uplift/layers/heads/two_tower_logits_head/LayeringConfig#__eq__)
        
*   [Class Variables](https://www.tensorflow.org/api_docs/python/tfm/uplift/layers/heads/two_tower_logits_head/LayeringConfig#class-variables)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/recommendation/uplift/layers/heads/two_tower_logits_head.py#L57-L82)

Configuration for all layering methods.

tfm.uplift.layers.heads.two_tower_logits_head.LayeringConfig(
        layering_method: LayeringMethod = LayeringMethod.NONE,
        linear_layering_config: (LinearLayeringConfig | None) = None
    )

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `layering_method` | specifies what layering method to apply. Defaults to [`LayeringMethod.NONE`](https://www.tensorflow.org/api_docs/python/tfm/uplift/layers/heads/two_tower_logits_head/LayeringMethod#NONE)<br>. |
| `linear_layering_config` | configuration for the linear layering method. Will only be used if the `layering_method` is set to [`LayeringMethod.LINEAR_LAYERING`](https://www.tensorflow.org/api_docs/python/tfm/uplift/layers/heads/two_tower_logits_head/LayeringMethod#LINEAR_LAYERING)<br>. |

Methods
-------

### `from_dict`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/recommendation/uplift/layers/heads/two_tower_logits_head.py#L72-L82)

@classmethod

### `__eq__`

__eq__(
        other
    )

Return self==value.

|     |     |
| --- | --- |
| Class Variables<br>--------------- |     |
| layering\_method | `<LayeringMethod.NONE: 'none'>` |
| linear\_layering\_config | `None` |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.