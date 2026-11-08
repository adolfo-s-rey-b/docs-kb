[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/image/adjust_brightness#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/image/adjust_brightness)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/image/adjust_brightness?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/image/adjust_brightness#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/image/adjust_brightness#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/image/adjust_brightness#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.image.adjust\_brightness Stay organized with collections Save and categorize content based on your preferences.
==================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/image/adjust_brightness#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/image/adjust_brightness#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/image/adjust_brightness#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/image_ops_impl.py#L2207-L2257)

Adjust the brightness of RGB or Grayscale images.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.image.adjust_brightness`](https://www.tensorflow.org/api_docs/python/tf/image/adjust_brightness)

tf.image.adjust_brightness(
        image, delta
    )

### Used in the notebooks

| Used in the tutorials |
| --- |
| *   [Data augmentation](https://www.tensorflow.org/tutorials/images/data_augmentation) |

This is a convenience method that converts RGB images to float representation, adjusts their brightness, and then converts them back to the original data type. If several adjustments are chained, it is advisable to minimize the number of redundant conversions.

The value `delta` is added to all components of the tensor `image`. `image` is converted to `float` and scaled appropriately if it is in fixed-point representation, and `delta` is converted to the same data type. For regular images, `delta` should be in the range `(-1,1)`, as it is added to the image in floating point representation, where pixel values are in the `[0,1)` range.\
\
#### Usage Example:\
\
    x = [[[1.0, 2.0, 3.0],\
\
|     |     |\
| --- | --- |\
| Args<br>---- |     |\
| `image` | RGB image or images to adjust. |\
| `delta` | A scalar. Amount to add to the pixel values. |\
\
|     |\
| --- |\
| Returns<br>------- |     |\
| A brightness-adjusted tensor of the same shape and type as `image`. |     |\
\
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)\
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)\
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)\
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)\
.\
\
Last updated 2026-10-31 UTC.