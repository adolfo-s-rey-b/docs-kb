[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/meshgrid#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/meshgrid)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/meshgrid?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/meshgrid#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/meshgrid#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/meshgrid#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/meshgrid#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.meshgrid Stay organized with collections Save and categorize content based on your preferences.
==================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/meshgrid#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/meshgrid#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/meshgrid#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/meshgrid#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/array_ops.py#L3378-L3457)

Broadcasts parameters for evaluation on an N-D grid.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.meshgrid`](https://www.tensorflow.org/api_docs/python/tf/meshgrid)

tf.meshgrid(
        *args, **kwargs
    )

### Used in the notebooks

| Used in the guide |
| --- |
| *   [Optimizers with Core APIs](https://www.tensorflow.org/guide/core/optimizers_core) |

Given N one-dimensional coordinate arrays `*args`, returns a list `outputs` of N-D coordinate arrays for evaluating expressions on an N-D grid.

#### Notes:

`meshgrid` supports cartesian ('xy') and matrix ('ij') indexing conventions. When the `indexing` argument is set to 'xy' (the default), the broadcasting instructions for the first two dimensions are swapped.

#### Examples:

Calling `X, Y = meshgrid(x, y)` with the tensors

x = [1, 2, 3]
    y = [4, 5, 6]
    X, Y = tf.meshgrid(x, y)
    # X = [[1, 2, 3],\
    #      [1, 2, 3],\
    #      [1, 2, 3]]
    # Y = [[4, 4, 4],\
    #      [5, 5, 5],\
    #      [6, 6, 6]]

|     |     |
| --- | --- |
| Args<br>---- |     |
| `*args` | `Tensor`s with rank 1. |
| `**kwargs` | *   indexing: Either 'xy' or 'ij' (optional, default: 'xy').<br>*   name: A name for the operation (optional). |

|     |     |
| --- | --- |
| Returns<br>------- |     |
| `outputs` | A list of N `Tensor`s with rank N. |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `TypeError` | When no keyword arguments (kwargs) are passed. |
| `ValueError` | When indexing keyword argument is not one of `xy` or `ij`. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.