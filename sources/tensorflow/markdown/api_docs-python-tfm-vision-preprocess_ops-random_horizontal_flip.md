[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops/random_horizontal_flip#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops/random_horizontal_flip)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops/random_horizontal_flip?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops/random_horizontal_flip#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops/random_horizontal_flip#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.vision.preprocess\_ops.random\_horizontal\_flip Stay organized with collections Save and categorize content based on your preferences.
==========================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops/random_horizontal_flip#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops/random_horizontal_flip#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/ops/preprocess_ops.py#L798-L840)

Randomly flips input image and bounding boxes and/or masks horizontally.

tfm.vision.preprocess_ops.random_horizontal_flip(
        image, normalized_boxes=None, masks=None, seed=1, prob=0.5
    )

Expects input tensors without the batch dimension; i.e. for RGB image assume rank-3 input like \[h, w, c\], for masks assume either \[h, w, 1\] or \[1, h, w\].

|     |     |
| --- | --- |
| Args<br>---- |     |
| `image` | [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br>, the image to apply the random flip, \[h, w, channels\]. |
| `normalized_boxes` | [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> or `None`, boxes corresponding to the image. |
| `masks` | [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> or `None`, masks corresponding to the image, \[h, w, 1\] or \[1, h, w\]. |
| `seed` | Seed for Tensorflow's random number generator. |
| `prob` | A float from 0 to 1 indicating the probability of flipping the input horizontally. |

|     |     |
| --- | --- |
| Returns<br>------- |     |
| `image` | [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br>, flipped image. |
| `boxes` | [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> or `None`, flipped normalized boxes corresponding to the image. |
| `masks` | [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> or `None`, flipped masks corresponding to the image. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.