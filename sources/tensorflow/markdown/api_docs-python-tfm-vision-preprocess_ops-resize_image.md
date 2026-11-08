[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops/resize_image#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops/resize_image)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops/resize_image?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/oauth2authorize?return_url=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftfm%2Fvision%2Fpreprocess_ops%2Fresize_image&scopes=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles.award+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdevprofiles.full_control.firstparty)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops/resize_image#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops/resize_image#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.vision.preprocess\_ops.resize\_image Stay organized with collections Save and categorize content based on your preferences.
===============================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops/resize_image#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops/resize_image#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/ops/preprocess_ops.py#L440-L528)

Resize image with size and max\_size.

tfm.vision.preprocess_ops.resize_image(
        image: tf.Tensor,
        size: Union[Tuple[int, int], int],
        max_size: Optional[int] = None,
        method: tf.image.ResizeMethod = tf.image.ResizeMethod.BILINEAR
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `image` | the image to be resized. |
| `size` | if list to tuple, resize to it. If scalar, we keep the same aspect ratio and resize the short side to the value. |
| `max_size` | only used when size is a scalar. When the larger side is larger than max\_size after resized with size we used max\_size to keep the aspect ratio instead. |
| `method` | the method argument passed to tf.image.resize. |

|     |     |
| --- | --- |
| Returns<br>------- |     |
| the resized image and image\_info to be used for downstream processing. |     |
| `image_info` | a 2D `Tensor` that encodes the information of the image and the applied preprocessing. It is in the format of \[\[original\_height, original\_width\], \[resized\_height, resized\_width\], \[y\_scale, x\_scale\], \[0, 0\]\], where \[resized\_height, resized\_width\] is the actual scaled image size, and \[y\_scale, x\_scale\] is the scaling factor, which is the ratio of scaled dimension / original dimension. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.