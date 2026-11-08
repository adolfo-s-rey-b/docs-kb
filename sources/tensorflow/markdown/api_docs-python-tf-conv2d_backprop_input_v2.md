[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/conv2d_backprop_input_v2#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   English
*   中文 – 简体

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.conv2d\_backprop\_input\_v2 Stay organized with collections Save and categorize content based on your preferences.
=====================================================================================================================

Computes the gradients of convolution with respect to the input.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.conv2d_backprop_input_v2`](https://www.tensorflow.org/api_docs/python/tf/conv2d_backprop_input_v2)

tf.conv2d_backprop_input_v2(
        input: Annotated[Any, TV_Conv2DBackpropInputV2_T],
        filter: Annotated[Any, TV_Conv2DBackpropInputV2_T],
        out_backprop: Annotated[Any, TV_Conv2DBackpropInputV2_T],
        strides,
        padding: str,
        use_cudnn_on_gpu: bool = True,
        explicit_paddings=[],
        data_format: str = 'NHWC',
        dilations=[1, 1, 1, 1],
        name=None
    ) -> Annotated[Any, TV_Conv2DBackpropInputV2_T]

|     |     |
| --- | --- |
| Args<br>---- |     |
| `input` | A `Tensor`. Must be one of the following types: `half`, `bfloat16`, `float32`, `float64`, `int32`. 4-D with shape `[batch, in_height, in_width, in_channels]`. Only shape of tensor is used. |
| `filter` | A `Tensor`. Must have the same type as `input`. 4-D with shape `[filter_height, filter_width, in_channels, out_channels]`. |
| `out_backprop` | A `Tensor`. Must have the same type as `input`. 4-D with shape `[batch, out_height, out_width, out_channels]`. Gradients w.r.t. the output of the convolution. |
| `strides` | A list of `ints`. The stride of the sliding window for each dimension of the input of the convolution. Must be in the same order as the dimension specified with format. |
| `padding` | A `string` from: `"SAME", "VALID", "EXPLICIT"`. The type of padding algorithm to use. |
| `use_cudnn_on_gpu` | An optional `bool`. Defaults to `True`. |
| `explicit_paddings` | An optional list of `ints`. Defaults to `[]`. If `padding` is `"EXPLICIT"`, the list of explicit padding amounts. For the ith dimension, the amount of padding inserted before and after the dimension is `explicit_paddings[2 * i]` and `explicit_paddings[2 * i + 1]`, respectively. If `padding` is not `"EXPLICIT"`, `explicit_paddings` must be empty. |
| `data_format` | An optional `string` from: `"NHWC", "NCHW"`. Defaults to `"NHWC"`. Specify the data format of the input and output data. With the default format "NHWC", the data is stored in the order of: \[batch, in\_height, in\_width, in\_channels\]. Alternatively, the format could be "NCHW", the data storage order of: \[batch, in\_channels, in\_height, in\_width\]. |
| `dilations` | An optional list of `ints`. Defaults to `[1, 1, 1, 1]`. 1-D tensor of length 4. The dilation factor for each dimension of `input`. If set to k > 1, there will be k-1 skipped cells between each filter element on that dimension. The dimension order is determined by the value of `data_format`, see above for details. Dilations in the batch and depth dimensions must be 1. |
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