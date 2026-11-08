[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops/random_crop_image#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops/random_crop_image)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops/random_crop_image?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftfm%2Fvision%2Fpreprocess_ops%2Frandom_crop_image&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops/random_crop_image#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops/random_crop_image#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.vision.preprocess\_ops.random\_crop\_image Stay organized with collections Save and categorize content based on your preferences.
=====================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops/random_crop_image#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops/random_crop_image#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/ops/preprocess_ops.py#L607-L642)

Randomly crop an arbitrary shaped slice from the input image.

tfm.vision.preprocess_ops.random_crop_image(
        image,
        aspect_ratio_range=(3.0 / 4.0, 4.0 / 3.0),
        area_range=(0.08, 1.0),
        max_attempts=10,
        seed=1
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `image` | a Tensor of shape \[height, width, 3\] representing the input image. |
| `aspect_ratio_range` | a list of floats. The cropped area of the image must have an aspect ratio = width / height within this range. |
| `area_range` | a list of floats. The cropped reas of the image must contain a fraction of the input image within this range. |
| `max_attempts` | the number of attempts at generating a cropped region of the image of the specified constraints. After max\_attempts failures, return the entire image. |
| `seed` | the seed of the random generator. |

|     |     |
| --- | --- |
| Returns<br>------- |     |
| `cropped_image` | a Tensor representing the random cropped image. Can be the original image if max\_attempts is exhausted. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.