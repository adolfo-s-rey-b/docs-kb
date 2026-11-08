[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/visualization/draw_segmentation_masks#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/visualization/draw_segmentation_masks)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/visualization/draw_segmentation_masks?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/visualization/draw_segmentation_masks#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/visualization/draw_segmentation_masks#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/keras/visualization/draw_segmentation_masks#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.visualization.draw\_segmentation\_masks Stay organized with collections Save and categorize content based on your preferences.
=======================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/visualization/draw_segmentation_masks#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/visualization/draw_segmentation_masks#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/keras/visualization/draw_segmentation_masks#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/visualization/draw_segmentation_masks.py#L8-L104)

Draws segmentation masks on images.

tf.keras.visualization.draw_segmentation_masks(
        images,
        segmentation_masks,
        num_classes=None,
        color_mapping=None,
        alpha=0.8,
        blend=True,
        ignore_index=-1,
        data_format=None
    )

The function overlays segmentation masks on the input images. The masks are blended with the images using the specified alpha value.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `images` | A batch of images as a 4D tensor or NumPy array. Shape should be (batch\_size, height, width, channels). |
| `segmentation_masks` | A batch of segmentation masks as a 3D or 4D tensor or NumPy array. Shape should be (batch\_size, height, width) or (batch\_size, height, width, 1). The values represent class indices starting from 1 up to `num_classes`. Class 0 is reserved for the background and will be ignored if `ignore_index` is not 0. |
| `num_classes` | The number of segmentation classes. If `None`, it is inferred from the maximum value in `segmentation_masks`. |
| `color_mapping` | A dictionary mapping class indices to RGB colors. If `None`, a default color palette is generated. The keys should be integers starting from 1 up to `num_classes`. |
| `alpha` | The opacity of the segmentation masks. Must be in the range `[0, 1]`. |
| `blend` | Whether to blend the masks with the input image using the `alpha` value. If `False`, the masks are drawn directly on the images without blending. Defaults to `True`. |
| `ignore_index` | The class index to ignore. Mask pixels with this value will not be drawn. Defaults to -1. |
| `data_format` | Image data format, either `"channels_last"` or `"channels_first"`. Defaults to the `image_data_format` value found in your Keras config file at `~/.keras/keras.json`. If you never set it, then it will be `"channels_last"`. |

|     |
| --- |
| Returns<br>------- |     |
| A NumPy array of the images with the segmentation masks overlaid. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | If the input `images` is not a 4D tensor or NumPy array. |
| `TypeError` | If the input `segmentation_masks` is not an integer type. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.