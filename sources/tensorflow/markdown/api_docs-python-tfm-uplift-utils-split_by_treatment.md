[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/uplift/utils/split_by_treatment#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/uplift/utils/split_by_treatment)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/uplift/utils/split_by_treatment?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/uplift/utils/split_by_treatment#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfm/uplift/utils/split_by_treatment#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.uplift.utils.split\_by\_treatment Stay organized with collections Save and categorize content based on your preferences.
============================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/uplift/utils/split_by_treatment#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfm/uplift/utils/split_by_treatment#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/recommendation/uplift/utils.py#L38-L98)

Splits a tensor into control and treatment tensors.

tfm.uplift.utils.split_by_treatment(
        values: tf.Tensor, is_treatment: tf.Tensor
    ) -> Tuple[tf.Tensor, tf.Tensor]

|     |     |
| --- | --- |
| Args<br>---- |     |
| `values` | a [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> of shape (D0, D1, ..., DN). |
| `is_treatment` | a [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> of shape (D0,) or (D0, 1) castable to boolean indicating if the example belongs to the treatment group (True) or control group (False). |

|     |
| --- |
| Returns<br>------- |     |
| A tuple with control and treatment values sliced by the is\_treatment tensor. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.