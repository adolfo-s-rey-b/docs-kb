[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/vision/target_gather/TargetGather#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/vision/target_gather/TargetGather)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/vision/target_gather/TargetGather?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/vision/target_gather/TargetGather#methods)
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tfm/vision/target_gather/TargetGather#__call__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.vision.target\_gather.TargetGather Stay organized with collections Save and categorize content based on your preferences.
=============================================================================================================================

*   On this page
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/vision/target_gather/TargetGather#methods)
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tfm/vision/target_gather/TargetGather#__call__)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/ops/target_gather.py#L20-L103)

Targer gather for dense object detector.

Methods
-------

### `__call__`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/ops/target_gather.py#L23-L49)

__call__(
        labels, match_indices, mask=None, mask_val=0.0
    )

Labels anchors with ground truth inputs.

B: batch\_size N: number of groundtruth boxes.

|     |     |
| --- | --- |
| Args |     |
| `labels` | An integer tensor with shape \[N, dims\] or \[B, N, ...\] representing groundtruth labels. |
| `match_indices` | An integer tensor with shape \[M\] or \[B, M\] representing match label index. |
| `mask` | An boolean tensor with shape \[M, dims\] or \[B, M,...\] representing match labels. |
| `mask_val` | An integer to fill in for mask. |

|     |     |
| --- | --- |
| Returns |     |
| `target` | An integer Tensor with shape \[M\] or \[B, M\] |

|     |     |
| --- | --- |
| Raises |     |
| `ValueError` | If `labels` is higher than rank 3. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.