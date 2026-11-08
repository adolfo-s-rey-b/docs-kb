[Skip to main content](https://www.tensorflow.org/api_docs/python/tfc/ops/soft_round_conditional_mean#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfc/ops/soft_round_conditional_mean)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfc/ops/soft_round_conditional_mean?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfc/ops/soft_round_conditional_mean#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfc/ops/soft_round_conditional_mean#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfc.ops.soft\_round\_conditional\_mean Stay organized with collections Save and categorize content based on your preferences.
=============================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfc/ops/soft_round_conditional_mean#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfc/ops/soft_round_conditional_mean#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/compression/blob/v2.14.1/tensorflow_compression/python/ops/round_ops.py#L111-L130)

Conditional mean of inputs given noisy soft rounded values.

#### View aliases

**Main aliases**

[`tfc.soft_round_conditional_mean`](https://www.tensorflow.org/api_docs/python/tfc/ops/soft_round_conditional_mean)

tfc.ops.soft_round_conditional_mean(
        y, alpha
    )

Computes g(z) = E\[Y | s(Y) + U = z\] where s is the soft-rounding function, U is uniform between -0.5 and 0.5 and Y is considered uniform when truncated to the interval \[z-0.5, z+0.5\].

This is described in Sec. 4.1. in the paper

> "Universally Quantized Neural Compression"  
> Eirikur Agustsson & Lucas Theis  
> [https://arxiv.org/abs/2006.09952](https://arxiv.org/abs/2006.09952)

|     |     |
| --- | --- |
| Args<br>---- |     |
| `y` | [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br>. Inputs to this function. |
| `alpha` | Float or [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br>. Controls smoothness of the approximation. |

|     |
| --- |
| Returns<br>------- |     |
| The conditional mean, of same shape as `inputs`. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2024-04-26 UTC.