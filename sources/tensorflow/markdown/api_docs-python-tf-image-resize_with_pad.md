[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/image/resize_with_pad#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/image/resize_with_pad)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/image/resize_with_pad?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/image/resize_with_pad#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/image/resize_with_pad#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/image/resize_with_pad#raises)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/image/resize_with_pad#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.image.resize\_with\_pad Stay organized with collections Save and categorize content based on your preferences.
=================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/image/resize_with_pad#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/image/resize_with_pad#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/image/resize_with_pad#raises)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/image/resize_with_pad#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/image_ops_impl.py#L1923-L1961)

Resizes and pads an image to a target width and height.

tf.image.resize_with_pad(
        image,
        target_height,
        target_width,
        method=ResizeMethod.BILINEAR,
        antialias=False
    )

### Used in the notebooks

| Used in the tutorials |
| --- |
| *   [Integrated gradients](https://www.tensorflow.org/tutorials/interpretability/integrated_gradients)<br>    <br>*   [Load video data](https://www.tensorflow.org/tutorials/load_data/video)<br>    <br>*   [Transfer learning for video classification with MoViNet](https://www.tensorflow.org/tutorials/video/transfer_learning_with_movinet)<br>    <br>*   [Video classification with a 3D convolutional neural network](https://www.tensorflow.org/tutorials/video/video_classification)<br>    <br>*   [Image Classification with TensorFlow Hub](https://www.tensorflow.org/hub/tutorials/image_classification) |

Resizes an image to a target width and height by keeping the aspect ratio the same without distortion. If the target dimensions don't match the image dimensions, the image is resized and then padded with zeroes to match requested dimensions.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `image` | 4-D Tensor of shape `[batch, height, width, channels]` or 3-D Tensor of shape `[height, width, channels]`. |
| `target_height` | Target height. |
| `target_width` | Target width. |
| `method` | Method to use for resizing image. See [`image.resize()`](https://www.tensorflow.org/api_docs/python/tf/image/resize) |
| `antialias` | Whether to use anti-aliasing when resizing. See 'image.resize()'. |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | if `target_height` or `target_width` are zero or negative. |

|     |
| --- |
| Returns<br>------- |     |
| Resized and padded image. If `images` was 4-D, a 4-D float Tensor of shape `[batch, new_height, new_width, channels]`. If `images` was 3-D, a 3-D float Tensor of shape `[new_height, new_width, channels]`. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.