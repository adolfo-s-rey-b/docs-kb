[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/vision/heads/RPNHead#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/vision/heads/RPNHead)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/vision/heads/RPNHead?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftfm%2Fvision%2Fheads%2FRPNHead&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/heads/RPNHead#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/vision/heads/RPNHead#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/vision/heads/RPNHead#call)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.vision.heads.RPNHead Stay organized with collections Save and categorize content based on your preferences.
===============================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/heads/RPNHead#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/vision/heads/RPNHead#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/vision/heads/RPNHead#call)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/modeling/heads/dense_prediction_heads.py#L537-L718)

Creates a Region Proposal Network (RPN) head.

tfm.vision.heads.RPNHead(
        min_level: int,
        max_level: int,
        num_anchors_per_location: int,
        num_convs: int = 1,
        num_filters: int = 256,
        use_separable_conv: bool = False,
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
| `min_level` | An `int` number of minimum feature level. |
| `max_level` | An `int` number of maximum feature level. |
| `num_anchors_per_location` | An `int` number of number of anchors per pixel location. |
| `num_convs` | An `int` number that represents the number of the intermediate convolution layers before the prediction. |
| `num_filters` | An `int` number that represents the number of filters of the intermediate convolution layers. |
| `use_separable_conv` | A `bool` that indicates whether the separable convolution layers is used. |
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

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/modeling/heads/dense_prediction_heads.py#L677-L711)

call(
        features: Mapping[str, tf.Tensor]
    )

Forward pass of the RPN head.

|     |     |
| --- | --- |
| Args |     |
| `features` | A `dict` of [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> where<br><br>*   key: A `str` of the level of the multilevel features.<br>*   values: A [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br>    , the feature map tensors, whose shape is \[batch, height\_l, width\_l, channels\]. |

|     |     |
| --- | --- |
| Returns |     |
| `scores` | A `dict` of [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> which includes scores of the predictions.<br><br>*   key: A `str` of the level of the multilevel predictions.<br>*   values: A [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br>     of the box scores predicted from a particular feature level, whose shape is \[batch, height\_l, width\_l, num\_classes \* num\_anchors\_per\_location\]. |
| `boxes` | A `dict` of [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> which includes coordinates of the predictions.*   key: A `str` of the level of the multilevel predictions.<br>*   values: A [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br>     of the box scores predicted from a particular feature level, whose shape is \[batch, height\_l, width\_l, 4 \* num\_anchors\_per\_location\]. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.