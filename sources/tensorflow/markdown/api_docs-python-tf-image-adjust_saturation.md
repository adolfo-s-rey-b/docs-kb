[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/image/adjust_saturation#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   English
*   中文 – 简体

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.image.adjust\_saturation Stay organized with collections Save and categorize content based on your preferences.
==================================================================================================================

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/image_ops_impl.py#L3115-L3167)

Adjust saturation of RGB images.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.image.adjust_saturation`](https://www.tensorflow.org/api_docs/python/tf/image/adjust_saturation)

tf.image.adjust_saturation(
        image, saturation_factor, name=None
    )

### Used in the notebooks

| Used in the tutorials |
| --- |
| *   [Data augmentation](https://www.tensorflow.org/tutorials/images/data_augmentation) |

This is a convenience method that converts RGB images to float representation, converts them to HSV, adds an offset to the saturation channel, converts back to RGB and then back to the original data type. If several adjustments are chained it is advisable to minimize the number of redundant conversions.

`image` is an RGB image or images. The image saturation is adjusted by converting the images to HSV and multiplying the saturation (S) channel by `saturation_factor` and clipping. The images are then converted back to RGB.

`saturation_factor` must be in the interval `[0, inf)`.\
\
#### Usage Example:\
\
    x = [[[1.0, 2.0, 3.0],\
\
|     |     |\
| --- | --- |\
| Args<br>---- |     |\
| `image` | RGB image or images. The size of the last dimension must be 3. |\
| `saturation_factor` | float. Factor to multiply the saturation by. |\
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
| `InvalidArgumentError` | input must have 3 channels |\
\
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)\
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)\
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)\
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)\
.\
\
Last updated 2026-10-31 UTC.