[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/image/adjust_gamma#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/image/adjust_gamma)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/image/adjust_gamma?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/image/adjust_gamma#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/image/adjust_gamma#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/image/adjust_gamma#raises)
    
*   [Notes](https://www.tensorflow.org/api_docs/python/tf/image/adjust_gamma#notes)
    
*   [References](https://www.tensorflow.org/api_docs/python/tf/image/adjust_gamma#references)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.image.adjust\_gamma Stay organized with collections Save and categorize content based on your preferences.
=============================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/image/adjust_gamma#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/image/adjust_gamma#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/image/adjust_gamma#raises)
    
*   [Notes](https://www.tensorflow.org/api_docs/python/tf/image/adjust_gamma#notes)
    
*   [References](https://www.tensorflow.org/api_docs/python/tf/image/adjust_gamma#references)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/image_ops_impl.py#L2319-L2382)

Performs [Gamma Correction](http://en.wikipedia.org/wiki/Gamma_correction)
.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.image.adjust_gamma`](https://www.tensorflow.org/api_docs/python/tf/image/adjust_gamma)

tf.image.adjust_gamma(
        image, gamma=1, gain=1
    )

on the input image.

Also known as Power Law Transform. This function converts the input images at first to float representation, then transforms them pixelwise according to the equation `Out = gain * In**gamma`, and then converts the back to the original data type.

#### Usage Example:

    x = [[[1.0, 2.0, 3.0],\
\
|     |     |\
| --- | --- |\
| Args<br>---- |     |\
| `image` | RGB image or images to adjust. |\
| `gamma` | A scalar or tensor. Non-negative real number. |\
| `gain` | A scalar or tensor. The constant multiplier. |\
\
|     |\
| --- |\
| Returns<br>------- |     |\
| A Tensor. A Gamma-adjusted tensor of the same shape and type as `image`. |     |\
\
|     |     |\
| --- | --- |\
| Raises<br>------ |     |\
| `ValueError` | If gamma is negative. |\
\
|     |\
| --- |\
| Notes<br>----- |     |\
| For gamma greater than 1, the histogram will shift towards left and the output image will be darker than the input image. For gamma less than 1, the histogram will shift towards right and the output image will be brighter than the input image. |     |\
\
|     |\
| --- |\
| References<br>---------- |     |\
| [Wikipedia](http://en.wikipedia.org/wiki/Gamma_correction) |     |\
\
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)\
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)\
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)\
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)\
.\
\
Last updated 2026-10-31 UTC.