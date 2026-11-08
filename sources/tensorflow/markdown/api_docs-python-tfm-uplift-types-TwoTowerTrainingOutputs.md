[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/uplift/types/TwoTowerTrainingOutputs#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/uplift/types/TwoTowerTrainingOutputs)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/uplift/types/TwoTowerTrainingOutputs?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Attributes](https://www.tensorflow.org/api_docs/python/tfm/uplift/types/TwoTowerTrainingOutputs#attributes)
    
*   [Child Classes](https://www.tensorflow.org/api_docs/python/tfm/uplift/types/TwoTowerTrainingOutputs#child_classes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/uplift/types/TwoTowerTrainingOutputs#methods)
    *   [\_\_eq\_\_](https://www.tensorflow.org/api_docs/python/tfm/uplift/types/TwoTowerTrainingOutputs#__eq__)
        
    *   [\_\_ne\_\_](https://www.tensorflow.org/api_docs/python/tfm/uplift/types/TwoTowerTrainingOutputs#__ne__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.uplift.types.TwoTowerTrainingOutputs Stay organized with collections Save and categorize content based on your preferences.
===============================================================================================================================

*   On this page
*   [Attributes](https://www.tensorflow.org/api_docs/python/tfm/uplift/types/TwoTowerTrainingOutputs#attributes)
    
*   [Child Classes](https://www.tensorflow.org/api_docs/python/tfm/uplift/types/TwoTowerTrainingOutputs#child_classes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/uplift/types/TwoTowerTrainingOutputs#methods)
    *   [\_\_eq\_\_](https://www.tensorflow.org/api_docs/python/tfm/uplift/types/TwoTowerTrainingOutputs#__eq__)
        
    *   [\_\_ne\_\_](https://www.tensorflow.org/api_docs/python/tfm/uplift/types/TwoTowerTrainingOutputs#__ne__)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/recommendation/uplift/types.py#L94-L121)

Training tensors computed by a `TwoTowerUpliftNetwork` layer.

Inherits From: [`TwoTowerPredictionOutputs`](https://www.tensorflow.org/api_docs/python/tfm/uplift/types/TwoTowerPredictionOutputs)
, [`TwoTowerNetworkOutputs`](https://www.tensorflow.org/api_docs/python/tfm/uplift/types/TwoTowerNetworkOutputs)

tfm.uplift.types.TwoTowerTrainingOutputs(
        shared_embedding,
        control_logits,
        treatment_logits,
        control_predictions,
        treatment_predictions,
        uplift,
        true_logits,
        true_predictions,
        is_treatment
    )

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `true_logits` | logits for either the control or treatment group, depending on the corresponding value in the `is_treatment` tensor. It will contain treatment group logits for the `is_treatment == 1` entries and control group logits otherwise. |
| `true_predictions` | predictions for either the control or treatment group, depending on the corresponding value in the `is_treatment` tensor. It will contain treatment group predictions for the `is_treatment == 1` entries and control group predictions otherwise. |
| `is_treatment` | a boolean [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> indicating if the example belongs to the treatment group (True) or control group (False). |
| `dtype` |     |
| `shape` |     |

Child Classes
-------------

[`class Spec`](https://www.tensorflow.org/api_docs/python/tfm/uplift/types/TwoTowerTrainingOutputs/Spec)

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