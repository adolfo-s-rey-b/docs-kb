[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/ops/meshgrid#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/ops/meshgrid)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/ops/meshgrid?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/meshgrid#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/meshgrid#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.ops.meshgrid Stay organized with collections Save and categorize content based on your preferences.
============================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/meshgrid#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/meshgrid#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L5319-L5353)

Creates grids of coordinates from coordinate vectors.

#### View aliases

**Main aliases**

[`tf.keras.ops.numpy.meshgrid`](https://www.tensorflow.org/api_docs/python/tf/keras/ops/meshgrid)

tf.keras.ops.meshgrid(
        *x, indexing='xy'
    )

Given `N` 1-D tensors `T0, T1, ..., TN-1` as inputs with corresponding lengths `S0, S1, ..., SN-1`, this creates an `N` N-dimensional tensors `G0, G1, ..., GN-1` each with shape `(S0, ..., SN-1)` where the output `Gi` is constructed by expanding `Ti` to the result shape.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `x` | 1-D tensors representing the coordinates of a grid. |
| `indexing` | `"xy"` or `"ij"`. "xy" is cartesian; `"ij"` is matrix indexing of output. Defaults to `"xy"`. |

|     |
| --- |
| Returns<br>------- |     |
| Sequence of N tensors. |     |

#### Example:

    from keras.src import ops

    grid_x, grid_y = ops.meshgrid(x, y, indexing="ij")

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.