[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/utils/load_img#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/utils/load_img)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/utils/load_img?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/keras/utils/load_img#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/utils/load_img#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/utils/load_img#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.utils.load\_img Stay organized with collections Save and categorize content based on your preferences.
===============================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/keras/utils/load_img#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/utils/load_img#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/utils/load_img#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/utils/image_utils.py#L199-L305)

Loads an image into PIL format.

#### View aliases

**Main aliases**

[`tf.keras.preprocessing.image.load_img`](https://www.tensorflow.org/api_docs/python/tf/keras/utils/load_img)

tf.keras.utils.load_img(
        path,
        color_mode='rgb',
        target_size=None,
        interpolation='nearest',
        keep_aspect_ratio=False
    )

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Using the SavedModel format](https://www.tensorflow.org/guide/saved_model) | *   [Image classification](https://www.tensorflow.org/tutorials/images/classification) |

#### Example:

image = keras.utils.load_img(image_path)
    input_arr = keras.utils.img_to_array(image)
    input_arr = np.array([input_arr])  # Convert single image to a batch.
    predictions = model.predict(input_arr)

|     |     |
| --- | --- |
| Args<br>---- |     |
| `path` | Path to image file. |
| `color_mode` | One of `"grayscale"`, `"rgb"`, `"rgba"`. Default: `"rgb"`. The desired image format. |
| `target_size` | Either `None` (default to original size) or tuple of ints `(img_height, img_width)`. |
| `interpolation` | Interpolation method used to resample the image if the target size is different from that of the loaded image. Supported methods are `"nearest"`, `"bilinear"`, and `"bicubic"`. If PIL version 1.1.3 or newer is installed, `"lanczos"` is also supported. If PIL version 3.4.0 or newer is installed, `"box"` and `"hamming"` are also supported. By default, `"nearest"` is used. |
| `keep_aspect_ratio` | Boolean, whether to resize images to a target size without aspect ratio distortion. The image is cropped in the center with target aspect ratio before resizing. |

|     |
| --- |
| Returns<br>------- |     |
| A PIL Image instance. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.