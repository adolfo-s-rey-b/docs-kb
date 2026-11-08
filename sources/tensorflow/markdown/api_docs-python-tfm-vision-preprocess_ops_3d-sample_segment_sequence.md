[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops_3d/sample_segment_sequence#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops_3d/sample_segment_sequence)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops_3d/sample_segment_sequence?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops_3d/sample_segment_sequence#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops_3d/sample_segment_sequence#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.vision.preprocess\_ops\_3d.sample\_segment\_sequence Stay organized with collections Save and categorize content based on your preferences.
===============================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops_3d/sample_segment_sequence#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops_3d/sample_segment_sequence#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/ops/preprocess_ops_3d.py#L126-L178)

Samples a single segment of size `num_frames` from a given sequence.

tfm.vision.preprocess_ops_3d.sample_segment_sequence(
        sequence: tf.Tensor,
        num_frames: int,
        is_training: bool,
        seed: Optional[int] = None
    ) -> tf.Tensor

This function follows the temporal segment network sampling style ([https://arxiv.org/abs/1608.00859](https://arxiv.org/abs/1608.00859)
). The video sequence would be divided into `num_frames` non-overlapping segments with same length. If `is_training` is `True`, we would randomly sampling one frame for each segment, and when `is_training` is `False`, only the center frame of each segment is sampled.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `sequence` | Any tensor where the first dimension is timesteps. |
| `num_frames` | Number of frames to take. |
| `is_training` | A boolean indicating sampling in training or evaluation mode. |
| `seed` | A deterministic seed to use when sampling. |

|     |
| --- |
| Returns<br>------- |     |
| A single [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> with first dimension `num_steps` with the sampled segment. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.