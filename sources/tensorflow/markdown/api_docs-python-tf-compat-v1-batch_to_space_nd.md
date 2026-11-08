[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/batch_to_space_nd#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/batch_to_space_nd)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/batch_to_space_nd?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/batch_to_space_nd#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/batch_to_space_nd#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.batch\_to\_space\_nd Stay organized with collections Save and categorize content based on your preferences.
========================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/batch_to_space_nd#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/batch_to_space_nd#returns)
    

BatchToSpace for N-D tensors of type T.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.manip.batch_to_space_nd`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/batch_to_space_nd)

tf.compat.v1.batch_to_space_nd(
        input: Annotated[Any, TV_BatchToSpaceND_T],
        block_shape: Annotated[Any, TV_BatchToSpaceND_Tblock_shape],
        crops: Annotated[Any, TV_BatchToSpaceND_Tcrops],
        name=None
    ) -> Annotated[Any, TV_BatchToSpaceND_T]

This operation reshapes the "batch" dimension 0 into `M + 1` dimensions of shape `block_shape + [batch]`, interleaves these blocks back into the grid defined by the spatial dimensions `[1, ..., M]`, to obtain a result with the same rank as the input. The spatial dimensions of this intermediate result are then optionally cropped according to `crops` to produce the output. This is the reverse of SpaceToBatch. See below for a precise description.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `input` | A `Tensor`. N-D with shape `input_shape = [batch] + spatial_shape + remaining_shape`, where spatial\_shape has M dimensions. |
| `block_shape` | A `Tensor`. Must be one of the following types: `int32`, `int64`. 1-D with shape `[M]`, all values must be >= 1. |
| `crops` | A `Tensor`. Must be one of the following types: `int32`, `int64`. 2-D with shape `[M, 2]`, all values must be >= 0. `crops[i] = [crop_start, crop_end]` specifies the amount to crop from input dimension `i + 1`, which corresponds to spatial dimension `i`. It is required that `crop_start[i] + crop_end[i] <= block_shape[i] * input_shape[i + 1]`.<br><br>This operation is equivalent to the following steps:<br><br>1.  Reshape `input` to `reshaped` of shape: \[block\_shape\[0\], ..., block\_shape\[M-1\], batch / prod(block\_shape), input\_shape\[1\], ..., input\_shape\[N-1\]\]<br>    <br>2.  Permute dimensions of `reshaped` to produce `permuted` of shape \[batch / prod(block\_shape),<br>    <br>    input\_shape\[1\], block\_shape\[0\], ..., input\_shape\[M\], block\_shape\[M-1\],<br>    <br>    input\_shape\[M+1\], ..., input\_shape\[N-1\]\]<br>    <br>3.  Reshape `permuted` to produce `reshaped_permuted` of shape \[batch / prod(block\_shape),<br>    <br>    input\_shape\[1\] \* block\_shape\[0\], ..., input\_shape\[M\] \* block\_shape\[M-1\],<br>    <br>    input\_shape\[M+1\], ..., input\_shape\[N-1\]\]<br>    <br>4.  Crop the start and end of dimensions `[1, ..., M]` of `reshaped_permuted` according to `crops` to produce the output of shape: \[batch / prod(block\_shape),<br>    <br>    input\_shape\[1\] \* block\_shape\[0\] - crops\[0,0\] - crops\[0,1\], ..., input\_shape\[M\] \* block\_shape\[M-1\] - crops\[M-1,0\] - crops\[M-1,1\],<br>    <br>    input\_shape\[M+1\], ..., input\_shape\[N-1\]\]<br>    <br><br>Some examples:<br><br>(1) For the following input of shape `[4, 1, 1, 1]`, `block_shape = [2, 2]`, and `crops = [[0, 0], [0, 0]]`:<br><br>[[[[1]]], [[[2]]], [[[3]]], [[[4]]]]<br><br>The output tensor has shape `[1, 2, 2, 1]` and value:<br><br>x = [[[[1], [2]], [[3], [4]]]]<br><br>(2) For the following input of shape `[4, 1, 1, 3]`, `block_shape = [2, 2]`, and `crops = [[0, 0], [0, 0]]`:<br><br>[[[[1, 2, 3]]], [[[4, 5, 6]]], [[[7, 8, 9]]], [[[10, 11, 12]]]]<br><br>The output tensor has shape `[1, 2, 2, 3]` and value:<br><br>x = [[[[1, 2, 3], [4, 5, 6]],<br>          [[7, 8, 9], [10, 11, 12]]]]<br><br>(3) For the following input of shape `[4, 2, 2, 1]`, `block_shape = [2, 2]`, and `crops = [[0, 0], [0, 0]]`:<br><br>x = [[[[1], [3]], [[9], [11]]],<br>         [[[2], [4]], [[10], [12]]],<br>         [[[5], [7]], [[13], [15]]],<br>         [[[6], [8]], [[14], [16]]]]<br><br>The output tensor has shape `[1, 4, 4, 1]` and value:<br><br>x = [[[[1],   [2],  [3],  [4]],<br>         [[5],   [6],  [7],  [8]],<br>         [[9],  [10], [11],  [12]],<br>         [[13], [14], [15],  [16]]]]<br><br>(4) For the following input of shape `[8, 1, 3, 1]`, `block_shape = [2, 2]`, and `crops = [[0, 0], [2, 0]]`:<br><br>x = [[[[0], [1], [3]]], [[[0], [9], [11]]],<br>         [[[0], [2], [4]]], [[[0], [10], [12]]],<br>         [[[0], [5], [7]]], [[[0], [13], [15]]],<br>         [[[0], [6], [8]]], [[[0], [14], [16]]]]<br><br>The output tensor has shape `[2, 2, 4, 1]` and value:<br><br>x = [[[[1],   [2],  [3],  [4]],<br>          [[5],   [6],  [7],  [8]]],<br>         [[[9],  [10], [11],  [12]],<br>          [[13], [14], [15],  [16]]]] |
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