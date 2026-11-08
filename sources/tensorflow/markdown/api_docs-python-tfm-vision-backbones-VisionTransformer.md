[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/vision/backbones/VisionTransformer#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/vision/backbones/VisionTransformer)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/vision/backbones/VisionTransformer?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Attributes](https://www.tensorflow.org/api_docs/python/tfm/vision/backbones/VisionTransformer#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/vision/backbones/VisionTransformer#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/vision/backbones/VisionTransformer#call)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.vision.backbones.VisionTransformer Stay organized with collections Save and categorize content based on your preferences.
=============================================================================================================================

*   On this page
*   [Attributes](https://www.tensorflow.org/api_docs/python/tfm/vision/backbones/VisionTransformer#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/vision/backbones/VisionTransformer#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/vision/backbones/VisionTransformer#call)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/modeling/backbones/vit.py#L222-L357)

Class to build VisionTransformer family model.

tfm.vision.backbones.VisionTransformer(
        mlp_dim=3072,
        num_heads=12,
        num_layers=12,
        attention_dropout_rate=0.0,
        dropout_rate=0.1,
        init_stochastic_depth_rate=0.0,
        input_specs=layers.InputSpec(shape=[None, None, None, 3]),
        patch_size=16,
        hidden_size=768,
        representation_size=0,
        pooler='token',
        kernel_regularizer=None,
        original_init: bool = True,
        output_encoded_tokens: bool = True,
        output_2d_feature_maps: bool = False,
        pos_embed_shape: Optional[Tuple[int, int]] = None,
        layer_scale_init_value: float = 0.0,
        transformer_partition_dims: Optional[Tuple[int, int, int, int]] = None,
        output_attention_scores: bool = False
    )

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `output_specs` | A dict of {level: TensorShape} pairs for the model output. |

Methods
-------

### `call`

call(
        inputs, training=None, mask=None
    )

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