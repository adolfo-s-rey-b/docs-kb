[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/image/resize_with_crop_or_pad#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/image/resize_with_crop_or_pad)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/image/resize_with_crop_or_pad?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/image/resize_with_crop_or_pad#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/image/resize_with_crop_or_pad#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/image/resize_with_crop_or_pad#raises)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/image/resize_with_crop_or_pad#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.image.resize\_with\_crop\_or\_pad Stay organized with collections Save and categorize content based on your preferences.
===========================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/image/resize_with_crop_or_pad#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/image/resize_with_crop_or_pad#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/image/resize_with_crop_or_pad#raises)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/image/resize_with_crop_or_pad#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/image_ops_impl.py#L1277-L1431)

Crops and/or pads an image to a target width and height.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.image.resize_image_with_crop_or_pad`](https://www.tensorflow.org/api_docs/python/tf/image/resize_with_crop_or_pad)
, [`tf.compat.v1.image.resize_with_crop_or_pad`](https://www.tensorflow.org/api_docs/python/tf/image/resize_with_crop_or_pad)

tf.image.resize_with_crop_or_pad(
        image, target_height, target_width
    )

### Used in the notebooks

| Used in the tutorials |
| --- |
| *   [Data augmentation](https://www.tensorflow.org/tutorials/images/data_augmentation)<br>    <br>*   [Artistic Style Transfer with TensorFlow Lite](https://www.tensorflow.org/lite/examples/style_transfer/overview) |

Resizes an image to a target width and height by either centrally cropping the image or padding it evenly with zeros.

If `width` or `height` is greater than the specified `target_width` or `target_height` respectively, this op centrally crops along that dimension.

#### For example:

    image = np.arange(75).reshape(5, 5, 3)  # create 3-D image input

If `width` or `height` is smaller than the specified `target_width` or `target_height` respectively, this op centrally pads with 0 along that dimension.

#### For example:

    image = np.arange(1, 28).reshape(3, 3, 3)  # create 3-D image input

|     |     |
| --- | --- |
| Args<br>---- |     |
| `image` | 4-D Tensor of shape `[batch, height, width, channels]` or 3-D Tensor of shape `[height, width, channels]`. |
| `target_height` | Target height. |
| `target_width` | Target width. |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | if `target_height` or `target_width` are zero or negative. |

|     |
| --- |
| Returns<br>------- |     |
| Cropped and/or padded image. If `images` was 4-D, a 4-D float Tensor of shape `[batch, new_height, new_width, channels]`. If `images` was 3-D, a 3-D float Tensor of shape `[new_height, new_width, channels]`. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.