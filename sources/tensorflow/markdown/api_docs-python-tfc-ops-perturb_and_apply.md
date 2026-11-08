[Skip to main content](https://www.tensorflow.org/api_docs/python/tfc/ops/perturb_and_apply#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfc/ops/perturb_and_apply)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfc/ops/perturb_and_apply?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfc/ops/perturb_and_apply#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfc/ops/perturb_and_apply#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfc.ops.perturb\_and\_apply Stay organized with collections Save and categorize content based on your preferences.
==================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfc/ops/perturb_and_apply#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfc/ops/perturb_and_apply#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/compression/blob/v2.14.1/tensorflow_compression/python/ops/math_ops.py#L157-L216)

Perturbs the inputs of a pointwise function.

#### View aliases

**Main aliases**

[`tfc.perturb_and_apply`](https://www.tensorflow.org/api_docs/python/tfc/ops/perturb_and_apply)

tfc.ops.perturb_and_apply(
        f, x, *args, u=None, x_plus_u=None, expected_grads=True
    )

This function adds uniform noise in the range -0.5 to 0.5 to the first argument of the given function. It further replaces derivatives of the function with (analytically computed) expected derivatives w.r.t. the noise.

This is described in Sec. 4.2. in the paper

> "Universally Quantized Neural Compression"  
> Eirikur Agustsson & Lucas Theis  
> [https://arxiv.org/abs/2006.09952](https://arxiv.org/abs/2006.09952)

|     |     |
| --- | --- |
| Args<br>---- |     |
| `f` | Callable. Pointwise function applied after perturbation. |
| `x` | The inputs. |
| `*args` | Other arguments to f. |
| `u` | The noise to perturb x with. If not set and x\_plus\_u is not provided, it will be sampled. |
| `x_plus_u` | Alternative way to provide the noise, as `x+u`. |
| `expected_grads` | If True, will compute expected gradients. |

|     |
| --- |
| Returns<br>------- |     |
| A tuple (y, x+u) where y=f(x+u, \*args) and u is uniform noise, and the gradient of `y` w.r.t. `x` uses expected derivatives w.r.t. the distribution of u. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2024-04-26 UTC.