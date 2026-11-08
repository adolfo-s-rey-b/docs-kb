[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/summary/image#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/summary/image)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/summary/image?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fsummary%2Fimage&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/summary/image#used-in-the-notebooks)
    
*   [Arguments](https://www.tensorflow.org/api_docs/python/tf/summary/image#arguments)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/summary/image#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/summary/image#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.summary.image Stay organized with collections Save and categorize content based on your preferences.
=======================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/summary/image#used-in-the-notebooks)
    
*   [Arguments](https://www.tensorflow.org/api_docs/python/tf/summary/image#arguments)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/summary/image#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/summary/image#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/summary/tb_summary.py#L161-L240)

Write an image summary.

tf.summary.image(
        name, data, step=None, max_outputs=3, description=None
    )

### Used in the notebooks

| Used in the tutorials |
| --- |
| *   [Displaying image data in TensorBoard](https://www.tensorflow.org/tensorboard/image_summaries) |

See also [`tf.summary.scalar`](https://www.tensorflow.org/api_docs/python/tf/summary/scalar)
, [`tf.summary.SummaryWriter`](https://www.tensorflow.org/api_docs/python/tf/summary/SummaryWriter)
.

Writes a collection of images to the current default summary writer. Data appears in TensorBoard's 'Images' dashboard. Like [`tf.summary.scalar`](https://www.tensorflow.org/api_docs/python/tf/summary/scalar)
 points, each collection of images is associated with a `step` and a `name`. All the image collections with the same `name` constitute a time series of image collections.

This example writes 2 random grayscale images:

w = tf.summary.create_file_writer('test/logs')
    with w.as_default():
      image1 = tf.random.uniform(shape=[8, 8, 1])
      image2 = tf.random.uniform(shape=[8, 8, 1])
      tf.summary.image("grayscale_noise", [image1, image2], step=0)

To avoid clipping, data should be converted to one of the following:

*   floating point values in the range \[0,1\], or
*   uint8 values in the range \[0,255\]

# Convert the original dtype=int32 `Tensor` into `dtype=float64`.
    rgb_image_float = tf.constant([\
      [[1000, 0, 0], [0, 500, 1000]],\
    ]) / 1000
    tf.summary.image("picture", [rgb_image_float], step=0)
    
    # Convert original dtype=uint8 `Tensor` into proper range.
    rgb_image_uint8 = tf.constant([\
      [[1, 1, 0], [0, 0, 1]],\
    ], dtype=tf.uint8) * 255
    tf.summary.image("picture", [rgb_image_uint8], step=1)

|     |     |
| --- | --- |
| Arguments<br>--------- |     |
| `name` | A name for this summary. The summary tag used for TensorBoard will be this name prefixed by any active name scopes. |
| `data` | A `Tensor` representing pixel data with shape `[k, h, w, c]`, where `k` is the number of images, `h` and `w` are the height and width of the images, and `c` is the number of channels, which should be 1, 2, 3, or 4 (grayscale, grayscale with alpha, RGB, RGBA). Any of the dimensions may be statically unknown (i.e., `None`). Floating point data will be clipped to the range \[0,1\]. Other data types will be clipped into an allowed range for safe casting to uint8, using [`tf.image.convert_image_dtype`](https://www.tensorflow.org/api_docs/python/tf/image/convert_image_dtype)<br>. |
| `step` | Explicit `int64`\-castable monotonic step value for this summary. If omitted, this defaults to [`tf.summary.experimental.get_step()`](https://www.tensorflow.org/api_docs/python/tf/summary/experimental/get_step)<br>, which must not be None. |
| `max_outputs` | Optional `int` or rank-0 integer `Tensor`. At most this many images will be emitted at each step. When more than `max_outputs` many images are provided, the first `max_outputs` many images will be used and the rest silently discarded. |
| `description` | Optional long-form description for this summary, as a constant `str`. Markdown is supported. Defaults to empty. |

|     |
| --- |
| Returns<br>------- |     |
| True on success, or false if no summary was emitted because no default summary writer was available. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | if a default writer exists, but no step was provided and [`tf.summary.experimental.get_step()`](https://www.tensorflow.org/api_docs/python/tf/summary/experimental/get_step)<br> is None. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.