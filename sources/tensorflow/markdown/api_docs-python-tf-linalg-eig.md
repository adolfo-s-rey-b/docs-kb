[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/linalg/eig#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/linalg/eig)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/linalg/eig?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/linalg/eig#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/linalg/eig#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/linalg/eig#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.linalg.eig Stay organized with collections Save and categorize content based on your preferences.
====================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/linalg/eig#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/linalg/eig#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/linalg/eig#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/linalg_ops.py#L382-L411)

Computes the eigen decomposition of a batch of matrices.

#### View aliases

**Main aliases**

[`tf.eig`](https://www.tensorflow.org/api_docs/python/tf/linalg/eig)

tf.linalg.eig(
        tensor, name=None
    )

### Used in the notebooks

| Used in the tutorials |
| --- |
| *   [Quantum data](https://www.tensorflow.org/quantum/tutorials/quantum_data) |

The eigenvalues and eigenvectors for a non-Hermitian matrix in general are complex. The eigenvectors are not guaranteed to be linearly independent.

Computes the eigenvalues and right eigenvectors of the innermost N-by-N matrices in `tensor` such that `tensor[...,:,:] * v[..., :,i] = e[..., i] * v[...,:,i]`, for i=0...N-1.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `tensor` | `Tensor` of shape `[..., N, N]`. Only the lower triangular part of each inner inner matrix is referenced. |
| `name` | string, optional name of the operation. |

|     |     |
| --- | --- |
| Returns<br>------- |     |
| `e` | Eigenvalues. Shape is `[..., N]`. The eigenvalues are not necessarily ordered. |
| `v` | Eigenvectors. Shape is `[..., N, N]`. The columns of the inner most matrices contain eigenvectors of the corresponding matrices in `tensor` |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.