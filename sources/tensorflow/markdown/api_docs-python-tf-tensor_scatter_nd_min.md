[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/tensor_scatter_nd_min#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/tensor_scatter_nd_min)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/tensor_scatter_nd_min?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Ftensor_scatter_nd_min&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/tensor_scatter_nd_min#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/tensor_scatter_nd_min#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/tensor_scatter_nd_min#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.tensor\_scatter\_nd\_min Stay organized with collections Save and categorize content based on your preferences.
==================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/tensor_scatter_nd_min#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/tensor_scatter_nd_min#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/tensor_scatter_nd_min#returns)
    

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.tensor_scatter_nd_min`](https://www.tensorflow.org/api_docs/python/tf/tensor_scatter_nd_min)

tf.tensor_scatter_nd_min(
        tensor: Annotated[Any, TV_TensorScatterMin_T],
        indices: Annotated[Any, TV_TensorScatterMin_Tindices],
        updates: Annotated[Any, TV_TensorScatterMin_T],
        bad_indices_policy: str = '',
        name=None
    ) -> Annotated[Any, TV_TensorScatterMin_T]

### Used in the notebooks

| Used in the guide |
| --- |
| *   [Introduction to tensor slicing](https://www.tensorflow.org/guide/tensor_slicing) |

|     |     |
| --- | --- |
| Args<br>---- |     |
| `tensor` | A `Tensor`. Tensor to update. |
| `indices` | A `Tensor`. Must be one of the following types: `int32`, `int64`. Index tensor. |
| `updates` | A `Tensor`. Must have the same type as `tensor`. Updates to scatter into output. |
| `bad_indices_policy` | An optional `string`. Defaults to `""`. |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| A `Tensor`. Has the same type as `tensor`. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.