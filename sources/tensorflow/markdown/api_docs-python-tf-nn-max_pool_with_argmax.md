[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/nn/max_pool_with_argmax#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/nn/max_pool_with_argmax)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/nn/max_pool_with_argmax?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/nn/max_pool_with_argmax#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/nn/max_pool_with_argmax#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.nn.max\_pool\_with\_argmax Stay organized with collections Save and categorize content based on your preferences.
====================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/nn/max_pool_with_argmax#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/nn/max_pool_with_argmax#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/nn_ops.py#L5133-L5203)

Performs max pooling on the input and outputs both max values and indices.

tf.nn.max_pool_with_argmax(
        input,
        ksize,
        strides,
        padding,
        data_format='NHWC',
        output_dtype=tf.dtypes.int64,
        include_batch_in_index=False,
        name=None
    )

The indices in `argmax` are flattened, so that a maximum value at position `[b, y, x, c]` becomes flattened index: `(y * width + x) * channels + c` if `include_batch_in_index` is False; `((b * height + y) * width + x) * channels + c` if `include_batch_in_index` is True.

The indices returned are always in `[0, height) x [0, width)` before flattening, even if padding is involved and the mathematically correct answer is outside (either negative or too large). This is a bug, but fixing it is difficult to do in a safe backwards compatible way, especially due to flattening.\
\
|     |     |\
| --- | --- |\
| Args<br>---- |     |\
| `input` | A `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `int64`, `bfloat16`, `uint16`, `half`, `uint32`, `uint64`. 4-D with shape `[batch, height, width, channels]`. Input to pool over. |\
| `ksize` | An int or list of `ints` that has length `1`, `2` or `4`. The size of the window for each dimension of the input tensor. |\
| `strides` | An int or list of `ints` that has length `1`, `2` or `4`. The stride of the sliding window for each dimension of the input tensor. |\
| `padding` | A `string` from: `"SAME", "VALID"`. The type of padding algorithm to use. See [here](https://www.tensorflow.org/api_docs/python/tf/nn#notes_on_padding_2)<br> for more information. |\
| `data_format` | An optional `string`, must be set to `"NHWC"`. Defaults to `"NHWC"`. Specify the data format of the input and output data. |\
| `output_dtype` | An optional [`tf.DType`](https://www.tensorflow.org/api_docs/python/tf/dtypes/DType)<br> from: `tf.int32, tf.int64`. Defaults to [`tf.int64`](https://www.tensorflow.org/api_docs/python/tf#int64)<br>. The dtype of the returned argmax tensor. |\
| `include_batch_in_index` | An optional `boolean`. Defaults to `False`. Whether to include batch dimension in flattened index of `argmax`. |\
| `name` | A name for the operation (optional). |\
\
|     |     |\
| --- | --- |\
| Returns<br>------- |     |\
| A tuple of `Tensor` objects (output, argmax). |     |\
| `output` | A `Tensor`. Has the same type as `input`. |\
| `argmax` | A `Tensor` of type `output_dtype`. |\
\
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)\
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)\
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)\
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)\
.\
\
Last updated 2026-10-31 UTC.