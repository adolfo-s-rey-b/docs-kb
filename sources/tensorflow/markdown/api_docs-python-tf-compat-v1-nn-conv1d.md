[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/conv1d?version=stable#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/conv1d)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/conv1d?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/conv1d?version=stable#args_1)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/conv1d?version=stable#returns_1)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/conv1d?version=stable#raises_1)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.nn.conv1d Stay organized with collections Save and categorize content based on your preferences.
=============================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/conv1d?version=stable#args_1)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/conv1d?version=stable#returns_1)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/conv1d?version=stable#raises_1)
    

See Stable See Nightly

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/nn_ops.py#L1982-L2096)

Computes a 1-D convolution of input with rank `>=3` and a `3-D` filter. (deprecated argument values) (deprecated argument values)

tf.compat.v1.nn.conv1d(
        value=None,
        filters=None,
        stride=None,
        padding=None,
        use_cudnn_on_gpu=None,
        data_format=None,
        name=None,
        input=None,
        dilations=None
    )

Given an input tensor of shape `batch_shape + [in_width, in_channels]` if `data_format` is `"NWC"`, or `batch_shape + [in_channels, in_width]` if `data_format` is `"NCW"`, and a filter / kernel tensor of shape `[filter_width, in_channels, out_channels]`, this op reshapes the arguments to pass them to `conv2d` to perform the equivalent convolution operation.

Internally, this op reshapes the input tensors and invokes [`tf.nn.conv2d`](https://www.tensorflow.org/api_docs/python/tf/nn/conv2d)
. For example, if `data_format` does not start with "NC", a tensor of shape `batch_shape + [in_width, in_channels]` is reshaped to `batch_shape + [1, in_width, in_channels]`, and the filter is reshaped to `[1, filter_width, in_channels, out_channels]`. The result is then reshaped back to `batch_shape + [out_width, out_channels]` (where out\_width is a function of the stride and padding as in conv2d) and returned to the caller.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `value` | A Tensor of rank at least 3. Must be of type `float16`, `float32`, or `float64`. |
| `filters` | A Tensor of rank at least 3. Must have the same type as `value`. |
| `stride` | An int or list of `ints` that has length `1` or `3`. The number of entries by which the filter is moved right at each step. |
| `padding` | 'SAME' or 'VALID' |
| `use_cudnn_on_gpu` | An optional `bool`. Defaults to `True`. |
| `data_format` | An optional `string` from `"NWC", "NCW"`. Defaults to `"NWC"`, the data is stored in the order of `batch_shape + [in_width, in_channels]`. The `"NCW"` format stores data as `batch_shape + [in_channels, in_width]`. |
| `name` | A name for the operation (optional). |
| `input` | Alias for value. |
| `dilations` | An int or list of `ints` that has length `1` or `3` which defaults to 1. The dilation factor for each dimension of input. If set to k > 1, there will be k-1 skipped cells between each filter element on that dimension. Dilations in the batch and depth dimensions must be 1. |

|     |
| --- |
| Returns<br>------- |     |
| A `Tensor`. Has the same type as input. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | if `data_format` is invalid. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.