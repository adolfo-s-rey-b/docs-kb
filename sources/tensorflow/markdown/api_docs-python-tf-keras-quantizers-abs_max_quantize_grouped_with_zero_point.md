[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/quantizers/abs_max_quantize_grouped_with_zero_point?version=stable#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/quantizers/abs_max_quantize_grouped_with_zero_point)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/quantizers/abs_max_quantize_grouped_with_zero_point?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/quantizers/abs_max_quantize_grouped_with_zero_point?version=stable#args_1)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/quantizers/abs_max_quantize_grouped_with_zero_point?version=stable#returns_1)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.quantizers.abs\_max\_quantize\_grouped\_with\_zero\_point Stay organized with collections Save and categorize content based on your preferences.
=========================================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/quantizers/abs_max_quantize_grouped_with_zero_point?version=stable#args_1)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/quantizers/abs_max_quantize_grouped_with_zero_point?version=stable#returns_1)
    

See Stable See Nightly

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/quantizers/quantizers.py#L123-L179)

Quantizes a 2D tensor using grouped asymmetric quantization with zero point.

tf.keras.quantizers.abs_max_quantize_grouped_with_zero_point(
        inputs,
        block_size,
        value_range=(-8, 7),
        dtype='int8',
        epsilon=backend.epsilon(),
        to_numpy=False
    )

Groups are formed along axis 0 (the input/contracting dimension). Each group of `block_size` rows gets its own scale factor and zero point per column. This is useful for weight distributions that are not centered around zero.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `inputs` | Input tensor to quantize. Shape: `(input_dim, output_dim)`. |
| `block_size` | Number of elements per group along axis 0. |
| `value_range` | Tuple of `(min, max)` quantization range. |
| `dtype` | Data type of quantized output. |
| `epsilon` | Small value to avoid division by zero. |
| `to_numpy` | Whether to perform computation in numpy for memory efficiency. |

|     |
| --- |
| Returns<br>------- |     |
| A tuple `(quantized_tensor, scale, zero_point)` where:<br><br>*   `quantized_tensor`: Same shape as inputs, dtype=`dtype`.<br>*   `scale`: Shape `(n_groups, output_dim)` where `n_groups = ceil(input_dim / block_size)`.<br>*   `zero_point`: Shape `(n_groups, output_dim)`, dtype=`uint8`. |     |

#### Example:

> > > import numpy as np from keras.quantizers import abs\_max\_quantize\_grouped\_with\_zero\_point kernel = np.random.randn(512, 256).astype("float32") quantized, scale, zero\_point = abs\_max\_quantize\_grouped\_with\_zero\_point( ... kernel, block\_size=128, value\_range=(-8, 7) ... ) quantized.shape (512, 256) scale.shape # 512 / 128 = 4 groups (4, 256) zero\_point.shape (4, 256)

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.