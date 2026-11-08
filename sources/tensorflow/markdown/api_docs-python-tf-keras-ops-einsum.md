[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/ops/einsum#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/ops/einsum)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/ops/einsum?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/einsum#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/einsum#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.ops.einsum Stay organized with collections Save and categorize content based on your preferences.
==========================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/einsum#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/einsum#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L3222-L3308)

Evaluates the Einstein summation convention on the operands.

#### View aliases

**Main aliases**

[`tf.keras.ops.numpy.einsum`](https://www.tensorflow.org/api_docs/python/tf/keras/ops/einsum)

tf.keras.ops.einsum(
        subscripts, *operands, **kwargs
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `subscripts` | Specifies the subscripts for summation as comma separated list of subscript labels. An implicit (classical Einstein summation) calculation is performed unless the explicit indicator `->` is included as well as subscript labels of the precise output form. |
| `operands` | The operands to compute the Einstein sum of. |

|     |
| --- |
| Returns<br>------- |     |
| The calculation based on the Einstein summation convention. |     |

#### Example:

    from keras.src import ops

#### Trace of a matrix:

    ops.einsum("ii", a)

#### Extract the diagonal:

    ops.einsum("ii -> i", a)

#### Sum over an axis:

    ops.einsum("ij -> i", a)

For higher dimensional tensors summing a single axis can be done with ellipsis:

    ops.einsum("...j -> ...", a)

Compute a matrix transpose or reorder any number of axes:

    ops.einsum("ji", c)

Matrix vector multiplication:

    ops.einsum("ij, j", a, b)

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.