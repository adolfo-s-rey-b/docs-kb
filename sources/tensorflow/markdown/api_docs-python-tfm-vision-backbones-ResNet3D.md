[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/vision/backbones/ResNet3D#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/vision/backbones/ResNet3D)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/vision/backbones/ResNet3D?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftfm%2Fvision%2Fbackbones%2FResNet3D&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/backbones/ResNet3D#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tfm/vision/backbones/ResNet3D#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/vision/backbones/ResNet3D#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/vision/backbones/ResNet3D#call)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.vision.backbones.ResNet3D Stay organized with collections Save and categorize content based on your preferences.
====================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/backbones/ResNet3D#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tfm/vision/backbones/ResNet3D#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/vision/backbones/ResNet3D#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/vision/backbones/ResNet3D#call)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/modeling/backbones/resnet_3d.py#L74-L398)

Creates a 3D ResNet family model.

tfm.vision.backbones.ResNet3D(
        model_id: int,
        temporal_strides: List[int],
        temporal_kernel_sizes: List[Tuple[int]],
        use_self_gating: Optional[List[int]] = None,
        input_specs: tf_keras.layers.InputSpec = layers.InputSpec(shape=[None, None, None, None, 3]),
        stem_type: str = 'v0',
        stem_conv_temporal_kernel_size: int = 5,
        stem_conv_temporal_stride: int = 2,
        stem_pool_temporal_stride: int = 2,
        init_stochastic_depth_rate: float = 0.0,
        activation: str = 'relu',
        se_ratio: Optional[float] = None,
        use_sync_bn: bool = False,
        norm_momentum: float = 0.99,
        norm_epsilon: float = 0.001,
        kernel_initializer: str = 'VarianceScaling',
        kernel_regularizer: Optional[tf_keras.regularizers.Regularizer] = None,
        bias_regularizer: Optional[tf_keras.regularizers.Regularizer] = None,
        **kwargs
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `model_id` | An `int` of depth of ResNet backbone model. |
| `temporal_strides` | A list of integers that specifies the temporal strides for all 3d blocks. |
| `temporal_kernel_sizes` | A list of tuples that specifies the temporal kernel sizes for all 3d blocks in different block groups. |
| `use_self_gating` | A list of booleans to specify applying self-gating module or not in each block group. If None, self-gating is not applied. |
| `input_specs` | A `tf_keras.layers.InputSpec` of the input tensor. |
| `stem_type` | A `str` of stem type of ResNet. Default to `v0`. If set to [`v1`](https://www.tensorflow.org/api_docs/python/tf/compat/v1)<br>, use ResNet-D type stem (https://arxiv.org/abs/1812.01187). |
| `stem_conv_temporal_kernel_size` | An `int` of temporal kernel size for the first conv layer. |
| `stem_conv_temporal_stride` | An `int` of temporal stride for the first conv layer. |
| `stem_pool_temporal_stride` | An `int` of temporal stride for the first pool layer. |
| `init_stochastic_depth_rate` | A `float` of initial stochastic depth rate. |
| `activation` | A `str` of name of the activation function. |
| `se_ratio` | A `float` or None. Ratio of the Squeeze-and-Excitation layer. |
| `use_sync_bn` | If True, use synchronized batch normalization. |
| `norm_momentum` | A `float` of normalization momentum for the moving average. |
| `norm_epsilon` | A `float` added to variance to avoid dividing by zero. |
| `kernel_initializer` | A str for kernel initializer of convolutional layers. |
| `kernel_regularizer` | A `tf_keras.regularizers.Regularizer` object for Conv2D. Default to None. |
| `bias_regularizer` | A `tf_keras.regularizers.Regularizer` object for Conv2D. Default to None. |
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