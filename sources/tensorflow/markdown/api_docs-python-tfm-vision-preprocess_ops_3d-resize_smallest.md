[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops_3d/resize_smallest#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops_3d/resize_smallest)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops_3d/resize_smallest?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops_3d/resize_smallest#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops_3d/resize_smallest#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.vision.preprocess\_ops\_3d.resize\_smallest Stay organized with collections Save and categorize content based on your preferences.
======================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops_3d/resize_smallest#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops_3d/resize_smallest#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/ops/preprocess_ops_3d.py#L307-L336)

Resizes frames so that min(`height`, `width`) is equal to `min_resize`.

tfm.vision.preprocess_ops_3d.resize_smallest(
        frames: tf.Tensor, min_resize: int
    ) -> tf.Tensor

This function will not do anything if the min(`height`, `width`) is already equal to `min_resize`. This allows to save compute time.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `frames` | A Tensor of dimension \[timesteps, input\_h, input\_w, channels\]. |
| `min_resize` | Minimum size of the final image dimensions. |

|     |
| --- |
| Returns<br>------- |     |
| A Tensor of shape \[timesteps, output\_h, output\_w, channels\] of type frames.dtype where min(output\_h, output\_w) = min\_resize. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.