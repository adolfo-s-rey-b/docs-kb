[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/vision/decoders/NASFPN#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/vision/decoders/NASFPN)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/vision/decoders/NASFPN?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftfm%2Fvision%2Fdecoders%2FNASFPN&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/decoders/NASFPN#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tfm/vision/decoders/NASFPN#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/vision/decoders/NASFPN#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/vision/decoders/NASFPN#call)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.vision.decoders.NASFPN Stay organized with collections Save and categorize content based on your preferences.
=================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/decoders/NASFPN#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tfm/vision/decoders/NASFPN#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/vision/decoders/NASFPN#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/vision/decoders/NASFPN#call)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/modeling/decoders/nasfpn.py#L62-L328)

Creates a NAS-FPN model.

tfm.vision.decoders.NASFPN(
        input_specs: Mapping[str, tf.TensorShape],
        min_level: int = 3,
        max_level: int = 7,
        block_specs: Optional[List[BlockSpec]] = None,
        num_filters: int = 256,
        num_repeats: int = 5,
        use_separable_conv: bool = False,
        activation: str = 'relu',
        use_sync_bn: bool = False,
        norm_momentum: float = 0.99,
        norm_epsilon: float = 0.001,
        kernel_initializer: str = 'VarianceScaling',
        kernel_regularizer: Optional[tf_keras.regularizers.Regularizer] = None,
        bias_regularizer: Optional[tf_keras.regularizers.Regularizer] = None,
        **kwargs
    )

This implements the paper: Golnaz Ghiasi, Tsung-Yi Lin, Ruoming Pang, Quoc V. Le. NAS-FPN: Learning Scalable Feature Pyramid Architecture for Object Detection. ([https://arxiv.org/abs/1904.07392](https://arxiv.org/abs/1904.07392)
)

|     |     |
| --- | --- |
| Args<br>---- |     |
| `input_specs` | A `dict` of input specifications. A dictionary consists of {level: TensorShape} from a backbone. |
| `min_level` | An `int` of minimum level in FPN output feature maps. |
| `max_level` | An `int` of maximum level in FPN output feature maps. |
| `block_specs` | a list of BlockSpec objects that specifies the NAS-FPN network topology. By default, the previously discovered architecture is used. |
| `num_filters` | An `int` number of filters in FPN layers. |
| `num_repeats` | number of repeats for feature pyramid network. |
| `use_separable_conv` | A `bool`. If True use separable convolution for convolution in FPN layers. |
| `activation` | A `str` name of the activation function. |
| `use_sync_bn` | A `bool`. If True, use synchronized batch normalization. |
| `norm_momentum` | A `float` of normalization momentum for the moving average. |
| `norm_epsilon` | A `float` added to variance to avoid dividing by zero. |
| `kernel_initializer` | A `str` name of kernel\_initializer for convolutional layers. |
| `kernel_regularizer` | A `tf_keras.regularizers.Regularizer` object for Conv2D. Default is None. |
| `bias_regularizer` | A `tf_keras.regularizers.Regularizer` object for Conv2D. |
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