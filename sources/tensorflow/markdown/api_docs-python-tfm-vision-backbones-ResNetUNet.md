[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/vision/backbones/ResNetUNet#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/vision/backbones/ResNetUNet)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/vision/backbones/ResNetUNet?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/backbones/ResNetUNet#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tfm/vision/backbones/ResNetUNet#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/vision/backbones/ResNetUNet#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/vision/backbones/ResNetUNet#call)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.vision.backbones.ResNetUNet Stay organized with collections Save and categorize content based on your preferences.
======================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/backbones/ResNetUNet#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tfm/vision/backbones/ResNetUNet#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/vision/backbones/ResNetUNet#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/vision/backbones/ResNetUNet#call)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/modeling/backbones/resnet_unet.py#L184-L553)

Creates ResNet and ResNet-RS family models.

tfm.vision.backbones.ResNetUNet(
        model_id: int,
        input_specs: tf_keras.layers.InputSpec = layers.InputSpec(shape=[None, None, None, 3]),
        depth_multiplier: float = 1.0,
        stem_type: str = 'v0',
        resnetd_shortcut: bool = False,
        replace_stem_max_pool: bool = False,
        se_ratio: Optional[float] = None,
        init_stochastic_depth_rate: float = 0.0,
        upsample_repeats: Optional[List[int]] = None,
        upsample_filters: Optional[List[int]] = None,
        upsample_kernel_sizes: Optional[List[int]] = None,
        scale_stem: bool = True,
        activation: str = 'relu',
        use_sync_bn: bool = False,
        norm_momentum: float = 0.99,
        norm_epsilon: float = 0.001,
        kernel_initializer: str = 'VarianceScaling',
        kernel_regularizer: Optional[tf_keras.regularizers.Regularizer] = None,
        bias_regularizer: Optional[tf_keras.regularizers.Regularizer] = None,
        bn_trainable: bool = True,
        classification_output: bool = False,
        **kwargs
    )

This implements the Deep Residual Network from: Kaiming He, Xiangyu Zhang, Shaoqing Ren, Jian Sun. Deep Residual Learning for Image Recognition. ([https://arxiv.org/pdf/1512.03385](https://arxiv.org/pdf/1512.03385)
) and Irwan Bello, William Fedus, Xianzhi Du, Ekin D. Cubuk, Aravind Srinivas, Tsung-Yi Lin, Jonathon Shlens, Barret Zoph. Revisiting ResNets: Improved Training and Scaling Strategies. ([https://arxiv.org/abs/2103.07579](https://arxiv.org/abs/2103.07579)
).

|     |     |
| --- | --- |
| Args<br>---- |     |
| `model_id` | An `int` of the depth of ResNet backbone model. |
| `input_specs` | A `tf_keras.layers.InputSpec` of the input tensor. |
| `depth_multiplier` | A `float` of the depth multiplier to uniformaly scale up all layers in channel size. This argument is also referred to as `width_multiplier` in (https://arxiv.org/abs/2103.07579). |
| `stem_type` | A `str` of stem type of ResNet. Default to `v0`. If set to [`v1`](https://www.tensorflow.org/api_docs/python/tf/compat/v1)<br>, use ResNet-D type stem (https://arxiv.org/abs/1812.01187). |
| `resnetd_shortcut` | A `bool` of whether to use ResNet-D shortcut in downsampling blocks. |
| `replace_stem_max_pool` | A `bool` of whether to replace the max pool in stem with a stride-2 conv, |
| `se_ratio` | A `float` or None. Ratio of the Squeeze-and-Excitation layer. |
| `init_stochastic_depth_rate` | A `float` of initial stochastic depth rate. |
| `upsample_repeats` | A `list` for upsample repeats of the ConvNext blocks for each level starting from L5, then L4, and so on. |
| `upsample_filters` | A `list` for the upsample filter sizes for the ConvNext blocks for each level. |
| `upsample_kernel_sizes` | A `list` for upsample kernel sizes for the ConvNext blocks for each level. |
| `scale_stem` | A `bool` of whether to scale stem layers. |
| `activation` | A `str` name of the activation function. |
| `use_sync_bn` | If True, use synchronized batch normalization. |
| `norm_momentum` | A `float` of normalization momentum for the moving average. |
| `norm_epsilon` | A small `float` added to variance to avoid dividing by zero. |
| `kernel_initializer` | A str for kernel initializer of convolutional layers. |
| `kernel_regularizer` | A `tf_keras.regularizers.Regularizer` object for Conv2D. Default to None. |
| `bias_regularizer` | A `tf_keras.regularizers.Regularizer` object for Conv2D. Default to None. |
| `bn_trainable` | A `bool` that indicates whether batch norm layers should be trainable. Default to True. |
| `classification_output` | A `bool` to output the correct level needed for classification (L3), only set to True for pretraining. |
| `**kwargs` | Additional keyword arguments to be passed. |

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