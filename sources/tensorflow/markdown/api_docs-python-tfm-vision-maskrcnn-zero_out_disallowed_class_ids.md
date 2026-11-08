[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/vision/maskrcnn/zero_out_disallowed_class_ids#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/vision/maskrcnn/zero_out_disallowed_class_ids)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/vision/maskrcnn/zero_out_disallowed_class_ids?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/maskrcnn/zero_out_disallowed_class_ids#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfm/vision/maskrcnn/zero_out_disallowed_class_ids#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.vision.maskrcnn.zero\_out\_disallowed\_class\_ids Stay organized with collections Save and categorize content based on your preferences.
============================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/maskrcnn/zero_out_disallowed_class_ids#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfm/vision/maskrcnn/zero_out_disallowed_class_ids#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/tasks/maskrcnn.py#L41-L62)

Zeroes out IDs of classes not in allowed\_class\_ids.

tfm.vision.maskrcnn.zero_out_disallowed_class_ids(
        batch_class_ids: tf.Tensor, allowed_class_ids: List[int]
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `batch_class_ids` | A \[batch\_size, num\_instances\] int tensor of input class IDs. |
| `allowed_class_ids` | A python list of class IDs which we want to allow. |

|     |     |
| --- | --- |
| Returns<br>------- |     |
| `filtered_class_ids` | A \[batch\_size, num\_instances\] int tensor with any class ID not in allowed\_class\_ids set to 0. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.