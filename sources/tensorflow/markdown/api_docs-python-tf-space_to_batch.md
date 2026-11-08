[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/space_to_batch#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/space_to_batch)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/space_to_batch?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/space_to_batch#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/space_to_batch#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.space\_to\_batch Stay organized with collections Save and categorize content based on your preferences.
==========================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/space_to_batch#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/space_to_batch#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/array_ops.py#L3785-L3788)

SpaceToBatch for N-D tensors of type T.

#### View aliases

**Main aliases**

[`tf.nn.space_to_batch`](https://www.tensorflow.org/api_docs/python/tf/space_to_batch)

tf.space_to_batch(
        input, block_shape, paddings, name=None
    )

This operation divides "spatial" dimensions `[1, ..., M]` of the input into a grid of blocks of shape `block_shape`, and interleaves these blocks with the "batch" dimension (0) such that in the output, the spatial dimensions `[1, ..., M]` correspond to the position within the grid, and the batch dimension combines both the position within a spatial block and the original batch position. Prior to division into blocks, the spatial dimensions of the input are optionally zero padded according to `paddings`. See below for a precise description.

This operation is equivalent to the following steps:

1.  Zero-pad the start and end of dimensions `[1, ..., M]` of the input according to `paddings` to produce `padded` of shape `padded_shape`.
    
2.  Reshape `padded` to `reshaped_padded` of shape:
    
    \[batch\] + \[padded\_shape\[1\] / block\_shape\[0\], block\_shape\[0\], ..., padded\_shape\[M\] / block\_shape\[M-1\], block\_shape\[M-1\]\] + remaining\_shape
    
3.  Permute dimensions of `reshaped_padded` to produce `permuted_reshaped_padded` of shape:
    
    block\_shape + \[batch\] + \[padded\_shape\[1\] / block\_shape\[0\], ..., padded\_shape\[M\] / block\_shape\[M-1\]\] + remaining\_shape
    
4.  Reshape `permuted_reshaped_padded` to flatten `block_shape` into the batch dimension, producing an output tensor of shape:
    
    \[batch \* prod(block\_shape)\] + \[padded\_shape\[1\] / block\_shape\[0\], ..., padded\_shape\[M\] / block\_shape\[M-1\]\] + remaining\_shape
    

#### Some examples:

(1) For the following input of shape `[1, 2, 2, 1]`, `block_shape = [2, 2]`, and `paddings = [[0, 0], [0, 0]]`:

x = [[[[1], [2]], [[3], [4]]]]

The output tensor has shape `[4, 1, 1, 1]` and value:

[[[[1]]], [[[2]]], [[[3]]], [[[4]]]]

(2) For the following input of shape `[1, 2, 2, 3]`, `block_shape = [2, 2]`, and `paddings = [[0, 0], [0, 0]]`:

x = [[[[1, 2, 3], [4, 5, 6]],\
          [[7, 8, 9], [10, 11, 12]]]]

The output tensor has shape `[4, 1, 1, 3]` and value:

[[[[1, 2, 3]]], [[[4, 5, 6]]], [[[7, 8, 9]]], [[[10, 11, 12]]]]

(3) For the following input of shape `[1, 4, 4, 1]`, `block_shape = [2, 2]`, and `paddings = [[0, 0], [0, 0]]`:

x = [[[[1],   [2],  [3],  [4]],\
          [[5],   [6],  [7],  [8]],\
          [[9],  [10], [11],  [12]],\
          [[13], [14], [15],  [16]]]]

The output tensor has shape `[4, 2, 2, 1]` and value:

x = [[[[1], [3]], [[9], [11]]],\
         [[[2], [4]], [[10], [12]]],\
         [[[5], [7]], [[13], [15]]],\
         [[[6], [8]], [[14], [16]]]]

(4) For the following input of shape `[2, 2, 4, 1]`, block\_shape = `[2, 2]`, and paddings = `[[0, 0], [2, 0]]`:

x = [[[[1],   [2],  [3],  [4]],\
          [[5],   [6],  [7],  [8]]],\
         [[[9],  [10], [11],  [12]],\
          [[13], [14], [15],  [16]]]]

The output tensor has shape `[8, 1, 3, 1]` and value:

x = [[[[0], [1], [3]]], [[[0], [9], [11]]],\
         [[[0], [2], [4]]], [[[0], [10], [12]]],\
         [[[0], [5], [7]]], [[[0], [13], [15]]],\
         [[[0], [6], [8]]], [[[0], [14], [16]]]]

Among others, this operation is useful for reducing atrous convolution into regular convolution.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `input` | A `Tensor`. N-D with shape `input_shape = [batch] + spatial_shape + remaining_shape`, where spatial\_shape has `M` dimensions. |
| `block_shape` | A `Tensor`. Must be one of the following types: `int32`, `int64`. 1-D with shape `[M]`, all values must be >= 1. |
| `paddings` | A `Tensor`. Must be one of the following types: `int32`, `int64`. 2-D with shape `[M, 2]`, all values must be >= 0. `paddings[i] = [pad_start, pad_end]` specifies the padding for input dimension `i + 1`, which corresponds to spatial dimension `i`. It is required that `block_shape[i]` divides `input_shape[i + 1] + pad_start + pad_end`. |
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

Last updated 2026-10-31 UTC.