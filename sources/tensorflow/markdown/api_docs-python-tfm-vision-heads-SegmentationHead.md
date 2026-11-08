[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/vision/heads/SegmentationHead#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/vision/heads/SegmentationHead)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/vision/heads/SegmentationHead?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/heads/SegmentationHead#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/vision/heads/SegmentationHead#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/vision/heads/SegmentationHead#call)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.vision.heads.SegmentationHead Stay organized with collections Save and categorize content based on your preferences.
========================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/heads/SegmentationHead#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/vision/heads/SegmentationHead#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/vision/heads/SegmentationHead#call)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/modeling/heads/segmentation_heads.py#L214-L472)

Creates a segmentation head.

tfm.vision.heads.SegmentationHead(
        num_classes: int,
        level: Union[int, str],
        num_convs: int = 2,
        num_filters: int = 256,
        use_depthwise_convolution: bool = False,
        prediction_kernel_size: int = 1,
        upsample_factor: int = 1,
        feature_fusion: Optional[str] = None,
        decoder_min_level: Optional[int] = None,
        decoder_max_level: Optional[int] = None,
        low_level: int = 2,
        low_level_num_filters: int = 48,
        num_decoder_filters: int = 256,
        activation: str = 'relu',
        logit_activation: Optional[str] = None,
        use_sync_bn: bool = False,
        norm_momentum: float = 0.99,
        norm_epsilon: float = 0.001,
        kernel_regularizer: Optional[tf_keras.regularizers.Regularizer] = None,
        bias_regularizer: Optional[tf_keras.regularizers.Regularizer] = None,
        **kwargs
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `num_classes` | An `int` number of mask classification categories. The number of classes does not include background class. |
| `level` | An `int` or `str`, level to use to build segmentation head. |
| `num_convs` | An `int` number of stacked convolution before the last prediction layer. |
| `num_filters` | An `int` number to specify the number of filters used. Default is 256. |
| `use_depthwise_convolution` | A bool to specify if use depthwise separable convolutions. |
| `prediction_kernel_size` | An `int` number to specify the kernel size of the prediction layer. |
| `upsample_factor` | An `int` number to specify the upsampling factor to generate finer mask. Default 1 means no upsampling is applied. |
| `feature_fusion` | One of the constants in nn\_layers.FeatureFusion, namely `deeplabv3plus`, `pyramid_fusion`, `panoptic_fpn_fusion`, `deeplabv3plus_sum_to_merge`, or None. If `deeplabv3plus`, features from decoder\_features\[level\] will be fused with low level feature maps from backbone. If `pyramid_fusion`, multiscale features will be resized and fused at the target level. |
| `decoder_min_level` | An `int` of minimum level from decoder to use in feature fusion. It is only used when feature\_fusion is set to `panoptic_fpn_fusion`. |
| `decoder_max_level` | An `int` of maximum level from decoder to use in feature fusion. It is only used when feature\_fusion is set to `panoptic_fpn_fusion`. |
| `low_level` | An `int` of backbone level to be used for feature fusion. It is used when feature\_fusion is set to `deeplabv3plus` or `deeplabv3plus_sum_to_merge`. |
| `low_level_num_filters` | An `int` of reduced number of filters for the low level features before fusing it with higher level features. It is only used when feature\_fusion is set to `deeplabv3plus` or `deeplabv3plus_sum_to_merge`. |
| `num_decoder_filters` | An `int` of number of filters in the decoder outputs. It is only used when feature\_fusion is set to `panoptic_fpn_fusion`. |
| `activation` | A `str` that indicates which activation is used, e.g. 'relu', 'swish', etc. |
| `logit_activation` | Activation applied to the final classifier layer logits, e.g. 'sigmoid', 'softmax'. Can be useful in cases when the task does not use only cross entropy loss. |
| `use_sync_bn` | A `bool` that indicates whether to use synchronized batch normalization across different replicas. |
| `norm_momentum` | A `float` of normalization momentum for the moving average. |
| `norm_epsilon` | A `float` added to variance to avoid dividing by zero. |
| `kernel_regularizer` | A `tf_keras.regularizers.Regularizer` object for Conv2D. Default is None. |
| `bias_regularizer` | A `tf_keras.regularizers.Regularizer` object for Conv2D. |
| `**kwargs` | Additional keyword arguments to be passed. |

Methods
-------

### `call`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/modeling/heads/segmentation_heads.py#L404-L464)

call(
        inputs: Tuple[Union[tf.Tensor, Mapping[str, tf.Tensor]], Union[tf.Tensor, Mapping[\
            str, tf.Tensor]]]
    )

Forward pass of the segmentation head.

It supports both a tuple of 2 tensors or 2 dictionaries. The first is backbone endpoints, and the second is decoder endpoints. When inputs are tensors, they are from a single level of feature maps. When inputs are dictionaries, they contain multiple levels of feature maps, where the key is the index of feature map.

|     |     |
| --- | --- |
| Args |     |
| `inputs` | A tuple of 2 feature map tensors of shape \[batch, height\_l, width\_l, channels\] or 2 dictionaries of tensors:<br><br>*   key: A `str` of the level of the multilevel features.<br>*   values: A [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br>     of the feature map tensors, whose shape is \[batch, height\_l, width\_l, channels\]. The first is backbone endpoints, and the second is decoder endpoints. |

|     |
| --- |
| Returns |     |
| segmentation prediction mask: A [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> of the segmentation mask scores predicted from input features. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.