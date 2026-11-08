[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/nn/max_pool2d#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/nn/max_pool2d)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/nn/max_pool2d?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fnn%2Fmax_pool2d&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/nn/max_pool2d#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/nn/max_pool2d#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/nn/max_pool2d#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.nn.max\_pool2d Stay organized with collections Save and categorize content based on your preferences.
========================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/nn/max_pool2d#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/nn/max_pool2d#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/nn/max_pool2d#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/nn_ops.py#L4976-L5084)

Performs max pooling on 2D spatial data such as images.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.nn.max_pool2d`](https://www.tensorflow.org/api_docs/python/tf/nn/max_pool2d)

tf.nn.max_pool2d(
        input, ksize, strides, padding, data_format='NHWC', name=None
    )

This is a more specific version of [`tf.nn.max_pool`](https://www.tensorflow.org/api_docs/python/tf/nn/max_pool)
 where the input tensor is 4D, representing 2D spatial data such as images. Using these APIs are equivalent

Downsamples the input images along theirs spatial dimensions (height and width) by taking its maximum over an input window defined by `ksize`. The window is shifted by `strides` along each dimension.

For example, for `strides=(2, 2)` and `padding=VALID` windows that extend outside of the input are not included in the output:

    x = tf.constant([[1., 2., 3., 4.],\
\
With `padding=SAME`, we get:\
\
    x = tf.constant([[1., 2., 3., 4.],\
\
We can also specify padding explicitly. The following example adds width-1 padding on all sides (top, bottom, left, right):\
\
    x = tf.constant([[1., 2., 3., 4.],\
\
For more examples and detail, see [`tf.nn.max_pool`](https://www.tensorflow.org/api_docs/python/tf/nn/max_pool)\
.\
\
|     |     |\
| --- | --- |\
| Args<br>---- |     |\
| `input` | A 4-D `Tensor` of the format specified by `data_format`. |\
| `ksize` | An int or list of `ints` that has length `1`, `2` or `4`. The size of the window for each dimension of the input tensor. If only one integer is specified, then we apply the same window for all 4 dims. If two are provided then we use those for H, W dimensions and keep N, C dimension window size = 1. |\
| `strides` | An int or list of `ints` that has length `1`, `2` or `4`. The stride of the sliding window for each dimension of the input tensor. If only one integer is specified, we apply the same stride to all 4 dims. If two are provided we use those for the H, W dimensions and keep N, C of stride = 1. |\
| `padding` | Either the `string` `"SAME"` or `"VALID"` indicating the type of padding algorithm to use, or a list indicating the explicit paddings at the start and end of each dimension. See [here](https://www.tensorflow.org/api_docs/python/tf/nn#notes_on_padding_2)<br> for more information. When explicit padding is used and data\_format is `"NHWC"`, this should be in the form `[[0, 0], [pad_top, pad_bottom], [pad_left, pad_right], [0, 0]]`. When explicit padding used and data\_format is `"NCHW"`, this should be in the form `[[0, 0], [0, 0], [pad_top, pad_bottom], [pad_left, pad_right]]`. When using explicit padding, the size of the paddings cannot be greater than the sliding window size. |\
| `data_format` | A string. 'NHWC', 'NCHW' and 'NCHW\_VECT\_C' are supported. |\
| `name` | Optional name for the operation. |\
\
|     |\
| --- |\
| Returns<br>------- |     |\
| A `Tensor` of format specified by `data_format`. The max pooled output tensor. |     |\
\
|     |     |\
| --- | --- |\
| Raises<br>------ |     |\
| `ValueError` | If explicit padding is used with data\_format='NCHW\_VECT\_C'. |\
\
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)\
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)\
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)\
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)\
.\
\
Last updated 2026-10-31 UTC.