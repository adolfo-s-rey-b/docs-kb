[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/ops/adaptive_average_pool#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/ops/adaptive_average_pool)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/ops/adaptive_average_pool?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/adaptive_average_pool#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/adaptive_average_pool#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.ops.adaptive\_average\_pool Stay organized with collections Save and categorize content based on your preferences.
===========================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/adaptive_average_pool#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/adaptive_average_pool#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/nn.py#L1388-L1444)

Adaptive average pooling operation.

#### View aliases

**Main aliases**

[`tf.keras.ops.nn.adaptive_average_pool`](https://www.tensorflow.org/api_docs/python/tf/keras/ops/adaptive_average_pool)

tf.keras.ops.adaptive_average_pool(
        inputs, output_size, data_format=None
    )

Applies an adaptive average pooling operation that automatically computes the kernel size and stride to pool the input to the specified `output_size`. This operation is useful when you want a fixed output size regardless of input size, commonly used in models like ResNet for global feature extraction.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `inputs` | Tensor of rank 4. Input tensor of shape:<br><br>*   If `data_format="channels_last"`: `(batch_size, height, width, channels)`.<br>*   If `data_format="channels_first"`: `(batch_size, channels, height, width)`. |
| `output_size` | Integer or tuple/list of 2 integers, specifying the target output spatial dimensions `(output_height, output_width)`. If a single integer is provided, the same value is used for both dimensions. |
| `data_format` | string, either `"channels_last"` or `"channels_first"`. Defaults to the value found in your Keras config file at `~/.keras/keras.json`. If never set, defaults to `"channels_last"`. |

|     |
| --- |
| Returns<br>------- |     |
| A tensor of rank 4 representing the adaptive average pooled result. |     |

#### Example:

    x = np.random.rand(2, 64, 64, 3)

    # Works with any input size

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.