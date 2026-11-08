[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/norm#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/norm)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/norm?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/norm#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/norm#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/norm#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/norm#raises)
    
*   [numpy compatibility](https://www.tensorflow.org/api_docs/python/tf/norm#numpy-compatibility)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.norm Stay organized with collections Save and categorize content based on your preferences.
==============================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/norm#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/norm#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/norm#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/norm#raises)
    
*   [numpy compatibility](https://www.tensorflow.org/api_docs/python/tf/norm#numpy-compatibility)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/linalg_ops.py#L561-L629)

Computes the norm of vectors, matrices, and tensors.

#### View aliases

**Main aliases**

[`tf.linalg.norm`](https://www.tensorflow.org/api_docs/python/tf/norm)

tf.norm(
        tensor, ord='euclidean', axis=None, keepdims=None, name=None
    )

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Advanced automatic differentiation](https://www.tensorflow.org/guide/advanced_autodiff)<br>    <br>*   [Matrix approximation with Core APIs](https://www.tensorflow.org/guide/core/matrix_core) | *   [Generate Artificial Faces with CelebA Progressive GAN Model](https://www.tensorflow.org/hub/tutorials/tf_hub_generative_image_module)<br>    <br>*   [Human Pose Classification with MoveNet and TensorFlow Lite](https://www.tensorflow.org/lite/tutorials/pose_classification)<br>    <br>*   [Generalized Linear Models](https://www.tensorflow.org/probability/examples/Generalized_Linear_Models)<br>    <br>*   [Neural machine translation with a Transformer and Keras](https://www.tensorflow.org/text/tutorials/transformer) |

This function can compute several different vector norms (the 1-norm, the Euclidean or 2-norm, the inf-norm, and in general the p-norm for p > 0) and matrix norms (Frobenius, 1-norm, 2-norm and inf-norm).

|     |     |
| --- | --- |
| Args<br>---- |     |
| `tensor` | `Tensor` of types `float32`, `float64`, `complex64`, `complex128` |
| `ord` | Order of the norm. Supported values are `'fro'`, `'euclidean'`, `1`, `2`, `np.inf` and any positive real number yielding the corresponding p-norm. Default is `'euclidean'` which is equivalent to Frobenius norm if `tensor` is a matrix and equivalent to 2-norm for vectors. Some restrictions apply: a) The Frobenius norm `'fro'` is not defined for vectors, b) If axis is a 2-tuple (matrix norm), only `'euclidean'`, '`fro'`, `1`, `2`, `np.inf` are supported. See the description of `axis` on how to compute norms for a batch of vectors or matrices stored in a tensor. |
| `axis` | If `axis` is `None` (the default), the input is considered a vector and a single vector norm is computed over the entire set of values in the tensor, i.e. `norm(tensor, ord=ord)` is equivalent to `norm(reshape(tensor, [-1]), ord=ord)`. If `axis` is a Python integer, the input is considered a batch of vectors, and `axis` determines the axis in `tensor` over which to compute vector norms. If `axis` is a 2-tuple of Python integers it is considered a batch of matrices and `axis` determines the axes in `tensor` over which to compute a matrix norm. Negative indices are supported. Example: If you are passing a tensor that can be either a matrix or a batch of matrices at runtime, pass `axis=[-2,-1]` instead of `axis=None` to make sure that matrix norms are computed. |
| `keepdims` | If True, the axis indicated in `axis` are kept with size 1. Otherwise, the dimensions in `axis` are removed from the output shape. |
| `name` | The name of the op. |

|     |     |
| --- | --- |
| Returns<br>------- |     |
| `output` | A `Tensor` of the same type as tensor, containing the vector or matrix norms. If `keepdims` is True then the rank of output is equal to the rank of `tensor`. Otherwise, if `axis` is none the output is a scalar, if `axis` is an integer, the rank of `output` is one less than the rank of `tensor`, if `axis` is a 2-tuple the rank of `output` is two less than the rank of `tensor`. |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | If `ord` or `axis` is invalid. |

numpy compatibility
-------------------

Mostly equivalent to numpy.linalg.norm. Not supported: ord <= 0, 2-norm for matrices, nuclear norm. Other differences: a) If axis is `None`, treats the flattened `tensor` as a vector regardless of rank. b) Explicitly supports 'euclidean' norm as the default, including for higher order tensors.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.