[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/experimental/fold#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/experimental/fold)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/experimental/fold?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/experimental/fold#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/experimental/fold#returns)
    
*   [Example](https://www.tensorflow.org/api_docs/python/tf/experimental/fold#example)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.experimental.fold Stay organized with collections Save and categorize content based on your preferences.
===========================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/experimental/fold#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/experimental/fold#returns)
    
*   [Example](https://www.tensorflow.org/api_docs/python/tf/experimental/fold#example)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/python/ops/array_ops.py#L6418-L6719)

Reconstructs an image from a tensor of extracted patches.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.experimental.fold`](https://www.tensorflow.org/api_docs/python/tf/experimental/fold)

tf.experimental.fold(
        patches,
        output_size,
        sizes,
        strides,
        padding='VALID',
        rates=1,
        reduction='sum'
    )

This op acts as an inverse of [`tf.image.extract_patches`](https://www.tensorflow.org/api_docs/python/tf/image/extract_patches)
.It takes a tensor of patches and folds them back into an image. When patches overlap (i.e., when strides are smaller than the patch sizes), the `reduction` argument determines whether the overlapping pixel values are accumulated(summed) or averaged.

[`tf.config.experimental.enable_op_determinism()`](https://www.tensorflow.org/api_docs/python/tf/config/experimental/enable_op_determinism)

When op determinism is enabled, TensorFlow ops will be deterministic. This means that if an op is run multiple times with the same inputs on the same hardware, it will have the exact same outputs each time. See [`tf.config.experimental.enable_op_determinism`](https://www.tensorflow.org/api_docs/python/tf/config/experimental/enable_op_determinism)
 for details.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `patches` | A 4D `Tensor` of shape `(batch, out_h, out_w, patch_dim)`, where `patch_dim = kernel_h * kernel_w * channels`. This matches the standard output format of [`tf.image.extract_patches`](https://www.tensorflow.org/api_docs/python/tf/image/extract_patches)<br>. |
| `output_size` | A tuple of integers `(height, width)` specifying the spatial dimensions of the reconstructed image (before removing padding if `padding="VALID"`). |
| `sizes` | An `int` or tuple `(kernel_h, kernel_w)` specifying the size of each patch. |
| `strides` | An `int` or tuple `(stride_h, stride_w)` specifying the step size between patches. A single value `int` specifies the same stride for both height and width. |
| `padding` | A `str` ("VALID", "SAME") or an `int`. - "VALID": No padding is applied (default). - "SAME": Matches the padding behavior of [`tf.image.extract_patches`](https://www.tensorflow.org/api_docs/python/tf/image/extract_patches)<br>. - `int`: Applies symmetric padding of this exact value to all sides. |
| `rates` | An `int` or tuple `(dilation_h, dilation_w)` specifying the dilation rate (spacing between kernel elements). Must be `>= 1`. Defaults to 1. |
| `reduction` | A `str`, either `"sum"` or `"mean"`. Specifies how to aggregate pixel values from overlapping patches. Defaults to `"sum"`. |

|     |
| --- |
| Returns<br>------- |     |
| A 4D `Tensor` of shape `(batch, height, width, channels)`. |     |

|     |     |
| --- | --- |
| Example<br>------- |     |
| `**Eg.1` | Basic non-overlapping patches:\*\*<br><br>>>> # Create a simple 4x4 image (batch=1, h=4, w=4, channels=1)<br>    >>> x = tf.reshape(tf.range(16, dtype=tf.float32), (1, 4, 4, 1))<br><br>    # Extract non-overlapping 2x2 patches<br><br>    # Reconstruct the original image |
| `**Eg.2` | Overlapping patches: (stride is smaller than sizes(kernel))\*\*<br><br>>>> # It's important to enable_op_determinism before<br>    >>> # using fold() in this case<br>    >>> tf.config.experimental.enable_op_determinism()<br>    >>> # Extract overlapping 2x2 patches<br>    >>> overlapping_patches = tf.image.extract_patches(<br>    ...     images=x,<br>    ...     sizes=[1, 2, 2, 1],<br>    ...     strides=[1, 1, 1, 1],<br>    ...     rates=[1, 1, 1, 1],<br>    ...     padding="VALID"<br>    ... )<br><br>    # Reconstruct the image using mean reduction to average the |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.