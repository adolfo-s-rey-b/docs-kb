[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/image/psnr#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/image/psnr)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/image/psnr?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fimage%2Fpsnr&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/image/psnr#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/image/psnr#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/image/psnr#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.image.psnr Stay organized with collections Save and categorize content based on your preferences.
====================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/image/psnr#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/image/psnr#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/image/psnr#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/image_ops_impl.py#L4194-L4246)

Returns the Peak Signal-to-Noise Ratio between a and b.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.image.psnr`](https://www.tensorflow.org/api_docs/python/tf/image/psnr)

tf.image.psnr(
        a, b, max_val, name=None
    )

### Used in the notebooks

| Used in the tutorials |
| --- |
| *   [Image Super Resolution using ESRGAN](https://www.tensorflow.org/hub/tutorials/image_enhancing) |

This is intended to be used on signals (or images). Produces a PSNR value for each image in batch.

The last three dimensions of input are expected to be \[height, width, depth\].

#### Example:

    # Read images from file.
        im1 = tf.decode_png('path/to/im1.png')
        im2 = tf.decode_png('path/to/im2.png')
        # Compute PSNR over tf.uint8 Tensors.
        psnr1 = tf.image.psnr(im1, im2, max_val=255)
    
        # Compute PSNR over tf.float32 Tensors.
        im1 = tf.image.convert_image_dtype(im1, tf.float32)
        im2 = tf.image.convert_image_dtype(im2, tf.float32)
        psnr2 = tf.image.psnr(im1, im2, max_val=1.0)
        # psnr1 and psnr2 both have type tf.float32 and are almost equal.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `a` | First set of images. |
| `b` | Second set of images. |
| `max_val` | The dynamic range of the images (i.e., the difference between the maximum the and minimum allowed values). |
| `name` | Namespace to embed the computation in. |

|     |
| --- |
| Returns<br>------- |     |
| The scalar PSNR between a and b. The returned tensor has type [`tf.float32`](https://www.tensorflow.org/api_docs/python/tf#float32)<br> and shape \[batch\_size, 1\]. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.