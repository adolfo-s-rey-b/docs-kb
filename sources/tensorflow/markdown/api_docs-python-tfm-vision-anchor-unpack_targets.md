[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/vision/anchor/unpack_targets#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/vision/anchor/unpack_targets)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/vision/anchor/unpack_targets?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/anchor/unpack_targets#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfm/vision/anchor/unpack_targets#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.vision.anchor.unpack\_targets Stay organized with collections Save and categorize content based on your preferences.
========================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/anchor/unpack_targets#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfm/vision/anchor/unpack_targets#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/ops/anchor.py#L477-L510)

Unpacks an array of labels into multi-scales labels.

tfm.vision.anchor.unpack_targets(
        targets: tf.Tensor, anchor_boxes_dict: Dict[str, tf.Tensor]
    ) -> Dict[str, tf.Tensor]

|     |     |
| --- | --- |
| Args<br>---- |     |
| `targets` | A tensor with shape \[num\_anchors, M\] representing the packed targets with M values stored for each anchor. |
| `anchor_boxes_dict` | An ordered dictionary with keys \[min\_level, min\_level+1, ..., max\_level\]. The values are tensor with shape \[height\_l, width\_l, num\_anchors\_per\_location \* 4\]. The height\_l and width\_l represent the dimension of the feature pyramid at l-th level. For each anchor box, the tensor stores \[y0, x0, y1, x1\] for the four corners. |

|     |     |
| --- | --- |
| Returns<br>------- |     |
| `unpacked_targets` | An ordered dictionary with keys \[min\_level, min\_level+1, ..., max\_level\]. The values are tensor with shape \[height\_l, width\_l, num\_anchors\_per\_location \* M\]. The height\_l and width\_l represent the dimension of the feature pyramid at l-th level. M is the number of values stored for each anchor. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.