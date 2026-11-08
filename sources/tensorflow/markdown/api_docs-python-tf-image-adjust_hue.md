[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/image/adjust_hue?version=stable#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/image/adjust_hue)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/image/adjust_hue?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/image/adjust_hue?version=stable#args_1)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/image/adjust_hue?version=stable#returns_1)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/image/adjust_hue?version=stable#raises_1)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.image.adjust\_hue Stay organized with collections Save and categorize content based on your preferences.
===========================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/image/adjust_hue?version=stable#args_1)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/image/adjust_hue?version=stable#returns_1)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/image/adjust_hue?version=stable#raises_1)
    

See Stable See Nightly

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/image_ops_impl.py#L2743-L2815)

Adjust hue of RGB images.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.image.adjust_hue`](https://www.tensorflow.org/api_docs/python/tf/image/adjust_hue)

tf.image.adjust_hue(
        image, delta, name=None
    )

This is a convenience method that converts an RGB image to float representation, converts it to HSV, adds an offset to the hue channel, converts back to RGB and then back to the original data type. If several adjustments are chained it is advisable to minimize the number of redundant conversions.

`image` is an RGB image. The image hue is adjusted by converting the image(s) to HSV and rotating the hue channel (H) by `delta`. The image is then converted back to RGB.

`delta` must be in the interval `[-1, 1]`.

#### Usage Example:

    x = [[[1.0, 2.0, 3.0],\
\
|     |     |\
| --- | --- |\
| Args<br>---- |     |\
| `image` | RGB image or images. The size of the last dimension must be 3. |\
| `delta` | float. How much to add to the hue channel. |\
| `name` | A name for this operation (optional). |\
\
|     |\
| --- |\
| Returns<br>------- |     |\
| Adjusted image(s), same shape and DType as `image`. |     |\
\
|     |     |\
| --- | --- |\
| Raises<br>------ |     |\
| `InvalidArgumentError` | image must have at least 3 dimensions. |\
| `InvalidArgumentError` | The size of the last dimension must be 3. |\
| `ValueError` | if `delta` is not in the interval of `[-1, 1]`. |\
\
#### Usage Example:\
\
    image = [[[1, 2, 3], [4, 5, 6]],\
\
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)\
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)\
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)\
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)\
.\
\
Last updated 2026-11-05 UTC.