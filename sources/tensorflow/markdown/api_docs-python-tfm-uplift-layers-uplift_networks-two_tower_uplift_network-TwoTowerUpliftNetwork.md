[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/uplift/layers/uplift_networks/two_tower_uplift_network/TwoTowerUpliftNetwork#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/uplift/layers/uplift_networks/two_tower_uplift_network/TwoTowerUpliftNetwork)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/uplift/layers/uplift_networks/two_tower_uplift_network/TwoTowerUpliftNetwork?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/uplift/layers/uplift_networks/two_tower_uplift_network/TwoTowerUpliftNetwork#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tfm/uplift/layers/uplift_networks/two_tower_uplift_network/TwoTowerUpliftNetwork#raises)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/uplift/layers/uplift_networks/two_tower_uplift_network/TwoTowerUpliftNetwork#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/uplift/layers/uplift_networks/two_tower_uplift_network/TwoTowerUpliftNetwork#call)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.uplift.layers.uplift\_networks.two\_tower\_uplift\_network.TwoTowerUpliftNetwork Stay organized with collections Save and categorize content based on your preferences.
===========================================================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/uplift/layers/uplift_networks/two_tower_uplift_network/TwoTowerUpliftNetwork#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tfm/uplift/layers/uplift_networks/two_tower_uplift_network/TwoTowerUpliftNetwork#raises)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/uplift/layers/uplift_networks/two_tower_uplift_network/TwoTowerUpliftNetwork#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/uplift/layers/uplift_networks/two_tower_uplift_network/TwoTowerUpliftNetwork#call)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/recommendation/uplift/layers/uplift_networks/two_tower_uplift_network.py#L27-L212)

Computes control and treatment logits in two separate towers.

Inherits From: [`BaseTwoTowerUpliftNetwork`](https://www.tensorflow.org/api_docs/python/tfm/uplift/layers/uplift_networks/base_uplift_networks/BaseTwoTowerUpliftNetwork)

tfm.uplift.layers.uplift_networks.two_tower_uplift_network.TwoTowerUpliftNetwork(
        backbone: tf_keras.layers.Layer,
        control_tower: tf_keras.layers.Layer,
        treatment_tower: tf_keras.layers.Layer,
        logits_head: tf_keras.layers.Layer,
        control_feature_encoder: (tf_keras.layers.Layer | None) = None,
        control_input_combiner: (tf_keras.layers.Layer | None) = None,
        treatment_feature_encoder: (tf_keras.layers.Layer | None) = None,
        treatment_input_combiner: (tf_keras.layers.Layer | None) = None,
        **kwargs
    )

Takes as input a dictionary of feature tensors and computes logits for the control and treatment groups. The layer returns a `TwoTowerNetworkOutputs` which contains the main tensors computed during the feed forward pass of the network.

See ../../README.md for more details on the network's architecture.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `backbone` | encodes input features into a shared embedding for the control and treatment towers. Its input is a dictionary with the input features and its output is expected to be a single dense embedding. |
| `control_tower` | computes an embedding for the control group. Its input and output is a single dense tensor. |
| `treatment_tower` | computes an embedding for the treatment group. Its input and output is a single dense tensor. |
| `logits_head` | computes control and treatment logits. Its inputs is a tuple of (control\_embedding, treatment\_embedding) and its output is expected to be a tuple of (control\_logits, treatment\_logits). |
| `control_feature_encoder` | encodes control specific input features into a dense tensor. Its input is the entire inputs dictionary. If this layer is provided, a control\_input\_combiner layer must also be given. |
| `control_input_combiner` | combines the shared embedding from the backbone with the control\_feature\_encoder output embedding. Its input is a list with the shared and control specific embedding, and its output is a single dense embedding to be fed into the control\_tower layer. This layer should only be provided if a control\_feature\_encoder is also provided. |
| `treatment_feature_encoder` | encodes treatment specific input features into a dense tensor. Its input is the entire inputs dictionary. If this layer is provided, a treatment\_input\_combiner layer must also be given. |
| `treatment_input_combiner` | combines the shared embedding from the backbone with the treatment\_feature\_encoder output embedding. Its input is a list with the shared and treatment specific embedding, and its output is a single dense embedding to be fed into the treatment\_tower layer. This layer should only be provided if a treatment\_feature\_encoder is also provided. |
| `**kwargs` | base layer keyword arguments. |

|     |
| --- |
| Raises<br>------ |     |
| ValueError if only one of the control encoder or combiner layers is set. Both must be a Keras layer or None. ValueError if only one of the treatment encoder or combiner layers is set. Both must be a Keras layer or None. |     |

Methods
-------

### `call`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/recommendation/uplift/layers/uplift_networks/two_tower_uplift_network.py#L126-L177)

call(
        inputs: types.DictOfTensors,
        training: (bool | None) = None,
        mask: (tf.Tensor | None) = None
    ) -> types.TwoTowerNetworkOutputs

Computes control and treatment logits.

|     |     |
| --- | --- |
| Args |     |
| `inputs` | dictionary of feature tensors to be passed to the backbone and control/treatment feature encoder layers when set. |
| `training` | unused optional training flag. |
| `mask` | unused optional mask. |

|     |
| --- |
| Returns |     |
| A `TwoTowerNetworkOutputs` ExtensionType which should be used as a dataclass to access the main tensors computed during the feed forward pass of the network. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.