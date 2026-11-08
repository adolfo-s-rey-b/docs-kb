[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/uplift/layers/uplift_networks/two_tower_output_head/TwoTowerOutputHead#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/uplift/layers/uplift_networks/two_tower_output_head/TwoTowerOutputHead)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/uplift/layers/uplift_networks/two_tower_output_head/TwoTowerOutputHead?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/oauth2authorize?return_url=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftfm%2Fuplift%2Flayers%2Fuplift_networks%2Ftwo_tower_output_head%2FTwoTowerOutputHead&scopes=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles.award+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdevprofiles.full_control.firstparty)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/uplift/layers/uplift_networks/two_tower_output_head/TwoTowerOutputHead#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/uplift/layers/uplift_networks/two_tower_output_head/TwoTowerOutputHead#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/uplift/layers/uplift_networks/two_tower_output_head/TwoTowerOutputHead#call)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.uplift.layers.uplift\_networks.two\_tower\_output\_head.TwoTowerOutputHead Stay organized with collections Save and categorize content based on your preferences.
=====================================================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/uplift/layers/uplift_networks/two_tower_output_head/TwoTowerOutputHead#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/uplift/layers/uplift_networks/two_tower_output_head/TwoTowerOutputHead#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/uplift/layers/uplift_networks/two_tower_output_head/TwoTowerOutputHead#call)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/recommendation/uplift/layers/uplift_networks/two_tower_output_head.py#L28-L180)

Two tower training and inference output computation.

tfm.uplift.layers.uplift_networks.two_tower_output_head.TwoTowerOutputHead(
        treatment_indicator_feature_name: str,
        uplift_network: base_uplift_networks.BaseTwoTowerUpliftNetwork,
        inverse_link_fn: (Callable[[tf.Tensor], tf.Tensor] | None) = None,
        **kwargs
    )

This layer is intended to be used in conjunction with a two tower uplift network layer to compute training and inference outputs. It passes the input dictionary of feature tensors to the uplift network and computes training and inference tensors from the uplift network's outputs.

The control, treatment, and uplift predictions are computed from the uplift network's control and treatment logits. Additionally, if the treatment indicator tensor is part of the inputs, the true logits are also computed to be used for loss computation. The treatment indicator tensor should therefore be present in the inputs dictionary during training and evaluation.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `treatment_indicator_feature_name` | the name of the feature representing the treatment indicator tensor, which should be castable to a boolean tensor (False for control and True for treatment). When this tensor is part of the layer inputs, additional true logits are returned for the loss computation. In this case the layer returns a `TwoTowerTrainingOutputs` instance, otherwise a `TwoTowerPredictionOutputs` instance is returned. |
| `uplift_network` | a layer for computing control and treatment logits. Its input is expected to be a dictionary of feature tensors and its output is exptected to be a `TwoTowerNetworkOutputs` instance. |
| `inverse_link_fn` | a function for computing the control and treatment predictions from their respective logits. If left as `None` it is functionally equivalent to the idendity function. |
| `**kwargs` | base layer keyword arguments. |

Methods
-------

### `call`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/recommendation/uplift/layers/uplift_networks/two_tower_output_head.py#L74-L155)

call(
        inputs: types.DictOfTensors,
        training: (bool | None) = None,
        mask: (tf.Tensor | None) = None
    ) -> (types.TwoTowerPredictionOutputs | types.TwoTowerTrainingOutputs)

Computes two tower inference and training outputs.

|     |     |
| --- | --- |
| Args |     |
| `inputs` | feature tensors to be passed to the uplift network. For training and evaluation, the treatment indicator tensor must be given as part of the inputs. |
| `training` | optional boolean training flag to pass to the uplift network. |
| `mask` | optional tensor mask to pass to the uplift network. |

|     |
| --- |
| Returns |     |
| `TwoTowerTrainingOutputs` when the treatment indicator tensor is part of the input features, otherwise `TwoTowerPredictionOutputs`. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.