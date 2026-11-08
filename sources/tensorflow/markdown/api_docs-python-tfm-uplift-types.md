[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/uplift/types#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/uplift/types)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/uplift/types?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Classes](https://www.tensorflow.org/api_docs/python/tfm/uplift/types#classes)
    
*   [Type Aliases](https://www.tensorflow.org/api_docs/python/tfm/uplift/types#type_aliases)
    
*   [Other Members](https://www.tensorflow.org/api_docs/python/tfm/uplift/types#other-members)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

Module: tfm.uplift.types Stay organized with collections Save and categorize content based on your preferences.
===============================================================================================================

*   On this page
*   [Classes](https://www.tensorflow.org/api_docs/python/tfm/uplift/types#classes)
    
*   [Type Aliases](https://www.tensorflow.org/api_docs/python/tfm/uplift/types#type_aliases)
    
*   [Other Members](https://www.tensorflow.org/api_docs/python/tfm/uplift/types#other-members)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/recommendation/uplift/types.py)

Defines types used by the keras uplift modeling library.

Classes
-------

[`class TwoTowerNetworkOutputs`](https://www.tensorflow.org/api_docs/python/tfm/uplift/types/TwoTowerNetworkOutputs)
: Tensors computed by a `BaseTwoTowerUpliftNetwork` layer.

[`class TwoTowerPredictionOutputs`](https://www.tensorflow.org/api_docs/python/tfm/uplift/types/TwoTowerPredictionOutputs)
: Inference tensors computed by a `TwoTowerUpliftNetwork` layer.

[`class TwoTowerTrainingOutputs`](https://www.tensorflow.org/api_docs/python/tfm/uplift/types/TwoTowerTrainingOutputs)
: Training tensors computed by a `TwoTowerUpliftNetwork` layer.

Type Aliases
------------

[`DictOfTensors`](https://www.tensorflow.org/api_docs/python/tfm/uplift/types/DictOfTensors)

[`ListOfTensors`](https://www.tensorflow.org/api_docs/python/tfm/uplift/types/ListOfTensors)

[`TupleOfTensors`](https://www.tensorflow.org/api_docs/python/tfm/uplift/types/TupleOfTensors)

|     |     |
| --- | --- |
| Other Members<br>------------- |     |
| CollectionOfTensors | Instance of `types.UnionType` |
| TensorType | Instance of `types.UnionType` |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.