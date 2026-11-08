[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/linalg/solve?version=stable#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/linalg/solve)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/linalg/solve?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/linalg/solve?version=stable#used-in-the-notebooks_1)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/linalg/solve?version=stable#args_1)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/linalg/solve?version=stable#returns_1)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.linalg.solve Stay organized with collections Save and categorize content based on your preferences.
======================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/linalg/solve?version=stable#used-in-the-notebooks_1)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/linalg/solve?version=stable#args_1)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/linalg/solve?version=stable#returns_1)
    

See Stable See Nightly

Solves systems of linear equations.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.linalg.solve`](https://www.tensorflow.org/api_docs/python/tf/linalg/solve)
, [`tf.compat.v1.matrix_solve`](https://www.tensorflow.org/api_docs/python/tf/linalg/solve)

tf.linalg.solve(
        matrix: Annotated[Any, TV_MatrixSolve_T],
        rhs: Annotated[Any, TV_MatrixSolve_T],
        adjoint: bool = False,
        name=None
    ) -> Annotated[Any, TV_MatrixSolve_T]

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Advanced automatic differentiation](https://www.tensorflow.org/guide/advanced_autodiff) | *   [A Tour of TensorFlow Probability](https://www.tensorflow.org/probability/examples/A_Tour_of_TensorFlow_Probability) |

`Matrix` is a tensor of shape `[..., M, M]` whose inner-most 2 dimensions form square matrices. `Rhs` is a tensor of shape `[..., M, K]`. The `output` is a tensor shape `[..., M, K]`. If `adjoint` is `False` then each output matrix satisfies `matrix[..., :, :] * output[..., :, :] = rhs[..., :, :]`. If `adjoint` is `True` then each output matrix satisfies `adjoint(matrix[..., :, :]) * output[..., :, :] = rhs[..., :, :]`.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `matrix` | A `Tensor`. Must be one of the following types: `float64`, `float32`, `half`, `complex64`, `complex128`. Shape is `[..., M, M]`. |
| `rhs` | A `Tensor`. Must have the same type as `matrix`. Shape is `[..., M, K]`. |
| `adjoint` | An optional `bool`. Defaults to `False`. Boolean indicating whether to solve with `matrix` or its (block-wise) adjoint. |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| A `Tensor`. Has the same type as `matrix`. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.