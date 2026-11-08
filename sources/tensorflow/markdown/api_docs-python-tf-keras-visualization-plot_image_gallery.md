[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/visualization/plot_image_gallery#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/visualization/plot_image_gallery)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/visualization/plot_image_gallery?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fkeras%2Fvisualization%2Fplot_image_gallery&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/visualization/plot_image_gallery#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/keras/visualization/plot_image_gallery#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.visualization.plot\_image\_gallery Stay organized with collections Save and categorize content based on your preferences.
==================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/visualization/plot_image_gallery#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/keras/visualization/plot_image_gallery#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/visualization/plot_image_gallery.py#L44-L200)

Displays a gallery of images with optional labels and predictions.

tf.keras.visualization.plot_image_gallery(
        images,
        y_true=None,
        y_pred=None,
        label_map=None,
        rows=None,
        cols=None,
        value_range=(0, 255),
        scale=2,
        path=None,
        show=None,
        transparent=True,
        dpi=60,
        legend_handles=None,
        data_format=None
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `images` | A 4D tensor or NumPy array of images. Shape should be `(batch_size, height, width, channels)`. |
| `y_true` | A 1D tensor or NumPy array of true labels (class indices). Defaults to `None`. |
| `y_pred` | A 1D tensor or NumPy array of predicted labels (class indices). Defaults to `None`. |
| `label_map` | A dictionary mapping class indices to class names. Required if `y_true` or `y_pred` are provided. Defaults to `None`. |
| `value_range` | A tuple specifying the value range of the images (e.g., `(0, 255)` or `(0, 1)`). Defaults to `(0, 255)`. |
| `rows` | The number of rows in the gallery. If `None`, it's calculated based on the number of images and `cols`. Defaults to `None`. |
| `cols` | The number of columns in the gallery. If `None`, it's calculated based on the number of images and `rows`. Defaults to `None`. |
| `scale` | A float controlling the size of the displayed images. The images are scaled by this factor. Defaults to `2`. |
| `path` | The path to save the generated gallery image. If `None`, the image is displayed using `plt.show()`. Defaults to `None`. |
| `show` | Whether to display the image using `plt.show()`. If `True`, the image is displayed. If `False`, the image is not displayed. Ignored if `path` is not `None`. Defaults to `True` if `path` is `None`, `False` otherwise. |
| `transparent` | A boolean, whether to save the figure with a transparent background. Defaults to `True`. |
| `dpi` | The DPI (dots per inch) for saving the figure. Defaults to 60. |
| `legend_handles` | A list of matplotlib `Patch` objects to use as legend handles. Defaults to `None`. |
| `data_format` | The image data format `"channels_last"` or `"channels_first"`. Defaults to the Keras backend data format. |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | If both `path` and `show` are set to non-`None` values, if `images` is not a 4D tensor or array, or if `y_true` or `y_pred` are provided without a `label_map`. |
| `ImportError` | if matplotlib is not installed. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.