[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/linalg/cholesky#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/linalg/cholesky)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/linalg/cholesky?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/linalg/cholesky#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/linalg/cholesky#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/linalg/cholesky#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.linalg.cholesky Stay organized with collections Save and categorize content based on your preferences.
=========================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/linalg/cholesky#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/linalg/cholesky#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/linalg/cholesky#returns)
    

Computes the Cholesky decomposition of one or more square matrices.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.cholesky`](https://www.tensorflow.org/api_docs/python/tf/linalg/cholesky)
, [`tf.compat.v1.linalg.cholesky`](https://www.tensorflow.org/api_docs/python/tf/linalg/cholesky)

tf.linalg.cholesky(
        input: Annotated[Any, TV_Cholesky_T], name=None
    ) -> Annotated[Any, TV_Cholesky_T]

### Used in the notebooks

| Used in the tutorials |
| --- |
| *   [TensorFlow Probability Case Study: Covariance Estimation](https://www.tensorflow.org/probability/examples/TensorFlow_Probability_Case_Study_Covariance_Estimation)<br>    <br>*   [TFP Release Notes notebook (0.13.0)](https://www.tensorflow.org/probability/examples/TFP_Release_Notebook_0_13_0)<br>    <br>*   [TensorFlow Distributions: A Gentle Introduction](https://www.tensorflow.org/probability/examples/TensorFlow_Distributions_Tutorial)<br>    <br>*   [Bayesian Gaussian Mixture Model and Hamiltonian MCMC](https://www.tensorflow.org/probability/examples/Bayesian_Gaussian_Mixture_Model)<br>    <br>*   [TFP Release Notes notebook (0.12.1)](https://www.tensorflow.org/probability/examples/TFP_Release_Notebook_0_12_1) |

The input is a tensor of shape `[..., M, M]` whose inner-most 2 dimensions form square matrices.

The input has to be symmetric and positive definite. Only the lower-triangular part of the input will be used for this operation. The upper-triangular part will not be read.

The output is a tensor of the same shape as the input containing the Cholesky decompositions for all input submatrices `[..., :, :]`.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `input` | A `Tensor`. Must be one of the following types: `float64`, `float32`, `half`, `complex64`, `complex128`. Shape is `[..., M, M]`. |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| A `Tensor`. Has the same type as `input`. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2024-04-26 UTC.