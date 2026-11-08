[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/sets/size#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/sets/size)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/sets/size?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/sets/size#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/sets/size#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/sets/size#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.sets.size Stay organized with collections Save and categorize content based on your preferences.
===================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/sets/size#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/sets/size#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/sets/size#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/sets_impl.py#L30-L58)

Compute number of unique elements along last dimension of `a`.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.sets.set_size`](https://www.tensorflow.org/api_docs/python/tf/sets/size)
, [`tf.compat.v1.sets.size`](https://www.tensorflow.org/api_docs/python/tf/sets/size)

tf.sets.size(
        a, validate_indices=True
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `a` | `SparseTensor`, with indices sorted in row-major order. |
| `validate_indices` | Whether to validate the order and range of sparse indices in `a`. Note that setting this to `false` allows for undefined behavior when calling this function with invalid indices. |

|     |
| --- |
| Returns<br>------- |     |
| `int32` `Tensor` of set sizes. For `a` ranked `n`, this is a `Tensor` with rank `n-1`, and the same 1st `n-1` dimensions as `a`. Each value is the number of unique elements in the corresponding `[0...n-1]` dimension of `a`. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `TypeError` | If `a` is an invalid types. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.