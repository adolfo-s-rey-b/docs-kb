Loading \[MathJax\]/jax/output/SVG/jax.js

[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/einsum#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/einsum)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/einsum?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Feinsum&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/einsum#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/einsum#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/einsum#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/einsum#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

Was this helpful?

tf.einsum Stay organized with collections Save and categorize content based on your preferences.
================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/einsum#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/einsum#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/einsum#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/einsum#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/special_math_ops.py#L618-L763)

Tensor contraction over specified indices and outer product.

#### View aliases

**Main aliases**

[`tf.linalg.einsum`](https://www.tensorflow.org/api_docs/python/tf/einsum)

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.einsum`](https://www.tensorflow.org/api_docs/python/tf/einsum)
, [`tf.compat.v1.linalg.einsum`](https://www.tensorflow.org/api_docs/python/tf/einsum)

tf.einsum(
        equation, *inputs, **kwargs
    )

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Matrix approximation with Core APIs](https://www.tensorflow.org/guide/core/matrix_core)<br>    <br>*   [Advanced automatic differentiation](https://www.tensorflow.org/guide/advanced_autodiff)<br>    <br>*   [Working with RNNs](https://www.tensorflow.org/guide/keras/working_with_rnns) | *   [Neural style transfer](https://www.tensorflow.org/tutorials/generative/style_transfer)<br>    <br>*   [Quantum data](https://www.tensorflow.org/quantum/tutorials/quantum_data)<br>    <br>*   [Modeling COVID-19 spread in Europe and the effect of interventions](https://www.tensorflow.org/probability/examples/Estimating_COVID_19_in_11_European_countries)<br>    <br>*   [Parametrized Quantum Circuits for Reinforcement Learning](https://www.tensorflow.org/quantum/tutorials/quantum_reinforcement_learning)<br>    <br>*   [Research tools](https://www.tensorflow.org/quantum/tutorials/research_tools) |

Einsum allows defining Tensors by defining their element-wise computation. This computation is defined by `equation`, a shorthand form based on Einstein summation. As an example, consider multiplying two matrices A and B to form a matrix C. The elements of C are given by:

Ci,k\=∑jAi,jBj,k

or

C[i,k] = sum_j A[i,j] * B[j,k]

The corresponding einsum `equation` is:

ij,jk->ik

In general, to convert the element-wise equation into the `equation` string, use the following procedure (intermediate strings for matrix multiplication example provided in parentheses):

1.  remove variable names, brackets, and commas, (`ik = sum_j ij * jk`)
2.  replace "\*" with ",", (`ik = sum_j ij , jk`)
3.  drop summation signs, and (`ik = ij, jk`)
4.  move the output to the right, while replacing "=" with "->". (`ij,jk->ik`)

Many common operations can be expressed in this way. For example:

**Matrix multiplication**

    m0 = tf.random.normal(shape=[2, 3])

Repeated indices are summed if the output indices are not specified.

    e = tf.einsum('ij,jk', m0, m1)  # output[i,k] = sum_j m0[i,j] * m1[j, k]

**Dot product**

    u = tf.random.normal(shape=[5])

**Outer product**

    u = tf.random.normal(shape=[3])

**Transpose**

    m = tf.ones(2,3)

**Diag**

    m = tf.reshape(tf.range(9), [3,3])

**Trace**

    # Repeated indices are summed.

**Batch matrix multiplication**

    s = tf.random.normal(shape=[7,5,3])

This method does not support broadcasting on named-axes. All axes with matching labels should have the same length. If you have length-1 axes, use [`tf.squeeze`](https://www.tensorflow.org/api_docs/python/tf/squeeze)
 or [`tf.reshape`](https://www.tensorflow.org/api_docs/python/tf/reshape)
 to eliminate them.

To write code that is agnostic to the number of indices in the input use an ellipsis. The ellipsis is a placeholder for "whatever other indices fit here".

For example, to perform a NumPy-style broadcasting-batch-matrix multiplication where the matrix multiply acts on the last two axes of the input, use:

    s = tf.random.normal(shape=[11, 7, 5, 3])

Einsum **will** broadcast over axes covered by the ellipsis.

    s = tf.random.normal(shape=[11, 1, 5, 3])

|     |     |
| --- | --- |
| Args<br>---- |     |
| `equation` | a `str` describing the contraction, in the same format as [`numpy.einsum`](https://www.tensorflow.org/api_docs/python/tf/keras/ops/einsum)<br>. |
| `*inputs` | the inputs to contract (each one a `Tensor`), whose shapes should be consistent with `equation`. |
| `**kwargs` | *   optimize: Optimization strategy to use to find contraction path using opt\_einsum. Must be 'greedy', 'optimal', 'branch-2', 'branch-all' or 'auto'. (optional, default: 'greedy').<br>*   name: A name for the operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| The contracted `Tensor`, with shape determined by `equation`. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | If<br><br>*   the format of `equation` is incorrect,<br>*   number of inputs or their shapes are inconsistent with `equation`. |

Was this helpful?

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.