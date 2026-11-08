[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/ops/max_pool#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/ops/max_pool)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/ops/max_pool?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fkeras%2Fops%2Fmax_pool&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/max_pool#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/max_pool#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.ops.max\_pool Stay organized with collections Save and categorize content based on your preferences.
=============================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/max_pool#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/max_pool#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/nn.py#L1133-L1182)

Max pooling operation.

#### View aliases

**Main aliases**

[`tf.keras.ops.nn.max_pool`](https://www.tensorflow.org/api_docs/python/tf/keras/ops/max_pool)

tf.keras.ops.max_pool(
        inputs,
        pool_size,
        strides=None,
        padding='valid',
        data_format=None
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `inputs` | Tensor of rank N+2. `inputs` has shape `(batch_size,) + inputs_spatial_shape + (num_channels,)` if `data_format="channels_last"`, or `(batch_size, num_channels) + inputs_spatial_shape` if `data_format="channels_first"`. Pooling happens over the spatial dimensions only. |
| `pool_size` | int or tuple/list of integers of size `len(inputs_spatial_shape)`, specifying the size of the pooling window for each spatial dimension of the input tensor. If `pool_size` is int, then every spatial dimension shares the same `pool_size`. |
| `strides` | int or tuple/list of integers of size `len(inputs_spatial_shape)`. The stride of the sliding window for each spatial dimension of the input tensor. If `strides` is int, then every spatial dimension shares the same `strides`. |
| `padding` | string, either `"valid"` or `"same"`. `"valid"` means no padding is applied, and `"same"` results in padding evenly to the left/right or up/down of the input such that output has the same height/width dimension as the input when `strides=1`. |
| `data_format` | A string, either `"channels_last"` or `"channels_first"`. `data_format` determines the ordering of the dimensions in the inputs. If `data_format="channels_last"`, `inputs` is of shape `(batch_size, ..., channels)` while if `data_format="channels_first"`, `inputs` is of shape `(batch_size, channels, ...)`. |

|     |
| --- |
| Returns<br>------- |     |
| A tensor of rank N+2, the result of the max pooling operation. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.