[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/vision/decoders/ASPP#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/vision/decoders/ASPP)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/vision/decoders/ASPP?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/decoders/ASPP#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/vision/decoders/ASPP#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/vision/decoders/ASPP#call)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.vision.decoders.ASPP Stay organized with collections Save and categorize content based on your preferences.
===============================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/decoders/ASPP#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/vision/decoders/ASPP#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/vision/decoders/ASPP#call)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/modeling/decoders/aspp.py#L28-L155)

Creates an Atrous Spatial Pyramid Pooling (ASPP) layer.

tfm.vision.decoders.ASPP(
        level: int,
        dilation_rates: List[int],
        num_filters: int = 256,
        pool_kernel_size: Optional[int] = None,
        use_sync_bn: bool = False,
        norm_momentum: float = 0.99,
        norm_epsilon: float = 0.001,
        activation: str = 'relu',
        dropout_rate: float = 0.0,
        kernel_initializer: str = 'VarianceScaling',
        kernel_regularizer: Optional[tf_keras.regularizers.Regularizer] = None,
        interpolation: str = 'bilinear',
        use_depthwise_convolution: bool = False,
        spp_layer_version: str = 'v1',
        output_tensor: bool = False,
        **kwargs
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| level: An `int` level to apply ASPP. dilation\_rates: A `list` of dilation rates. num\_filters: An `int` number of output filters in ASPP. pool\_kernel\_size: A `list` of \[height, width\] of pooling kernel size or None. Pooling size is with respect to original image size, it will be scaled down by 2\*\*level. If None, global average pooling is used. use\_sync\_bn: A `bool`. If True, use synchronized batch normalization. norm\_momentum: A `float` of normalization momentum for the moving average. norm\_epsilon: A `float` added to variance to avoid dividing by zero. activation: A `str` activation to be used in ASPP. dropout\_rate: A `float` rate for dropout regularization. kernel\_initializer: A `str` name of kernel\_initializer for convolutional layers. kernel\_regularizer: A `tf_keras.regularizers.Regularizer` object for Conv2D. Default is None. interpolation: A `str` of interpolation method. It should be one of `bilinear`, `nearest`, `bicubic`, `area`, `lanczos3`, `lanczos5`, `gaussian`, or `mitchellcubic`. use\_depthwise\_convolution: If True depthwise separable convolutions will be added to the Atrous spatial pyramid pooling. |     |
| `spp_layer_version` | A `str` of spatial pyramid pooling layer version. |
| `output_tensor` | Whether to output a single tensor or a dictionary of tensor. Default is false. \*\*kwargs: Additional keyword arguments to be passed. |

Methods
-------

### `call`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/modeling/decoders/aspp.py#L122-L147)

call(
        inputs: TensorMapUnion
    ) -> TensorMapUnion

Calls the Atrous Spatial Pyramid Pooling (ASPP) layer on an input.

The output of ASPP will be a dict of {`level`, [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)
} even if only one level is present, if output\_tensor is false. Hence, this will be compatible with the rest of the segmentation model interfaces. If output\_tensor is true, a single tensot is output.

|     |     |
| --- | --- |
| Args |     |
| `inputs` | A [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> of shape \[batch, height\_l, width\_l, filter\_size\] or a `dict` of [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> where<br><br>*   key: A `str` of the level of the multilevel feature maps.<br>*   values: A [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br>     of shape \[batch, height\_l, width\_l, filter\_size\]. |

|     |
| --- |
| Returns |     |
| A [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> of shape \[batch, height\_l, width\_l, filter\_size\] or a `dict` of [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> where<br><br>*   key: A `str` of the level of the multilevel feature maps.<br>*   values: A [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br>     of output of ASPP module. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.