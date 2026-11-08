[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/ops/unfold#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/ops/unfold)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/ops/unfold?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/unfold#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/unfold#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.ops.unfold Stay organized with collections Save and categorize content based on your preferences.
==========================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/unfold#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/unfold#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/nn.py#L3300-L3342)

Extract sliding local blocks from a 4-D input (batched image).

#### View aliases

**Main aliases**

[`tf.keras.ops.nn.unfold`](https://www.tensorflow.org/api_docs/python/tf/keras/ops/unfold)

tf.keras.ops.unfold(
        x, kernel_size, dilation=1, padding=0, stride=1
    )

This operation is known as **im2col** when used with convolution. It rearranges the image into overlapping or non-overlapping patches and returns a tensor whose _depth_ (last axis) contains the flattened patches.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `x` | A 4-D tensor of shape `(N, C, H, W)` (**channels-first** format). |
| `kernel_size` | int or tuple of two ints, the size of the sliding window `(kH, kW)`. If a single int is given, it is used for both dimensions. |
| `dilation` | int or tuple of two ints, the spacing between kernel points (a.k.a. **dilation** or **atrous** convolution). Default: 1. |
| `padding` | int or tuple of two ints, the amount of zero-padding to apply to both spatial dimensions. Default: 0. |
| `stride` | int or tuple of two ints, the step size of the sliding window. Default: 1. |

|     |
| --- |
| Returns<br>------- |     |
| A 3-D tensor of shape `(N, C * kH * kW, L)` where `L = num_patches_H * num_patches_W` is the total number of patches extracted. |     |

#### Example:

    x = keras.ops.ones((1, 2, 4, 4))

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.