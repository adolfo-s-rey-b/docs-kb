[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/vision/heads/MaskScoring#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/vision/heads/MaskScoring)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/vision/heads/MaskScoring?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftfm%2Fvision%2Fheads%2FMaskScoring&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/heads/MaskScoring#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/vision/heads/MaskScoring#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/vision/heads/MaskScoring#call)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.vision.heads.MaskScoring Stay organized with collections Save and categorize content based on your preferences.
===================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/heads/MaskScoring#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/vision/heads/MaskScoring#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/vision/heads/MaskScoring#call)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/modeling/heads/segmentation_heads.py#L24-L211)

Creates a mask scoring layer.

tfm.vision.heads.MaskScoring(
        num_classes: int,
        fc_input_size: List[int],
        num_convs: int = 3,
        num_filters: int = 256,
        use_depthwise_convolution: bool = False,
        fc_dims: int = 1024,
        num_fcs: int = 2,
        activation: str = 'relu',
        use_sync_bn: bool = False,
        norm_momentum: float = 0.99,
        norm_epsilon: float = 0.001,
        kernel_regularizer: Optional[tf_keras.regularizers.Regularizer] = None,
        bias_regularizer: Optional[tf_keras.regularizers.Regularizer] = None,
        **kwargs
    )

This implements mask scoring layer from the paper:

Zhaojin Huang, Lichao Huang, Yongchao Gong, Chang Huang, Xinggang Wang. Mask Scoring R-CNN. ([https://arxiv.org/pdf/1903.00241.pdf](https://arxiv.org/pdf/1903.00241.pdf)
)

|     |     |
| --- | --- |
| Args<br>---- |     |
| `num_classes` | An `int` for number of classes. |
| `fc_input_size` | A List of `int` for the input size of the fully connected layers. |
| `num_convs` | An`int` for number of conv layers. |
| `num_filters` | An `int` for the number of filters for conv layers. |
| `use_depthwise_convolution` | A `bool`, whether or not using depthwise convs. |
| `fc_dims` | An `int` number of filters for each fully connected layers. |
| `num_fcs` | An `int` for number of fully connected layers. |
| `activation` | A `str` name of the activation function. |
| `use_sync_bn` | A bool, whether or not to use sync batch normalization. |
| `norm_momentum` | A float for the momentum in BatchNorm. Defaults to 0.99. |
| `norm_epsilon` | A float for the epsilon value in BatchNorm. Defaults to 0.001. |
| `kernel_regularizer` | A `tf_keras.regularizers.Regularizer` object for Conv2D. Default is None. |
| `bias_regularizer` | A `tf_keras.regularizers.Regularizer` object for Conv2D. |
| `**kwargs` | Additional keyword arguments to be passed. |

Methods
-------

### `call`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/modeling/heads/segmentation_heads.py#L170-L204)

call(
        inputs: tf.Tensor, training: bool = None
    )

Forward pass mask scoring head.

|     |     |
| --- | --- |
| Args |     |
| `inputs` | A [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> of the shape \[batch\_size, width, size, num\_classes\], representing the segmentation logits. |
| `training` | a `bool` indicating whether it is in `training` mode. |

|     |     |
| --- | --- |
| Returns |     |
| `mask_scores` | A [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> of predicted mask scores \[batch\_size, num\_classes\]. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.