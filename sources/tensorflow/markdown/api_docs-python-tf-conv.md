[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/conv#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/conv)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/conv?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/conv#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/conv#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.conv Stay organized with collections Save and categorize content based on your preferences.
==============================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/conv#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/conv#returns)
    

Computes a N-D convolution given (N+1+batch\_dims)-D `input` and (N+2)-D `filter` tensors.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.conv`](https://www.tensorflow.org/api_docs/python/tf/conv)

tf.conv(
        input: Annotated[Any, TV_Conv_T],
        filter: Annotated[Any, TV_Conv_T],
        strides,
        padding: str,
        explicit_paddings=[],
        data_format: str = 'CHANNELS_LAST',
        dilations=[],
        batch_dims: int = 1,
        groups: int = 1,
        name=None
    ) -> Annotated[Any, TV_Conv_T]

General function for computing a N-D convolution. It is required that `1 <= N <= 3`.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `input` | A `Tensor`. Must be one of the following types: `half`, `bfloat16`, `float32`, `float64`, `int32`. Tensor of type T and shape `batch_shape + spatial_shape + [in_channels]` in the case that `channels_last_format = true` or shape `batch_shape + [in_channels] + spatial_shape` if `channels_last_format = false`. spatial\_shape is N-dimensional with `N=2` or `N=3`. Also note that `batch_shape` is dictated by the parameter `batch_dims` and defaults to 1. |
| `filter` | A `Tensor`. Must have the same type as `input`. An `(N+2)-D` Tensor with the same type as `input` and shape `spatial_filter_shape + [in_channels, out_channels]`, where spatial\_filter\_shape is N-dimensional with `N=2` or `N=3`. |
| `strides` | A list of `ints`. 1-D tensor of length `N+2`. The stride of the sliding window for each dimension of `input`. Must have `strides[0] = strides[N+1] = 1`. |
| `padding` | A `string` from: `"SAME", "VALID", "EXPLICIT"`. The type of padding algorithm to use. |
| `explicit_paddings` | An optional list of `ints`. Defaults to `[]`. If `padding` is `"EXPLICIT"`, the list of explicit padding amounts. For the ith dimension, the amount of padding inserted before and after the dimension is `explicit_paddings[2 * i]` and `explicit_paddings[2 * i + 1]`, respectively. If `padding` is not `"EXPLICIT"`, `explicit_paddings` must be empty. |
| `data_format` | An optional `string` from: `"CHANNELS_FIRST", "CHANNELS_LAST"`. Defaults to `"CHANNELS_LAST"`. Used to set the data format. By default `CHANNELS_FIRST`, uses `NHWC (2D) / NDHWC (3D)` or if `CHANNELS_LAST`, uses `NCHW (2D) / NCDHW (3D)`. |
| `dilations` | An optional list of `ints`. Defaults to `[]`. 1-D tensor of length `N+2`. The dilation factor for each dimension of `input`. If set to `k > 1`, there will be `k-1` skipped cells between each filter element on that dimension. The dimension order is determined by the value of `channels_last_format`, see above for details. Dilations in the batch and depth dimensions must be 1. |
| `batch_dims` | An optional `int`. Defaults to `1`. A positive integer specifying the number of batch dimensions for the input tensor. Should be less than the rank of the input tensor. |
| `groups` | An optional `int`. Defaults to `1`. A positive integer specifying the number of groups in which the input is split along the channel axis. Each group is convolved separately with `filters / groups` filters. The output is the concatenation of all the groups results along the channel axis. Input channels and filters must both be divisible by groups. |
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