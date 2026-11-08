[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/uplift/models/two_tower_uplift_model/TwoTowerUpliftModel#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/uplift/models/two_tower_uplift_model/TwoTowerUpliftModel)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/uplift/models/two_tower_uplift_model/TwoTowerUpliftModel?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/uplift/models/two_tower_uplift_model/TwoTowerUpliftModel#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/uplift/models/two_tower_uplift_model/TwoTowerUpliftModel#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/uplift/models/two_tower_uplift_model/TwoTowerUpliftModel#call)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.uplift.models.two\_tower\_uplift\_model.TwoTowerUpliftModel Stay organized with collections Save and categorize content based on your preferences.
======================================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/uplift/models/two_tower_uplift_model/TwoTowerUpliftModel#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/uplift/models/two_tower_uplift_model/TwoTowerUpliftModel#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/uplift/models/two_tower_uplift_model/TwoTowerUpliftModel#call)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/recommendation/uplift/models/two_tower_uplift_model.py#L29-L131)

Training and inference model for a `BaseTwoTowerUpliftNetwork` layer.

tfm.uplift.models.two_tower_uplift_model.TwoTowerUpliftModel(
        treatment_indicator_feature_name: str,
        uplift_network: base_uplift_networks.BaseTwoTowerUpliftNetwork,
        inverse_link_fn: (Callable[[tf.Tensor], tf.Tensor] | None) = None,
        **kwargs
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `treatment_indicator_feature_name` | the name of the feature representing the treatment\_indicator tensor, which should be castable to a boolean tensor (False for control and True for treatment). This tensor is required during training and evaluation to compute the true logits needed for loss computation. |
| `uplift_network` | a layer for computing control and treatment logits. Its input is expected to be a dictionary of feature tensors and its output is exptected to be a `TwoTowerNetworkOutputs` instance. |
| `inverse_link_fn` | a function for computing the control and treatment predictions from their respective logits. If left as `None` it is functionally equivalent to the identity function. |
| `**kwargs` | base model keyword arguments. |

Methods
-------

### `call`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/recommendation/uplift/models/two_tower_uplift_model.py#L68-L74)

call(
        inputs: types.DictOfTensors,
        training: (bool | None) = None,
        mask: (tf.Tensor | None) = None
    ) -> (types.TwoTowerPredictionOutputs | types.TwoTowerTrainingOutputs)

Calls the model on new inputs and returns the outputs as tensors.

In this case `call()` just reapplies all ops in the graph to the new inputs (e.g. build a new computational graph from the provided inputs).

|     |     |
| --- | --- |
| Args |     |
| `inputs` | Input tensor, or dict/list/tuple of input tensors. |
| `training` | Boolean or boolean scalar tensor, indicating whether to run the `Network` in training mode or inference mode. |
| `mask` | A mask or list of masks. A mask can be either a boolean tensor or None (no mask). For more details, check the guide [here](https://www.tensorflow.org/guide/keras/masking_and_padding)<br>. |

|     |
| --- |
| Returns |     |
| A tensor if there is a single output, or a list of tensors if there are more than one outputs. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.