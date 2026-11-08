[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops/random_horizontal_flip_with_roi#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops/random_horizontal_flip_with_roi)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops/random_horizontal_flip_with_roi?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops/random_horizontal_flip_with_roi#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops/random_horizontal_flip_with_roi#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.vision.preprocess\_ops.random\_horizontal\_flip\_with\_roi Stay organized with collections Save and categorize content based on your preferences.
=====================================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops/random_horizontal_flip_with_roi#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops/random_horizontal_flip_with_roi#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/ops/preprocess_ops.py#L843-L892)

Randomly flips input image and bounding boxes horizontally.

tfm.vision.preprocess_ops.random_horizontal_flip_with_roi(
        image: tf.Tensor,
        boxes: Optional[tf.Tensor] = None,
        masks: Optional[tf.Tensor] = None,
        roi_boxes: Optional[tf.Tensor] = None,
        seed: int = 1
    ) -> Tuple[tf.Tensor, Optional[tf.Tensor], Optional[tf.Tensor], Optional[tf.Tensor]]

Extends preprocess\_ops.random\_horizontal\_flip to also flip roi\_boxes used by ViLD.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `image` | [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br>, the image to apply the random flip. |
| `boxes` | [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> or `None`, boxes corresponding to the image. |
| `masks` | [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> or `None`, masks corresponding to the image. |
| `roi_boxes` | [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> or `None`, RoIs corresponding to the image. |
| `seed` | Seed for Tensorflow's random number generator. |

|     |     |
| --- | --- |
| Returns<br>------- |     |
| `image` | [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br>, flipped image. |
| `boxes` | [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> or `None`, flipped boxes corresponding to the image. |
| `masks` | [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> or `None`, flipped masks corresponding to the image. |
| `roi_boxes` | [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> or `None`, flipped RoIs corresponding to the image. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.