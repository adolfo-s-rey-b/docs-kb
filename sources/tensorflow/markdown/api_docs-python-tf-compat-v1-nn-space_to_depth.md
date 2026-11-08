[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/space_to_depth#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/space_to_depth)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/space_to_depth?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/space_to_depth#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/space_to_depth#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.nn.space\_to\_depth Stay organized with collections Save and categorize content based on your preferences.
=======================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/space_to_depth#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/space_to_depth#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/array_ops.py#L3794-L3798)

SpaceToDepth for tensors of type T.

tf.compat.v1.nn.space_to_depth(
        input, block_size, name=None, data_format='NHWC'
    )

Rearranges blocks of spatial data, into depth. More specifically, this op outputs a copy of the input tensor where values from the `height` and `width` dimensions are moved to the `depth` dimension. The attr `block_size` indicates the input block size.

*   Non-overlapping blocks of size `block_size x block size` are rearranged into depth at each location.
*   The depth of the output tensor is `block_size * block_size * input_depth`.
*   The Y, X coordinates within each block of the input become the high order component of the output channel index.
*   The input tensor's height and width must be divisible by block\_size.

The `data_format` attr specifies the layout of the input and output tensors with the following options: "NHWC": `[ batch, height, width, channels ]` "NCHW": `[ batch, channels, height, width ]` "NCHW\_VECT\_C": `qint8 [ batch, channels / 4, height, width, 4 ]`

It is useful to consider the operation as transforming a 6-D Tensor. e.g. for data\_format = NHWC, Each element in the input tensor can be specified via 6 coordinates, ordered by decreasing memory layout significance as: n,oY,bY,oX,bX,iC (where n=batch index, oX, oY means X or Y coordinates within the output image, bX, bY means coordinates within the input block, iC means input channels). The output would be a transpose to the following layout: n,oY,oX,bY,bX,iC

This operation is useful for resizing the activations between convolutions (but keeping all data), e.g. instead of pooling. It is also useful for training purely convolutional models.

For example, given an input of shape `[1, 2, 2, 1]`, data\_format = "NHWC" and block\_size = 2:

x = [[[[1], [2]],\
          [[3], [4]]]]

This operation will output a tensor of shape `[1, 1, 1, 4]`:

[[[[1, 2, 3, 4]]]]

Here, the input has a batch of 1 and each batch element has shape `[2, 2, 1]`, the corresponding output will have a single element (i.e. width and height are both 1) and will have a depth of 4 channels (1 \* block\_size \* block\_size). The output element shape is `[1, 1, 4]`.

For an input tensor with larger depth, here of shape `[1, 2, 2, 3]`, e.g.

x = [[[[1, 2, 3], [4, 5, 6]],\
          [[7, 8, 9], [10, 11, 12]]]]

This operation, for block\_size of 2, will return the following tensor of shape `[1, 1, 1, 12]`

[[[[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]]]]

Similarly, for the following input of shape `[1 4 4 1]`, and a block size of 2:

x = [[[[1],   [2],  [5],  [6]],\
          [[3],   [4],  [7],  [8]],\
          [[9],  [10], [13],  [14]],\
          [[11], [12], [15],  [16]]]]

the operator will return the following tensor of shape `[1 2 2 4]`:

x = [[[[1, 2, 3, 4],\
           [5, 6, 7, 8]],\
          [[9, 10, 11, 12],\
           [13, 14, 15, 16]]]]

|     |     |
| --- | --- |
| Args<br>---- |     |
| `input` | A `Tensor`. |
| `block_size` | An `int` that is `>= 2`. The size of the spatial block. |
| `data_format` | An optional `string` from: `"NHWC", "NCHW", "NCHW_VECT_C"`. Defaults to `"NHWC"`. |
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