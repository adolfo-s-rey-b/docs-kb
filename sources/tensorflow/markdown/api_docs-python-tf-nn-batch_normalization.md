Loading \[MathJax\]/jax/output/SVG/jax.js

[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/nn/batch_normalization#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/nn/batch_normalization)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/nn/batch_normalization?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fnn%2Fbatch_normalization&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/nn/batch_normalization#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/nn/batch_normalization#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/nn/batch_normalization#returns)
    
*   [References](https://www.tensorflow.org/api_docs/python/tf/nn/batch_normalization#references)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.nn.batch\_normalization Stay organized with collections Save and categorize content based on your preferences.
=================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/nn/batch_normalization#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/nn/batch_normalization#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/nn/batch_normalization#returns)
    
*   [References](https://www.tensorflow.org/api_docs/python/tf/nn/batch_normalization#references)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/nn_impl.py#L1429-L1497)

Batch normalization.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.nn.batch_normalization`](https://www.tensorflow.org/api_docs/python/tf/nn/batch_normalization)

tf.nn.batch_normalization(
        x, mean, variance, offset, scale, variance_epsilon, name=None
    )

### Used in the notebooks

| Used in the tutorials |
| --- |
| *   [Distributed training with DTensors](https://www.tensorflow.org/tutorials/distribute/dtensor_ml_tutorial) |

Normalizes a tensor by `mean` and `variance`, and applies (optionally) a `scale` γ to it, as well as an `offset` β:

γ(x−μ)σ+β

`mean`, `variance`, `offset` and `scale` are all expected to be of one of two shapes:

*   In all generality, they can have the same number of dimensions as the input `x`, with identical sizes as `x` for the dimensions that are not normalized over (the 'depth' dimension(s)), and dimension 1 for the others which are being normalized over. `mean` and `variance` in this case would typically be the outputs of [`tf.nn.moments(..., keepdims=True)`](https://www.tensorflow.org/api_docs/python/tf/nn/moments)
     during training, or running averages thereof during inference.
*   In the common case where the 'depth' dimension is the last dimension in the input tensor `x`, they may be one dimensional tensors of the same size as the 'depth' dimension. This is the case for example for the common `[batch, depth]` layout of fully-connected layers, and `[batch, height, width, depth]` for convolutions. `mean` and `variance` in this case would typically be the outputs of [`tf.nn.moments(..., keepdims=False)`](https://www.tensorflow.org/api_docs/python/tf/nn/moments)
     during training, or running averages thereof during inference.

See equation 11 in Algorithm 2 of source: [Batch Normalization: Accelerating Deep Network Training by Reducing Internal Covariate Shift; S. Ioffe, C. Szegedy](http://arxiv.org/abs/1502.03167)
.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `x` | Input `Tensor` of arbitrary dimensionality. |
| `mean` | A mean `Tensor`. |
| `variance` | A variance `Tensor`. |
| `offset` | An offset `Tensor`, often denoted β in equations, or None. If present, will be added to the normalized tensor. |
| `scale` | A scale `Tensor`, often denoted γ in equations, or `None`. If present, the scale is applied to the normalized tensor. |
| `variance_epsilon` | A small float number to avoid dividing by 0. |
| `name` | A name for this operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| the normalized, scaled, offset tensor. |     |

|     |
| --- |
| References<br>---------- |     |
| Batch Normalization - Accelerating Deep Network Training by Reducing Internal Covariate Shift: [Ioffe et al., 2015](http://arxiv.org/abs/1502.03167)<br> ([pdf](http://proceedings.mlr.press/v37/ioffe15.pdf)<br>) |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.