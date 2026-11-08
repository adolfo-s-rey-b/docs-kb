[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/pool#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/pool)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/pool?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/pool#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/pool#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/pool#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.nn.pool Stay organized with collections Save and categorize content based on your preferences.
===========================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/pool#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/pool#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/pool#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/nn_ops.py#L1508-L1686)

Performs an N-D pooling operation.

tf.compat.v1.nn.pool(
        input,
        window_shape,
        pooling_type,
        padding,
        dilation_rate=None,
        strides=None,
        name=None,
        data_format=None,
        dilations=None
    )

In the case that `data_format` does not start with "NC", computes for 0 <= b < batch\_size, 0 <= x\[i\] < output\_spatial\_shape\[i\], 0 <= c < num\_channels:

output[b, x[0], ..., x[N-1], c] =
      REDUCE_{z[0], ..., z[N-1]}
        input[b,\
              x[0] * strides[0] - pad_before[0] + dilation_rate[0]*z[0],\
              ...\
              x[N-1]*strides[N-1] - pad_before[N-1] + dilation_rate[N-1]*z[N-1],\
              c],

where the reduction function REDUCE depends on the value of `pooling_type`, and pad\_before is defined based on the value of `padding` as described in the "returns" section of [`tf.nn.convolution`](https://www.tensorflow.org/api_docs/python/tf/nn/convolution)
 for details. The reduction never includes out-of-bounds positions.

In the case that `data_format` starts with `"NC"`, the `input` and output are simply transposed as follows:

pool(input, data_format, **kwargs) =
      tf.transpose(pool(tf.transpose(input, [0] + range(2,N+2) + [1]),
                        **kwargs),
                   [0, N+1] + range(1, N+1))

|     |     |
| --- | --- |
| Args<br>---- |     |
| `input` | Tensor of rank N+2, of shape `[batch_size] + input_spatial_shape + [num_channels]` if data\_format does not start with "NC" (default), or `[batch_size, num_channels] + input_spatial_shape` if data\_format starts with "NC". Pooling happens over the spatial dimensions only. |
| `window_shape` | Sequence of N ints >= 1. |
| `pooling_type` | Specifies pooling operation, must be "AVG" or "MAX". |
| `padding` | The padding algorithm, must be "SAME" or "VALID". See the "returns" section of [`tf.nn.convolution`](https://www.tensorflow.org/api_docs/python/tf/nn/convolution)<br> for details. |
| `dilation_rate` | Optional. Dilation rate. List of N ints >= 1. Defaults to `[1]*N`. If any value of dilation\_rate is > 1, then all values of strides must be 1. |
| `strides` | Optional. Sequence of N ints >= 1. Defaults to `[1]*N`. If any value of strides is > 1, then all values of dilation\_rate must be 1. |
| `name` | Optional. Name of the op. |
| `data_format` | A string or None. Specifies whether the channel dimension of the `input` and output is the last dimension (default, or if `data_format` does not start with "NC"), or the second dimension (if `data_format` starts with "NC"). For N=1, the valid values are "NWC" (default) and "NCW". For N=2, the valid values are "NHWC" (default) and "NCHW". For N=3, the valid values are "NDHWC" (default) and "NCDHW". |
| `dilations` | Alias for dilation\_rate |

|     |
| --- |
| Returns<br>------- |     |
| Tensor of rank N+2, of shape \[batch\_size\] + output\_spatial\_shape + \[num\_channels\]<br><br>if data\_format is None or does not start with "NC", or<br><br>\[batch\_size, num\_channels\] + output\_spatial\_shape<br><br>if data\_format starts with "NC", where `output_spatial_shape` depends on the value of padding:<br><br>If padding = "SAME": output\_spatial\_shape\[i\] = ceil(input\_spatial\_shape\[i\] / strides\[i\])<br><br>If padding = "VALID": output\_spatial\_shape\[i\] = ceil((input\_spatial\_shape\[i\] - (window\_shape\[i\] - 1) \* dilation\_rate\[i\]) / strides\[i\]). |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | if arguments are invalid. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.