[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/conv3d_backprop_filter#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/conv3d_backprop_filter)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/conv3d_backprop_filter?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/conv3d_backprop_filter#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/conv3d_backprop_filter#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.nn.conv3d\_backprop\_filter Stay organized with collections Save and categorize content based on your preferences.
===============================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/conv3d_backprop_filter#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/conv3d_backprop_filter#returns)
    

Computes the gradients of 3-D convolution with respect to the filter.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.nn.conv3d_backprop_filter_v2`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/conv3d_backprop_filter)

tf.compat.v1.nn.conv3d_backprop_filter(
        input: Annotated[Any, TV_Conv3DBackpropFilterV2_T],
        filter_sizes: Annotated[Any, _atypes.Int32],
        out_backprop: Annotated[Any, TV_Conv3DBackpropFilterV2_T],
        strides,
        padding: str,
        data_format: str = 'NDHWC',
        dilations=[1, 1, 1, 1, 1],
        name=None
    ) -> Annotated[Any, TV_Conv3DBackpropFilterV2_T]

|     |     |
| --- | --- |
| Args<br>---- |     |
| `input` | A `Tensor`. Must be one of the following types: `half`, `bfloat16`, `float32`, `float64`. Shape `[batch, depth, rows, cols, in_channels]`. |
| `filter_sizes` | A `Tensor` of type `int32`. An integer vector representing the tensor shape of `filter`, where `filter` is a 5-D `[filter_depth, filter_height, filter_width, in_channels, out_channels]` tensor. |
| `out_backprop` | A `Tensor`. Must have the same type as `input`. Backprop signal of shape `[batch, out_depth, out_rows, out_cols, out_channels]`. |
| `strides` | A list of `ints` that has length `>= 5`. 1-D tensor of length 5. The stride of the sliding window for each dimension of `input`. Must have `strides[0] = strides[4] = 1`. |
| `padding` | A `string` from: `"SAME", "VALID"`. The type of padding algorithm to use. |
| `data_format` | An optional `string` from: `"NDHWC", "NCDHW"`. Defaults to `"NDHWC"`. The data format of the input and output data. With the default format "NDHWC", the data is stored in the order of: \[batch, in\_depth, in\_height, in\_width, in\_channels\]. Alternatively, the format could be "NCDHW", the data storage order is: \[batch, in\_channels, in\_depth, in\_height, in\_width\]. |
| `dilations` | An optional list of `ints`. Defaults to `[1, 1, 1, 1, 1]`. 1-D tensor of length 5. The dilation factor for each dimension of `input`. If set to k > 1, there will be k-1 skipped cells between each filter element on that dimension. The dimension order is determined by the value of `data_format`, see above for details. Dilations in the batch and depth dimensions must be 1. |
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