[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/get_mask#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/get_mask)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/get_mask?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/oauth2authorize?return_url=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftfm%2Fnlp%2Flayers%2Fget_mask&scopes=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles.award+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdevprofiles.full_control.firstparty)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/get_mask#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/get_mask#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.nlp.layers.get\_mask Stay organized with collections Save and categorize content based on your preferences.
===============================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/get_mask#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/get_mask#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/modeling/layers/self_attention_mask.py#L20-L45)

Gets a 3D self-attention mask.

tfm.nlp.layers.get_mask(
        inputs: tf.Tensor, to_mask: tf.Tensor, dtype: Optional[tf.DType] = None
    ) -> tf.Tensor

|     |     |
| --- | --- |
| Args<br>---- |     |
| `inputs` | from\_tensor: 2D or 3D Tensor of shape \[batch\_size, from\_seq\_length, ...\]. |
| `to_mask` | int32 Tensor of shape \[batch\_size, to\_seq\_length\]. |
| `dtype` | the output Tensor dtype. |

|     |
| --- |
| Returns<br>------- |     |
| float Tensor of shape \[batch\_size, from\_seq\_length, to\_seq\_length\]. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.