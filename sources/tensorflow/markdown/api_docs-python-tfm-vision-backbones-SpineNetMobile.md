[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/vision/backbones/SpineNetMobile#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/vision/backbones/SpineNetMobile)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/vision/backbones/SpineNetMobile?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [This implements](https://www.tensorflow.org/api_docs/python/tfm/vision/backbones/SpineNetMobile#this-implements)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/backbones/SpineNetMobile#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tfm/vision/backbones/SpineNetMobile#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/vision/backbones/SpineNetMobile#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/vision/backbones/SpineNetMobile#call)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.vision.backbones.SpineNetMobile Stay organized with collections Save and categorize content based on your preferences.
==========================================================================================================================

*   On this page
*   [This implements](https://www.tensorflow.org/api_docs/python/tfm/vision/backbones/SpineNetMobile#this-implements)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/backbones/SpineNetMobile#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tfm/vision/backbones/SpineNetMobile#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/vision/backbones/SpineNetMobile#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/vision/backbones/SpineNetMobile#call)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/modeling/backbones/spinenet_mobile.py#L117-L509)

Creates a Mobile SpineNet family model.

tfm.vision.backbones.SpineNetMobile(
        input_specs: tf_keras.layers.InputSpec = tf_keras.layers.InputSpec(shape=[None, None, None, 3]),
        min_level: int = 3,
        max_level: int = 7,
        block_specs: Optional[List[BlockSpec]] = None,
        endpoints_num_filters: int = 256,
        se_ratio: float = 0.2,
        block_repeats: int = 1,
        filter_size_scale: float = 1.0,
        expand_ratio: int = 6,
        init_stochastic_depth_rate=0.0,
        kernel_initializer: str = 'VarianceScaling',
        kernel_regularizer: Optional[tf_keras.regularizers.Regularizer] = None,
        bias_regularizer: Optional[tf_keras.regularizers.Regularizer] = None,
        activation: str = 'relu',
        use_sync_bn: bool = False,
        norm_momentum: float = 0.99,
        norm_epsilon: float = 0.001,
        use_keras_upsampling_2d: bool = False,
        **kwargs
    )

|     |     |
| --- | --- |
| This implements<br>--------------- |     |
| \[1\] Xianzhi Du, Tsung-Yi Lin, Pengchong Jin, Golnaz Ghiasi, Mingxing Tan, Yin Cui, Quoc V. Le, Xiaodan Song. |     |
| `SpineNet` | Learning Scale-Permuted Backbone for Recognition and Localization. (https://arxiv.org/abs/1912.05027). \[2\] Xianzhi Du, Tsung-Yi Lin, Pengchong Jin, Yin Cui, Mingxing Tan, Quoc Le, Xiaodan Song. Efficient Scale-Permuted Backbone with Learned Resource Distribution. (https://arxiv.org/abs/2010.11426). |

|     |     |
| --- | --- |
| Args<br>---- |     |
| `input_specs` | A `tf_keras.layers.InputSpec` of the input tensor. |
| `min_level` | An `int` of min level for output mutiscale features. |
| `max_level` | An `int` of max level for output mutiscale features. |
| `block_specs` | The block specifications for the SpineNet model discovered by NAS. |
| `endpoints_num_filters` | An `int` of feature dimension for the output endpoints. |
| `se_ratio` | A `float` of Squeeze-and-Excitation ratio. |
| `block_repeats` | An `int` of number of blocks contained in the layer. |
| `filter_size_scale` | A `float` of multiplier for the filters (number of channels) for all convolution ops. The value must be greater than zero. Typical usage will be to set this value in (0, 1) to reduce the number of parameters or computation cost of the model. |
| `expand_ratio` | An `integer` of expansion ratios for inverted bottleneck blocks. |
| `init_stochastic_depth_rate` | A `float` of initial stochastic depth rate. |
| `kernel_initializer` | A str for kernel initializer of convolutional layers. |
| `kernel_regularizer` | A `tf_keras.regularizers.Regularizer` object for Conv2D. Default to None. |
| `bias_regularizer` | A `tf_keras.regularizers.Regularizer` object for Conv2D. Default to None. |
| `activation` | A `str` name of the activation function. |
| `use_sync_bn` | If True, use synchronized batch normalization. |
| `norm_momentum` | A `float` of normalization momentum for the moving average. |
| `norm_epsilon` | A small `float` added to variance to avoid dividing by zero. |
| `use_keras_upsampling_2d` | If True, use keras UpSampling2D layer. |
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