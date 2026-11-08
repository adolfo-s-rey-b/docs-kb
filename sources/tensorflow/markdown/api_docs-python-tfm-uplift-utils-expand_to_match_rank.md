[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/uplift/utils/expand_to_match_rank#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/uplift/utils/expand_to_match_rank)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/uplift/utils/expand_to_match_rank?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftfm%2Fuplift%2Futils%2Fexpand_to_match_rank&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/uplift/utils/expand_to_match_rank#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfm/uplift/utils/expand_to_match_rank#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.uplift.utils.expand\_to\_match\_rank Stay organized with collections Save and categorize content based on your preferences.
===============================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/uplift/utils/expand_to_match_rank#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfm/uplift/utils/expand_to_match_rank#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/recommendation/uplift/utils.py#L21-L35)

Expands tensor a to match the rank of tensor b.

tfm.uplift.utils.expand_to_match_rank(
        a: tf.Tensor, b: tf.Tensor
    ) -> tf.Tensor

|     |     |
| --- | --- |
| Args<br>---- |     |
| `a` | a [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> of shape (D0, D1, ..., Dn). |
| `b` | a [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> of shape (D0, D1, ..., Dn, Dn+1, ... Dn+m). |

|     |
| --- |
| Returns<br>------- |     |
| A [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> of shape (D0, D1, ..., DN, 1, ..., 1) if b has a higher rank than a, otherwise a [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> of shape (D0, D1, ..., Dn) |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.