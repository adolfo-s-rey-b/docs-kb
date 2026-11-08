[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/uplift/types/TwoTowerNetworkOutputs#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/uplift/types/TwoTowerNetworkOutputs)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/uplift/types/TwoTowerNetworkOutputs?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Attributes](https://www.tensorflow.org/api_docs/python/tfm/uplift/types/TwoTowerNetworkOutputs#attributes)
    
*   [Child Classes](https://www.tensorflow.org/api_docs/python/tfm/uplift/types/TwoTowerNetworkOutputs#child_classes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/uplift/types/TwoTowerNetworkOutputs#methods)
    *   [\_\_eq\_\_](https://www.tensorflow.org/api_docs/python/tfm/uplift/types/TwoTowerNetworkOutputs#__eq__)
        
    *   [\_\_ne\_\_](https://www.tensorflow.org/api_docs/python/tfm/uplift/types/TwoTowerNetworkOutputs#__ne__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.uplift.types.TwoTowerNetworkOutputs Stay organized with collections Save and categorize content based on your preferences.
==============================================================================================================================

*   On this page
*   [Attributes](https://www.tensorflow.org/api_docs/python/tfm/uplift/types/TwoTowerNetworkOutputs#attributes)
    
*   [Child Classes](https://www.tensorflow.org/api_docs/python/tfm/uplift/types/TwoTowerNetworkOutputs#child_classes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/uplift/types/TwoTowerNetworkOutputs#methods)
    *   [\_\_eq\_\_](https://www.tensorflow.org/api_docs/python/tfm/uplift/types/TwoTowerNetworkOutputs#__eq__)
        
    *   [\_\_ne\_\_](https://www.tensorflow.org/api_docs/python/tfm/uplift/types/TwoTowerNetworkOutputs#__ne__)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/recommendation/uplift/types.py#L28-L66)

Tensors computed by a `BaseTwoTowerUpliftNetwork` layer.

tfm.uplift.types.TwoTowerNetworkOutputs(
        shared_embedding, control_logits, treatment_logits
    )

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `shared_embedding` | embedding computed by the backbone layer and used as a shared representation for the control and treatment towers. |
| `control_logits` | logits for the control group. Its shape and dtype must be the same as the treatment logits. |
| `treatment_logits` | logits for the treatment group. Its shape and dtype must be the same as the control logits. |
| `dtype` |     |
| `shape` |     |

Child Classes
-------------

[`class Spec`](https://www.tensorflow.org/api_docs/python/tfm/uplift/types/TwoTowerNetworkOutputs/Spec)

Methods
-------

### `__eq__`

__eq__(
        other
    )

Return self==value.

### `__ne__`

__ne__(
        other
    )

Return self!=value.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.