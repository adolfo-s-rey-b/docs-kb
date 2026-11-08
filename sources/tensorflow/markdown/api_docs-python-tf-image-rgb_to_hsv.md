[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/image/rgb_to_hsv#main-content)

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
    

tf.image.rgb\_to\_hsv Stay organized with collections Save and categorize content based on your preferences.
============================================================================================================

Converts one or more images from RGB to HSV.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.image.rgb_to_hsv`](https://www.tensorflow.org/api_docs/python/tf/image/rgb_to_hsv)

tf.image.rgb_to_hsv(
        images: Annotated[Any, TV_RGBToHSV_T], name=None
    ) -> Annotated[Any, TV_RGBToHSV_T]

Outputs a tensor of the same shape as the `images` tensor, containing the HSV value of the pixels. The output is only well defined if the value in `images` are in `[0,1]`.

`output[..., 0]` contains hue, `output[..., 1]` contains saturation, and `output[..., 2]` contains value. All HSV values are in `[0,1]`. A hue of 0 corresponds to pure red, hue 1/3 is pure green, and 2/3 is pure blue.

#### Usage Example:

    blue_image = tf.stack([\
\
|     |     |\
| --- | --- |\
| Args<br>---- |     |\
| `images` | A `Tensor`. Must be one of the following types: `half`, `bfloat16`, `float32`, `float64`. 1-D or higher rank. RGB data to convert. Last dimension must be size 3. |\
| `name` | A name for the operation (optional). |\
\
|     |\
| --- |\
| Returns<br>------- |     |\
| A `Tensor`. Has the same type as `images`. |     |\
\
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)\
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)\
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)\
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)\
.\
\
Last updated 2024-04-26 UTC.