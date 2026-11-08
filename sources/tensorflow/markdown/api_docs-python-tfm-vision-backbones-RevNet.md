[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/vision/backbones/RevNet#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/vision/backbones/RevNet)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/vision/backbones/RevNet?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [This implements](https://www.tensorflow.org/api_docs/python/tfm/vision/backbones/RevNet#this-implements)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/backbones/RevNet#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tfm/vision/backbones/RevNet#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/vision/backbones/RevNet#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/vision/backbones/RevNet#call)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.vision.backbones.RevNet Stay organized with collections Save and categorize content based on your preferences.
==================================================================================================================

*   On this page
*   [This implements](https://www.tensorflow.org/api_docs/python/tfm/vision/backbones/RevNet#this-implements)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/backbones/RevNet#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tfm/vision/backbones/RevNet#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/vision/backbones/RevNet#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/vision/backbones/RevNet#call)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/modeling/backbones/revnet.py#L50-L209)

Creates a Reversible ResNet (RevNet) family model.

tfm.vision.backbones.RevNet(
        model_id: int,
        input_specs: tf_keras.layers.InputSpec = tf_keras.layers.InputSpec(shape=[None, None, None, 3]),
        activation: str = 'relu',
        use_sync_bn: bool = False,
        norm_momentum: float = 0.99,
        norm_epsilon: float = 0.001,
        kernel_initializer: str = 'VarianceScaling',
        kernel_regularizer: Optional[tf_keras.regularizers.Regularizer] = None,
        **kwargs
    )

|     |
| --- |
| This implements<br>--------------- |     |
| Aidan N. Gomez, Mengye Ren, Raquel Urtasun, Roger B. Grosse. The Reversible Residual Network: Backpropagation Without Storing Activations. ([https://arxiv.org/pdf/1707.04585.pdf](https://arxiv.org/pdf/1707.04585.pdf)<br>) |     |

|     |     |
| --- | --- |
| Args<br>---- |     |
| `model_id` | An `int` of depth/id of ResNet backbone model. |
| `input_specs` | A `tf_keras.layers.InputSpec` of the input tensor. |
| `activation` | A `str` name of the activation function. |
| `use_sync_bn` | If True, use synchronized batch normalization. |
| `norm_momentum` | A `float` of normalization momentum for the moving average. |
| `norm_epsilon` | A `float` added to variance to avoid dividing by zero. |
| `kernel_initializer` | A str for kernel initializer of convolutional layers. |
| `kernel_regularizer` | A `tf_keras.regularizers.Regularizer` object for Conv2D. Default to None. |
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