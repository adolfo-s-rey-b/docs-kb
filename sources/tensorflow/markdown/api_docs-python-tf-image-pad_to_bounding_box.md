[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/image/pad_to_bounding_box#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/image/pad_to_bounding_box)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/image/pad_to_bounding_box?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fimage%2Fpad_to_bounding_box&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/image/pad_to_bounding_box#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/image/pad_to_bounding_box#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/image/pad_to_bounding_box#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/image/pad_to_bounding_box#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.image.pad\_to\_bounding\_box Stay organized with collections Save and categorize content based on your preferences.
======================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/image/pad_to_bounding_box#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/image/pad_to_bounding_box#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/image/pad_to_bounding_box#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/image/pad_to_bounding_box#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/image_ops_impl.py#L1006-L1070)

Pad `image` with zeros to the specified `height` and `width`.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.image.pad_to_bounding_box`](https://www.tensorflow.org/api_docs/python/tf/image/pad_to_bounding_box)

tf.image.pad_to_bounding_box(
        image, offset_height, offset_width, target_height, target_width
    )

### Used in the notebooks

| Used in the tutorials |
| --- |
| *   [Frame interpolation using the FILM model](https://www.tensorflow.org/hub/tutorials/tf_hub_film_example) |

Adds `offset_height` rows of zeros on top, `offset_width` columns of zeros on the left, and then pads the image on the bottom and right with zeros until it has dimensions `target_height`, `target_width`.

This op does nothing if `offset_*` is zero and the image already has size `target_height` by `target_width`.

#### Usage Example:

    x = [[[1., 2., 3.],\
\
|     |     |\
| --- | --- |\
| Args<br>---- |     |\
| `image` | 4-D Tensor of shape `[batch, height, width, channels]` or 3-D Tensor of shape `[height, width, channels]`. |\
| `offset_height` | Number of rows of zeros to add on top. |\
| `offset_width` | Number of columns of zeros to add on the left. |\
| `target_height` | Height of output image. |\
| `target_width` | Width of output image. |\
\
|     |\
| --- |\
| Returns<br>------- |     |\
| If `image` was 4-D, a 4-D float Tensor of shape `[batch, target_height, target_width, channels]` If `image` was 3-D, a 3-D float Tensor of shape `[target_height, target_width, channels]` |     |\
\
|     |     |\
| --- | --- |\
| Raises<br>------ |     |\
| `ValueError` | If the shape of `image` is incompatible with the `offset_*` or `target_*` arguments, or either `offset_height` or `offset_width` is negative. |\
\
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)\
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)\
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)\
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)\
.\
\
Last updated 2026-10-31 UTC.