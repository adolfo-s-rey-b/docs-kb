[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/vision/backbones/EfficientNet#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/vision/backbones/EfficientNet)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/vision/backbones/EfficientNet?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/backbones/EfficientNet#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tfm/vision/backbones/EfficientNet#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/vision/backbones/EfficientNet#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/vision/backbones/EfficientNet#call)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.vision.backbones.EfficientNet Stay organized with collections Save and categorize content based on your preferences.
========================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/backbones/EfficientNet#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tfm/vision/backbones/EfficientNet#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/vision/backbones/EfficientNet#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/vision/backbones/EfficientNet#call)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/modeling/backbones/efficientnet.py#L93-L301)

Creates an EfficientNet family model.

tfm.vision.backbones.EfficientNet(
        model_id: str,
        input_specs: tf_keras.layers.InputSpec = layers.InputSpec(shape=[None, None, None, 3]),
        se_ratio: float = 0.0,
        stochastic_depth_drop_rate: float = 0.0,
        kernel_initializer: str = 'VarianceScaling',
        kernel_regularizer: tf_keras.regularizers.Regularizer = None,
        bias_regularizer: tf_keras.regularizers.Regularizer = None,
        activation: str = 'relu',
        se_inner_activation: str = 'relu',
        use_sync_bn: bool = False,
        norm_momentum: float = 0.99,
        norm_epsilon: float = 0.001,
        **kwargs
    )

This implements the EfficientNet model from: Mingxing Tan, Quoc V. Le. EfficientNet: Rethinking Model Scaling for Convolutional Neural Networks. ([https://arxiv.org/pdf/1905.11946](https://arxiv.org/pdf/1905.11946)
)

|     |     |
| --- | --- |
| Args<br>---- |     |
| `model_id` | A `str` of model ID of EfficientNet. |
| `input_specs` | A `tf_keras.layers.InputSpec` of the input tensor. |
| `se_ratio` | A `float` of squeeze and excitation ratio for inverted bottleneck blocks. |
| `stochastic_depth_drop_rate` | A `float` of drop rate for drop connect layer. |
| `kernel_initializer` | A `str` for kernel initializer of convolutional layers. |
| `kernel_regularizer` | A `tf_keras.regularizers.Regularizer` object for Conv2D. Default to None. |
| `bias_regularizer` | A `tf_keras.regularizers.Regularizer` object for Conv2D. Default to None. |
| `activation` | A `str` of name of the activation function. |
| `se_inner_activation` | A `str` of name of the activation function used in Sequeeze and Excitation layer. |
| `use_sync_bn` | If True, use synchronized batch normalization. |
| `norm_momentum` | A `float` of normalization momentum for the moving average. |
| `norm_epsilon` | A `float` added to variance to avoid dividing by zero. |
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