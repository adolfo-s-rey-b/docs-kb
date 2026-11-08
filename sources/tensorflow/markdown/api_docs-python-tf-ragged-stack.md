[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/ragged/stack#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/ragged/stack)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/ragged/stack?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fragged%2Fstack&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/ragged/stack#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/ragged/stack#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/ragged/stack#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.ragged.stack Stay organized with collections Save and categorize content based on your preferences.
======================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/ragged/stack#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/ragged/stack#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/ragged/stack#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/ragged/ragged_concat_ops.py#L73-L124)

Stacks a list of rank-`R` tensors into one rank-`(R+1)` `RaggedTensor`.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.ragged.stack`](https://www.tensorflow.org/api_docs/python/tf/ragged/stack)

tf.ragged.stack(
        values: typing.List[ragged_tensor.RaggedOrDense], axis=0, name=None
    )

Given a list of tensors or ragged tensors with the same rank `R` (`R >= axis`), returns a rank-`R+1` `RaggedTensor` `result` such that `result[i0...iaxis]` is `[value[i0...iaxis] for value in values]`.

#### Examples:

    # Stacking two ragged tensors.

    # Stacking two dense tensors with different sizes.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `values` | A list of [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> or [`tf.RaggedTensor`](https://www.tensorflow.org/api_docs/python/tf/RaggedTensor)<br>. May not be empty. All `values` must have the same rank and the same dtype; but unlike [`tf.stack`](https://www.tensorflow.org/api_docs/python/tf/stack)<br>, they can have arbitrary dimension sizes. |
| `axis` | A python integer, indicating the dimension along which to stack. (Note: Unlike [`tf.stack`](https://www.tensorflow.org/api_docs/python/tf/stack)<br>, the `axis` parameter must be statically known.) Negative values are supported only if the rank of at least one `values` value is statically known. |
| `name` | A name prefix for the returned tensor (optional). |

|     |
| --- |
| Returns<br>------- |     |
| A `RaggedTensor` with rank `R+1` (if `R>0`). If `R==0`, then the result will be returned as a 1D `Tensor`, since `RaggedTensor` can only be used when `rank>1`. `result.ragged_rank=1+max(axis, max(rt.ragged_rank for rt in values]))`. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | If `values` is empty, if `axis` is out of bounds or if the input tensors have different ranks. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.