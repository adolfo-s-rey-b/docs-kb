[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/max_pool#main-content)

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
    

tf.compat.v1.nn.max\_pool Stay organized with collections Save and categorize content based on your preferences.
================================================================================================================

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/nn_ops.py#L4854-L4912)

Performs the max pooling on the input.

tf.compat.v1.nn.max_pool(
        value,
        ksize,
        strides,
        padding,
        data_format='NHWC',
        name=None,
        input=None
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `value` | A 4-D `Tensor` of the format specified by `data_format`. |
| `ksize` | An int or list of `ints` that has length `1`, `2` or `4`. The size of the window for each dimension of the input tensor. |
| `strides` | An int or list of `ints` that has length `1`, `2` or `4`. The stride of the sliding window for each dimension of the input tensor. |
| `padding` | Either the `string` `"SAME"` or `"VALID"` indicating the type of padding algorithm to use, or a list indicating the explicit paddings at the start and end of each dimension. When explicit padding is used and data\_format is `"NHWC"`, this should be in the form `[[0, 0], [pad_top, pad_bottom], [pad_left, pad_right], [0, 0]]`. When explicit padding used and data\_format is `"NCHW"`, this should be in the form `[[0, 0], [0, 0], [pad_top, pad_bottom], [pad_left, pad_right]]`. When using explicit padding, the size of the paddings cannot be greater than the sliding window size. |
| `data_format` | A string. 'NHWC', 'NCHW' and 'NCHW\_VECT\_C' are supported. |
| `name` | Optional name for the operation. |
| `input` | Alias for value. |

|     |
| --- |
| Returns<br>------- |     |
| A `Tensor` of format specified by `data_format`. The max pooled output tensor. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.