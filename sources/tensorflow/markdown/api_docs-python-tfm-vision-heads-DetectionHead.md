[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/vision/heads/DetectionHead#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/vision/heads/DetectionHead)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/vision/heads/DetectionHead?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/oauth2authorize?return_url=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftfm%2Fvision%2Fheads%2FDetectionHead&scopes=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles.award+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdevprofiles.full_control.firstparty)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/heads/DetectionHead#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/vision/heads/DetectionHead#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/vision/heads/DetectionHead#call)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.vision.heads.DetectionHead Stay organized with collections Save and categorize content based on your preferences.
=====================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/heads/DetectionHead#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/vision/heads/DetectionHead#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/vision/heads/DetectionHead#call)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/modeling/heads/instance_heads.py#L23-L217)

Creates a detection head.

tfm.vision.heads.DetectionHead(
        num_classes: int,
        num_convs: int = 0,
        num_filters: int = 256,
        use_separable_conv: bool = False,
        num_fcs: int = 2,
        fc_dims: int = 1024,
        class_agnostic_bbox_pred: bool = False,
        activation: str = 'relu',
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
| `num_classes` | An `int` for the number of classes. |
| `num_convs` | An `int` number that represents the number of the intermediate convolution layers before the FC layers. |
| `num_filters` | An `int` number that represents the number of filters of the intermediate convolution layers. |
| `use_separable_conv` | A `bool` that indicates whether the separable convolution layers is used. |
| `num_fcs` | An `int` number that represents the number of FC layers before the predictions. |
| `fc_dims` | An `int` number that represents the number of dimension of the FC layers. |
| `class_agnostic_bbox_pred` | `bool`, indicating whether bboxes should be predicted for every class or not. |
| `activation` | A `str` that indicates which activation is used, e.g. 'relu', 'swish', etc. |
| `use_sync_bn` | A `bool` that indicates whether to use synchronized batch normalization across different replicas. |
| `norm_momentum` | A `float` of normalization momentum for the moving average. |
| `norm_epsilon` | A `float` added to variance to avoid dividing by zero. |
| `kernel_regularizer` | A `tf_keras.regularizers.Regularizer` object for Conv2D. Default is None. |
| `bias_regularizer` | A `tf_keras.regularizers.Regularizer` object for Conv2D. |
| `**kwargs` | Additional keyword arguments to be passed. |

Methods
-------

### `call`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/modeling/heads/instance_heads.py#L176-L210)

call(
        inputs: tf.Tensor, training: bool = None
    )

Forward pass of box and class branches for the Mask-RCNN model.

|     |     |
| --- | --- |
| Args |     |
| `inputs` | A [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> of the shape \[batch\_size, num\_instances, roi\_height, roi\_width, roi\_channels\], representing the ROI features. |
| `training` | a `bool` indicating whether it is in `training` mode. |

|     |     |
| --- | --- |
| Returns |     |
| `class_outputs` | A [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> of the shape \[batch\_size, num\_rois, num\_classes\], representing the class predictions. |
| `box_outputs` | A [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> of the shape \[batch\_size, num\_rois, num\_classes \* 4\], representing the box predictions. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.