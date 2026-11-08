[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops/random_contrast#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops/random_contrast)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops/random_contrast?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops/random_contrast#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops/random_contrast#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.vision.preprocess\_ops.random\_contrast Stay organized with collections Save and categorize content based on your preferences.
==================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops/random_contrast#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops/random_contrast#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/ops/preprocess_ops.py#L972-L989)

Jitters contrast of an image, similarly to torchvision\`s ColorJitter.

tfm.vision.preprocess_ops.random_contrast(
        image: tf.Tensor, contrast: float = 0.0, seed: Optional[int] = None
    ) -> tf.Tensor

|     |     |
| --- | --- |
| Args<br>---- |     |
| `image` | [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br><br>Of shape \[height, width, 3\] and type uint8. |
| `contrast` | `float, optional`<br><br>Magnitude for contrast jitter. Defaults to 0. |
| `seed` | `int, optional`<br><br>Random seed. Defaults to None. |

|     |     |
| --- | --- |
| Returns<br>------- |     |
| [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor) | The augmented `image` of type uint8. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.