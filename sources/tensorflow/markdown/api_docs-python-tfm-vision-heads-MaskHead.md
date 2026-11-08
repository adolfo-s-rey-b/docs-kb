[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/vision/heads/MaskHead#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/vision/heads/MaskHead)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/vision/heads/MaskHead?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/heads/MaskHead#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/vision/heads/MaskHead#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/vision/heads/MaskHead#call)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.vision.heads.MaskHead Stay organized with collections Save and categorize content based on your preferences.
================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/heads/MaskHead#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/vision/heads/MaskHead#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/vision/heads/MaskHead#call)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/modeling/heads/instance_heads.py#L220-L432)

Creates a mask head.

tfm.vision.heads.MaskHead(
        num_classes: int,
        upsample_factor: int = 2,
        num_convs: int = 4,
        num_filters: int = 256,
        use_separable_conv: bool = False,
        activation: str = 'relu',
        use_sync_bn: bool = False,
        norm_momentum: float = 0.99,
        norm_epsilon: float = 0.001,
        kernel_regularizer: Optional[tf_keras.regularizers.Regularizer] = None,
        bias_regularizer: Optional[tf_keras.regularizers.Regularizer] = None,
        class_agnostic: bool = False,
        **kwargs
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `num_classes` | An `int` of the number of classes. |
| `upsample_factor` | An `int` that indicates the upsample factor to generate the final predicted masks. It should be >= 1. |
| `num_convs` | An `int` number that represents the number of the intermediate convolution layers before the mask prediction layers. |
| `num_filters` | An `int` number that represents the number of filters of the intermediate convolution layers. |
| `use_separable_conv` | A `bool` that indicates whether the separable convolution layers is used. |
| `activation` | A `str` that indicates which activation is used, e.g. 'relu', 'swish', etc. |
| `use_sync_bn` | A `bool` that indicates whether to use synchronized batch normalization across different replicas. |
| `norm_momentum` | A `float` of normalization momentum for the moving average. |
| `norm_epsilon` | A `float` added to variance to avoid dividing by zero. |
| `kernel_regularizer` | A `tf_keras.regularizers.Regularizer` object for Conv2D. Default is None. |
| `bias_regularizer` | A `tf_keras.regularizers.Regularizer` object for Conv2D. |
| `class_agnostic` | A `bool`. If set, we use a single channel mask head that is shared between all classes. |
| `**kwargs` | Additional keyword arguments to be passed. |

Methods
-------

### `call`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/modeling/heads/instance_heads.py#L382-L425)

call(
        inputs: List[tf.Tensor], training: bool = None
    )

Forward pass of mask branch for the Mask-RCNN model.

|     |     |
| --- | --- |
| Args |     |
| `inputs` | A `list` of two tensors where inputs\[0\]: A [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> of shape \[batch\_size, num\_instances, roi\_height, roi\_width, roi\_channels\], representing the ROI features. inputs\[1\]: A [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> of shape \[batch\_size, num\_instances\], representing the classes of the ROIs. |
| `training` | A `bool` indicating whether it is in `training` mode. |

|     |     |
| --- | --- |
| Returns |     |
| `mask_outputs` | A [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> of shape \[batch\_size, num\_instances, roi\_height \* upsample\_factor, roi\_width \* upsample\_factor\], representing the mask predictions. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.