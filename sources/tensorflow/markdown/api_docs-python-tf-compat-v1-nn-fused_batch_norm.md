[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/fused_batch_norm#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/fused_batch_norm)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/fused_batch_norm?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/fused_batch_norm#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/fused_batch_norm#returns)
    
*   [References](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/fused_batch_norm#references)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.nn.fused\_batch\_norm Stay organized with collections Save and categorize content based on your preferences.
=========================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/fused_batch_norm#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/fused_batch_norm#returns)
    
*   [References](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/fused_batch_norm#references)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/nn_impl.py#L1500-L1600)

Batch normalization.

tf.compat.v1.nn.fused_batch_norm(
        x,
        scale,
        offset,
        mean=None,
        variance=None,
        epsilon=0.001,
        data_format='NHWC',
        is_training=True,
        name=None,
        exponential_avg_factor=1.0
    )

See Source: [Batch Normalization: Accelerating Deep Network Training by Reducing Internal Covariate Shift; S. Ioffe, C. Szegedy](http://arxiv.org/abs/1502.03167)
.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `x` | Input `Tensor` of 4 or 5 dimensions. |
| `scale` | A `Tensor` of 1 dimension for scaling. |
| `offset` | A `Tensor` of 1 dimension for bias. |
| `mean` | A `Tensor` of 1 dimension for population mean. The shape and meaning of this argument depends on the value of is\_training and exponential\_avg\_factor as follows: is\_trainingFalse (inference): Mean must be a `Tensor` of the same shape as scale containing the estimated population mean computed during training. is\_trainingTrue and exponential\_avg\_factor == 1.0: Mean must be None. is\_trainingTrue and exponential\_avg\_factor != 1.0: Mean must be a `Tensor` of the same shape as scale containing the exponential running mean. |
| `variance` | A `Tensor` of 1 dimension for population variance. The shape and meaning of this argument depends on the value of is\_training and exponential\_avg\_factor as follows: is\_trainingFalse (inference): Variance must be a `Tensor` of the same shape as scale containing the estimated population variance computed during training. is\_training==True and exponential\_avg\_factor == 1.0: Variance must be None. is\_training==True and exponential\_avg\_factor != 1.0: Variance must be a `Tensor` of the same shape as scale containing the exponential running variance. |
| `epsilon` | A small float number added to the variance of x. |
| `data_format` | The data format for x. Support "NHWC" (default) or "NCHW" for 4D tenors and "NDHWC" or "NCDHW" for 5D tensors. |
| `is_training` | A bool value to specify if the operation is used for training or inference. |
| `name` | A name for this operation (optional). |
| `exponential_avg_factor` | A float number (usually between 0 and 1) used for controlling the decay of the running population average of mean and variance. If set to 1.0, the current batch average is returned. |

|     |     |
| --- | --- |
| Returns<br>------- |     |
| `y` | A 4D or 5D Tensor for the normalized, scaled, offsetted x. |
| `running_mean` | A 1D Tensor for the exponential running mean of x. The output value is (1 - exponential\_avg\_factor) \* mean + exponential\_avg\_factor \* batch\_mean), where batch\_mean is the mean of the current batch in x. |
| `running_var` | A 1D Tensor for the exponential running variance The output value is (1 - exponential\_avg\_factor) \* variance + exponential\_avg\_factor \* batch\_variance), where batch\_variance is the variance of the current batch in x. |

|     |
| --- |
| References<br>---------- |     |
| Batch Normalization - Accelerating Deep Network Training by Reducing Internal Covariate Shift: [Ioffe et al., 2015](http://proceedings.mlr.press/v37/ioffe15.html)<br> ([pdf](http://proceedings.mlr.press/v37/ioffe15.pdf)<br>) |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.