[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/visualization/plot_segmentation_mask_gallery#main-content)

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
    

tf.keras.visualization.plot\_segmentation\_mask\_gallery Stay organized with collections Save and categorize content based on your preferences.
===============================================================================================================================================

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/visualization/plot_segmentation_mask_gallery.py#L14-L121)

Plots a gallery of images with corresponding segmentation masks.

tf.keras.visualization.plot_segmentation_mask_gallery(
        images,
        num_classes,
        value_range=(0, 255),
        y_true=None,
        y_pred=None,
        color_mapping=None,
        blend=True,
        alpha=0.8,
        ignore_index=-1,
        data_format=None,
        **kwargs
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `images` | A 4D tensor or NumPy array of images. Shape should be `(batch_size, height, width, channels)`. |
| `num_classes` | The number of segmentation classes. Class indices should start from `1`. Class `0` will be treated as background and ignored if `ignore_index` is not 0. |
| `value_range` | A tuple specifying the value range of the images (e.g., `(0, 255)` or `(0, 1)`). Defaults to `(0, 255)`. |
| `y_true` | A 3D/4D tensor or NumPy array representing the ground truth segmentation masks. Shape should be `(batch_size, height, width)` or `(batch_size, height, width, 1)`. Defaults to `None`. |
| `y_pred` | A 3D/4D tensor or NumPy array representing the predicted segmentation masks. Shape should be the same as `y_true`. Defaults to `None`. |
| `color_mapping` | A dictionary mapping class indices to RGB colors. If `None`, a default color palette is used. Class indices start from `1`. Defaults to `None`. |
| `blend` | Whether to blend the masks with the input image using the `alpha` value. If `False`, the masks are drawn directly on the images without blending. Defaults to `True`. |
| `alpha` | The opacity of the segmentation masks (a float between 0 and 1). Defaults to `0.8`. |
| `ignore_index` | The class index to ignore when drawing masks. Defaults to `-1`. |
| `data_format` | The image data format `"channels_last"` or `"channels_first"`. Defaults to the Keras backend data format. |
| `kwargs` | Additional keyword arguments to be passed to [`keras.visualization.plot_image_gallery`](https://www.tensorflow.org/api_docs/python/tf/keras/visualization/plot_image_gallery)<br>. |

|     |
| --- |
| Returns<br>------- |     |
| The output of [`keras.visualization.plot_image_gallery`](https://www.tensorflow.org/api_docs/python/tf/keras/visualization/plot_image_gallery)<br>. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | If `images` is not a 4D tensor/array. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.