[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/nn/batch_norm_with_global_normalization#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/nn/batch_norm_with_global_normalization)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/nn/batch_norm_with_global_normalization?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/nn/batch_norm_with_global_normalization#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/nn/batch_norm_with_global_normalization#returns)
    
*   [References](https://www.tensorflow.org/api_docs/python/tf/nn/batch_norm_with_global_normalization#references)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.nn.batch\_norm\_with\_global\_normalization Stay organized with collections Save and categorize content based on your preferences.
=====================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/nn/batch_norm_with_global_normalization#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/nn/batch_norm_with_global_normalization#returns)
    
*   [References](https://www.tensorflow.org/api_docs/python/tf/nn/batch_norm_with_global_normalization#references)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/nn_impl.py#L1658-L1705)

Batch normalization.

tf.nn.batch_norm_with_global_normalization(
        input,
        mean,
        variance,
        beta,
        gamma,
        variance_epsilon,
        scale_after_normalization,
        name=None
    )

This op is deprecated. See [`tf.nn.batch_normalization`](https://www.tensorflow.org/api_docs/python/tf/nn/batch_normalization)
.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `input` | A 4D input Tensor. |
| `mean` | A 1D mean Tensor with size matching the last dimension of t. This is the first output from tf.nn.moments, or a saved moving average thereof. |
| `variance` | A 1D variance Tensor with size matching the last dimension of t. This is the second output from tf.nn.moments, or a saved moving average thereof. |
| `beta` | A 1D beta Tensor with size matching the last dimension of t. An offset to be added to the normalized tensor. |
| `gamma` | A 1D gamma Tensor with size matching the last dimension of t. If "scale\_after\_normalization" is true, this tensor will be multiplied with the normalized tensor. |
| `variance_epsilon` | A small float number to avoid dividing by 0. |
| `scale_after_normalization` | A bool indicating whether the resulted tensor needs to be multiplied with gamma. |
| `name` | A name for this operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| A batch-normalized `t`. |     |

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