[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/unravel_index#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/unravel_index)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/unravel_index?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Funravel_index&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/unravel_index#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/unravel_index#returns)
    
*   [numpy compatibility](https://www.tensorflow.org/api_docs/python/tf/unravel_index#numpy-compatibility)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.unravel\_index Stay organized with collections Save and categorize content based on your preferences.
========================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/unravel_index#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/unravel_index#returns)
    
*   [numpy compatibility](https://www.tensorflow.org/api_docs/python/tf/unravel_index#numpy-compatibility)
    

Converts an array of flat indices into a tuple of coordinate arrays.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.unravel_index`](https://www.tensorflow.org/api_docs/python/tf/unravel_index)

tf.unravel_index(
        indices: Annotated[Any, TV_UnravelIndex_Tidx],
        dims: Annotated[Any, TV_UnravelIndex_Tidx],
        name=None
    ) -> Annotated[Any, TV_UnravelIndex_Tidx]

#### Example:

y = tf.unravel_index(indices=[2, 5, 7], dims=[3, 3])
    # 'dims' represent a hypothetical (3, 3) tensor of indices:
    # [[0, 1, *2*],\
    #  [3, 4, *5*],\
    #  [6, *7*, 8]]
    # For each entry from 'indices', this operation returns
    # its coordinates (marked with '*'), such as
    # 2 ==> (0, 2)
    # 5 ==> (1, 2)
    # 7 ==> (2, 1)
    y ==> [[0, 1, 2], [2, 2, 1]]

|     |     |
| --- | --- |
| Args<br>---- |     |
| `indices` | A `Tensor`. Must be one of the following types: `int32`, `int64`. An 0-D or 1-D `int` Tensor whose elements are indices into the flattened version of an array of dimensions dims. |
| `dims` | A `Tensor`. Must have the same type as `indices`. An 1-D `int` Tensor. The shape of the array to use for unraveling indices. |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| A `Tensor`. Has the same type as `indices`. |     |

numpy compatibility
-------------------

Equivalent to np.unravel\_index

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2024-04-26 UTC.