[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/uplift/layers/heads/two_tower_logits_head#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/uplift/layers/heads/two_tower_logits_head)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/uplift/layers/heads/two_tower_logits_head?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Classes](https://www.tensorflow.org/api_docs/python/tfm/uplift/layers/heads/two_tower_logits_head#classes)
    
*   [Other Members](https://www.tensorflow.org/api_docs/python/tfm/uplift/layers/heads/two_tower_logits_head#other-members)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

Module: tfm.uplift.layers.heads.two\_tower\_logits\_head Stay organized with collections Save and categorize content based on your preferences.
===============================================================================================================================================

*   On this page
*   [Classes](https://www.tensorflow.org/api_docs/python/tfm/uplift/layers/heads/two_tower_logits_head#classes)
    
*   [Other Members](https://www.tensorflow.org/api_docs/python/tfm/uplift/layers/heads/two_tower_logits_head#other-members)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/recommendation/uplift/layers/heads/two_tower_logits_head.py)

Builds a TwoTowerLogitsHead layer.

Classes
-------

[`class LayeringConfig`](https://www.tensorflow.org/api_docs/python/tfm/uplift/layers/heads/two_tower_logits_head/LayeringConfig)
: Configuration for all layering methods.

[`class LayeringMethod`](https://www.tensorflow.org/api_docs/python/tfm/uplift/layers/heads/two_tower_logits_head/LayeringMethod)
: Layering method between the control and treatment towers.

[`class LinearLayeringConfig`](https://www.tensorflow.org/api_docs/python/tfm/uplift/layers/heads/two_tower_logits_head/LinearLayeringConfig)
: Configuration for the linear layering method.

[`class TwoTowerLogitsHead`](https://www.tensorflow.org/api_docs/python/tfm/uplift/layers/heads/two_tower_logits_head/TwoTowerLogitsHead)
: Computes control and treatment logits from their respective embeddings.

|     |     |
| --- | --- |
| Other Members<br>------------- |     |
| annotations | Instance of `__future__._Feature` |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.