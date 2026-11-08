[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops_3d/sample_linspace_sequence#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   English
*   中文 – 简体

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.vision.preprocess\_ops\_3d.sample\_linspace\_sequence Stay organized with collections Save and categorize content based on your preferences.
================================================================================================================================================

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/ops/preprocess_ops_3d.py#L38-L75)

Samples `num_windows` segments from sequence with linearly spaced offsets.

tfm.vision.preprocess_ops_3d.sample_linspace_sequence(
        sequence: tf.Tensor, num_windows: int, num_steps: int, stride: int
    ) -> tf.Tensor

The samples are concatenated in a single [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)
 in order to have the same format structure per timestep (e.g. a single frame). If `num_steps` \* `stride` is bigger than the number of timesteps, the sequence is repeated. This function can be used in evaluation in order to extract enough segments to span the entire sequence.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `sequence` | Any tensor where the first dimension is timesteps. |
| `num_windows` | Number of windows retrieved from the sequence. |
| `num_steps` | Number of steps (e.g. frames) to take. |
| `stride` | Distance to sample between timesteps. |

|     |
| --- |
| Returns<br>------- |     |
| A single [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> with first dimension `num_windows` \* `num_steps`. The tensor contains the concatenated list of `num_windows` tensors which offsets have been linearly spaced from input. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.