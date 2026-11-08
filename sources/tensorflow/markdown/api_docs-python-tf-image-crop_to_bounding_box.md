[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/image/crop_to_bounding_box#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/image/crop_to_bounding_box)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/image/crop_to_bounding_box?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/image/crop_to_bounding_box#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/image/crop_to_bounding_box#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/image/crop_to_bounding_box#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/image/crop_to_bounding_box#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.image.crop\_to\_bounding\_box Stay organized with collections Save and categorize content based on your preferences.
=======================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/image/crop_to_bounding_box#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/image/crop_to_bounding_box#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/image/crop_to_bounding_box#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/image/crop_to_bounding_box#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/image_ops_impl.py#L1170-L1274)

Crops an `image` to a specified bounding box.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.image.crop_to_bounding_box`](https://www.tensorflow.org/api_docs/python/tf/image/crop_to_bounding_box)

tf.image.crop_to_bounding_box(
        image, offset_height, offset_width, target_height, target_width
    )

### Used in the notebooks

| Used in the tutorials |
| --- |
| *   [Image Super Resolution using ESRGAN](https://www.tensorflow.org/hub/tutorials/image_enhancing)<br>    <br>*   [Fast Style Transfer for Arbitrary Styles](https://www.tensorflow.org/hub/tutorials/tf2_arbitrary_image_stylization)<br>    <br>*   [Frame interpolation using the FILM model](https://www.tensorflow.org/hub/tutorials/tf_hub_film_example) |

This op cuts a rectangular bounding box out of `image`. The top-left corner of the bounding box is at `offset_height, offset_width` in `image`, and the lower-right corner is at `offset_height + target_height, offset_width + target_width`.

#### Example Usage:

    image = tf.constant(np.arange(1, 28, dtype=np.float32), shape=[3, 3, 3])

|     |     |
| --- | --- |
| Args<br>---- |     |
| `image` | 4-D `Tensor` of shape `[batch, height, width, channels]` or 3-D `Tensor` of shape `[height, width, channels]`. |
| `offset_height` | Vertical coordinate of the top-left corner of the bounding box in `image`. Must be 0-D int32 `Tensor` or python integer. |
| `offset_width` | Horizontal coordinate of the top-left corner of the bounding box in `image`. Must be 0-D int32 `Tensor` or python integer. |
| `target_height` | Height of the bounding box. Must be 0-D int32 `Tensor` or python integer. |
| `target_width` | Width of the bounding box. Must be 0-D int32 `Tensor` or python integer. |

|     |
| --- |
| Returns<br>------- |     |
| If `image` was 4-D, a 4-D `Tensor` of shape `[batch, target_height, target_width, channels]`. If `image` was 3-D, a 3-D `Tensor` of shape `[target_height, target_width, channels]`. It has the same dtype with `image`. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | `image` is not a 3-D or 4-D `Tensor`. |
| `ValueError` | `offset_width < 0` or `offset_height < 0`. |
| `ValueError` | `target_width <= 0` or `target_height <= 0`. |
| `ValueError` | `width < offset_width + target_width` or `height < offset_height + target_height`. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.