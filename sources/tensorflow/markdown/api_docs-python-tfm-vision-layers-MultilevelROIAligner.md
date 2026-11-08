[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/vision/layers/MultilevelROIAligner#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/vision/layers/MultilevelROIAligner)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/vision/layers/MultilevelROIAligner?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/layers/MultilevelROIAligner#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/vision/layers/MultilevelROIAligner#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/vision/layers/MultilevelROIAligner#call)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.vision.layers.MultilevelROIAligner Stay organized with collections Save and categorize content based on your preferences.
=============================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/layers/MultilevelROIAligner#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/vision/layers/MultilevelROIAligner#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/vision/layers/MultilevelROIAligner#call)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/modeling/layers/roi_aligner.py#L23-L74)

Performs ROIAlign for the second stage processing.

tfm.vision.layers.MultilevelROIAligner(
        crop_size: int = 7, sample_offset: float = 0.5, **kwargs
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `crop_size` | An `int` of the output size of the cropped features. |
| `sample_offset` | A `float` in \[0, 1\] of the subpixel sample offset. |
| `**kwargs` | Additional keyword arguments passed to Layer. |

Methods
-------

### `call`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/modeling/layers/roi_aligner.py#L41-L67)

call(
        features: Mapping[str, tf.Tensor], boxes: tf.Tensor, training: bool = None
    )

Generates ROIs.

|     |     |
| --- | --- |
| Args |     |
| `features` | A dictionary with key as pyramid level and value as features. The features are in shape of \[batch\_size, height\_l, width\_l, num\_filters\]. |
| `boxes` | A 3-D [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> of shape \[batch\_size, num\_boxes, 4\]. Each row represents a box with \[y1, x1, y2, x2\] in un-normalized coordinates. from grid point. |
| `training` | A `bool` of whether it is in training mode. |

|     |
| --- |
| Returns |     |
| A 5-D [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> representing feature crop of shape \[batch\_size, num\_boxes, crop\_size, crop\_size, num\_filters\]. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.